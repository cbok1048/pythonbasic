#!/usr/bin/env python
# coding: utf-8

# In[7]:


#필요한 모듈 설치 #인터넷 연결 모듈 #사진 관련 모듈 #그림 관련 #사진관련


# In[10]:


get_ipython().system('pip install pillow')
get_ipython().system('pip install requests')


# In[19]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg

get_ipython().run_line_magic('matplotlib', 'inline')


# In[20]:


img = mpimg.imread('face1.jpg')

plt.figure(figsize= (10,8))
plt.imshow(img)
plt.show()


# In[28]:


import requests  # 인터넷 연결

client_id = "UtgUj1KnH2vFy2bFGeot"
client_secret = "UyWCQZ3DPB"

url = "https://openapi.naver.com/v1/vision/celebrity"
files = {'image':open('face1.jpg','rb')}
headers = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret': client_secret}

response = requests.post(url, files = files, headers = headers)

get_ipython().run_line_magic('matplotlib', 'inline')


# In[25]:


import json   # json형식을 다루는 모듈
parsed = json.loads(response.text)
print(json.dumps(parsed, indent = 4, sort_keys=False, ensure_ascii=False))


# In[32]:


import requests  # 인터넷 연결 face 는 얼굴인식 감정표현

client_id = "UtgUj1KnH2vFy2bFGeot"
client_secret = "UyWCQZ3DPB"

url = "https://openapi.naver.com/v1/vision/face"
files = {'image':open('face1.jpg','rb')}
headers = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret': client_secret}

response = requests.post(url, files = files, headers = headers)

get_ipython().run_line_magic('matplotlib', 'inline')


# In[33]:


import json   # json형식을 다루는 모듈
parsed = json.loads(response.text)
print(json.dumps(parsed, indent = 4, sort_keys=False, ensure_ascii=False))


# In[34]:


#####################
#기본문법
#####################


# In[36]:


# dic형과 json에 대해 

dict=  {
    'Name': 'pinkwink'
    ,'Age':'None'
    ,'Class':['beginner', 'blog']
}
dict


# In[38]:


dict.keys()


# In[39]:


dict.values()


# In[41]:


dict['Class']


# In[42]:


dict.get('Name')


# In[43]:


dict.get('Room','nothing')


# In[44]:


########################
#json (Java Script Object Notation)
########################


# In[51]:


customer = {
    'id':'0001',
    'name' : '홍길동',
    'history':[
        {'date': '2019-03-01', 'log': True},
        {'date': '2019-03-02', 'log': False}
    ]
}


# In[52]:


import json
json_test = json.dumps(customer, indent=4, ensure_ascii=False)
print(json_test)


# In[54]:


##################################
#사진위에 개인정보 표시
##################################


# In[55]:


img = mpimg.imread('face1.jpg')

plt.figure(figsize= (10,8))
plt.imshow(img)
plt.show()


# In[56]:


import requests  # 인터넷 연결 face 는 얼굴인식 감정표현

client_id = "UtgUj1KnH2vFy2bFGeot"
client_secret = "UyWCQZ3DPB"

url = "https://openapi.naver.com/v1/vision/face"
files = {'image':open('face1.jpg','rb')}
headers = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret': client_secret}

response = requests.post(url, files = files, headers = headers)

get_ipython().run_line_magic('matplotlib', 'inline')


# In[57]:


import json   # json형식을 다루는 모듈
parsed = json.loads(response.text)
print(json.dumps(parsed, indent = 4, sort_keys=False, ensure_ascii=False))


# In[60]:


parsed.keys()


# In[62]:


parsed['faces'][0][r]


# In[69]:


parsed['faces'][0]['gender']


# In[84]:


x, y, w ,h = parsed['faces'][0]['roi'].values()
gender,gen_confi = parsed['faces'][0]['gender'].values()
emotion,emo_confi = parsed['faces'][0]['emotion'].values()
pose,po_confi = parsed ['faces'][0]['pose'].values()


# In[85]:


annotation = gender +" : " + str(gen_confi) + "\n" +emotion + " : " + str(emo_confi) + "\n" +pose + " : " + str(po_confi)
        


# In[72]:


print(x)


# In[73]:


print(y)


# In[74]:


print(w)


# In[75]:


print(h)


# In[78]:


print(gender)


# In[131]:


print(annotation)


# In[132]:


import matplotlib.patches as patches
img = mpimg.imread('face1.jpg')
fig, ax= plt.subplots(figsize= (10,10))
ax.imshow(img)

rect_face = patches.Rectangle((x,y),w,h,linewidth= 5,edgecolor = 'r',facecolor = 'none')
ax.add_patch(rect_face)

plt.text(10,400, annotation, wrap= True, fontsize = 17,color = 'white')
plt.show()


# In[115]:


img = mpimg.imread('face2.jpg')

plt.figure(figsize= (10,8))
plt.imshow(img)
plt.show()


# In[116]:


import requests  # 인터넷 연결 face 는 얼굴인식 감정표현

client_id = "UtgUj1KnH2vFy2bFGeot"
client_secret = "UyWCQZ3DPB"

url = "https://openapi.naver.com/v1/vision/face"
files = {'image':open('face2.jpg','rb')}
headers = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret': client_secret}

response = requests.post(url, files = files, headers = headers)

get_ipython().run_line_magic('matplotlib', 'inline')


# In[117]:


import json   # json형식을 다루는 모듈
parsed = json.loads(response.text)
print(json.dumps(parsed, indent = 4, sort_keys=False, ensure_ascii=False))


# In[118]:


parsed.keys()


# In[121]:


parsed['faces'][1]['roi']


# In[138]:


for each in parsed['faces']:
    x, y, w ,h = each['roi'].values()
    gender,gen_confi = each['gender'].values()
    emotion,emo_confi = each['emotion'].values()
    pose,po_confi = each['pose'].values()


# In[139]:


annotation = gender +" : " + str(gen_confi) + "\n" +emotion + " : " + str(emo_confi) + "\n" +pose + " : " + str(po_confi)


# In[177]:


import matplotlib.patches as patches
img = mpimg.imread('face2.jpg')
fig, ax= plt.subplots(figsize= (10,10))
ax.imshow(img)

rect_face = patches.Rectangle((x,y),w,h,linewidth= 2,
                              edgecolor = 'r',
                              facecolor = 'none')
ax.add_patch(rect_face)


plt.text(x-15,y-20, annotation, wrap= True, fontsize = 10,color = 'red')
plt.show


# In[180]:


import matplotlib.patches as patches

img = mpimg.imread('face2.jpg')

fig, ax = plt.subplots(figsize = (10,10))
ax.imshow(img)



for each in parsed['faces']:
    x,y,w,h = each['roi'].values()
    gender,gen_confi = each['gender'].values()
    emotion,emo_confi = each['emotion'].values()
    age,age_confi = each['age'].values()
    
    rect_face = patches.Rectangle((x,y),w,h,
                                 linewidth = 2,
                                 edgecolor = 'r',
                                 facecolor = 'none')
    ax.add_patch(rect_face)    
    
    annotation = gender + " : " + str(round(gen_confi,3)*100)+'%' + '\n' + emotion + " : " + str(round(emo_confi,2)*100)+'%' + '\n' + age + " : " + str(round(age_confi,2)*100)+'%'
    plt.text(x-10, y-20, annotation, wrap=True, fontsize=6, color = 'black')
    
plt.show()


# In[ ]:




