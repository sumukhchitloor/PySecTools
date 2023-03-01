import requests

# Set the URL or IP address to connect to
url = 'http://www.example.com'

# Make a GET request to the URL or IP address
response = requests.get(url)

# Display the response status code and content
print(f'Status code: {response.status_code}')
print('Response content:')
print(response.content.decode())
