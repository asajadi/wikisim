# This scripts creates a database and starts importing the tables
# Usage: bash startimport.sh <dir> <vesrion> <user> <pass>
# Current version of the dumps is 20160305
#%%system
mysql -u $1 -p$2 -e 'CREATE SCHEMA `enwikilast` DEFAULT CHARACTER SET binary;'
./importall  ~/Downloads/wikidumps last $1 $2

