"""
Making this file for security function, # v19(Authentication)
separate file is always good as to keep the code clean.
"""
from passlib.context import CryptContext

"""We are using passlib to hash our password so that they could get encrypt"""

pwd_context = CryptContext(schemes=["bcrypt"])
from models.jwt_user import JWTUser

"""
We need 2 functions,
1) Function will hash plan password
2) Function will verify if the plain password is same as the hashed password. 
"""


def get_hashed_password(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except Exception as e:
        return "Error occurred **Not Matched**"


# hashed = "$2b$12$ICQ72wTQI6xWrC5v2HILBu2MUwQZobq/XMNBSZ4NZwdel44MbYYDS"

# print(get_hashed_password("Shweta"))
"""
Above line output - $2b$12$ICQ72wTQI6xWrC5v2HILBu2MUwQZobq/XMNBSZ4NZwdel44MbYYDS.
And we are saving it in a variable so that we can verify it in second function. 
"""

# print(verify_password("Shweta", hashed))
"""
This will return True if both the password matches.
"""

"""
Now lets pass JWT part.
First, we need to authenticate username and password to give JWT token to the user. 
User sends its username and password to get the JWt token.
And we need to verify if the username and password is correct or not.
"""

# Authenticate username and password to give JWT token.
""" Before making this function we are making endpoint.
    After making the endpoint, to continue we will make a model(JWT_user)"""

# Create access Jwt token.

# Checks whether JWT token is correct or not.

# Lastly, check some other constraint for us and return final results
