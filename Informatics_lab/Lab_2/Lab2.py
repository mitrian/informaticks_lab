def ff(x):
    if x=='1':
        return '0'
    else:
        return '1'
print('Введите набор из 7 цифр "0" и "1" ')
s = input()
if (s.count("1")+s.count("0"))!=7 or (s.count("1")+s.count("0"))!=len(s) :
    print('Вы ввели неправильный набор')
else:
    nb=0
    k=0
    r1=s[0]
    r2=s[1]
    r3=s[3]
    sind1 = (r1+s[2]+s[4]+s[6])
    sind2 = (r2+s[2]+s[5]+s[6])
    sind3 = (r3+s[4]+s[5]+s[6])
    if sind1.count("1")%2!=0:
        k+=1
    if sind2.count("1")%2!=0:
        k+=2
    if sind3.count("1")%2!=0:
        k+=4
    t=(s[:k-1]+ff(s[k-1])+s[k:])
    print(t[2]+t[4]+t[5]+t[6])
    if k==0:
        print('Ошибка не обнаружена')
    else:
        print('Ошибка в бите № '+ str(k))
