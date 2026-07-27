# import requests
# response=requests.get("https://www.google.com")
# print(response.text)

# url="https://jsonplaceholder.typicode.com/posts"

# data={
#     "title": 'Coding',
#     "Language": 'Python',
#     "Version": '3.13.7',
# }
# headers={
#     'Content-type': 'application/json;charset=UTF-8',
# }
# response=requests.post(url, headers = headers,json=data)
# print("\n")
# print(response.text)

# requests Python ki wo library hai jo aapke code ko internet se jodti hai. Ise aap ek waiter samajh sakte hain jo aapka order (Request) lekar kitchen (Server) jaata hai aur wahan se khana (Response) wapas laata hai

import requests
def joke():
    url="https://official-joke-api.appspot.com/random_joke"
    response=requests.get(url)
    data=response.json()
    # print(f"type:  {data['type']}")
    print(f"setup:  {data['setup']}")
    print(f"Punchline: {data['punchline']}")
    # print(f"id: {data['id']}")
joke()