####################################
# @class falcon api entrypoint 
# @author ritesh.patel 
# @email ritesh@line89.com
####################################
import falcon
import VrtxWelcome
import Login
import List
from AuthMiddleware import AuthMiddleware


# falcon.API instance with auth middleware
app = falcon.API(middleware=[AuthMiddleware()])

# set up welcome / instruments & login processors
welcome = VrtxWelcome.VrtxWelcome()
instruments = List.Instruments()
login = Login.ProcessLogin()

# define routes
app.add_route('/', welcome)
app.add_route('/instruments', instruments)
app.add_route('/login', login)
