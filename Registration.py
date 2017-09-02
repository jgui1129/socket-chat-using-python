


class Registration:
    
    def __init__(self):
        #self.printList()
        print self.printList()
    
    def register(self):
        name = raw_input("enter name: ")
        email = raw_input("enter email: ")
        if (self.isEmailExist(email.lower())):
            print "email already exist"
        username = raw_input("enter username: ")
        if (self.isUsernameExist(username.lower())):
            print "username already exist"
        pass1 = raw_input("enter password: ")
        if not (self.validatePassword(pass1)):
            print "Password must be 8-16 characters."
        pass2 = raw_input("enter again the password: ")
        if not (self.isPasswordMatch(pass1, pass2)):
            print "password not match"

        f = open("database/accounts.txt","a")
        f.write(name.lower()+" "+email.lower()+" "+username.lower()+" "+pass1+" ");
        f.write("\n")
        f.close()

    
    def validatePassword(self,password):
        if (len(password) >= 8 and len(password) <= 16):
            return True
        else:
            return False
    
    def isPasswordMatch(self,pass1,pass2):
        if (pass1 == pass2):
            return True
        else:
            return False
              
        
    def isUsernameExist(self,username):
        userlist = []; 
        f = open("database/accounts.txt","r")
        y = f.read().split()
        f.close()
        
        ctr = 2
        for a in range(len(y)/4):
            userlist.append(y[ctr])
            ctr+=4
            
        if username in userlist:
            return True
        else:
            return False
    

    def isEmailExist(self,email):
        emaillist = []
        f = open("database/accounts.txt","r")
        y = f.read().split()
        f.close()

        ctr = 1
        for a in range(len(y)/4):
            emaillist.append(y[ctr])
            ctr+=4

        if email in emaillist:
            return True
        else:
            return False
    
    def printList(self):
        userlist = []; emaillist = []
        f = open("database/accounts.txt","r")
        y = f.read().split()
        f.close()

        ctr = 2
        ctr1 = 1 
        for a in range(len(y)/4):
            userlist.append(y[ctr])
            emaillist.append(y[ctr1])
            ctr+=4
            ctr1+=4
        print userlist
        print emaillist
        
    
    def loginCheck(self):
        usernamelist = []; emaillist = []; passwordlist = []
        f = open("accounts.txt","r")
        y = f.read().split()
        
        ctr = 1
        for a in range(len(y)/4):
            emaillist.append(y[ctr])
            usernamelist.append(y[(ctr+1)])
            passwordlist.append(y[(ctr+2)])
            ctr+=4
            
            
    
    
    
    
x = Registration()