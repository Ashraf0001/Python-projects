
# This is the extended version of code with two factor authentication

import hashlib
import random

# List of user accounts and their passwords
users = {'user1': 'password1', 'user2': '123456', 'user3': 'qwerty'}

# List of common passwords to check against
common_passwords = ['password', '123456', 'qwerty', '123456789', 'admin', 'letmein', 'welcome', 'monkey', 'dragon', 'baseball']

# Function to check if a password is weak
def is_weak_password(password):
    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    # Check if the hashed password is in the list of common passwords
    if hashed_password in [hashlib.sha256(common_password.encode('utf-8')).hexdigest() for common_password in common_passwords]:
        return True
    else:
        return False

# Function to generate a random code for two-factor authentication
def generate_code():
    return random.randint(100000, 999999)

# Loop through the user accounts and check their passwords
for user, password in users.items():
    if is_weak_password(password):
        print(f'Weak password detected for user {user}: {password}')
    else:
        # Generate a random code for two-factor authentication
        code = generate_code()
        print(f'Two-factor authentication code for user {user}: {code}')
        # Prompt the user to enter the code
        user_code = input('Enter the code: ')
        # Check if the code entered by the user is correct
        if int(user_code) == code:
            print(f'Authentication successful for user {user}')
        else:
            print(f'Authentication failed for user {user}')
