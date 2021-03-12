# 리스트안에있는 중복된 값을 제외하고 갯수를 새라 
people = [("이호준"),("12"),("asdas")]

people1 =set(people)  # 셋으로 바꾸면 중복된값이 사라진다 셋은 각요소들의 순서를 매길수없으며 중복된값 허용하지않는다

people2 = list(people1)

print(len(people1))

# 문자열이 주어지면 대문자와 소문자를 바꿔서 출력

a = input() # 입력받기

print(a.swapcase) #대문자와 소문자 바꾸는 모듈


a = input()
for i in a:
    if i.islower() : 
        print(i.upper(),end="") 
    elif i.isupper() : 
        print(i.lower(),end="")
    else: print(i,end="")

#순서가 없는 10개의 숫자가 공백으로 구분되어 주어진다 주어진 숫자들중 최댓값을 변환해라

a = map(int,input().split()) #정수로 받기
print(max(a)) #최댓값

#max 쓰지말고
a = list(map(int,input().split())) #리스트로 받기

a.sort() #순서대로 정렬
print(a.sort(a[-1])) #리스트마지막 프린트

# 4개의 조건 만족
s = 'bccddddddddd'

zero = s.count('a')
one = s.count('b')
two = s.count('c')
nine = s.count('d')

print(two,zero,one,nine,one,zero,one,one,sep='')

# 어떤 입력값의 맨앞글자만 따기

a = list(input().split()) #a 에 리스트로 받아라
b = '' #b 문자열지정
for i in a: 
  b += i[0] #각 인덱스 0번째값 
print(b) #출력 

#양의정수 입력받아서 몇자리수인지 출력
print('{0} 자리수'.format(len(input())))
# 입력받은 리스트 자리수를 포멧팅

print('%s 자리수입니다' %len(input()))
