score=[1,2,0,0,4,1,6,2,1,3]
bat1=[]
bat2=[]
count=0
for i in range(1,10):
       count=count+1
       
       if ((score[i]%2==0) |(score[i]==0)) :
           bat2.append(score[i])

       if((((i+1)%6)==0) & (score[i]%2!=0)):
               bat2.append(score[i])
               
       if (((i+1)%3!=0) & (score[i]%2!=0)):
               bat1.append(score[i])
               bat1=score[i]
               #bat1=score[0]
               def Diff(bat1, bat2):
                   li_dif = [i for i in bat1 + bat2 if i not in bat1 or i not in bat2]
                   return li_dif
        
