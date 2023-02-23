# Lab 10b

# Use the Request library
import requests

# Set the target webpage
url = 'http://www.wikipedia.org'


# Perform a GET request on the target website
webpage = requests.get(url)
# This will print the full webpage in text
print(webpage.text)


# Display an "OK" return status code
print("Status code:")
print("\t *", webpage.status_code)


# Display the website header
h = requests.head(url)
print("Header:")
print("**********")
# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")


# Modify the Header user-agent to display "iPhone 14"
headers = {'User-Agent': 'Mobile'}
# Test against test site that output the requester user-agent
url2 = 'http://httpbin.org/headers'
url2 = 'http://172.18.58.80/headers.php'
request_header = requests.get(url2, headers=headers)
print(request_header.text)

