####################################
# @class Processes welcome route
# @author ritesh.patel 
# @email ritesh@line89.com
####################################
import falcon
class VrtxWelcome(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('Welcome to Vrtx Api')