## VrtxApp with VueJs, Python Falcon, JWT & CouchDB

Author: Ritesh Patel | Last Updated: Dec 4, 2017

## Overview

This is a simple VueJs app with Python Falcon API & CouchDB persistent store. REST api is designed with Falcon. It uses a JWT token based authentication model. User logs into the app and adds / lists lab instruments from CouchDB.

### NGINX Setup

App sits behind NGINX with gunicorn proxied to serve the API endpoints.

### Tools Used

- VueJs
- Python Falcon API
- CouchDB
- JWT Token (pyJwt)

### Gotchas

I had to put together this app in less than a day (non-paid :)) and therefore I have taken some shortcuts. As it stands, User is validated against a local array. Additionally, decoded JWT token is not doing any validation against the payload yet.

### Contact

Gimme a holler if you have an exciting project for me :) Fork and enjoy!

Ritesh Patel
ritesh@line89.com