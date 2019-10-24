import requests
from urlparse import urlunparse
from requests.auth import HTTPBasicAuth
import json

def simple_get_request(host, username, password, resource):
    """
    A simple Get Request. GET the value from the URL.
    :param host: The URL to the server
    :param username: The API username
    :param password: The API password
    :param resource: The URI representing the API operation to perform
    :return: A Requests Response type object
    """
    # build the URL
    url = urlunparse(('https', host, resource, None, None, None))
 
    print "GET: %s" % url

    return requests.get(url, auth=HTTPBasicAuth(username, password), verify=False)

def sample_post_request(host, username, password, resource, data):
   """
   A Simple POST request to the API Server
   :param host: The URL to the server
   :param username: The API username
   :param password: The API password
   :param resource: The URI representing the API operation to perform
   :param data: A JSON object holding the data for the POST request.
   :return: A Requests Response type object
   """
   # build the URL
   url = urlunparse(('https', host, resource, None, None, None))
   print "POST: %s" % url

   return requests.post(url, json=data, auth=HTTPBasicAuth(username, password), verify=False)


def sample_patch_request(host, username, password, resource, data):
   """
   A Simple PATCH request to the API Server
   :param host: The URL to the server
   :param username: The API username
   :param password: The API password
   :param resource: The URI representing the API operation to perform
   :param data: A JSON object holding the data for the PATCH request.
   :return: A Requests Response type object
   """
   # build the URL
   url = urlunparse(('https', host, resource, None, None, None))
   print "PATCH: %s" % url

   return requests.patch(url, json=data, auth=HTTPBasicAuth(username, password), verify=False)

def sample_delete_request(host, username, password, resource):
   """
   A Simple DELETE request to the API Server
   :param host: The URL to the server
   :param username: The API username
   :param password: The API password
   :param resource: The URI representing the API operation to perform
   :return: A Requests Response type object
   """
   # build the URL
   url = urlunparse(('https', host, resource, None, None, None))
   print "PATCH: %s" % url

   return requests.patch(url, json=data, auth=HTTPBasicAuth(username, password), verify=False)



#Performing a sample GET Request as an example
host = "X.X.X.X"
username = "username"
password = "password"
resource = "resource-url"

#Getting the preliminary response 
response = simple_get_request(host,username,password,resource)

#simple check for response
if response.status_code != 200:
  print('An error has occurred.')
else:
  #Getting the response in json Format
  json_response = response.json()

  #Convert the JSON response to dictionary for further automation possibilities
  dict_response = json.loads(json_response)

  #From this point on, one would simple take the expected response output and use the variables 
  #for further automation processes 
