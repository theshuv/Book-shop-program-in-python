#functions for book shop program

#  function for choice 1
def addBook(flist):
    aflag=False
    mflag=False
    
    choice=int(input("1.Add at position 2.Add at end : "))
    id=input("Enter id :")
    bname=input("Enter Book name : ")
    auth=input("Enter author name : ")
    price=input("Enter the price : ")
    pages=input("Enter pages : ")
    bk=id+","+bname+","+auth+","+price+","+pages
    if(choice==1):
        pos=int(input("Enter the position : "))
        flist.insert(pos,bk)
        if(mflag==False):
            mflag=True
        else:
            if aflag==False:
                aflag=True
                flist.append(bk)
        print("Book Details added successfully .")        
#---------------------------------------------------------
# function for choice 7
        
def writefile(flist):
    
    if mflag==True:
        print("Over-writing the data......")
        with open("bookdata.dat","w") as fh:
            for i in fh:
                fh.write(i)
    elif aflag==True:
        print("Appending new data.......")
        with open("bookdata.dat","a") as fh:
            for i in flist[datalen:]:
                fh.write(i)
    else:
        print("Exiting......")
#---------------------------------------------------------
#function for choice 2
def deleteBook(flist,id):
    mflag=False
    pos=0
    for b in flist:
        if b.split(",")[0]==id:
            flist.pop(pos)
            if(mflag==False):
                mflag=True
            print("Deleted successfully..")
            break
        pos=pos+1
    else:
        print("Book with ",id,"not found.")

#-----------------------------------------------------------
#function for choice 3
def modifyBook(flist,id,pr):
    mflag=False
    pos=0
    for b in flist:
        lst=b.split(",")
        if lst[0]==id:
            lst[3]=pr
            flist[pos]=",".join(lst)
            if mflag==False:
                mflag=True
            print("Modification done successfully..")
            break
        pos=pos+1
    else:
        print("Book with ",id,"not found.")

#------------------------------------------------
#function for choice 4 
def dispauth(flist,authname):
    for a in flist:
        lst=a.split(",")
        if lst[2]==authname:
            print(lst)    
    else:
        print("no more author details found....")
#-----------------------------------------------
#function for choice 6        
def priauth(flist,price):
    choic=input("Choose 1.Less than entered price, 2.Greater than entered price : ?")
    if(choic==1):
        for a in flist:
            lst=a.split(",")
            if float(lst[3])<=float(price):
                print(lst)
    else:
        for a in flist:
            lst=a.split(",")
            if float(lst[3])>float(price):
                print(lst)
        

     
        
