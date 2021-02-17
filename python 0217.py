#!/usr/bin/env python
# coding: utf-8

# In[1]:


i = 1

i = i + 1
i += 1

i = i - 1
i -= 1

i = i * 1
i *= 1


# In[2]:


i -= 1


# In[3]:


print(i)


# In[4]:


coffee -= 1


# In[6]:


###########################
## 클래스
###########################


# In[7]:


a = 0
while a < 10:
    a +=1
    if a % 2 == 0:
        continue
    print(a)


# In[8]:


for i in range(2, 10):
    for j in range(1 ,10):
        print(i*j, end=" ")
        
    print('')
    


# In[9]:


result= 0

def add(num):
    global result# 전역 변수 선언
    result += num # result = result + num
    return result


print(add(3))
print(add(4))


# In[10]:


print(add(6))


# In[17]:


result1 = 0
result2 = 0
def add1(num):
    global result1
    result1 += num 
    return result1

def add2(num):
    global result2
    result2 += num 
    return result2

print(add1(3))
print(add1(4))



print(add2(3))
print(add2(4))


# In[18]:


class calculater:
    def __init__(self): # 던더바 이닛
        self.result = 0
        
        
    def add(self, num):
        self.result += num
        return self.result
    
    def sub(self, num):
        self.result -= num
        return self.result


# In[19]:


cal1 = calculater()


# In[20]:


cal2 = calculater()


# In[21]:


print(cal1.add(3))


# In[22]:


print(cal2.add(4))


# In[23]:


# 함수를 클라스 안에서 구현하면 매서드 method 라 부른다.

class fourcal:
    def __init__(self,first,second): # 던더바 넣으면 setdat 값 지정안해도  자동호출
        self.first = first
        self.second = second
    def setdata(self, first, second): #self는 다른의미가 있다
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result


# In[24]:


a = fourcal(4, 2)


# In[25]:


print(a.first)


# In[26]:


print(a.second)


# In[27]:


b = fourcal()


# In[28]:


print(b.first)


# In[29]:


print(a.first)


# In[30]:


id(b.first)


# In[31]:


id(a.first)


# In[32]:


print(div.first)


# In[33]:


a.add()


# In[34]:


a.div()


# In[35]:


a = fourcal(12,222)


# In[36]:


a.add()


# In[37]:


class morefourcal(fourcal):
    pass


# In[38]:


a = morefourcal(4, 2)


# In[39]:


a.add()


# In[40]:


a.sub()


# In[41]:


a  = fourcal(4, 0)


# In[42]:


a.div()


# In[43]:


class safefourcal(fourcal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first/ self.second


# In[44]:


a = safefourcal(4, 0)


# In[45]:


a.div()


# In[46]:


b = safefourcal(4, 2)


# In[47]:


b.div()


# In[48]:


class family:
    lastname = '김'


# In[49]:


print(family.lastname)


# In[50]:


a = lastname()


# In[51]:


def add(a, b):
    return a + b

def sub(a, b): 
    return a-b


# In[ ]:





# In[52]:


print(add(3, 4))


# In[58]:


# 예외처리


# In[55]:


try:
    a = [1, 2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌수 없습니다")
except IndexError:
    print("인덱싱 할 수 없습니다")
    


# In[56]:


try:
    a = [1, 2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)


# In[57]:


try:
    a =[1, 2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)


# In[ ]:




