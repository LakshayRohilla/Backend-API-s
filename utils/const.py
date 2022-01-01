"""
In this we will be addind JWT information, the info that is required.
What all info is required you can have a look on its docs and you will get an idea about it.
Documentation - JWT token docs.
"""
JWT_SECRET_KEY = "secret_key"
"""
Here, we have option to add this key by yourself 
or
Run - "openssl rand -hex 32" , this approach is best to follow.
This command will return some random generated value 
"""
JWT_ALORITH = "HS256"
# You get this value from the docs, basically we mostly use this algo from the available one
JWT_EXPIRATION_TIME_MINUTES = 60 * 24 * 5

