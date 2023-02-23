# Lab 10b

# Use the Request library
import requests
# target webpage
url = 'http://172.18.58.80/snow'
webpage = requests.get(url)
print(webpage.text)

# Status code
print("Status Code:")
print("\t *", webpage.status_code)

# website headers
h = requests.head(url)
print("Header:")
print("**********")
# print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")

# modify the headers user-agent
headers = {'User-Agent': 'Mobile'}
# testing the modified header
url2= 'http://172.18.58.80/headers.php'
request_header = requests.get(url2, headers=headers)
print(request_header.text)

