#!/usr/bin/env python
# coding: utf-8

# In[1]:


t1 = ()


# In[2]:


type(t1)


# In[3]:


a = []


# In[4]:


type(a)


# In[5]:


t4 = 1, 2, 3, 4


# In[6]:


type(t4)


# In[7]:


t2 = 1


# In[8]:


type(t2)


# In[9]:


t3 = (1)


# In[10]:


type(t3)


# In[11]:


t5 = (1,)


# In[12]:


type(t5)


# In[13]:


# 숫자가 하나 일떈 꼭 ,쉼표 찍어줘야 튜플로인식 됨 꼭쉼표찍자


# In[14]:


s2 = set("hello")
s2


# In[15]:


type(s2)


# In[16]:


s2


# In[17]:


# 중복을 허용하지않는다  ll이 2개여야하는데 순서가없고 중복허용하지않는다


# In[18]:


# & = intersection 교집합


# In[19]:


# 불 자료형 
2 > 1


# In[20]:


1 == 1


# In[21]:


2 < 1


# In[22]:


a = 0
while a < 10:
    a = a + 1
    print(a)


# In[23]:


a = 3
while a < 1000:
    a = a * 3
    print(a)
    
    


# In[24]:


##############################
# for
##############################


# In[25]:


test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)


# In[26]:


marks = [90, 25, 67, 45, 80]


# In[27]:


number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print('%d 번 학생은 합격입니다'% number)
    else:
        print('%d 번 학생은 불합격입니다'% number)


# In[28]:


marks = [90, 25, 67, 45, 80]


# In[29]:


number = 0


# In[30]:


for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print('%d 번 학생 합격 축하드립니다'% number)


# In[31]:


a = range(10)


# In[32]:


a


# In[33]:


add = 0
for i in range(1, 11):
    add = add + i
    print(add)


# In[34]:


for i in range(1,11):
    print(i)


# In[35]:


for i in range(1,11):
    if i % 2 == 1:
        print(i)
    else:
        continue


# In[36]:


for i in range(1,11):
    if i % 2 == 1:
        print(i) # 포문에서 else 문이 없어도  출력이된다


# In[37]:


marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d 번 학생 축하드립니다"% number)


# In[38]:


for i in range(2, 10):
        for j in range(1,10):
            print(i*j, end =" ") #, end =" " 
        print('')   # end = " " 추가하는이유 결괏값을 아래로 출력하지말고 찍었으면 옆에서 찍으라는 매게변수 end


# In[39]:


a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result) 


# In[40]:


a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)    # 리스트축약 list compersstion  더 직관적이진 않다


# In[41]:


a = "Life is too short, you need python"   #결괏값은? if의 특징은 트루면 거기서끝난다!

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none") 


# In[42]:


# while 문을 사용해 1부터 1000까지의 자연수중 3의 배수의 합을 구해 보자.
i = 1 # i를 1이라고 알려줘서  정수라고 입력해줌
sum = 0
while i <= 1000:
    if i % 3 == 0: # 3의 배수 인지 확인 %는 나머지 나머지연산자 나누기가아니라 FOR문으로도 풀어봐라
        sum = sum + i
    i =  i + 1


print(sum)


# In[43]:


# while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.

# *
# **
# ***
# ****
# *****                FOR문으로도 풀어봐라
i = 0 
while True:
    i = i + 1
    if i > 5:break
    print(i * '*') # 과정값도 나온다 분리시키지않으면


# In[44]:


# FOR문을 사용해서 1부터 100까지의 숫자들의 합을 출력해 보자.
sum =0
for i in range(1,101):
    sum= sum + i
    
    
print(sum)  # 프린트를 분리시켜서 런하면 달라!


# In[45]:


#파이썬 함수 
##################
# def 함수명 (매게변수)
#     <수행할문장1>
#     <수행할문장2>
#     <수행할문장3>


# In[46]:


def add(a,b):
    return a+b # add 함수


# In[47]:


a = 3
b = 4
c = add(a,b)


# In[48]:


print(c)


# In[49]:


d = add(1,2)
print(d)


# In[50]:


def add(a,b): #a ,b 매게변수 라고부르고 parameter
    return a + b


print(add(3,4))  # 3 , 4는 인수라고 부른다 aguments
                # 프로그래밍언어 배울떄 제일 어려운점 .같은뜻인 많은용어가 여러가지 다른말로 표현된다 


# In[51]:


# 함수의형태 는 4가지이다. <일반적인 함수>
# def 함수이름 (매게변수):
#   <수행할문장>
#     ...
#     return


# In[52]:


def add(a, b):
    result = a + b
    return result


# In[53]:


a = add(3, 4)
print(a)


# In[54]:


# 입력값이 없는 함수 입력은 없지만 결과는 있다


# In[55]:


def say():
    return 'hi'


# In[56]:


a = say()
print(a)


# In[57]:


#결괏값이 없는 함수


# In[58]:


def add(a, b):
    print('%d, %d의 합은 %d 입니다.'% (a, b,a + b))


# In[59]:


add(3, 4)


# In[60]:


a = add(3, 4)
print(a)   ## 리턴이 없으면 결괏값이 없다 함수구성요소 수행할문장 실행한거 결괏값x


# In[61]:


# 결괏값 입력값 둘다없는 함수


# In[62]:


def say():
    print('hi')
    


# In[63]:


say()


# In[64]:


## 매게변수 지정하여 호출하기
#함수를 호출할 때 매개변수를 지정할 수도 있다. 다음 예를 보자.

# >>> def add(a, b):
# ...     return a+b
# ... 
# 앞에서 알아본 add 함수이다. 이 함수를 다음과 같이 매개변수를 지정하여 사용할 수 있다.

# >>> result = add(a=3, b=7)  # a에 3, b에 7을 전달
# >>> print(result)
# 10
# 매개변수를 지정하면 다음과 같이 순서에 상관없이 사용할 수 있다는 장점이 있다.

# >>> result = add(b=5, a=3)  # b에 5, a에 3을 전달
# >>> print(result)
# 8


# In[65]:


## 여러게의 입력값을 받는 함수 만들기

def add_many(*args):
    result = 0
    for i in args:
        result = result + i
        return result
    


# In[66]:


result = add_many(1, 2, 3)
print(result)


# In[67]:


result = add_many(1,2,3,4,5,6,7,8,9)


# In[68]:


print(result)


# In[69]:


def add_mul(choice, *args):
    if choice =='add':
        result = 0
        for i in args:
            result = result + i
    elif choice == 'mul':
        result = 1
        for i in args:
            result =result * i
    return result


# In[70]:


result = add_mul('add', 1, 2, 3, 4, 5)
print(result)


# In[71]:


result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)


# In[72]:


## 함수의 결괏값은 언제나 하나이다


# In[73]:


def add_and_mul(a, b):
    return a+b, a*b


# In[74]:


result =add_and_mul(3, 4)


# In[75]:


print(result)


# In[76]:


#결괏값은 두개인데 변수는 result 하나만쓰였으니 오류가  발생해야하지않나? 지만
# 튜플값 () 로 돌려준다 


# In[77]:


# 따로받고싶다 
result, result2 = add_and_mul(3, 4)


# In[78]:


print(result)


# In[79]:


print(result2)


# In[80]:


def add_and_mul(a, b):
    return a + b
    return a * b


# In[81]:


result = add_and_mul(3, 4)
print (result)


# In[82]:


# 함수는 결괏값 즉 result  를만나면 즉시 다음으로 빠져나온다


# In[83]:


#매게변수 초기값 미리설정하기
def say_myself (name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살 입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


# In[84]:


say_myself("조영우",27)


# In[85]:


a = 1
def vartest(a):
    a = a +1
    
    
vartest(a)
print(a)


# In[86]:


## def vartest(a) 로 입력값을 받은 매개변수 a는 함수안에서만 사용하는 변수이다
## 지역변수 : 특정범위 안에서만 통용 전역변수 : 전체통용
## 즉 함수 안에서 사용하는 매게변수는 함수밖에 변수 이름과는 상관없다 


# In[87]:


def vartest(a):
    a = a + 1
    
vartest(3)
print(a)


# In[88]:


a = 1
def vartest(a):
    a = a + 1
    return a

a= vartest(a)
print(a)


# In[89]:


a = 1
def vartest():
    global a
    a = a + 1
    
vartest()


# In[90]:


print(a)


# In[91]:


## 람다 리스트 축약 ==
add =lambda a, b: a+b


# In[92]:


result = add(3, 4)
print(result)


# In[93]:


## 람다로 만든 함수는 return이 없어도 돌려준다


# In[94]:


###################
##사용자 입력과출력
###################


# In[95]:


a = input()


# In[96]:


a


# In[97]:


## input 은 숫자를 넣어도 무조껀 문자로 취급


# In[98]:


number = input("숫자를 입력하세요:")


# In[99]:


number


# In[100]:


#숫자로 받고싶으면
number = int(input("숫자를 입력하세요"))


# In[101]:


number


# In[102]:


## print


# In[103]:


a = 123
print(a)


# In[104]:


print("LIfe" "is" "too" "short")


# In[105]:


print("LIfe", "is", "too", "short") #문자열 띄어쓰기 = ,


# In[106]:


print("LIfe"+"is"+"too"+"short")


# In[107]:


for i in range(10):
    print(i,end = ' ') ## ' ' <<이안에 띄어쓰기 한만큼 띄어줌


# In[108]:


## 파일 읽고 쓰기
f = open('새파일.txt', 'w')
f.close()# 닫아줘야한다 끝날때 !!


# In[109]:


## cmd열기

# 관리자 명령 프롬프트 cui 커멘드 유저 인터페이스 gui 그래픽 유저 인터페이스

# dir : 은 디렉토리 안에 있는 파일의 목록 확인
# cd 디렉토리명 : 특정 디렉토리 안으로 이동
# md 디렉토리명 : 디렉토리 만들기
# cd .. : 디렉토리 에서 빠져나올때
# rd 디렉토리명: 디렉토리 삭제


# In[110]:


f = open('새파일.txt','w')
for i in range(1,10):
    data = '%d번째 줄입니다. \n' % i
    f.write(data)
f.close()


# In[111]:


f = open('새파일.txt','r')
line = f.readline()
print(line)
f.close()


# In[112]:


f = open('새파일.txt', 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()


# In[116]:


f = open('새파일.txt', 'a')
for i in range(11,20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()


# In[117]:


# dos 명령어 사용해서 새파일 .txt 열어서 확인하기


# In[119]:


##  주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.


# In[121]:


def is_odd(i):
    if i % 2 == 0:
        return print('%d는 짝수입니다' % i)
    else:
        return print('%d는 홀수입니다' % i)
    
is_odd(7)


# In[122]:


#입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)


# In[126]:



def average(*args):
    sum = 0    #초기화 
    for i in args:
        sum = sum + i
        
    return sum / len(args)


average(1, 2, 3) 


# In[127]:


input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)   #오류를 수정해보자 인트


# In[133]:


input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)


# In[135]:


#다음 중 출력 결과가 다른 것 한 개를 골라 보자.

print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))


# In[141]:


f1 = open("test.txt", 'w')
f1.write("Life is too short")
f.close
### 닫거나 whit 함수 쓰기
f2 = open("test.txt", 'r')
print(f2.read())


# In[ ]:




