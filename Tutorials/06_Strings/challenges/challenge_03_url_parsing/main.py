"""
  URL Parsing Project
  --------------------
  This program will parse an URL and returns three parts of it, i.e. - (1) The Protocol part, (2) The Domain Name part, and (3) The Page/Query String part 
"""

url = input("Enter an URL: ")

parsed_url = url.split("/")
protocol = parsed_url[0].rstrip(":")
domain = parsed_url[2]
domain_name = domain.split(".")[1]
page = "/" + parsed_url[3]

print(
    f"The parsed URL is:\nProtocol: {protocol}\nDomain Name: {domain_name}\nPage: {page}")
