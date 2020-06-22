import requests

url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"

headers = {
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
    'x-rapidapi-key': "70ea83bd4bmsh68c7b5c1ac58be1p12899djsnf077076a9195"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
