####################################
# @class Instruments listing
# @author ritesh.patel 
# @email ritesh@line89.com
####################################
import falcon
from Connection import Connection
import json 

class Instruments(object):
    def on_get(self, req, resp):
        """Get DB Connection"""
        conn = Connection()
        db = conn.get_db()
        data = {}

        for item in db.view('_design/list/_view/instruments'):
            key = item.key
            value = item.value 
            data[key] = value
        
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = json.dumps({'status': 'success', 'data': data}, sort_keys=True, indent=4)
    
    def on_post(self, req, resp):
        '''proceses post requests'''
        conn = Connection()
        db = conn.get_db() 
        
        try:
            raw_json = req.stream.read() 
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', ex.message) 
        
        try:
            result_json = json.loads(raw_json, encoding='utf-8')
            doc_id, doc_rev = db.save(result_json)
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400, 'Malformed JSON', 'Could not decode the request body')

        resp.status = falcon.HTTP_202 
        resp.body = json.dumps({'status': 'success', 'data': result_json}, encoding='utf-8')