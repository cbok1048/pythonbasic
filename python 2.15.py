#!/usr/bin/env python
# coding: utf-8

# In[1]:


a =[1, 2, 3]


# In[2]:


id(a)


# In[3]:


a = b


# In[4]:


b = a


# In[5]:


a


# In[6]:


b


# In[7]:


input(a)


# In[8]:


a


# In[9]:


a[0] = 4


# In[10]:


a


# In[15]:


a[0:2

 ]


# In[16]:


a[:]


# In[17]:


a[1] = 13


# In[18]:


a


# In[19]:


b


# In[20]:


b = a[:]


# In[21]:


a[2] = 51


# In[22]:


a


# In[23]:


b


# In[24]:


a, b = 'python' , 'life'


# In[25]:


a


# In[26]:


b


# In[27]:


a, b =  b, a


# In[28]:


a


# In[31]:


#정수형 ~실수형~


# In[32]:


int(1)


# In[33]:


3.4e10


# In[34]:


float


# In[35]:


a = 14


# In[36]:


b = 2


# In[37]:


a + b


# In[38]:


a -  b


# In[39]:


a ** b


# In[40]:


a / b


# In[41]:


a // b


# In[42]:


a % b


# In[43]:


a %% b


# In[44]:


'"python is very easy." he says.'


# In[50]:


'\"python is  very easy.\" he says.'


# In[53]:


print('='* 100)


# In[54]:


a = "Life is good too short"


# In[55]:


len[a]


# In[56]:


len(a)


# In[57]:


a + ",you need python"


# In[58]:


a[0:15]


# In[64]:


a = "20210215 sunday"


# In[66]:


date =a[:4]


# In[67]:


year = a[:4]


# In[68]:


year


# In[69]:


day = a[5:7]


# In[70]:


day


# In[71]:


day=a[4:6]


# In[72]:


day


# In[73]:


'i eat %d apples' % 3


# In[75]:


odd = [1, 3, 5, 7, 9]


# In[78]:


a = []
b = [1, 2, 3]
c = ['life' , 'is', 'good']
d = [1, 2, 'life', 'is']
e = [1, 2, ['Life','is']]


# In[79]:


e


# In[80]:


a = [1 ,2 ,3]


# In[81]:


a[0]


# In[82]:


a[0] + a[2] 


# In[83]:


a[-1]


# In[94]:


a = [1, 2, 3,['a', 'b', 'c']]


# In[95]:


a


# In[96]:


a[0]


# In[97]:


a[-1][2]


# In[98]:


a = [1, 2, 3, 4, 5]


# In[99]:


a[0:2]


# In[100]:


a =[1, 2, 3]
b = [4, 5, 6]


# In[101]:


a + b


# In[102]:


len(a)


# In[106]:


a.append([5, 6])


# In[107]:


a


# In[108]:


a = [1, 4, 3, 2]


# In[109]:


a.sort()


# In[110]:


a


# In[113]:


a.reverse()


# In[114]:


a


# In[115]:


a.sort()


# In[116]:


a


# In[117]:


a.append([5, 6])


# In[118]:


a


# In[119]:


a.sort()


# In[120]:


a.remove(-1)


# In[121]:


a = [2, 3, 1]


# In[122]:


a.sort()
a.reverse()


# In[123]:


a


# In[125]:


a.insert(0,4)


# In[126]:


a


# In[127]:


a = [1, 2, 3, 1, 2, 3]


# In[128]:


a.remove(3)


# In[129]:


a


# In[130]:


a.remove(3)


# In[131]:


a


# In[137]:


a.remove(1)


# In[138]:


a


# In[135]:


a.remove(2)


# In[136]:


a


# In[139]:


a = [1, 2, 3]


# In[140]:


a.pop()


# In[141]:


a


# In[142]:


a.pop(0)


# In[143]:


a = [1, 2, 3, 4]


# In[146]:


a.count(1)


# In[147]:


a.extend([5, 6, 7])


# In[148]:


a


# In[149]:


########################
# tuple
########################


# In[150]:


t1 = ()
t2 = (1,) #요소가 하나일떈 쉼표를 꼭 넣는다
t3 = (1, 2, 3)
t4 = 1, 2, 3   #괄호 생략가능
t5 = ('a', 'b', ('ab', 'cd'))


# In[151]:


t2 * 2


# In[152]:


a = { 'a': [1,2,3]}


# In[153]:


a


# In[154]:


a = {1:'a'}
a[2] = 'b'
a


# In[156]:


a['name'] ='pay'
a


# In[157]:


a[3] = [1, 2, 3]


# In[162]:


a


# In[163]:


del a[2]


# In[164]:


a


# In[167]:


del a['name']


# In[168]:


a


# In[169]:


grade = {'pey':10, 'julliet': 99}


# In[173]:


grade['pey']


# In[174]:


a = {1: 'a', 2: 'b'}


# In[178]:


a[1]


# In[177]:


a[3]


# In[ ]:





# In[179]:


a[3] = c


# In[180]:


a


# In[181]:


c


# In[182]:


c = c


# In[183]:


c


# In[184]:


dic = {'name' : 'pey', 'phone': '0119993323', 'birth': '1118'}


# In[185]:


dic['name']


# In[186]:


dic['phone']


# In[187]:


a = {'name': 'pey', 'phone':'011992323', 'birht':'1118'}


# In[188]:


a.keys()


# In[191]:


a.values()


# In[196]:


for k in a.keys():
    print(k)


# In[199]:


a.get('phone')


# In[200]:


s1 = set([1, 2, 3])


# In[201]:


s1


# In[202]:


l1 = list(s1)


# In[203]:


l1


# In[204]:


t1 = tuple(s1)


# In[205]:


s1


# In[206]:


t1


# In[207]:


s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])


# In[208]:


s1 & s2


# In[209]:


s1. intersection(s2)


# In[211]:


s1 | s2


# In[213]:


s1.union(s2)


# In[214]:


s1 - s2


# In[215]:


s1.difference(s2)


# In[216]:


s1 = set([1, 2, 3])
s1.add(4)
s1


# In[221]:


s1 = set([1, 2, 3])
s1.update([4, 5, 6])
s1


# In[222]:


s1.remove(1)


# In[223]:


s1.remove(2)


# In[229]:


s1


# In[225]:


a = True
b = False


# In[226]:


type(a)


# In[227]:


type(b)


# In[230]:


1 == 1


# In[231]:


2 > 1


# In[232]:


2 < 1


# In[236]:


a = [1, 2, 3, 4]
while a:
    print(a.pop())


# In[238]:


a


# In[240]:


if []:
    print("참")
else:
    print("거짓")


# In[241]:


if [1, 2, 3]:
    print('참')
else:
    print("거짓")


# In[242]:


bool('python')


# In[243]:


bool('')


# In[244]:


bool(0)


# In[245]:


bool(3)


# In[246]:


국어 = 80
영어 = 75
수학 = 55


# In[247]:


국어, 영어, 수학//3


# In[248]:


(국어+영어+수학)//3


# In[249]:


a= 13


# In[250]:


a%2


# In[254]:


jumin = '881120-1068234'


# In[255]:


junum = jumin[:6]


# In[256]:


junum


# In[257]:


unm = jumin[7:]


# In[258]:


unm


# In[260]:


gender = jumin[7]


# In[261]:


gender


# In[262]:


###########################
# IF
###########################


# In[272]:


money = 0

if money:
    print('택시를')
    print('타고')
    print("가라")
else:
    print("택시를")
    print("타지마라")


# In[277]:


money = 2000
card = True
if money >=3000 or card:
    print("택시 타자")
else:
    print("걸어 가자")


# In[287]:


pocket = ['paper' , 'cellphone', 'money']

if 'money' in pocket:
    pass
else:
    print('카드를 꺼내라')


# In[290]:


pocket = ['paper' , 'handphone']
card = True
if 'money' in pocket:
     print('택시를 타고가라')
else:
    if card:
        print('택시를 타고가라')
    else:
        print('걸어가라')
        


# In[294]:


pocket = ['paper', 'cellphone']
card = True

if 'money' in pocket: pass
else: print('카드를 써라')
# if 'money' in pocket:
#     print('택시를 타고가라')
# elif card:
#     print('택시를 타고가라')
# else:
#     print('걸어가라')


# In[301]:



if score >= 60:
    message = "success"
else:
    message = "failure"


# In[302]:


#######################
#  While
#######################


# In[303]:


treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print('나무를 %d번 찍었습니다' % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다")


# In[305]:


treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print('나무를 %d번 찍었습니다' % treeHit)
    else treeHit
        print("나무 넘어갑니다")


# In[ ]:


treeHit = 0
while treeHit < 10:
    treeHit = treeHit += 1
    print('나무를 %d번 찍었습니다' % treeHit)
    else treeHit
        print("나무 넘어갑니다")


# In[ ]:


prompt = """
1. Add
2. Del
3. List
4. Quit
...
Enter number:
"""

number = 0 
while number != 4 :
    print(prompt)
    number = int(input())


# In[ ]:





# In[ ]:




