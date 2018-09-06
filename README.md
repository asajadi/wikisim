<div id="webaddress">
    <div class="container">
        <div class="panel-group">
            <div class="panel panel-default">
                <div class="panel-heading">
                    <h2>Web Addresses</h2>
                    <a name="curraddress"></a>
                </div>
                <div class="panel-body">
                    <h2>API Adress (current):
                        <a href="http://cgm6.research.cs.dal.ca/~sajadi/wikisim/">http://cgm6.research.cs.dal.ca/~sajadi/wikisim/</a>
                    </h2>
                    <h2>Sourcce code:
                        <a href="https://github.com/asajadi/wikisim">https://github.com/asajadi/wikisim</a>
                    </h2>
                </div>
            </div>
        </div>
    </div>
</div>
<div class="container" id="docdiv">
    <div class="panel-group">
        <div class="panel panel-default">
            <div class="panel-heading">
                <a name="doc"></a>
                <h2> What is Wikisim? </h2>
            </div>
            <div class="panel-body">
                <p>
                    <h3>Wikisim provides the following serrvices:</h3>
                </p>
                <ul>
                    <li>Vector-Space Representation of Wikipedia Concepts</li>
                    <li>Semantic Relatedness between Wikipedia Concepts</li>
                    <li>Wikification: Entity Linking to Wikipedia</li>
                </ul>
                <p>
                    <h3>Publications: </h3>
                </p>
                <p>
                    Detailed decription of the architecture and algorithms can be found in the following publications:
                </p>
                <ul>
                    <li>Armin Sajadi, Evangelos E. Milios, Vlado Keselj: "Vector Space Representation of Concepts Using
                        Wikipedia Graph Structure".
                        <a href="https://dblp.uni-trier.de/db/conf/nldb/nldb2017.html">NLDB 2017</a>: 393-405 (
                        <a href="https://dblp.uni-trier.de/rec/bibtex/conf/nldb/SajadiMK17">bib</a>,
                        <a href="https://link.springer.com/chapter/10.1007%2F978-3-319-59569-6_48">pdf</a>)
                    </li>
                    <li>Armin Sajadi, Evangelos E. Milios, Vlado Keselj, Jeannette C. M. Janssen, "Domain-Specific Semantic
                        Relatedness from Wikipedia Structure: A Case Study in Biomedical Text"
                        <a href="http://dblp.uni-trier.de/db/conf/cicling/cicling2015-1.html#SajadiMKJ15">CICLing (1) 2015</a>: 347-360 (
                        <a href="http://dblp.uni-trier.de/rec/bibtex/conf/cicling/SajadiMKJ15">bib</a>,
                        <a href="http://link.springer.com/chapter/10.1007%2F978-3-319-18111-0_26">pdf</a>)</li>
                    <li>Armin Sajadi,"
                        <em>Graph-Based Domain-Speciﬁc Semantic Relatedness from Wikipedia</em>", Canadian AI 2014, LNAI
                        8436, pp. 381–386, 2014 (
                        <a href="../resrc/caai14.bib">bib</a>,
                        <a href="http://link.springer.com/chapter/10.1007%2F978-3-319-06483-3_42#">pdf</a>)</li>
                </ul>
                <p>
                    <h3>Awards</h3>
                </p>
                <ul>
                    <li>Verifiability, Reproducibility, and Working Description Award, Computational Linguistics and
                        In- telligent Text Processing, 16th International Conference, CICLing 2015, Cairo, Egypt,
                        April 14-20, 2015
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <div class="panel-group">
        <div class="panel panel-default">
            <div class="panel-heading">
                <a name="api"></a>
                <h2> API </h2>
            </div>
            <div class="panel-body">
                <h3> Webservice Address </h3>
                Check the <a href="#curraddress">current address</a>: 
                <h3> Single mode </h3>
                <p>The webservice provides three basic functions (or tasks): Wikification, Simiarity and Embedding calculation.
                    All requests can be processed in
                    <em>single</em> or
                    <em>batch mode</em>.
                </p>
                <ul>
                    <li>
                        <strong>Wikification:</strong>
                        <br> parameters:
                        <br>
                        <code>modelparams</code>: should be 0 for using
                        <em>CoreNLP</em>, 1 for our
                        <em>high-precision trained model</em> and 2 for our
                        <em>high-recall trained method</em>
                        <br>
                        <code>wikitext</code>: the text to be wikified
                        <br> Example (using curl):
                        <br>
                        <code>curl --request POST 'http://35.231.242.71/wikisim/cgi-bin/cgi-wikify.py' -F 'modelparams=0'  -F 'wikitext=Lee Jun-fan known professionally as Bruce Lee, was founder of the martial art Jeet Kune Do'
        </code>
                        <li>
                            <strong>Similarity Calculation</strong>:
                            <br> parameters:
                            <br>
                            <code>task</code>: should be 'sim' for this task
                            <br>
                            <code>direction</code>: 0 for using incomming links, 1 for outgoing links and 2 for both. We recommend using
                            only outgoing links as it provides decent results and is significantly faster
                            <br>
                            <code>c1 (and c2)</code>: the concept to be processed
                            <br> Example (using curl):
                            <br>
                            <code>curl --request POST 'http://35.231.242.71/wikisim/cgi-bin/cgi-pairsim.py' -F 'task=sim' -F 'dir=1' -F 'c1=Bruce_Lee' -F 'c2=Arnold_Schwarzenegger'</code>
                        </li>
                        <li>
                            <strong>Concept Representation (Embedding): </strong>
                            <br> parameters:
                            <br>
                            <code>task</code>: should be 'emb' for this task
                            <br>
                            <code>direction</code>: 0 for using
                            <em>incomming links</em>, 1 for
                            <em>outgoing links</em> and 2 for
                            <em>both</em>. We recommend using only outgoing links as it provides decent results and is
                            significantly faster
                            <br>
                            <code>cutoff</code>: the dimensionality of the embedding. This parameter is only used for returning the
                            embeddings, the similarity calculation always uses all the dimensions.
                            <br>
                            <code>c1</code>: the concept to be processed
                            <br> Example (using curl):
                            <br>
                            <code>curl --request POST 'http://35.231.242.71/wikisim/cgi-bin/cgi-pairsim.py' -F 'task=emb' -F 'dir=1' -F 'cutoff=10' -F 'c1=Bruce_Lee'</code>
                        </li>
                </ul>
                <h3> Batch mode </h3>
                <p> We strongly recommend using batch mode, either by post request and sending the file, or simply uploading
                    the file in the batch mode input.</p>
                <p>For Wikification, documents should be seperated by new lines. For similarity calculation, the file
                    should be tab seperated, each line containing a pair of Wikipedia Concepts. For embedding calculation,
                    each line of the file contains a single concept. </p>
                <p>The parameters are the same, however, the target cgi-files are different:</p>
                <ul>
                    <li>
                        Wikification: use
                        <code>cgi-batchwikify.py</code>
                        <br> Example (using curl):
                        <br>
                        <code>curl --request POST 'http://35.231.242.71/wikisim/cgi-bin/cgi-batchwikify.py' -F 'modelparams=0'  -F 'file=@filename'</code>
                    </li>
                    <li>
                        Similarity: use
                        <code>cgi-batchsim.py</code>
                        <br> Example (using curl):
                        <br>
                        <code>curl --request POST 'http://35.231.242.71/wikisim/cgi-bin/cgi-batchsim.py' -F 'task=sim' -F 'dir=1' -F 'file=@filename'</code>
                    </li>
                    <li>
                        Embedding: use
                        <code>cgi-batchsim.py</code>
                        <br> Example (using curl):
                        <br>
                        <code>curl --request POST 'http://35.231.242.71/wikisim/cgi-bin/cgi-batchsim.py' -F task='emb' -F 'dir=1' -F 'cutoff=10' -F 'file=@filename'</code>
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <div class="panel-group">
        <div class="panel panel-default">
            <div class="panel-heading">
                <a name="download"></a>
                <h2> Downloading the embeddings </h2>
            </div>
            <div class="panel-body">
                <strong> Current Version: enwiki20160305 </strong>
                <p> You can download the embeddings, however, using our API has the following advantages:
                </p>
                <ol>
                    <li>
                        The embeddings are provided for wikipedia concepts page_ids and you need another table to find the concepts titles, moreover,
                        redirect concepts are not included, so let's say you want to find the embeddings for "US",
                        you have to follow the following steps:
                        <ol>
                            <li>
                                From the page table, find "US", and you see that its redirect field is 1, meaning that it's a redirect page; take its id,
                                that is: 31643
                            </li>
                            <li>
                                Go to redirect table and find out that it's redirected to 3434750 (the id for United_States)
                            </li>
                            <li>
                                Go to embedding table and find the embedding for 3434750
                            </li>
                        </ol>
                    </li>
                    <li>
                        The nonzero dimentions are not included in the embedding, so there is a need for efficient alignment
                    </li>
                </ol>
                <p> But if you still want to use your own data-sturctures, download the following tables:</p>
                <ol>
                    <li>
                        <p>
                            <a href="../data/enwiki20160305/edited/enwiki-20160305-page.main.tsv.gz">Page Table</a>
                        </p>
                        Layout:
                        <p>
                            <code>page_id , page_namespace (0:page,14: Category) , page_title , page_is_redirect </code>
                        </p>
                    </li>
                    <li>
                        <p>
                            <a href="../data/enwiki20160305/edited/enwiki-20160305-redirect.main.tsv.gz"> Redirect Table</a>
                        </p>
                        Layout:
                        <p>
                            <code> rd_from , rd_to </code>
                        </p>
                        <p>As stated in the paper, out-links are shorter and leads to faster process. If you want to
                            get the full embedding for a word, find both its in-embedding and out-embedding and add
                            them up.
                        </p>
                    </li>
                    <li>
                        <p>
                            <a href="../data/enwiki20160305/edited/enwiki-20160305-pagelinksorderedin.main.tsv.gz">Embeddings (in-links)</a>
                        </p>
                        <ul>
                            <li>Layout:
                                <p>
                                    <code> page_id , embedding as a pickled tuple(ids, values) </code>
                                </p>
                            </li>
                            <li>
                                <b>Note</b>
                                The second field is a binary string and needs to be properly unescaped. 
                            The following function, defined in the
                                <code>utils module</code> in the
                                <a href="https://github.com/asajadi/wikisim/blob/master/wikisim/wikisim.ipynb#Utils">Wikisim notebook</a>, can read the embedding file.
                                <p>
                                    <code>read_embedding_file(filename, records_number)</code>
                                </p>
                            </li>
                        </ul>
                    </li>
                    <li>
                        <p>
                            <a href="../data/enwiki20160305/edited/enwiki-20160305-pagelinksorderedout.main.tsv.gz">Embeddings (Out-Links) </a>
                        </p>
                        <ul>
                            <li>Layout:
                                <p>
                                    <code> page_id , embedding </code>
                                </p>
                            </li>
                            <li>
                                <b>Note</b>
                            </li>
                            <p>Similar to the above explained sutuation with pagelinksorderedin, you need to use
                                <code>read_embedding_file(filename, records_number)</code> to read the file. </p>
                        </ul>
                    </li>                    
                </ol>
            </div>
        </div>
    </div>
    <div class="panel-group">
        <div class="panel panel-default">
            <div class="panel-heading">
                <a name="hosting"></a>
                <h2>Hosting Wikisim</h2>
            </div>
            <div class="panel-body">
                You can run Wikisim locally and freely modify the source code.
                <h3>Step 1. </h3> Prepare the environement
                <ul>
                    <li>Install
                        <a href="https://conda.io/docs/user-guide/install/index.html">conda</a>
                    </li>
                    <li>
                        <p>run</p>
                        <code>conda env create -f environment.yml</code>
                    </li>
                </ul>
                <h3> Step 2. Clone the <a href="https://github.com/asajadi/wikisim">Source Code</a></h3>
                It is mostrly written in Python. The repository contains several files, but the following two notbooks are the main entries
                to the source code and contain all the core features of the system
                <ul>
                    <li>
                        <a href="https://github.com/asajadi/wikisim/blob/master/wikisim/wikisim.ipynb"> wikisim.ipynb notebook </a>: Contains the
                        <em>embedding</em> and
                        <em>relatedness</em> methods.
                    </li>
                    <li>
                        <a href="https://github.com/asajadi/wikisim/blob/master/wikify/wikify.ipynb"> wikify.ipynb notebook </a>: Contains the
                        <em>word-sense disambiguation</em> and
                        <em>entity linking</em> methods.
                    </li>
                </ul>
                Having prepared the conda environement, you have two options for Step 3:
                <h3> Step3.</h3> Preparing the MariaDB and Apache Solr servers
                <h3>Option 1. Downloading the prepared servers</h3>
                <p>This option saves you a lot of time if it works! It requires the following two steps:</p>
                <p>You can download our MariaDB server and Solr Cores. If you are using Linux, there is a chance that
                    you can download the whole servers and they work out-of-the box.</p>
                <ul>
                    <li>
                        <a href="../wikipedia/mariadb-10.1.13-linux-x86_64-prembeddings.tar">Download MariaDB (+graph tables)</a>
                    </li>
                    <li>
                        <a href="../wikipedia/solr-6.0.0-context.tar">Download Solr (+text cores)</a>
                    </li>
                </ul>
                <h3>Option 2. Starting from the scratch and importing a different version of Wikipedia</h3>
                It requires downloading and preprocessing the Wikipedia dumps and extracting the graph-structure and textual information
                from them. The whole process can be done in two major steps:
                <ul>
                    <li>Setting up a MariaDB server and preparing the graph-strcuture.
                        <p>The full instruction is given in
                            <a href="https://github.com/asajadi/wikisim/blob/master/preparation_scripts/db/prepare_graph_db.ipynb">this jupyter notebook </a>
                        </p>
                    </li>
                    <li>Processing the text and setting up the Apache Solr
                        <p>The full instruction is given in
                            <a href="https://github.com/asajadi/wikisim/blob/master/preparation_scripts/text/prepare_annonated_indexed_wiki.ipynb">this jupyter notebook </a>
                        </p>
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <div class="panel-group">
        <div class="panel panel-default">
            <div class="panel-heading">
                <a name="about"></a>
                <h2> About </h2>
            </div>
            <div class="panel-body">
                <p>
                    Wikisim was developed in
                    <a href="https://projects.cs.dal.ca/malnis/">
                        Machine Learning and Networked Information Spaces (MALNIS) Lab</a> at Dalhousie University.
                    This research was funded by the Natural Sciences and Engineering Research Council of Canada (NSERC),
                    the Boeing Company, and Mitacs</p>
                <p>
                    <h3>
                        Contributors:</h3>
                </p>
                <ul>
                    <li>
                        <a title="Armin Sajadi" href="http://projects.cs.dal.ca/visualtextanalytics/people/sajadi/">Armin Sajadi</a> - Faculty of Computer Science
                    </li>
                    <li>
                        Ryan Amaral- Faculty of Computer Science
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <div class="panel-group">
        <div class="panel panel-default">
            <div class="panel-heading">
                <a name="contact"></a>
                <h2> Contact </h2>
            </div>
            <div class="panel-body">
                <h3>
                    <a title="Armin Sajadi" href="http://web.cs.dal.ca/~sajadi/">Armin Sajadi</a>
                </h3>
                We appreciate and value any question, special feature request or bug report, just let us know at:
                <br>
                <a href="mailto:sajadi@cs.dal.ca?Subject=Wikisim">sajadi@cs.dal.ca</a>
                <br>
                <a href="mailto:asajadi@gmail.com?Subject=Wikisim">asajadi@gmail.com</a>
            </div>
        </div>
    </div>
</div>
