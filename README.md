## VrtxApp with VueJs, Python Falcon, JWT & CouchDB

Author: Ritesh Patel | Last Updated: Dec 4, 2017

## Overview

This is a simple VueJs app with Python Falcon API & CouchDB persistent store. REST api is designed with Falcon. It uses a JWT token based authentication model. User logs into the app and adds / lists lab instruments from CouchDB.

### NGINX Setup

App sits behind NGINX with gunicorn proxied to serve the API endpoints. Below is a sample proxy setting. Gunicorn is started on port 8000.

```shell
location / {
    root   /users/ritesh.patel/websites/vrtxapp;
    index  index.html index.htm;
}

location /api/ {
    proxy_pass http://localhost:8000/;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection 'upgrade';
    proxy_set_header Host $host;
    proxy_cache_bypass $http_upgrade;
}
```

### CouchDB Setup

I am using CouchDB 2.1.1 with Fauxton. Database is listening on a standard default port 5984. Install CouchDB locally and create a database ```vrtxdb```. 

### App configuration 

Setup NGINX with gunicorn proxy. Fire up app @ http://localhost:8080/. If all setup correctly you should see the app login page. 

### App login

Use admin@yahoo.com / password to log into the app

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