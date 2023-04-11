import hashlib
import random

# List of user accounts and their passwords
users = {'user1': 'password1', 'user2': '123456', 'user3': 'qwerty'}

# List of common passwords to check against
common_passwords = ['password', '123456', 'qwerty', '123456789', 'admin', 'letmein', 'welcome', 'monkey', 'dragon', 'baseball']

# Dictionary to store user authentication tokens
auth_tokens = {}

# Function to check if a password is weak
def is_weak_password(password):
    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    # Check if the hashed password is in the list of common passwords
    if hashed_password in [hashlib.sha256(common_password.encode('utf-8')).hexdigest() for common_password in common_passwords]:
        return True
    else:
        return False

# Function to generate a random authentication token
def generate_auth_token():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=16))

# Function to authenticate a user
def authenticate_user(username, password):
    # Check if the username exists in the user dictionary
    if username in users:
        # Check if the password is correct
        if users[username] == password:
            # Generate an authentication token and store it in the auth_tokens dictionary
            auth_token = generate_auth_token()
            auth_tokens[username] = auth_token
            return auth_token
        else:
            return None
    else:
        return None

# Function to verify a user's authentication token
def verify_auth_token(username, auth_token):
    # Check if the username exists in the auth_tokens dictionary
    if username in auth_tokens:
        # Check if the authentication token matches the stored token
        if auth_tokens[username] == auth_token:
            return True
        else:
            return False
    else:
        return False

# Loop through the user accounts and authenticate each user
for user, password in users.items():
    auth_token = authenticate_user(user, password)
    if auth_token:
        print(f'User {user} authenticated with token {auth_token}')
    else:
        print(f'Authentication failed for user {user}')

# Test the authentication tokens
for user, auth_token in auth_tokens.items():
    if verify_auth_token(user, auth_token):
        print(f'Authentication token verified for user {user}')
    else:
        print(f'Authentication token verification failed for user {user}')
