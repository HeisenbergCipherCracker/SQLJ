import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = "http://testfire.net/login.jsp"
# requests.packages.urllib3.disable_warnings()  #! Disable SSL warnings for http requests and testing

response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

# Find the database table elements
table_elements = soup.find_all("table")
if table_elements is not None:
# Print the table names or perform further processing
    for table_element in table_elements:
        print(table_element.get("name"))
else:
    print("No table elements found")