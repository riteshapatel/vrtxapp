####################################
# @class Auth Middleware 
# @author ritesh.patel 
# @email ritesh@line89.com
####################################
import jwt 
import falcon 
import json 

USERS = ['rpatel@yahoo.com', 'admin@yahoo.com']
JWT_SECRET = 'VrtxApp'
JWT_ALGO = 'HS256'

class AuthMiddleware(object):
    def process_request(self, req, resp):
        '''processes JWT token'''
        arr = req.url.rsplit('/', 1)
        endpoint = arr[1]
        
        if (endpoint == 'login'):
            return True
        else:
            token = req.get_header('Authorization')
            if token is None:
                description = ('Please provide an auth token as part of the request')

                raise falcon.HTTPUnauthorized('Auth token required', description)
            else:
                decoded = jwt.decode(token, JWT_SECRET, JWT_ALGO)
                print decoded
                if (decoded['email'] in USERS):
                    return True
                else:
                    return False
        