#!/usr/bin/env python
# coding: utf-8

# In[1]:


i = 0
while i < 3:
    i=i+1
    print(i)


# In[4]:


for a in (1,2,3):
    print(a)


# In[5]:


# for 문과 while 문은 같다 for 문은 명확할떄 쓰임


# In[7]:


def add(a,b):    # 함수 정의
    return a + b
add(3,4)


# In[9]:


#######################################
# 숫자형
#######################################


# In[10]:


# 제곱 ** 


# In[12]:


#나머지 연산자


14 % 3


# In[13]:


3 % 7


# In[14]:


13 % 2 # 2로나눈 나머지가 0이면 짝수 1이면 홀수


# In[17]:


30 % 5 # 특정수로 나누었을떄 값이 0이면 특정수의 배수이다


# In[18]:


7 / 4 


# In[23]:


7 // 4


# In[24]:


##############################
#문자형
##############################


# In[25]:


"hello world"


# In[26]:


'python is fun'


# In[27]:


"""life is too short, you need python"""


# In[29]:


"python's favorite food is perl"


# In[30]:


'"python is very easy."  he says'


# In[32]:


'python\'s favorite food is perl'


# In[45]:


multiline = "life is too short you need python"


# In[57]:


multiline


# In[53]:


mutiline = """
Life istoo short 
you need python
"""


# In[54]:


head = 'python'
tail = ' is fun'
head + tail


# In[56]:


a = 'python'
a * 2


# In[60]:


multiline = "life is too short \n you need python"


# In[61]:


print('=' * 50)
print("My program")
print('=' * 50)


# In[62]:


print("#" * 50)
print("#len 함수 - 길이를 구한다 ")
print('#' * 50)


# In[63]:


a = 'life is good'
len(a)


# In[73]:


a = 'Life is too short. you need python'


# In[77]:


a[3] # 파이썬은 0부터 시작 f가 아니라 e인 이유 (R은 1에서 부터 시작) 인덱싱


# In[78]:


a[-1]


# In[79]:


a[-0]


# In[80]:


a[0:4]


# In[85]:


a[0:3] #0123 으로 4개를 가져와야하지만 슬라이싱은 미만판정이라 마지막 은안가져옴 


# In[86]:


len(a)


# In[87]:


a[0:34]


# In[88]:


a[0:35]


# In[89]:


a[0:333]


# In[90]:


a[0:33]


# In[91]:


a[5:7]


# In[92]:


a[19:]


# In[93]:


a[:17]


# In[94]:


a[:]


# In[95]:


a[19:-7]


# In[96]:


a = '20010331Rainy'


# In[104]:


date = a[4:8]


# In[105]:


date


# In[106]:


weather = a[8:]


# In[107]:


weather


# In[108]:


year = a[:4]


# In[109]:


year


# In[110]:


date


# In[111]:


weather


# In[113]:


b = "simbo gold player"


# In[116]:


id = b[:5]


# In[117]:


id


# In[118]:


a = 'pithon'


# In[120]:


a[1] = y


# In[121]:


#문자열 포멧팅


# In[123]:


"i eat %d apples" % 3 #%d 숫자문자열 포멧코드


# In[124]:


"i eat %d apples" % 10 


# In[127]:


"i eat %s apples" % "five" # %s 문자열 포멧코드


# In[129]:


number = 3
"i eat %d apples" % number #변수로 대입  


# In[130]:


number = 10
day = "three"
" i ate %d apples. so i was sick for %s days" %(number,day)


# In[131]:


" i ate %d%%" %12


# In[133]:


"%10s" %"hi"


# In[134]:


"%-10sjane" %"hi"


# In[136]:


'%f' %3.421343


# In[137]:


'%0.4f' %3.421343


# In[138]:


'%46.4f' %3.421343


# In[140]:


'i eat {0} apples'.format(3) # 다른방법


# In[141]:


'i eat {0} apples'.format('five')


# In[143]:


number = 10
day ="three"


# In[144]:


"i ate {0} apples. so i was sick for {1} days.".format(number,day)


# In[146]:


"i ate {number} apples so i was sick for {day} days". format(number=10,day=3)


# In[147]:


"simbo is {0} palyer".format("gold")


# In[148]:


"i ate {0} apples . so i was sick for {day} days". format(10, day=2)


# In[149]:


'{0:<10}'.format("hi")


# In[150]:


"{0:^10}".format("hi")


# In[156]:


a = 'hobby' #위치 알려주기
a.count('b')


# In[157]:


a = 'python is the best choice'
a.count('b')


# In[160]:


a.find(b)


# In[154]:


a = "life is too short"


# In[155]:


a.index('t')


# In[165]:


'.'.join('abcd') # 삽입


# In[166]:


' '.join('abcd')


# In[170]:


a = 'hi'
a.upper()


# In[174]:


a = 'HI'
a.lower()


# In[175]:


a


# In[178]:


a = ' hi '
a.strip() #strip 앞에 r이나l 넣었을떄 방향대로 지워줌


# In[181]:


a = "life is too short"
a.replace("life", "your leg") #교체


# In[183]:


a = "life is short"
a.split()     #문자 나누기 자르기


# In[184]:


b = 'a:b:c:d'
b.split(':') 


# In[198]:


b = 'a:b:c:d'
b.split(-:-)


# In[200]:


############################################

# 리스트 자료형

############################################


# In[212]:


#리스트이름 = [요소1,요소2,요소3 ...]   리스트 =대괄호사용[]

a = [] #공리스트
b = [1,2,3,]
c = ['life', 'is', 'too', 'short']
d = [1, 2, 'life', 'is'] #숫자 문자 조합
e = [1, 2, ['life, 'too']]      


# In[208]:


a = [1,2,3]
a


# In[207]:


a[0]


# In[209]:


a[0] + a[2]


# In[210]:


a[-1]


# In[213]:


a = [1, 2, 3, ['a', 'b', 'c']]


# In[214]:


a[1]


# In[215]:


a[-1]


# In[216]:


a[-1][0]


# In[217]:


a = [1,2,3,4,5]
a[0:2] # 2는 포함하지 않는다


# In[218]:


a = [1, 2, 3, 4, 5]
a[0:2]


# In[219]:


a = [1, 2, 3]
b = [4, 5, 6]


# In[220]:


a + b


# In[222]:


a *3


# In[223]:


len(a)


# In[224]:


a = [1, 2, 3]


# In[225]:


a[2] + 'hi'


# In[230]:


str(a[2]) + '   hi' #스트링함수 


# In[231]:


# 리스트는 값을 수정,삭제 할수있다  튜플은 불가능하다


# In[232]:


a = [1, 2, 3]
a[2] = 4


# In[233]:


a


# In[234]:


a[-1] = 13


# In[235]:


a


# In[236]:


del a[1]


# In[237]:


a


# In[241]:


a = [1, 2, 3, 4, 5]
del a[2:]
a


# In[247]:


#리스트에 요소 추가 (많이쓴다)업뎃 a.append


# In[248]:


a = [1, 2, 3]
a. append(4)
a


# In[249]:


a.append([5, 6])


# In[250]:


a


# In[251]:


a = [1, 4, 2, 3]


# In[254]:


a.sort() #a 를 정리해라 순서대로


# In[255]:


a


# In[258]:


a = ['a', 'c', 'b']
a.reverse() # 단어 그대로 뒤집는다
a


# In[260]:


a = ['a', 'c', 'b']
a.sort()


# In[261]:


a


# In[262]:


a.reverse()


# In[263]:


a


# In[272]:


a = ['a', 'c', 'b']
a.sort()


# In[273]:


# INDEX 위치 변환 위치알려줌


# In[274]:


a = ['a', 'b', 'c']


# In[275]:


a.index('c')


# In[276]:


a.index('w')


# In[ ]:




