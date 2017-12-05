#######################################
# @class Login processor with JWT token
# @author ritesh.patel 
# @email ritesh@line89.com
######################################
import jwt 
import falcon 
import json 

USERS = ['rpatel@yahoo.com', 'admin@yahoo.com']
JWT_SECRET = 'VrtxApp'
JWT_ALGO = 'HS256'

class ProcessLogin():
    '''processes post request'''
    def on_post(self, req, resp):
        try:
            raw_json = req.stream.read() 
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', ex.message) 
        
        try:
            result_json = json.loads(raw_json, encoding='utf-8')
            if (result_json['email'] in USERS):
                data = {'status': 'success', 'data': jwt.encode(result_json, JWT_SECRET, JWT_ALGO)}
            else:
                data = {'status': 'failure', 'data': 'Error generating token'}
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400, 'Malformed JSON', 'Could not decode the request body')

        resp.status = falcon.HTTP_202 
        resp.body = json.dumps(data, encoding='utf-8')        