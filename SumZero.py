#Question --10
#Create a List and sort it
#Create recursive function to get subset which sum is zero


GList=[4,2,-3,1,6]
GList.sort()
AList=[]


def subset(glist,s,f,clist):
    if s==0 and clist:
        print("Subset of given list which making sum Zero:",clist)
        return

    for i in range(f,len(glist)):

        if s+glist[i]>0:
               break
        clist.append(glist[i])
        subset(glist,s+glist[i],i+1,clist)
        clist.pop()

#calling function
subset(GList,0,0,AList)




