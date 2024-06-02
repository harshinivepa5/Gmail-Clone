class message:
    def __init__(self,receiver,sub,body,id,flag,star):
        self.receiver=receiver
        self.sub=sub
        self.body=body
        self.star=star
        self.id=id
        self.flag=flag
################################################################

#GLOBAL
id=1
numbers={}
accounts={}   
account_name={}
account_pass={}
current=''

##################################################################
class mail:
    def __init__(self,name,email,number):
        self.name=name
        self.email=email
        self.number=number

    inbox=[]
    sent=[]
    draft=[]
    id=0
    def compose(self,receiver,sub,body,id,flag,star):
        if(flag==1):
            self.draft.append(message(receiver,sub,body,id,0,0))
        else:
            self.sent.append(message(self.email,sub,body,id,0,0))
            id+=1
            for i in accounts.keys():
                if i==receiver:
                    accounts[i].inbox.append(message(self.email,sub,body,id,0,0))
                    break
    
    def display(self):
        for i in self.inbox:
                print(i.sub,i.body,i.id)

    def dispdraft(self):
        for i in self.draft:
            print(i.sub,i.body)

    
    def delete(self,id):
        for i in self.inbox:
            if i.id==id:
                self.inbox.remove(i)

    def multiple(self,n):
        print("Sub")
        sub=input()
        print("Body")
        bod=input()
        for i in range(n):
            print("recepient")
            s=input()
            self.compose(s,sub,bod,id,0,0)

    def star(self,id):
        for i in self.inbox:
            if id==i.id:
                i.star=1
            print("Starred Message=",i.body,i.sub)

def filldata():
    names=['shaik','sampath','harshini']
    email=['sameer@gmail.com','sampath@gmail.com','harshini@gmail.com']
    account_pass=['jamez','vindula','vepa']
    number=[70325,85209,94410]
    for i in range(3):
        create(names[i],email[i],number[i],account_pass[i])

def create(name,email,num,passw):
    accounts[email]=(mail(name,email,num))
    account_pass[email]=passw
    numbers[email]=num
    

def login(email,passw):
    if(account_name[email]==passw):
        print("Login Succes")
    else:
        print("Unsuccesful")

    
print('Welcome to Gmail clone ')
filldata()
while(1):
    print("1.Create accont\n2.Login\n3.Compose\n4.Exit\n5.Display inbox\n6.Display Draft\n7.Multiple sends\n8.Remove message\n9.Star Message\n10.Logout")
    c=int(input())
    if c==1:
        print("Enter Name")
        nam=input()
        print("enter email")
        em=input()
        if em not in account_pass.keys():
            print("enter number")
            number=int(input())
            if number not in numbers.keys():
                print("Enter Password")
                password=input()
                create(nam,em,number,password)
                print("Registered Succesfully")
            else:
                print("invalid number")
        else:
            print("invalid email")
    if c==2:
        print("Enter email")
        em=input()
        print("enter Password")
        password=input()
        if account_pass[em]==password:
            print("Login succesfull id=",em)
            current=em
            ob=accounts[em]
        else:
            print("Wrong password or id")
        # print(current)
    if c==4:
        break
    if c==3:
        if not(current):
            print("Please login")
            continue
        print("Enter receipent")
        rec=input()
        print("sub: ",end='')
        sub=input()
        print('body: ',end='')
        body=input()
        print("1.Send\n2.Cancel")
        ch=int(input())
        if ch==2:
            ob.compose(rec,sub,body,id,1,0)
            continue
        if(rec not in accounts.keys()):
            print("User not found")
            continue
        ob.compose(rec,sub,body,id,0,0)
        for i in range(len(ob.sent)):
            print(ob.sent[i].sub)
        #print(ob.sub,ob.sent.body)
    if c==5:
        ob.display()
    if c==6:
        ob.dispdraft()
    if c==7:
        print("Number of users")
        n=int(input())
        ob.multiple(n)
    if c==8:
        ob.display()
        print("Enter id to be removed")
        id=int(input())
        ob.delete(id)
    if c==9:
        ob.display()
        print("Enter id to star")
        id=int(input())
        ob.star(id)
    if c==10:
        current=''
