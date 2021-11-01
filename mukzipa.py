import random
shobu={1:'승리', 0:'무승부', -1:'패배'}
RtoM={'바위':'묵', '가위':'찌', '보':'빠'} #R은 RockScissorsPaper
MtoR={'묵':'바위', '찌':'가위', '빠':'보'} #M은 MukZiPa

#가위바위보 rsp는 rock scissors papar의 준말
#rsp(플레이어1, 플레이어2) -> 플레이어1의 승부값 반환
def rsp(com, plr): 
    if not (plr=='가위' or plr=='바위' or plr=='보'):
        print('뭐? 다시') #잘못 입력되었을 때
    if com==plr:
        return 0
    elif com=="가위":
        if plr=="바위":
            return 1
        if plr=="보":
            return -1
    elif com=="바위":
        if plr=="보":
            return 1
        if plr=="가위":
            return -1
    elif com=="보":
        if plr=="가위":
            return 1
        if plr=="바위":
            return -1

#컴퓨터
#묵찌빠 랜덤함수와 가위바위보 랜덤함수가 모두 필요하므로 class 생성
class Com(): 
    def __init__(self, game):
        if game=='rsp':
            self.a='가위'
            self.b='바위'
            self.c='보'
        if game=='mzp':
            self.a='찌'
            self.b='묵'
            self.c='빠'
    def com(self):
        c=random.randint(-1, 1)
        if c==-1:
            return self.a
        if c==0:
            return self.b
        if c==1:
            return self.c
        
comR=Com('rsp') #comR.com() -> 가위바위보 랜덤생성
comM=Com('mzp') #comM.com() ->묵찌빠 랜덤생성

while True:
    #시작할 때는 가위바위보
    print("컴퓨터와 묵찌빠~ 가위바위보!")
    result=0
    while result==None or result==0:
        me=input("(가위, 바위, 보) 나는 : ") #변수 me, bot은 가위/바위/보 중 하나
        bot=comR.com()
        result=rsp(bot, me) #가위바위보 결과
        print()
        print('나:%3s // 컴:%3s' %(me, bot))

    #묵찌빠 진행
    while True:
        if result==-1:
            print('컴 : %s...' %(2*RtoM[bot])) #가위/바위/보를 묵/찌/빠로
        elif result==1:
            print('나 : %s...' %(2*RtoM[me]))
        else:
            exit
    

        meM=input("(묵, 찌, 빠) 나는 : ") #변수 meM, botM은 묵/찌/빠 중 하나
        botM=comM.com() #컴퓨터 새로운 난수 생성
        print()
        print('나:%3s // 컴:%3s' %(meM, botM))

        if meM==botM: #양쪽이 같으면 종료
            print('나의 ', shobu[result]) #결과
            break
        else:
            bot=MtoR[botM] #가위바위보를 하기 위해 묵/찌/빠를 가위/바위/보로
            me=MtoR[meM]
            result=rsp(bot, me) #다음 차례를 정하는 가위바위보 
    re=input('그만두시려면 ㅇ를 눌러주세요 ')
    if re is 'ㅇ':
        break
    else:
        print()
