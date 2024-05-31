# Remzi Alpaslan 
# alpaslanremzi529@gmail.com

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
            pass
        else:
            if map[indeks[0]-1][indeks[1]-1]==1:
                liste.append(indeks)
    return liste

MAP=[[1, 1, 0],
     [0, 1, 1],
     [0, 1, 0],
     [1, 1, 1],
     [1, 1, 0],
     [1, 0, 1],
     [1, 1, 1],
     [0, 1, 0]]

def bir_ileri(nokta,map):

    indeksler=[[nokta[0]+1,nokta[1]],[nokta[0],nokta[1]+1],[nokta[0]-1,nokta[1]],[nokta[0],nokta[1]-1]]

    liste=[]
    for i in range(4) :
        if indeksler[i][0]>=1 and indeksler[i][0]<=len(map) and indeksler[i][1]>=1 and indeksler[i][1]<=len(map[0]):
            liste.append(indeksler[i])
    return liste

#print(bir_ileri([4, 1],MAP))


def deger_kontrol(matris,map):

    y=[]
    
    for indexs in matris:
         if(map[indexs[0]-1][indexs[1]-1]==1):
            y.append(indexs)

    return y

#print(deger_kontrol([[5, 1], [4, 2], [3, 1]],MAP))

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
    liste4=[]
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
        
    elif size==4:
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
        for n in range(eleman_sayısı):
            liste4.append(yapilacaklar_listesi[0][n])
        liste4.append(indeksler[3])
        liste0.append(liste4)
        
    return liste0
         

def astar(map,start,goal):
    yapilacaklar_listesi=[[start]]
    yapilanlar_listesi=[]
    #print("astar içi 1",yapilacaklar_listesi)
    while yapilacaklar_listesi[0][-1]!=goal:
        for F in eleman_ekleme(yapilacaklar_listesi,karşılaştırma(deger_kontrol(bir_ileri(yapilacaklar_listesi[0][-1],map),map),yapilanlar_listesi)):


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
        liste1.append("ileri")
    elif a==90:
        liste1.append("sağ")
    elif a==180:
        liste1.append("geri")
    elif a==270:
        liste1.append("sol")
        
    return liste1[0] 

# print(götüren(90,270))

def yön_değiştirme(yön,a):
    if a=="sağ":
        yön=(yön+270)%360
    elif a=="sol":
        yön=(yön+90)%360
    elif a=="geri":
        yön=(yön+180)%360
    return yön


MAP=[[1,0,1,1,1,0,1,1,1],
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




map=[[1]]
konum=[1,1]
yön=270
yapılanlar_listesi=[]
yapılacaklar_listesi=[]
adım=1
while True:

    for i in sol_ön_sağ_değerleri([konum[0],konum[1],yön],MAP):    # haritayı ve sol ön sağ prosedürünün kullanarak sahte hc verilerini oluşturdum.
        map=matris_büyütme(map,i)# mapi oluşturmaya başladım
        if i not in yapılacaklar_listesi and i not in yapılanlar_listesi:
            yapılacaklar_listesi.append(i)
    #print("yapılacaklar_listesi",yapılacaklar_listesi)
    #print(yön)
    print("adım= ",adım)
    adım+=1
    for row in map:
        print(row)
    print("\n")
    
    if yapılacaklar_listesi==[]:
        break


    #print(yapılacaklar_listesi)    
    #print(yapılacaklar_listesi[-1])
    hareketler=[]
    for i in indeks_düzelten(map,konum,yapılacaklar_listesi[-1]):# hareket kodlarını yazdım

        hareketler.append(götüren(i,yön))
        yön=(yön_değiştirme(yön,götüren(i,yön)))
    konum=yapılacaklar_listesi[-1]
    yapılanlar_listesi.append(yapılacaklar_listesi[-1])
    yapılacaklar_listesi.pop()
    print(hareketler)
    #print(yön)
    #print(konum)
    #print(yapılacaklar_listesi)
    #print(yapılanlar_listesi)





        
    

    
    
    
    

    

    