"""A General Class to interact with Wiki datasets"""
# uncomment

import MySQLdb
import sys;
import os
import scipy as sp
import pandas as pd
#from collections import defaultdict
import cPickle as pickle

__author__ = "Armin Sajadi"
__copyright__ = "Copyright 215, The Wikisim Project"
__credits__ = ["Armin Sajadi", "Evangelo Milios", "Armin Sajadi"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Armin Sajadi"
__email__ = "sajadi@cs.dal.ca"
__status__ = "Development"


DISABLE_CACHE=False;
MAX_GRAPH_SIZE=1000000

DIR_IN=0;
DIR_OUT=1;
DIR_BOTH=2;
_db = MySQLdb.connect(host="127.0.0.1",port=3307,user='root',passwd="emilios",db="enwiki20160305")
_cursor = _db.cursor()
#WIKI_SIZE = 10216236;
#WIKI_SIZE = 13670498; #2016
WIKI_SIZE = 5576365; #no redirect, 2016

def close():
    global _db, _cursor;
    if _cursor is not None: 
        _cursor.close();
        _db.close();
    _cursor=_db=None;
def reopen():
    global _db, _cursor;
    if _db is None:
        _db = MySQLdb.connect(host="127.0.0.1",port=3307,user='root',passwd="emilios",db="enwiki20160305")
        _cursor = _db.cursor()
page2id_dict=None
redir_dict=None
shalam=3
def load_tables():
    global page2id_dict, redir_dict
    title=None;
    query = "SELECT * FROM `page` where page_namespace=0"
        
    _cursor.execute(query)
    rows = _cursor.fetchall();
    page2id_dict={r[2]:(r[0],r[1],r[3]) for r in rows}
    
    query = "SELECT * FROM `redirect`"
        
    _cursor.execute(query)
    rows = _cursor.fetchall();
    redir_dict={r[0]:r[1] for r in rows}

def id2title(wid):
    """ Returns the title for a given id

    Args: 
        wid: Wikipedia id       
    Returns: 
        The title of the page
    """
    
    title=None;

    _cursor.execute("""SELECT * FROM `page` where page_id = %s""", (wid,))
    row= _cursor.fetchone();
    if row is not None:
        title=row[2];          
    return title;

def ids2title(wids):
    """ Returns the titles for given list of wikipedia ids 

    Args: 
        wids: A list of Wikipedia ids          
    Returns: 
        The list of titles
    """

    wid_list = [str(wid) for wid in wids] ;
    order = ','.join(['page_id'] + wid_list) ;
    wid_str = ",".join(wid_list)
    query = "SELECT page_id, page_title FROM `page` where page_id in ({0})" \
    .format(wid_str, order);
    _cursor.execute(query);
    rows = _cursor.fetchall();
    rows_dict = dict(rows)
    titles = [rows_dict[wid] for wid in wids]
    return titles;

def encode_for_db(instr):
    if isinstance(instr, unicode):
        instr = instr.encode('utf-8')  
    return instr
        
def normalize_str(title):
    
    title = encode_for_db(title)
    title = title.replace(' ','_')
    return title
def title2id(title):
    """ Returns the id for a given title

    Args: 
        wid: Wikipedia id          
    Returns: 
        The title of the page
    """        
    wid=None;
    title = normalize_str(title)
    if title in page2id_dict:
        row=page2id_dict[title]
        wid = getredir_id(row[0]) if row[2] else row[0];
    return wid;


def getredir_id(wid):
    """ Returns the target of a redirected page 

    Args:
        wid: wikipedia id of the page
    Returns:
        The id of the target page
    """
    if wid in redir_dict:
        return redir_dict[wid]
    return None


def resolveredir(wid):
    tid = getredir_id(wid);
    print tid
    if tid is not None:
        wid = tid;    
    return wid

def getredir_title(wid):
    """ Returns the target title of a redirected page 

    Args:
        wid: wikipedia id of the page
    Returns:
        The title of the target page
    """
    
    return None;

def synonymring_titles(wid):
    """ Returns the synonim ring of a page

    Example: synonymring_titles('USA')={('U.S.A', 'US', 'United_States_of_America', ...)}

    Args:
        wid: the wikipedia id
    Returns:
        all the titles in its synonym ring
    """
    wid = resolveredir(wid)
    q="""(select page_title from page where page_id=%s) union 
                 (select page_title from redirect INNER JOIN page
                    on redirect.rd_from = page.page_id 
                    where redirect.rd_to =%s);"""% (wid,wid)
    _cursor.execute(q);
    rows=_cursor.fetchall();
    if rows:
        rows = tuple(r[0] for r in rows)
    return rows;



def checkcache(wid, direction):
    if DISABLE_CACHE:
        return None
    

    
    em=None
    
    if direction == DIR_IN: 
        tablename = 'pagelinksorderedin';
        colname = 'in_neighb'
    elif direction == DIR_OUT: 
        tablename = 'pagelinksorderedout';
        colname = 'out_neighb';
    query =    """select {0} from {1} where cache_id={2}""".format(colname, tablename, wid)
    _cursor.execute(query);
    row = _cursor.fetchone();
    if row is not None:
        values, index = pickle.loads(row[0])
        em=pd.Series(values, index=index)

    return em