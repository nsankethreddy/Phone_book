import os
db = "phonebook.db"


#Entry function.
def WriteEntry():
    name  = input ("        Enter name        : ")
    phone = input ("        Enter phone number: ")
    if phoneError(phone) == True:
        WriteEntry()
        return
   
    f=open(db,'a')
    f.write (name+";"+phone+"\n")
    f.close()
    print (name + "--->" + phone + "-->> add to phonebook.db\n")
    input("finished <hit Enter>")

#Phone error. 
def phoneError(phone) :
    temp = 0
    try : 
        for i in phone :
            if int(i) not in range(0,10):
                temp+=1

    except ValueError  :
        print("Enter an integer")
        return True
            
    if temp != 0  :
        return True
    
        
    if len(phone) != 10:
        print("Invalid Phone Number len")
        return True

    else:
        return False
    

#Printing PhoneBook.
def printfile():
    print ("+-------------------------------------------+\n")
    print ("|                 PHONEBOOK                 |\n")
    print ("+-------------------------------------------+\n")


    f=open(db)
    entry=f.readline()
    while entry:
        s={}
        (s['nm'],s['ph'])=entry.split(";")
        print("name       :"+ s['nm'])
        print("phone      :"+ s['ph'])
        entry=f.readline()
    f.close()
    input ("<-----hit Enter----->")

    
#Search function.
def carimenu():
    os.system(['clear','cls'][os.name == 'nt'])
    while True:
        
        # Menu Displayed.    
        print ("  +-------------------------------------------+\n")
        print ("  |                SEARCH MODE                |\n")
        print ("  +-------------------------------------------+\n")

        menuname = input("\n\
        Search mode on, choise here:\n\
        1) search with name\n\
        2) search with phone number\n\
        q) quit \n\n\
        What would you like to do?  \n")

        if menuname == "1":
            name=input ("Enter the name :")
            finddetailnm(name)
        elif menuname == "2":
            
            def phonenumber():
                try:
                    phone=int(input ("Enter the phone:"))
                    phonestr=str (phone)
                    finddetailph(phonestr)
                except (ValueError):
                    print ("   Error.... <Enter just the number>")
                    phonenumber()
            phonenumber()
        elif menuname == "q":
            break
        else:
            print ("        Not a valid Choice.")
        #input("        Hit Enter to continue")

            
#search function continuation.......

            
def finddetailnm(carie):
    f=open(db)
    entry=f.readline()
    while entry:
        s={}
        (s['nm'],s['ph'])=entry.split(";")
        nam= s['nm']
        #print (nam.find(carie))
        searc=(nam.find(carie))
        entry=f.readline()
        if (searc != -1):
            search= (s)
            #print (search) #--> {'em': 'jjjj\n', 'ph': '987', 'nm': 'oxoode'}
            if search:
                print("name       :"+ search['nm'])
                print("phone      :"+ search['ph'])


            
    f.close()
    pilihcarinm()

    
#search function continuation........

    
def pilihcarinm():
    menuname=input ("Do you want search with name again y/n? ")
    if menuname == "y":
        name=input (" enter the name :")
        finddetailnm(name)
    elif menuname == "n":
        pass
    else:
        print ("        Not a valid Choice.")
        pilihcarinm()
        
#search function continuation........

        
def finddetailph(carie):
    f=open(db)
    entry=f.readline()
    while entry:
        s={}
        (s['nm'],s['ph'])=entry.split(";")
        nam= s['ph']
        #print (nam.find(carie))
        searc=(nam.find(carie))
        entry=f.readline()
        if (searc != -1):
            search= (s)
            #print (search) #--> {'em': 'jjjj\n', 'ph': '987', 'nm': 'oxoode'}
            if search:
                print("name       :"+ search['nm'])
                print("phone      :"+ search['ph'])

    f.close()
    pilihcariph()

#search function continuation........
    
    
def pilihcariph():
    menuname=input ("Do you want search with phone again y/n? ")
    if menuname == "y":
        phone=input ("enter the phone :")
        finddetailph(phone)
    elif menuname == "n":
        pass
    else:
        print ("        Not a valid Choice.")
        pilihcariph()


#delete function.
def delete():
    namd=input("type the name to be deleted:")
    f=open(db,"r")
    lines=f.readlines()
    print(lines)
    f.close()
    f=open(db,"w")
    if namd in lines:
        for line in lines:
            if namd not in line:
                f.write(line)
        print("\n\n<------Deleted successfully------>\n\n")        
    else:
        print("\n\n<--------- The name is not there in the PhoneBook .....So there is nothing to delete ---------->\n\n")
        for line in lines:
            f.write(line)
    f.close()
            
# The Menu
os.system(['clear','cls'][os.name == 'nt'])
while True:
    
    # Menu Displayed
    print ("+-------------------------------------------+\n")
    print ("|                PHONE BOOK                 |\n")
    print ("+-------------------------------------------+\n")

    menuname = input("\n\
    a) Add to Phonebook\n\
    p) List phonebook\n\
    s) Search\n\
    d) delete\n\
    q) Quit\n\n\
    What would you like to do?  \n")

    # Returned Answer
    if menuname == "p":
        printfile()
    elif menuname == "a":
        WriteEntry()
    elif menuname == "s":
        carimenu()
    elif menuname == "d":
        delete ()
    elif menuname == "q":
        break
    else:
        print ("Error.......<------Please enter a vied input------>)")
exit



