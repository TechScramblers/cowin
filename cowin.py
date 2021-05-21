#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
url2 ="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin"
PARAMS = {'Accept-Language':'hi_IN','pincode':'282005', 'date':'18-05-2021'}
headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}
r = requests.get(url = url2 ,headers=headers, params = PARAMS)
data = r.json()

print(data)

print()
print()

for center in data['sessions']:
    print(center['name'] ,' :', center['available_capacity'])
    for slot in center['slots']:
        print(slot)


# In[ ]:




