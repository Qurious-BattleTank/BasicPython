from sympy import Symbol, symbols, simplify, Derivative
from random import random
from numpy import array

'''
I. 실제 데이터 수집
'''
prime=[]
def is_prime(n):
    #소수 판별 함수
    for k in prime:
        if n%k==0:
            return False
    else:
        return True

for k in range(2, 1001):
    #에라테네토스의 체
    if is_prime(k)==True:
        prime.append(k)

def prime_count(n):
    #소수 계량 함수 (정의역 1000까지)
    k=0
    while n>=prime[k]:
        k+=1
        if k==168: break
    return k

data=[] #순서쌍
for k in range(1, 1001):
    data.append([k, prime_count(k)])

X=list( array(data)[:,0] ) #x성분만 추출 (numpy.array 이용)
Y=list( array(data)[:,1] ) #y성분만 추출 (numpy.array 이용)

X=X[:100]
Y=Y[:100]
#1부터 100까지 데이터로만 하겠음

'''
II. 예측함수와 목적함수
'''

x=Symbol('x')

#최소제곱법
def minimal_square(x_data, y_data, expr):
    #x_data (리스트), y_data (리스트), 수식(sympy) --> 목적함수 함숫값 (sympy)
    S=0
    for k in range(len(x_data)):
        square=( y_data[k] - expr.subs({'x':x_data[k]}) )**2
        S+=( y_data[k] - expr.subs({'x':x_data[k]}) )**2
        log="목적함수를 구하기 위해 {}를 더했습니다."
        print(log.format(square))
    S*= 1/2
    S=simplify(S)
    print("목적함수 E는 {}입니다.".format(S))
    return S

#예측함수
def f(t):
    #매개변수 t를 받아 sympy 객체 t*x 반환
    return t*x

#목적함수
def E(t):
    #매개변수 t --> 목적함수의 식 (sympy 객체)
    result=minimal_square(X, Y, f(t))
    return result

'''
III. 최급하강법을 이용한 학습
'''
eta=1e-6
diff=1
theta=10*random()
t=Symbol('t')
cnt=0

dEdt=Derivative(E(t), t).doit()
while diff>0.001:
    tmp = theta - eta*dEdt.subs({'t':theta})
    diff=abs(theta-tmp)
    theta=tmp
    cnt+=1
    print("{}회째: theta={:.3f}, 차분 = {:.4f}".format(cnt, theta, diff))
