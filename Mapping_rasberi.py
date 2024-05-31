# Mapping 24/07/2022

# Remzi Alpaslan
# Evin Uyar
# Meryem Sena Karabulut
# Pınar Kınalı


import RPi.GPIO as GPIO
from time import sleep
import time
import random


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
E1=4
E2=3
GPIO.setup(E1,GPIO.IN)
GPIO.setup(E2,GPIO.IN)
liste1=[]
liste2=[]


In1,In2 = 27,22
In3,In4 = 23,24

GPIO.setup(In1,GPIO.OUT)
GPIO.setup(In2,GPIO.OUT)

GPIO.setup(16,GPIO.OUT)
p=GPIO.PWM(16,100)
GPIO.setup(19,GPIO.OUT)
q=GPIO.PWM(19,100)

GPIO.setup(In3,GPIO.OUT)
GPIO.setup(In4,GPIO.OUT)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG1 = 10
ECHO1 = 17
TRIG2 = 6
ECHO2 = 5
TRIG3 = 15
ECHO3 = 14



GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO2,GPIO.IN)
GPIO.setup(TRIG3,GPIO.OUT)
GPIO.setup(ECHO3,GPIO.IN)

def mesafe1():
 GPIO.output(TRIG1, False)

 time.sleep(0.1)

 GPIO.output(TRIG1, True)
 time.sleep(0.00001)
 GPIO.output(TRIG1, False)
 
 pulse_start = time.time()
 pulse_end = time.time()

 while GPIO.input(ECHO1)==0:
     pulse_start = time.time()

 while GPIO.input(ECHO1)==1:
     pulse_end = time.time()

 pulse_duration = pulse_end - pulse_start

 distance = pulse_duration * 17150
 distance = round(distance, 2)

 if distance < 3 :
     return 3
 elif distance > 300:
     return 300
 else:
     return distance
 GPIO.cleanup()
 
def mesafe2():
 GPIO.output(TRIG2, False)

 time.sleep(0.1)

 GPIO.output(TRIG2, True)
 time.sleep(0.00001)
 GPIO.output(TRIG2, False)
 
 pulse_start = time.time()
 pulse_end = time.time()

 while GPIO.input(ECHO2)==0:
     pulse_start = time.time()

 while GPIO.input(ECHO2)==1:
     pulse_end = time.time()

 pulse_duration = pulse_end - pulse_start

 distance = pulse_duration * 17150
 distance = round(distance, 2)

 if distance < 3 :
     return 3
 elif distance > 300:
     return 300
 else:
     return distance
 GPIO.cleanup()
 
def mesafe3():

 GPIO.output(TRIG3, False)

 time.sleep(0.1)

 GPIO.output(TRIG3, True)
 time.sleep(0.00001)
 GPIO.output(TRIG3, False)
 
 pulse_start = time.time()
 pulse_end = time.time()

 while GPIO.input(ECHO3)==0:
     pulse_start = time.time()

 while GPIO.input(ECHO3)==1:
     pulse_end = time.time()

 pulse_duration = pulse_end - pulse_start

 distance = pulse_duration * 17150
 distance = round(distance, 2)

 if distance < 3 :
     return 3
 elif distance > 300:
     return 300
 else:
     return distance
 GPIO.cleanup()
 
def encodersağ():
    liste1.append(GPIO.input(E1))
    if len(liste1)>=3:
        liste1.pop(0)   
    if len(liste1)==1:
        return 0
    elif liste1[-1]!=liste1[-2]:
        return 1
    else:
        return 0
      
def encodersol():
    liste2.append(GPIO.input(E2))
    if len(liste2)>=3:
        liste2.pop(0)   
    if len(liste2)==1:
        return 0
    elif liste2[-1]!=liste2[-2]:
        return 1
    else:
        return 0
 






 
def fren():
    p.start(20)
    q.start(20)
    GPIO.output(In1,GPIO.HIGH)
    GPIO.output(In2,GPIO.HIGH)
    GPIO.output(In3,GPIO.HIGH)
    GPIO.output(In4,GPIO.HIGH)
    p.ChangeDutyCycle(100)
    q.ChangeDutyCycle(100)
    time.sleep(0.1)
    

def boş():
    p.start(0)
    q.start(0)
    GPIO.output(In1,GPIO.LOW)
    GPIO.output(In2,GPIO.LOW)
    GPIO.output(In3,GPIO.LOW)
    GPIO.output(In4,GPIO.LOW)
    p.ChangeDutyCycle(0)
    q.ChangeDutyCycle(0)
    time.sleep(0.1)


def ileri():
    count1=0
    count2=0
    count1=count1+encodersağ()
    count2=count2+encodersol()
    a=1
    b=1
    while a+b!=0:
        count1=count1+encodersağ()
        count2=count2+encodersol()
        if count1>count2:
            hizp=60
            hizq=100

        elif count2>count1:
            hizp=100
            hizq=60
        else:
            hizp=80
            hizq=80
            
        p.start(80)
        q.start(80)
        if 68>count1: 
            GPIO.output(In1,GPIO.HIGH)
            GPIO.output(In2,GPIO.LOW)
            p.ChangeDutyCycle(hizp)
            a=1
        else:
            GPIO.output(In1,GPIO.HIGH)
            GPIO.output(In2,GPIO.HIGH)
            a=0
        if 68>count2:
            GPIO.output(In3,GPIO.LOW)
            GPIO.output(In4,GPIO.HIGH)
            q.ChangeDutyCycle(hizq)
            b=1
        else:
            GPIO.output(In3,GPIO.HIGH)
            GPIO.output(In4,GPIO.HIGH)
            b=0
        time.sleep(0.01)
    if  1<count1 or 1<count2:
        fren()
        boş()
        count1=0
        count2=0




def sağ():
    count1=0
    count2=0
    count1=count1+encodersağ()
    count2=count2+encodersol()
    a=1
    b=1
    while a+b!=0:
        count1=count1+encodersağ()
        count2=count2+encodersol()
        if count1>count2:
            hizp=60
            hizq=100

        elif count2>count1:
            hizp=100
            hizq=60
        else:
            hizp=80
            hizq=80
            
        p.start(80)
        q.start(80)
        if 16>count1: 
            GPIO.output(In1,GPIO.LOW)
            GPIO.output(In2,GPIO.HIGH)
            p.ChangeDutyCycle(hizp)
            a=1
        else:
            GPIO.output(In1,GPIO.HIGH)
            GPIO.output(In2,GPIO.HIGH)
            a=0
        if 16>count2:
            GPIO.output(In3,GPIO.LOW)
            GPIO.output(In4,GPIO.HIGH)
            q.ChangeDutyCycle(hizq)
            b=1
        else:
            GPIO.output(In3,GPIO.HIGH)
            GPIO.output(In4,GPIO.HIGH)
            b=0
        time.sleep(0.01)
    if  1<count1 or 1<count2:
        fren()
        boş()
        count1=0
        count2=0
    ileri()


def sol():
    count1=0
    count2=0
    count1=count1+encodersağ()
    count2=count2+encodersol()
    a=1
    b=1
    while a+b!=0:
        count1=count1+encodersağ()
        count2=count2+encodersol()
        if count1>count2:
            hizp=60
            hizq=100

        elif count2>count1:
            hizp=100
            hizq=60
        else:
            hizp=80
            hizq=80
            
        p.start(80)
        q.start(80)
        if 16>count1: 
            GPIO.output(In1,GPIO.HIGH)
            GPIO.output(In2,GPIO.LOW)
            p.ChangeDutyCycle(hizp)
            a=1
        else:
            GPIO.output(In1,GPIO.HIGH)
            GPIO.output(In2,GPIO.HIGH)
            a=0
        if 16>count2:
            GPIO.output(In3,GPIO.HIGH)
            GPIO.output(In4,GPIO.LOW)
            q.ChangeDutyCycle(hizq)
            b=1
        else:
            GPIO.output(In3,GPIO.HIGH)
            GPIO.output(In4,GPIO.HIGH)
            b=0
        time.sleep(0.01)
    if  1<count1 or 1<count2:
        fren()
        boş()
        count1=0
        count2=0
    ileri()



def geri():
    count1=0
    count2=0
    count1=count1+encodersağ()
    count2=count2+encodersol()
    a=1
    b=1
    while a+b!=0:
        count1=count1+encodersağ()
        count2=count2+encodersol()
        print(count2,count1)
        if count1>count2:
            hizp=60
            hizq=100

        elif count2>count1:
            hizp=100
            hizq=60
        else:
            hizp=80
            hizq=80
            
        p.start(80)
        q.start(80)
        if 35>count1: 
            GPIO.output(In1,GPIO.HIGH)
            GPIO.output(In2,GPIO.LOW)
            p.ChangeDutyCycle(hizp)
            a=1
        else:
            GPIO.output(In1,GPIO.HIGH)
            GPIO.output(In2,GPIO.HIGH)
            a=0
        if 35>count2:
            GPIO.output(In3,GPIO.HIGH)
            GPIO.output(In4,GPIO.LOW)
            q.ChangeDutyCycle(hizq)
            b=1
        else:
            GPIO.output(In3,GPIO.HIGH)
            GPIO.output(In4,GPIO.HIGH)
            b=0
        time.sleep(0.01)
    if  1<count1 or 1<count2:
        fren()
        boş()
        count1=0
        count2=0
    ileri()
    
    

    






def yön_değiştirme(yön,a):
    if a==2:
        yön=(yön+270)%360
    elif a==3:
        yön=(yön+90)%360
    elif a==4:
        yön=(yön+180)%360
    return yön

def konum_ilerletme(konum,yön):
    if yön==0:
        konum=[konum[0],konum[1]+1]
    elif yön==90:
        konum=[konum[0]-1,konum[1]]
    elif yön==180:
        konum=[konum[0],konum[1]-1]
    elif yön==270:
        konum=[konum[0]+1,konum[1]]
    return konum
    
def konum_düzeltme(konum):
    xaks=(konum[0])
    yaks=(konum[1])

    if xaks<1:
        konum=[xaks+1,yaks]
    elif yaks<1:
        konum=[xaks,yaks+1]
    return konum


def matris_büyütme(map,konum):

    xsize=len(map)
    ysize=len(map[0])

    xaks=(konum[0])
    yaks=(konum[1])
    if xaks>xsize:
        liste=[]
        for i in range(ysize):
            liste.append(0)
        map.append(liste)
        map[konum[0]-1][konum[1]-1]=1

    elif xaks<1:
        liste=[]
        for i in range(ysize):
            liste.append(0)
        map.insert(0,liste)
        konum=[xaks+1,yaks]
        map[konum[0]-1][konum[1]-1]=1

    elif yaks>ysize:
        liste=[]
        for i in map:
            i.append(0)
        map[konum[0]-1][konum[1]-1]=1
            
    elif yaks<1:
        liste=[]
        for i in map:
            i.insert(0,0)
        konum=[xaks,yaks+1]
        map[konum[0]-1][konum[1]-1]=1
    else:
        map[konum[0]-1][konum[1]-1]=1
    return map


def mapping(map,konum,yön,a):
    A=yön_değiştirme(yön,a)
    B=konum_ilerletme(konum,A)
    C=matris_büyütme(map,B)
    return C
 


def çirkin_kod(konum,map):

    row_plus=[konum[0]+1,konum[1]]
    row_minus=[konum[0]-1,konum[1]]
    colomns_plus=[konum[0],konum[1]+1]
    colomns_minus=[konum[0],konum[1]-1]

    if konum[2]==0:
        indeksler=[row_minus,colomns_plus,row_plus]
    elif konum[2]==90:
        indeksler=[colomns_minus,row_minus,colomns_plus]
    elif konum[2]==180:
        indeksler=[row_plus,colomns_minus,row_minus]
    elif konum[2]==270:
        indeksler=[colomns_plus,row_plus,colomns_minus]
    liste=[]
    for indeks in indeksler:
        if indeks[0]<1 or indeks[0]>len(map) or indeks[1]<1 or indeks[1]>len(map[0]):
            liste.append(0)
        else:
            liste.append(map[indeks[0]-1][indeks[1]-1])
    return liste


A=[[1]]
konum=[1,1]
yön=90

while True:
    count1=0
    count2=0
    count1=count1+encodersağ()
    count2=count2+encodersol()
    liste11=[]
    liste22=[]
    liste33=[]
    temp=0
    while temp!=10:
        liste11.append(mesafe1())
        liste22.append(mesafe2())
        liste33.append(mesafe3())
        temp=temp+1
    sağhc=int(sum(liste11)/10)
    solhc=int(sum(liste33)/10)
    önhc=int(sum(liste22)/10)

    print("sol=",solhc,"ön=",önhc,"sağ=",sağhc)
    indeks1=çirkin_kod([konum[0],konum[1],yön],A)
    print("indkes",indeks1)

    
    mesafe=40
    if önhc>mesafe and sağhc<=mesafe and solhc<=mesafe:
        a=1
    elif önhc<=mesafe and sağhc>mesafe and solhc<=mesafe:
        a=2
    elif önhc<=mesafe and sağhc<=mesafe and solhc>mesafe:
        a=3
    elif önhc>mesafe and sağhc>mesafe and solhc<=mesafe and indeks1[2]==0:
        a=2
    elif önhc>mesafe and sağhc>mesafe and solhc<=mesafe and indeks1[1]==0:
        a=1
    elif önhc>mesafe and sağhc>mesafe and solhc<=mesafe:
        yapılacak=[1,2]
        x = random.randint(0, 1)
        a=yapılacak[x]
        
    elif önhc<=mesafe and sağhc>mesafe and solhc>mesafe and indeks1[0]==0:
        a=3
    elif önhc<=mesafe and sağhc>mesafe and solhc>mesafe and indeks1[2]==0:
        a=2
    elif önhc<=mesafe and sağhc>mesafe and solhc>mesafe:
        yapılacak=[2,3]
        x = random.randint(0, 1)
        a=yapılacak[x]
    elif önhc>mesafe and sağhc<=mesafe and solhc>mesafe and indeks1[0]==0:
        a=3
    elif önhc>mesafe and sağhc<=mesafe and solhc>mesafe and indeks1[1]==0:
        a=1
    elif önhc>mesafe and sağhc<=mesafe and solhc>mesafe:
        yapılacak=[1,3]
        x = random.randint(0, 1)
        a=yapılacak[x]
    elif önhc>mesafe and sağhc>mesafe and solhc>mesafe and indeks1[0]==0:
        a=3
    elif önhc>mesafe and sağhc>mesafe and solhc>mesafe and indeks1[1]==0:
        a=1
    elif önhc>mesafe and sağhc>mesafe and solhc>mesafe and indeks1[2]==0:
        a=2
    elif önhc>mesafe and sağhc>mesafe and solhc>mesafe:
        yapılacak=[1,2,3]
        x = random.randint(0, 2)
        a=yapılacak[x]
    elif önhc<=mesafe and sağhc<=mesafe and solhc<=mesafe:
        a=4
    else:
        a=0
    print(a)
        
    if a==1:
        ileri()
    elif a==2:
        sağ()       
    elif a==3:
        sol()
    elif a==4:
        geri()
    else:
        boş()

    mapping(A,konum,yön,a)
    for i in A:
        print(i)
    yön=(yön_değiştirme(yön,a))
    konum=(konum_düzeltme(konum_ilerletme(konum,yön)))
    print(yön)
    print(konum)