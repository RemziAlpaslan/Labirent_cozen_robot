# localization 24/07/2022

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
    
    
    


def sampling(map):
    satir=len(map)
    stun = len(map[0])
    liste=[]

    for i in range(1,satir+1):
        for j in range(1,stun+1):
            liste.append([i,j,0,1])
            liste.append([i,j,90,1])
            liste.append([i,j,180,1])
            liste.append([i,j,270,1])

    liste1=[]
    
    for indexs in liste:
         if(map[indexs[0]-1][indexs[1]-1]==1):
            liste1.append(indexs)

    return liste1

# print(sampling(A))

# Noktaları hareket ettirmek için bir kod oluşturuyorun.
# bu kok hangi yöne gidmesi gerektiğinide söylüyor.
# Bu koda sahte harekat yani fake_move ismini veriyorum.  

def fake_move(liste,yön):

    if yön==2:
        for i in liste:
            i[2]=(i[2]+270)%360
    elif yön==3:
        for i in liste:
            i[2]=(i[2]+90)%360
    elif yön==4:
        for i in liste:
            i[2]=(i[2]+180)%360
    elif yön==1:
        for i in liste:
            i[2]=i[2]


    for point in liste:   
        if point[2]==0:
                point[1]=point[1]+1
        elif point[2]==90:
                point[0]=point[0]-1
        elif point[2]==180:
            point[1]=point[1]-1
        elif point[2]==270:
            point[0]=point[0]+1

    return liste

# print(fake_move(sampling(A),"sağ"))
# Posiblity kodu mapin dışına çıkan noktaları listeden çıkartıyor.
# Duvarların içine giren noktaları listeden çıkartıyor.
# Kalan değerlerin olasılık bölümlerine 3 puan veriyor.






def sol_ön_sağ_değerleri(konum,map):

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




def possibility(liste,map,indeks):
    liste1=[]
    for i in range(0,len(liste)):
        if liste[i][0]>=1 and liste[i][1]>=1 and liste[i][0]<=len(map) and liste[i][1]<=len(map[0]):
            liste1.append(liste[i])

    liste2=[]
    for indexs in liste1:
         if(map[indexs[0]-1][indexs[1]-1]==1):
            liste2.append(indexs)

    liste3=[]
    liste4=[]
    for i in liste2:
        liste3.append(i[0])
        liste3.append(i[1])
        liste3.append(i[2])
        liste3.append(i[3]+3)
        liste4.append(liste3)
        liste3=[]


    liste5=[]
    liste6=[]
    for i in liste4:

        if indeks==sol_ön_sağ_değerleri(i,map):
            liste5.append(i[0])
            liste5.append(i[1])
            liste5.append(i[2])
            liste5.append(i[3]+10)
            liste6.append(liste5)
            liste5=[]
    liste7=[]
    for i in liste4:
        if indeks!=sol_ön_sağ_değerleri(i,map):
            liste7.append(i[0])
            liste7.append(i[1])
            liste7.append(i[2])
            liste7.append(i[3])
            liste6.append(liste7)
            liste7=[]
    
    
    return liste6


# print(possibility(fake_move(sampling(A),"ileri"),A,fake_move([[1,1,0]],"ileri")[0],"ileri"))
# print(fake_move([[1,1,0]],"ileri")[0])
A=[[0, 1, 0],
   [1, 1, 1],
   [0, 1, 1],
   [1, 1, 0],
   [0, 1, 1],
   [1, 1, 1],
   [1, 1, 1],
   [0, 1, 0]]

örnekler=sampling(A)
konum=[1,1]
yön=90
a=1

while a!=0:
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
    liste44=[]
    if solhc>40:
        liste44.append(1)
    else:
        liste44.append(0)
        
    if önhc>40:
        liste44.append(1)
    else:
        liste44.append(0)
        
    if sağhc>40:
        liste44.append(1)
    else:
        liste44.append(0)
    print(liste44)
    
    örnekler=possibility(örnekler,A,liste44)
    print(örnekler)


    
    mesafe=40
    if önhc>mesafe and sağhc<=mesafe and solhc<=mesafe:
        a=1
    elif önhc<=mesafe and sağhc>mesafe and solhc<=mesafe:
        a=2
    elif önhc<=mesafe and sağhc<=mesafe and solhc>mesafe:
        a=3
    elif önhc>mesafe and sağhc>mesafe and solhc<=mesafe:
        yapılacak=[1,2]
        x = random.randint(0, 1)
        a=yapılacak[x]
    elif önhc<=mesafe and sağhc>mesafe and solhc>mesafe:
        yapılacak=[2,3]
        x = random.randint(0, 1)
        a=yapılacak[x]
    elif önhc>mesafe and sağhc<=mesafe and solhc>mesafe:
        yapılacak=[1,3]
        x = random.randint(0, 1)
        a=yapılacak[x]
    elif önhc>mesafe and sağhc>mesafe and solhc>mesafe:
        yapılacak=[1,2,3]
        x = random.randint(0, 2)
        a=yapılacak[x]
    elif önhc<=mesafe and sağhc<=mesafe and solhc<=mesafe:
        a=4
    else:
        a=0
    if örnekler[0][3]>örnekler[1][3]+10:
        a=0
        yön=örnekler[0][2]
        indeksler=indeks_düzelten(A,[örnekler[0][0],örnekler[0][1]],[1,2])   
        
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
    if a!=0:
        B=fake_move(örnekler,a)
    
    
    

while indeksler!=[]:
    count1=0
    count2=0
    count1=count1+encodersağ()
    count2=count2+encodersol()
    time.sleep(3)

    print(indeksler)
    print(yön)
    print(indeksler[0])
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