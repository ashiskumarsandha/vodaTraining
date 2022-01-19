#Add Package
import requests

url="https://api.github.com/users/ashiskumarsandha"

res=requests.get(url)

print(res.content)