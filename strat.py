import math
import time

Obj=[['m',[230,2022],0],['m',[635,2022],0],['p',[300,0],0],['b',[300,400],0,'r'],['b',[450,510],0,'v'],['b',[450,1080],0,'r'],['b',[300,1200],0,'v'],['b',[670,100],0,'r'],['b',[950,400],0,'v'],['b',[1100,800],0,'r'],['b',[1270,1200],0,'v'],['b',[1065,1650],0,'v'],['b',[1005,1955],0,'r'],['b',[1335,1650],0,'r'],['b',[1395,1955],0,'v'],['b',[-67,1450],0,'r'],['b',[-67,1525],0,'v'],['b',[-67,1600],0,'r'],['b',[-67,1675],0,'v'],['b',[-67,1750],0,'r']]; # Liste des objectifs
# b= bouee / m=manche a air / v=vert / r=rouge / p = phare
Obstacle=[[1600,1600]];
Pos=[300,800];

def distance(x,y,x1,y1):
    return math.sqrt((x-x1)**2+(y-y1)**2);

def calculobs(x,y,x1,y1,Pos1):
    if Pos1[0]==x:
        A=0;
        B=y;
        C=0;
    else:
        A=((Pos1[1]-y)/(Pos1[0]-x));
        C=y-A*x;
        B=1;

    d=abs((A*x1+B*y1+C)/math.sqrt(A**2+B**2));
    if d<200:
        return 1;
    else:
        return 0;



def mainobs(Obstacle1,Obj1,Posi):
    i=0;
    for k in Obstacle1:
        if calculobs(k[0],k[1],Obj1[0],Obj1[1],Posi):
            i=1;
    return i;


#for i in Obj:
    #print(distance(Pos[0],Pos[1],i[1][0],i[1][1]));



n=len(Obj);
while n!=0:
        Objsuiv=[0,0,30000];
        for k in range(len(Obj)):

            if Obj[k][0]=='m' and Obj[k][2]==0 and distance(Pos[0],Pos[1],Obj[k][1][0],Obj[k][1][1])< Objsuiv[2] and mainobs(Obstacle,Obj[k][1],Pos)==0: # Manche a air prioritaire:
                Objsuiv=['m',k,distance(Pos[0],Pos[1],Obj[k][1][0],Obj[k][1][1])];
                i=k;
            elif Obj[k][0]=='p':
                if Obj[k][2]==0 and distance(Pos[0],Pos[1],Obj[k][1][0],Obj[k][1][1])< Objsuiv[2] and Objsuiv[0]!='m' and mainobs(Obstacle,Obj[k][1],Pos)==0:
                        Objsuiv=['p',k,distance(Pos[0],Pos[1],Obj[k][1][0],Obj[k][1][1])];
                        i=k;
            elif Obj[k][0]=='b':

                if Obj[k][2]==0 and distance(Pos[0],Pos[1],Obj[k][1][0],Obj[k][1][1])< Objsuiv[2] and Objsuiv[0]!='m' and Objsuiv[0]!='p' and mainobs(Obstacle,Obj[k][1],Pos)==0:
                    if Obj[k][3]=='r':
                        Objsuiv=['b',k,distance(Pos[0],Pos[1],Obj[k][1][0],Obj[k][1][1]),'r'];
                        i=k;                                                                            #Bouee la plus proche
                    else:
                        Objsuiv=['b',k,distance(Pos[0],Pos[1],Obj[k][1][0],Obj[k][1][1]),'v'];
                        i=k;

        n-=1;
        Obj[i][2]=1;
        Pos=[Obj[i][1][0],Obj[i][1][1]];

        print(Objsuiv);
