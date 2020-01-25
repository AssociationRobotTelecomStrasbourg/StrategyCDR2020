import math

Obj=[['m',[230,2022],0],['m',[635,2022],0],['b',[300,400],0,'r'],['b',[450,510],0,'v'],['b',[450,1080],0,'r'],['b',[300,1200],0,'v'],['b',[670,100],0,'r'],['b',[950,400],0,'v'],['b',[1100,800],0,'r'],['b',[1270,1200],0,'v'],['b',[1065,1650],0,'v'],['b',[1005,1955],0,'r'],['b',[1335,1650],0,'r'],['b',[1395,1955],0,'v'],['b',[-67,1450],0,'r'],['b',[-67,1525],0,'v'],['b',[-67,1600],0,'r'],['b',[-67,1675],0,'v'],['b',[-67,1750],0,'r']]; # Liste des objectifs
# b= bouee / m=manche a air / v=vert / r=rouge

Pos=[300,800];

def distance(x,y,x1,y1):
    return math.sqrt((x-x1)**2+(y-y1)**2);




for i in Obj:
    print(distance(Pos[0],Pos[1],i[1][0],i[1][1]));



n=len(Obj);
while n!=0:
        Objsuiv=[0,0,3000];
        for k in range(len(Obj)):
            if Obj[k][0]=='m':
                if Obj[k][2]==0 and distance(Pos[0],Pos[1],Obj[k][1][0],Obj[k][1][1])< Objsuiv[2]: # Manche a air prioritaire
                    Objsuiv=['m',k,distance(Pos[0],Pos[1],Obj[k][1][0],Obj[k][1][1])];
                    i=k;
            elif Obj[k][0]=='b':

                if Obj[k][2]==0 and distance(Pos[0],Pos[1],Obj[k][1][0],Obj[k][1][1])< Objsuiv[2] and Objsuiv[0]!='m':
                    if Obj[k][3]=='r':
                        Objsuiv=['b',k,distance(Pos[0],Pos[1],Obj[k][1][0],Obj[k][1][1]),'r'];
                        i=k;         #Bouee la plus proche
                    else:
                        Objsuiv=['b',k,distance(Pos[0],Pos[1],Obj[k][1][0],Obj[k][1][1]),'v'];
                        i=k;

        n-=1;
        Obj[i][2]=1;
        print(Objsuiv);
