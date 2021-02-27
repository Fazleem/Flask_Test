import requests

BASE = "http://127.0.0.1:5000/"
data = [{"name":"fazleem","views":1000,"likes": 10},
        {"name":"How to make a figma page","views":34343,"likes": 434},
        {"name":"Python tutorial","views":1000,"likes": 4343}
        ]
for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/1")
print(response.json())
input()


response = requests.get(BASE + "video/6", {"likes": 10})
print(response.json())