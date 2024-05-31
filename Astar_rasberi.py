# Astar 24/07/2022

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


def bir_ileri(matris,map):

    xsize=len(map)
    ysize=len(map[0])

    xaks=(matris[0])
    yaks=(matris[1])

    x1=[xaks-1,yaks]
    x2=[xaks+1,yaks]
    y1=[xaks,yaks-1]
    y2=[xaks,yaks+1]

    if xaks-1<1 and yaks-1<1:
        y=[x2,y2]

    elif xaks+1>xsize and yaks-1<1:
        y=[x1,y2]
        
    elif xaks+1>xsize and yaks+1>ysize:
        y=[x1,y1]

    elif xaks-1<1 and yaks+1>ysize:
        y=[x2,y1]

    elif xaks-1<1:
        y=[y1,x2,y2]

    elif xaks+1>xsize:
        y=[x1,y1,y2]

    elif yaks-1<1:
        y=[x1,x2,y2]

    elif yaks+1>ysize:
        y=[x1,y1,x2]

    else:
        y=[x1,y1,x2,y2]

    return y


def deger_kontrol(matris,map):

    y=[]
    
    for indexs in matris:
         if(map[indexs[0]-1][indexs[1]-1]==1):
            y.append(indexs)

    return y


def karşılaştırma(indeksler,yapilanlar_listesi):
    liste=[]
    for i in indeksler:
        if i not in yapilanlar_listesi:
            liste.append(i)
    
    return liste


def eleman_ekleme(yapilacaklar_listesi,indeksler):
    liste0=[]
    liste1=[]
    liste2=[]
    liste3=[]
    size=len(indeksler)
    eleman_sayısı=len(yapilacaklar_listesi[0])
   
    if size ==1:
        for i in range(eleman_sayısı):
            liste1.append(yapilacaklar_listesi[0][i])
        liste1.append(indeksler[0])
        liste0.append(liste1)

    elif size==2:
        for i in range(eleman_sayısı):
            liste1.append(yapilacaklar_listesi[0][i])
        liste1.append(indeksler[0])
        liste0.append(liste1)
        for j in range(eleman_sayısı):
            liste2.append(yapilacaklar_listesi[0][j])
        liste2.append(indeksler[1])
        liste0.append(liste2)

    elif size==3:
        for i in range(eleman_sayısı):
            liste1.append(yapilacaklar_listesi[0][i])
        liste1.append(indeksler[0])
        liste0.append(liste1)
        for j in range(eleman_sayısı):
            liste2.append(yapilacaklar_listesi[0][j])
        liste2.append(indeksler[1])
        liste0.append(liste2)
        for k in range(eleman_sayısı):
            liste3.append(yapilacaklar_listesi[0][k])
        liste3.append(indeksler[2])
        liste0.append(liste3)
    return liste0
         

def astar(map,start,goal):
    yapilacaklar_listesi=[[start]]
    yapilanlar_listesi=[]
    while yapilacaklar_listesi[0][-1]!=goal:
        
        indeks=yapilacaklar_listesi[0][-1]
        A=bir_ileri(indeks,map)
        
        B=deger_kontrol(A,map)
        
        C=karşılaştırma(B,yapilanlar_listesi)
        
        D=eleman_ekleme(yapilacaklar_listesi,C)
        
        
        for F in D:
            yapilacaklar_listesi.append(F)
        yapilanlar_listesi.append(yapilacaklar_listesi[0][-1])
        yapilacaklar_listesi=yapilacaklar_listesi[1:]

    return yapilacaklar_listesi[0]


A=[[1, 1, 1],
   [1, 0, 1],
   [0, 0, 1],
   [1, 1, 1],
   [1, 1, 0],
   [1, 0, 1],
   [1, 1, 1],
   [0, 1, 0]]

B=[[1,0],
   [1,1]]


C=[[1,0,1,1,1,0,1,1,1],
   [1,1,1,0,1,0,1,1,1],
   [0,1,0,0,1,0,1,1,1],
   [0,1,0,0,1,0,1,1,1],
   [0,0,1,0,1,0,1,1,1],
   [0,1,1,1,1,0,1,1,1],
   [0,1,0,0,1,0,0,1,1],
   [0,1,0,0,0,1,1,1,1],
   [0,1,0,0,1,1,1,1,1],
   [0,1,1,1,1,1,1,1,1],
   [0,1,0,0,1,0,0,0,1],
   [0,1,0,0,1,1,1,1,1]]

def indeks_düzelten(map,start,goal):
    A=(astar(map,start,goal))
    liste1=[]
    for i in range(len(A)-1):
        liste1.append([A[i+1][0]-A[i][0],A[i+1][1]-A[i][1]])
    liste2=[]
    for i in liste1:
        if i==[1,0]:
            liste2.append(270)
        elif i==[0,1]:
            liste2.append(0)
        elif i==[-1,0]:
            liste2.append(90)
        elif i==[0,-1]:
            liste2.append(180)
    return liste2

# print(indeks_düzelten(A,[1,1],[5,5]))

def götüren(indeks,yön):
    liste1=[]
 
    a=(yön-indeks+360)%360
    if a==0:
        liste1.append(1)
    elif a==90:
        liste1.append(2)
    elif a==180:
        liste1.append(4)
    elif a==270:
        liste1.append(3)

    return liste1[0] 

# print(götüren(90,270))

def yön_değiştirme(yön,a):
    if a==2:
        yön=(yön+270)%360
    elif a==3:
        yön=(yön+90)%360
    elif a==4:
        yön=(yön+180)%360
    return yön

yön=90
indeksler=indeks_düzelten(A,[6,3],[2,1])
while indeksler!=[]:
    count1=0
    count2=0
    count1=count1+encodersağ()
    count2=count2+encodersol()
    time.sleep(3)

    print(indeksler)
    a=götüren(indeksler[0],yön)
    indeksler.pop(0)
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


    yön=(yön_değiştirme(yön,a))