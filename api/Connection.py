####################################
# @class CouchDB Connection
# @author ritesh.patel 
# @email ritesh@line89.com
####################################
import couchdb

class Connection(object):
    '''sets couchdb connection string'''
    def __init__(self):
        self.couch = couchdb.Server('http://admin:admin@localhost:5984')
        self.db = self.couch['vrtxdb'] 
    
    def get_db(self):
        '''returns database connection'''
        return self.db
