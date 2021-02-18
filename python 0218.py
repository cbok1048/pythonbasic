#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Fourcal:
    def setdata(self, first, second):
        self.first = first
        self.second = second


# In[2]:


a = Fourcal()


# In[3]:


a.setdata(4, 2)


# In[4]:


a.first


# In[5]:


a.second


# In[6]:


b = Fourcal()


# In[7]:


b.setdata(3,7)


# In[8]:


b.first


# In[9]:


class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result


# In[10]:


class Bird:
    def fly(self):
        raise NotImplementedError


# In[11]:


class Eagle(Bird):
    pass


# In[13]:


eagle = Eagle()
eagle.fly()


# In[14]:


class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()


# In[15]:


class MyError(Exception):
    pass


# In[19]:


def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)


# In[20]:


say_nick('천사')


# In[21]:


say_nick('바보')


# In[22]:


try:
    say_nick('천사')
    say_nick('바보')
except MyError:
    print('허용되지 않은 별명입니다')


# In[23]:


try:                 # 에러 메세지를 변경하고싶다
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(e)


# In[24]:


class MyError(Execption):
    def __str__(self):
        return "허용되지 않는 별명입니다."


# In[26]:


abs(-31) # 절댓값 구하기


# In[27]:


all([1, 2, 3])  #true fales 리스트중에 하나라도 false가있으면 false 표시


# In[28]:


all([0])


# In[31]:


any([1, 2, 3, 0]) # 하나만 트루면 트루리턴


# In[32]:


any([0])


# In[34]:


chr(97) # 아스키코드  ASCII


# In[35]:


dir([1, 2, 3])


# In[36]:


dir({'1':'a'})


# In[37]:


for i,name in enumerate(['body', 'foo', 'bar']):
    print(i, name)


# In[51]:


def positive(l):
    result = []
    for i in l:
        if  i > 0:
            result.append(i)
    return result


# In[52]:


print(positive([1,-3,2,0,-5,6]))


# In[53]:


def positive(x):
    return x > 0


# In[54]:


print(list(filter(positive, [1, -3, 2, 0, -5, 6])))


# In[55]:


len([1, 2, 3])


# In[56]:


list('python')


# In[57]:


list((1,2,3,))


# In[61]:


def two_times(numberList):
    result = []
    for number in  numberList:
        result.append(number*2)
    return result


# In[62]:


result = two_times([1,2,3,4])
print(result)


# In[64]:


max(1, 2, 3)


# In[65]:


max('python')#최댓값


# In[66]:


min([1, 2, 3])


# In[81]:


min('python')# 최솟값


# In[68]:


ord('a')


# In[69]:


list(range(5)) #레인지 거리~~~이거 개꿀


# In[70]:


list(range(5, 10))


# In[73]:


list(range(1, 10, 2))


# In[75]:


list(range(0, -10,-1))


# In[80]:


round(3.5) #반올림 


# In[79]:


round(5.563, 2)


# In[86]:


str(3124) # 문자형으로 돌려주는 함수이다


# In[84]:


sum([1, 2, 3]) #  모든 요소의 합을 돌려주는 함수이다


# In[88]:


a = [332, 342, 456]


# In[90]:


sum(a) / len(a)


# In[91]:


a.average


# In[95]:


list(zip([1, 2, 3], [4, 5, 6]))


# In[96]:


x= 50


# In[97]:


y = float(x) 


# In[98]:


type(x)


# In[99]:


str(x)


# In[100]:


type(x)


# In[101]:


type(float(x))


# In[103]:


x = y = z = 8 
print(y) 


# In[104]:


x = y = z = 300 


# In[105]:


x


# In[106]:


y


# In[107]:


z


# In[118]:


x = [[0.0, 1.0, 2.0],[4.0, 5.0, 6.0]]

y = x[1][0]+x[0][1]
print(y)


# In[120]:


x = [15, 45, 85, 95] 
print(x[3]-x[1]) 


# In[121]:


x = [5, 4, 3, 2]
print(x) 


# In[122]:


x = [5, 4, 3, 2] 
x.append(1) 
print(x) 


# In[123]:


x = [5, 4, 3, 2]
x.insert(1, 0)
print(x)


# In[124]:


x < y


# In[127]:


x = 72 
y = 64
print(x < y)


# In[130]:


if (y % 2 == 0):
    print(y)


# In[ ]:




