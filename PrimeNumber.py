M=int(input('상한을 입력하세요 : '))

def is_prime(n):
    for i in p:
        if n%i==0:
            return False
    return True

p=[]
count=0
for k in range(2, M+1):
    if is_prime(k)==True:
        p.append(k)
        count+=1
print('%d 이하 소수의 개수는 %d개' %(M, count))

print("구름에서 추가했어요.")