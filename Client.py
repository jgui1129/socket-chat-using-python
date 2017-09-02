from Tkinter import *
import time
import tkMessageBox
import socket,pickle
import threading
from datetime import datetime
import os.path
from FoulWords import filter

class Client(threading.Thread):

        
    def __init__(self):
        
        global sendMessageToUser
        
        print "User currently logged in: " + userUsername
        
        threading.Thread.__init__(self)
        self.root = Tk()
        self.root.config(bg="#2cbcff")
        self.root.title("ChatPinas")
        self.root.protocol('WM_DELETE_WINDOW', self.logout) 

        w = 800
        h = 500
        
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
    
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        
                
        self.rootBgImage = PhotoImage(file="img/bgtest.gif") 
        self.bg1 = PhotoImage(file="img/bg1.gif")
        self.bg2 = PhotoImage(file="img/bg2.gif")
        self.bg3 = PhotoImage(file="img/bg3.gif")
        self.bg4 = PhotoImage(file="img/bg4.gif")   
        self.bg = Label(image=self.rootBgImage)
        self.bg.pack()
        
        self.emo1 = PhotoImage(file="img/emoticons/1.gif")
        self.emo2 = PhotoImage(file="img/emoticons/2.gif")
        self.emo3 = PhotoImage(file="img/emoticons/3.gif")
        self.emo4 = PhotoImage(file="img/emoticons/4.gif")
        self.emo5 = PhotoImage(file="img/emoticons/5.gif")
        self.emo6 = PhotoImage(file="img/emoticons/6.gif")
        self.emo7 = PhotoImage(file="img/emoticons/7.gif")
        self.emo8 = PhotoImage(file="img/emoticons/8.gif")
        self.emo9 = PhotoImage(file="img/emoticons/9.gif")
        self.emo10 = PhotoImage(file="img/emoticons/10.gif")
        self.emo11 = PhotoImage(file="img/emoticons/11.gif")
        self.emo12 = PhotoImage(file="img/emoticons/12.gif")
        self.emo13 = PhotoImage(file="img/emoticons/13.gif")
        self.emo14 = PhotoImage(file="img/emoticons/14.gif")
        self.emo15 = PhotoImage(file="img/emoticons/15.gif")
        
        self.setEmo1 = PhotoImage(file="img/emoticons/setEmo1.gif")
        self.setEmo2 = PhotoImage(file="img/emoticons/setEmo2.gif")
        self.setEmo3 = PhotoImage(file="img/emoticons/setEmo3.gif")
        self.setEmo4 = PhotoImage(file="img/emoticons/setEmo4.gif")
        self.setEmo5 = PhotoImage(file="img/emoticons/setEmo5.gif")
        self.setEmo6 = PhotoImage(file="img/emoticons/setEmo6.gif")
        self.setEmo7 = PhotoImage(file="img/emoticons/setEmo7.gif")
        self.setEmo8 = PhotoImage(file="img/emoticons/setEmo8.gif")
        self.setEmo9 = PhotoImage(file="img/emoticons/setEmo9.gif")
        self.setEmo10 = PhotoImage(file="img/emoticons/setEmo10.gif")
        self.setEmo11 = PhotoImage(file="img/emoticons/setEmo11.gif")
        self.setEmo12 = PhotoImage(file="img/emoticons/setEmo12.gif")
        self.setEmo13 = PhotoImage(file="img/emoticons/setEmo13.gif")
        self.setEmo14 = PhotoImage(file="img/emoticons/setEmo14.gif")
        self.setEmo15 = PhotoImage(file="img/emoticons/setEmo15.gif")
        
        
        self.bgPreview1 = PhotoImage(file="img/bgPreview1.gif")
        self.bgPreview2 = PhotoImage(file="img/bgPreview2.gif")
        self.bgPreview3 = PhotoImage(file="img/bgPreview3.gif")
        self.bgPreview4 = PhotoImage(file="img/bgPreview4.gif")
        
        frame0 = Frame(self.root,relief="ridge",width=700,height=430,border=5,bg="#81d1f7")
        frame0.place(x=40,y=35)
        
        #main chatbox
        frame = Frame(self.root,relief="groove",width=350,height=230,border=5,bg="#e6f0f1")
        frame.place(x=80,y=150)
        
        changeThemeBtn = Button(self.root,text="Change Theme", bg="yellow", fg="black", command = self.changeTheme)
        changeThemeBtn.place(width=150,height=30,x=600,y=20)
        
        self.chatCount = StringVar()
        
        lblmainchat = Label(self.root,textvariable = self.chatCount ,font=('Applemint',10),bg="orange", relief="solid")
        lblmainchat.place(width=150,height=30,x=85,y=130) 
        
        self.sentBysender = StringVar() #emoticon
        self.sentBysender.set("Welcome to chatpinas!")
        
        self.lblEmoticonSentByUser = Label(self.root,width=40,height=40,image=self.setEmo1,bg="#81d1f7")
        self.lblEmoticonSentByUser.place(x=245,y=105)
        
        self.lblEmoticonSender = Label(self.root,text="Welcome to chatpinas!",textvariable=self.sentBysender)
        self.lblEmoticonSender.config(font = "arial 8 bold")
        self.lblEmoticonSender.place(x=295,y=125)
        
        self.chatbox = Listbox(self.root)
        self.chatbox.place(width = 340, height = 220, x = 85, y = 155)
        self.Scrollbar = Scrollbar(self.root,orient= VERTICAL)
        self.Scrollbar.place(width = 340, height = 220, x = 85, y = 155)
        self.Scrollbar.config(command = self.chatbox.yview)

        frame1 = Frame(self.root,relief="groove",width=250,height=130,border=5,bg="#e6f0f1")
        frame1.place(x=450,y=80)
        
        lblonline = Label(text="Online Users",font=('Applemint',10),bg="orange", relief="solid")
        lblonline.place(width=120,height=30,x=470,y=60)
        

        self.onlinelist = Listbox(self.root)
        self.onlinelist.bind('<<ListboxSelect>>',self.onselectOnline)
        self.onlinelist.place(width = 240, height = 120, x = 455, y = 85)
        self.Scrollbar1 = Scrollbar(self.root,orient= VERTICAL)
        self.Scrollbar1.place(width = 240, height = 120, x = 455, y = 85)
        self.Scrollbar1.config(command = self.onlinelist.yview)

                     
        #offline users
        frame2 = Frame(self.root,relief="groove",width=250,height=130,border=5,bg="#e6f0f1")
        frame2.place(x=450,y=250)
        
        lbloffline = Label(text="Offline Users",font=('Applemint',10),bg="orange", relief="solid")
        lbloffline.place(width=120,height=30,x=470,y=230)
                
        self.offlinelist = Listbox(self.root)
        self.offlinelist.bind('<<ListboxSelect>>',self.onselectOffline)
        self.offlinelist.place(width = 240, height = 120, x = 455, y = 255)
        self.Scrollbar2 = Scrollbar(self.root,orient= VERTICAL)
        self.Scrollbar2.place(width = 240, height = 120, x = 455, y = 255)
        self.Scrollbar2.config(command = self.offlinelist.yview)
                     
        self.txtChatMessage = Entry(self.root, borderwidth=3, relief="groove")
        self.txtChatMessage.config(font=("consolas", 12))
        self.txtChatMessage.bind('<Return>',self.sendMessage)
        self.txtChatMessage.bind('<FocusIn>',self.serverSendTyping)
        self.txtChatMessage.place(width=210,height=50,x=80,y=390)
        
        
        imgEmoticon = PhotoImage(file="img/emoticon.gif")
        btnEmoticon = Button(image=imgEmoticon, command=self.viewEmoticons, bg="orange")
        btnEmoticon.place(width=50,height=50,x=295,y=390)
        
        imgSend = PhotoImage(file="img/send.gif")
        
        btnSend = Button(self.root,text="Send", bg="green",fg="white", image=imgSend,command=self.sendMessage)
        btnSend.place(width=80,height=50,x=350,y=390)
        
        imgUser = PhotoImage(file="img/user.gif")
        self.imgInbox = PhotoImage(file="img/inbox.gif")
        imgCalendar = PhotoImage(file="img/calendar.gif")
        imgLogout = PhotoImage(file="img/logout.gif")
        self.imgmailopen = PhotoImage(file="img/mailopen.gif")

        welcomeUser = Label(self.root,text="Hi "+userUsername+"!",font=('Applemint',11),bg="#81d1f7")
        welcomeUser.place(width=150,height=50,x=90,y=50) 

        userIcon = Label(image = imgUser, bg="#81d1f7")
        userIcon.place(width=50,height=50,x=80,y=50)
                           
        txtDate = time.strftime("%a, %d %b %Y", time.gmtime())
        lblDateTodaySign = Label(self.root,text="Date Today!",bg="#81d1f7")
        lblDateTodaySign.place(width=90,height=20,x=320,y=55)
        lblDateToday = Label(self.root,text=txtDate, bg="#81d1f7")
        lblDateToday.place(width=100,height=20,x=323,y=75)
        
        lblCalendar = Label(self.root,image=imgCalendar, bg="#81d1f7")
        lblCalendar.place(width=50,height=50,x=265,y=50)       

        userInbox = Button(self.root,image = self.imgInbox, bg="#ffa926",command=self.viewInbox)
        userInbox.place(width=50,height=40,x=450,y=400)
        
        self.messageCount = StringVar()        
        lblinbox = Label(self.root,text="You have 4 new messages",textvariable=self.messageCount)
        lblinbox.place(width=150,height=40,x=500,y=400)
        
        self.btnLogout = Button(self.root,image = imgLogout, bg="red",command=self.logout)
        self.btnLogout.place(width=40,height=40,x=670,y=400)
        
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.resizable(width=False, height=False)
        
        self.start()
        self.root.mainloop()
        
        
    def run(self):
        self.name = userUsername
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('127.0.0.1', 1024))
        self.client.send(self.name)
        self.flag = 1
        msg=self.client.recv(1024)
        self.chatbox.insert(END, msg)
        self.checkForNewUsers()
        self.checkOfflineUsers()
        self.countInboxMessage()
        self.receive()

    def changeTheme(self):
        self.themes = Toplevel()
        self.themes.title("Change themes")
        self.themes.config(bg="#2cbcff")
        
        w = 390
        h = 250 
        
        self.themes.geometry('%dx%d+%d+%d' % (w, h, 730, 250))
        self.themes.resizable(width=False, height=False)
        
        lbltheme = Label(self.themes,text="Click image to change the background")
        lbltheme.pack(fill=X,padx=10,pady=10,ipadx=10,ipady=10)
        
        bgChange1 = Button(self.themes,image=self.bgPreview1, bg="#2cbcff",fg="white",command=lambda: self.changeBackground("1"))
        bgChange1.place(width=180,height=80,x=10,y=60)

        bgChange2 = Button(self.themes,image=self.bgPreview2, bg="#2cbcff",fg="white",command=lambda: self.changeBackground("2"))
        bgChange2.place(width=180,height=80,x=200,y=60)
        
        bgChange3 = Button(self.themes,image=self.bgPreview3, bg="#2cbcff",fg="white",command=lambda: self.changeBackground("3"))
        bgChange3.place(width=180,height=80,x=10,y=150)

        bgChange4 = Button(self.themes,image=self.bgPreview4, bg="#2cbcff",fg="white",command=lambda: self.changeBackground("4"))
        bgChange4.place(width=180,height=80,x=200,y=150)
        
    def changeBackground(self,pos):
        if pos == "1":
            self.bg.config(image=self.bg1)
            self.serverSendThemeChange("background1")
        elif pos == "2":
            self.bg.config(image=self.bg2)
            self.serverSendThemeChange("background2")
        elif pos == "3":
            self.bg.config(image=self.bg3)
            self.serverSendThemeChange("background3")
        else:
            self.bg.config(image=self.bg4)
            self.serverSendThemeChange("background4")

    def changeBackgroundFromServer(self,pos):
        if pos == "background1":
            self.bg.config(image=self.bg1)
        elif pos == "background2":
            self.bg.config(image=self.bg2)
        elif pos == "background3":
            self.bg.config(image=self.bg3)
        else:
            self.bg.config(image=self.bg4)

    def viewEmoticons(self):
        self.windowEmoticons = Toplevel()
        self.windowEmoticons.title("Emoticons")
        self.windowEmoticons.config(bg="#2cbcff")
        
        w = 290
        h = 250 
        
        self.windowEmoticons.geometry('%dx%d+%d+%d' % (w, h, 730, 250))
        self.windowEmoticons.resizable(width=False, height=False)
        
        lblEmoticons = Label(self.windowEmoticons,text="Click emoticon to send to everyone")
        lblEmoticons.pack(fill=X,padx=10,pady=10,ipadx=10,ipady=10)
        
        btn1 = Button(self.windowEmoticons,image=self.emo1, bg="orange",fg="white",command=lambda: self.sendEmoticon("emoticon1"))
        btn1.place(width=50,height=50,x=10,y=60)
        
        btn2 = Button(self.windowEmoticons,image=self.emo2, bg="orange",fg="white",command=lambda: self.sendEmoticon("emoticon2"))
        btn2.place(width=50,height=50,x=65,y=60)
        
        btn3 = Button(self.windowEmoticons,image=self.emo3, bg="orange",fg="white",command=lambda: self.sendEmoticon("emoticon3"))
        btn3.place(width=50,height=50,x=120,y=60)
        
        btn4 = Button(self.windowEmoticons,image=self.emo4, bg="orange",fg="white",command=lambda: self.sendEmoticon("emoticon4"))
        btn4.place(width=50,height=50,x=175,y=60)
        
        btn5 = Button(self.windowEmoticons,image=self.emo5, bg="orange",fg="white",command=lambda: self.sendEmoticon("emoticon5"))
        btn5.place(width=50,height=50,x=230,y=60)

        btn6 = Button(self.windowEmoticons,image=self.emo6, bg="orange",fg="white",command=lambda: self.sendEmoticon("emoticon6"))
        btn6.place(width=50,height=50,x=10,y=120)
        
        btn7 = Button(self.windowEmoticons,image=self.emo7, bg="orange",fg="white",command=lambda: self.sendEmoticon("emoticon7"))
        btn7.place(width=50,height=50,x=65,y=120)
        
        btn8 = Button(self.windowEmoticons,image=self.emo8, bg="orange",fg="white",command=lambda: self.sendEmoticon("emoticon8"))
        btn8.place(width=50,height=50,x=120,y=120)
        
        btn9 = Button(self.windowEmoticons,image=self.emo9, bg="orange",fg="white",command=lambda: self.sendEmoticon("emoticon9"))
        btn9.place(width=50,height=50,x=175,y=120)
        
        btn10 = Button(self.windowEmoticons,image=self.emo10, bg="orange",fg="white",command=lambda: self.sendEmoticon("emoticon10"))
        btn10.place(width=50,height=50,x=230,y=120)
        
        btn11 = Button(self.windowEmoticons,image=self.emo11, bg="orange",fg="white",command=lambda: self.sendEmoticon("emoticon11"))
        btn11.place(width=50,height=50,x=10,y=180)
        
        btn12 = Button(self.windowEmoticons,image=self.emo12, bg="orange",fg="white",command=lambda: self.sendEmoticon("emoticon12"))
        btn12.place(width=50,height=50,x=65,y=180)
        
        btn13 = Button(self.windowEmoticons,image=self.emo13, bg="orange",fg="white",command=lambda: self.sendEmoticon("emoticon13"))
        btn13.place(width=50,height=50,x=120,y=180)
        
        btn14 = Button(self.windowEmoticons,image=self.emo14, bg="orange",fg="white",command=lambda: self.sendEmoticon("emoticon14"))
        btn14.place(width=50,height=50,x=175,y=180)
        
        btn15 = Button(self.windowEmoticons,image=self.emo15, bg="orange",fg="white",command=lambda: self.sendEmoticon("emoticon15"))
        btn15.place(width=50,height=50,x=230,y=180)
       
        
    def sendEmoticon(self,emoticon):
        if emoticon == "emoticon1":
            self.lblEmoticonSentByUser.config(image=self.setEmo1)
            self.serverSendEmoticon("##################01")
        elif emoticon == "emoticon2":
            self.lblEmoticonSentByUser.config(image=self.setEmo2)
            self.serverSendEmoticon("##################02")
        elif emoticon == "emoticon3":
            self.lblEmoticonSentByUser.config(image=self.setEmo3)
            self.serverSendEmoticon("##################03")
        elif emoticon == "emoticon4":
            self.lblEmoticonSentByUser.config(image=self.setEmo4)
            self.serverSendEmoticon("##################04")
        elif emoticon == "emoticon5":
            self.lblEmoticonSentByUser.config(image=self.setEmo5)
            self.serverSendEmoticon("##################05")
        elif emoticon == "emoticon6":
            self.lblEmoticonSentByUser.config(image=self.setEmo6)
            self.serverSendEmoticon("##################06")
        elif emoticon == "emoticon7":
            self.lblEmoticonSentByUser.config(image=self.setEmo7)
            self.serverSendEmoticon("##################07")
        elif emoticon == "emoticon8":
            self.lblEmoticonSentByUser.config(image=self.setEmo8)
            self.serverSendEmoticon("##################08")
        elif emoticon == "emoticon9":
            self.lblEmoticonSentByUser.config(image=self.setEmo9)
            self.serverSendEmoticon("##################09")
        elif emoticon == "emoticon10":
            self.lblEmoticonSentByUser.config(image=self.setEmo10)
            self.serverSendEmoticon("##################10")
        elif emoticon == "emoticon11":
            self.lblEmoticonSentByUser.config(image=self.setEmo11)
            self.serverSendEmoticon("##################11")
        elif emoticon == "emoticon12":
            self.lblEmoticonSentByUser.config(image=self.setEmo12)
            self.serverSendEmoticon("##################12")
        elif emoticon == "emoticon13":
            self.lblEmoticonSentByUser.config(image=self.setEmo13)
            self.serverSendEmoticon("##################13")
        elif emoticon == "emoticon14":
            self.lblEmoticonSentByUser.config(image=self.setEmo14)
            self.serverSendEmoticon("##################14")
        elif emoticon == "emoticon15":
            self.lblEmoticonSentByUser.config(image=self.setEmo15)
            self.serverSendEmoticon("##################15")
        
        self.sentBysender.set("sent by: " + userUsername)
        self.chatbox.insert(END, "!: You sent an emoticon.")
        
    def setEmoji(self,emoji):
        if emoji == "##################01":
            self.lblEmoticonSentByUser.config(image=self.setEmo1)
        elif emoji == "##################02":
            self.lblEmoticonSentByUser.config(image=self.setEmo2)
        elif emoji == "##################03":
            self.lblEmoticonSentByUser.config(image=self.setEmo3)
        elif emoji == "##################04":
            self.lblEmoticonSentByUser.config(image=self.setEmo4)
        elif emoji == "##################05":
            self.lblEmoticonSentByUser.config(image=self.setEmo5)
        elif emoji == "##################06":
            self.lblEmoticonSentByUser.config(image=self.setEmo6)
        elif emoji == "##################07":
            self.lblEmoticonSentByUser.config(image=self.setEmo7)
        elif emoji == "##################08":
            self.lblEmoticonSentByUser.config(image=self.setEmo8)
        elif emoji == "##################09":
            self.lblEmoticonSentByUser.config(image=self.setEmo9)
        elif emoji == "##################10":
            self.lblEmoticonSentByUser.config(image=self.setEmo10)
        elif emoji == "##################11":
            self.lblEmoticonSentByUser.config(image=self.setEmo11)
        elif emoji == "##################12":
            self.lblEmoticonSentByUser.config(image=self.setEmo12)
        elif emoji == "##################13":
            self.lblEmoticonSentByUser.config(image=self.setEmo13)
        elif emoji == "##################14":
            self.lblEmoticonSentByUser.config(image=self.setEmo14)
        elif emoji == "##################15":
            self.lblEmoticonSentByUser.config(image=self.setEmo15)
        
        
      
    def receive(self):
        while self.flag==1:
            x=self.client.recv(1024)
            temp = x.split("*")
            if len(temp[0]) == 20:
                if (temp[0] == "##################01" or temp[0] == "##################02" or temp[0] == "##################03" 
                    or temp[0] == "##################04" or temp[0] == "##################05" or temp[0] == "##################06" 
                    or temp[0] == "##################07" or temp[0] == "##################08" or temp[0] == "##################09" 
                    or temp[0] == "##################10" or temp[0] == "##################11" or temp[0] == "##################12" 
                    or temp[0] == "##################13" or temp[0] == "##################14" or temp[0] == "##################15"):
                    self.setEmoji(temp[0])
                    self.sentBysender.set("sent by: " + temp[1])
                else:
                    self.chatbox.insert(END, x)
                    self.chatbox.yview(END)
            else:
                if (x == "background1" or x == "background2" or x == "background3" or x == "background4"):
                    self.changeBackgroundFromServer(x)
                else:    
                    self.chatbox.insert(END, x)
                    self.chatbox.yview(END)
                
    
    def countInboxMessage(self):
        
        if(os.path.isfile("database/"+userUsername+".txt")):
            f = open("database/"+userUsername+".txt","r")
            count = f.read().split("*")
            
            messageCounter = 0
            for a in range(len(count)/3):
                messageCounter+=1
                
            
            if (messageCounter == 1):
                self.messageCount.set("You have "+str(messageCounter)+" new message.");
            else:
                self.messageCount.set("You have "+str(messageCounter)+" new messages.");
        else:
            self.messageCount.set("You have no new messages");
            
        
        self.root.after(1000, self.countInboxMessage) 
        
        
    def checkForNewUsers(self):
        self.onlinelist.delete(0, END)
        f = open("database/onlinelist.txt")
        list = f.read().split()
        
        count = 0
        for user in list:
            if user == userUsername:
                pass
            else:
                self.onlinelist.insert(END, user)
                
            count+=1
            
        self.chatCount.set("ChatPinas Chatbox ("+str(count)+")")
        
        self.root.after(2000, self.checkForNewUsers)    
   
    def checkOfflineUsers(self):
        self.offlinelist.delete(0, END)
        userlist = []; 
        f = open("database/accounts.txt","r")
        y = f.read().split()
        f.close()
        
        ctr = 2
        for a in range(len(y)/4):
            userlist.append(y[ctr])
            ctr+=4
        
        f = open("database/onlinelist.txt","r")
        onlinelist = f.read().split()
        f.close()
        
        for user in userlist:
            if user == userUsername:
                pass
            elif user in onlinelist:
                pass
            else:
                self.offlinelist.insert(END, user)
        
        self.root.after(2000, self.checkOfflineUsers)   
        
        
    def onselectOnline(self,evt):
        index = self.onlinelist.curselection()
        sendMessageToUser = self.onlinelist.get(index)
        self.privateMessage(sendMessageToUser)
        
    def onselectOffline(self,evt):
        index = self.offlinelist.curselection()
        sendMessageToUser = self.offlinelist.get(index)
        self.privateMessage(sendMessageToUser)
    
    def onselectInbox(self,*args):
        index = self.inboxlist.curselection()
        if index != "":
            sender = index[0]
            self.temp = sender
            self.messageReply(sender)
    
    def viewInbox(self):
        
        self.userInboxWindow = Toplevel()
        self.userInboxWindow.title("Inbox")
        self.userInboxWindow.config(bg="#2cbcff")
        
        w = 500 
        h = 400 
        
        
        ws = self.userInboxWindow.winfo_screenwidth()
        hs = self.userInboxWindow.winfo_screenheight()
        
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        
        self.userInboxWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.userInboxWindow.resizable(width=False, height=False)
        
        frame0 = Frame(self.userInboxWindow,relief="groove",width=480,height=250,border=5,bg="#81d1f7")
        frame0.place(x=10,y=80)
        
        pmReceiver = Label(self.userInboxWindow,text="Inbox",font=('Applemint',20),bg="#2cbcff")
        pmReceiver.place(width=120,height=50,x=80,y=20) 

        pmMessageIcon = Label(self.userInboxWindow,image=self.imgInbox)
        pmMessageIcon.place(width=70,height=50,x=20,y=20) 
        
        self.inboxlist = Listbox(self.userInboxWindow,font=('Applemint',15))
        self.inboxlist.bind('<<ListboxSelect>>',self.onselectInbox)
        self.inboxlist.place(width = 470, height = 240, x=15, y=85)
        self.Scrollbar = Scrollbar(self.userInboxWindow,orient= VERTICAL)
        self.Scrollbar.place(width = 470, height = 240, x=15, y=85)
        self.Scrollbar.config(command = self.inboxlist.yview)
        
        
        if(os.path.isfile("database/"+userUsername+".txt")):
            f = open("database/"+userUsername+".txt","r")
            item =  f.read().split('*')
            userlist = []
            messageCount = []
            ctr = 0
        
            for i in range(len(item)/3):
                if (item[ctr]) not in userlist:
                    userlist.append(item[ctr])
                    self.inboxlist.insert(END,">> "+item[ctr]+ "("+str(item.count(item[ctr]))+")")
                ctr+=3
                
    def deleteMessage(self,*args):
        
        f = open("database/"+userUsername+".txt","r")
        content = f.read().split("*")
        f.close()
        newContent = ""
        ctr = 0
        for a in range(len(content)/3):
            if content[ctr] != self.xuser:
                newContent += content[ctr]+"*"+content[ctr+1]+"*"+content[ctr+2]+"*"
            ctr+=3
        
        f = open("database/"+userUsername+".txt","w")
        f.write(newContent)
        f.close()
        
        tkMessageBox.showinfo("Delete Message", "Message deleted successfully!")
        self.replywindow.destroy()
        self.viewInbox()
    
    def closeWindow(self):
        self.replywindow.destroy()
        self.viewInbox()
    
    def messageReply(self,sender):
        
        self.sender = sender #index of sender
        self.replywindow = Toplevel()
        self.replywindow.title("Message Reply")
        self.replywindow.config(bg="#2cbcff")
        self.userInboxWindow.destroy()
        self.replywindow.protocol('WM_DELETE_WINDOW', self.closeWindow) 
        
        w = 500 
        h = 400 
        
        ws = self.replywindow.winfo_screenwidth()
        hs = self.replywindow.winfo_screenheight()
        
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        
        self.replywindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.replywindow.resizable(width=False, height=False)
        
        frame0 = Frame(self.replywindow,relief="groove",width=480,height=250,border=5,bg="#81d1f7")
        frame0.place(x=10,y=80)
        
        self.messageFrom = StringVar()
        pmReceiver = Label(self.replywindow,textvariable = self.messageFrom,font=('Applemint',18),bg="#2cbcff")
        pmReceiver.place(width=250,height=50,x=80,y=20) 

        pmMessageIcon = Label(self.replywindow,image=self.imgmailopen,bg="#2cbcff")
        pmMessageIcon.place(width=70,height=50,x=20,y=20) 
        
        frame1 = Frame(self.replywindow,relief="groove",width=460,height=105,border=5,bg="#81d1f7")
        frame1.place(x=20,y=90)         
        
        self.inboxmessagelist = Listbox(self.replywindow)
        self.inboxmessagelist.place(width = 450, height = 95, x = 25, y = 95)
        self.Scrollbar3 = Scrollbar(self.replywindow,orient= VERTICAL)
        self.Scrollbar3.place(width = 450, height = 95, x = 25, y = 95)
        self.Scrollbar3.config(command = self.inboxmessagelist.yview)
        
        
        f = open("database/"+userUsername+".txt","r")
        item =  f.read().split('*')
        f.close()
        userlist = []
        ctr = 0
        
        for i in range(len(item)/3):
            if (item[ctr]) not in userlist:
                userlist.append(item[ctr])
            ctr+=3
        
        self.xuser =  userlist.pop(int(self.sender))
        self.messageFrom.set("Message from "+self.xuser)
        ctr = 0; ctr2 = 1
        for a in range(len(item)/3):
            if item[ctr] == self.xuser:
                self.inboxmessagelist.insert(END," ("+str(ctr2)+") "+item[ctr+1] +" -- " + item[ctr+2])
                ctr2+=1
            ctr+=3
        
        frame2 = Frame(self.replywindow,relief="groove",width=460,height=85,border=5,bg="#81d1f7")
        frame2.place(x=20,y=230)         
    
        
        self.txtMessageReply = Text(self.replywindow, borderwidth=3, relief="groove")
        self.txtMessageReply.config(font=("consolas", 12), undo=True, wrap='word')
        self.txtMessageReply.place(width=450,height=75,x=25,y=235)
    
        lblMessage = Label(self.replywindow,text="Reply: ",font=('Applemint',15),bg="#81d1f7")
        lblMessage.place(width=70,height=20,x=20,y=205) 
        
        btn = Button(self.replywindow,text="Send Reply", bg="orange",fg="white",command=self.sendReply)
        btn.place(width=100,height=30,x=270,y=345)
        
        btn1 = Button(self.replywindow,text="Delete", bg="red",fg="white",command=self.deleteMessage)
        btn1.place(width=100,height=30,x=380,y=345)
    
    def privateMessage(self,recipient):
               
        self.recipient = recipient;
        
        self.top = Toplevel()
        self.top.title("Send Private Message")
        self.top.config(bg="#2cbcff")
        
        w = 500 
        h = 400 
        
        ws = self.top.winfo_screenwidth()
        hs = self.top.winfo_screenheight()
        
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        
        self.top.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.top.resizable(width=False, height=False)
        
        frame0 = Frame(self.top,relief="groove",width=480,height=250,border=5,bg="#81d1f7")
        frame0.place(x=10,y=80)
        
        
        pmReceiver = Label(self.top,text="Private Message",font=('Applemint',20),bg="#2cbcff")
        pmReceiver.place(width=250,height=50,x=80,y=20) 

        pmMessageIcon = Label(self.top,image=self.imgInbox)
        pmMessageIcon.place(width=70,height=50,x=20,y=20) 
        

        lblReceiver = Label(self.top,text="Receiver: ",font=('Applemint',15),bg="#81d1f7")
        lblReceiver.place(width=100,height=30,x=20,y=100) 
        
        self.receiver = Entry(self.top,width=100,font=('Applemint',10),relief="solid")
        self.receiver.place(width=200,height=30,x=130,y=100)

        self.userlist = []
        f = open("database/accounts.txt","r")
        y = f.read().split()
        f.close()
        
        ctr = 2
        usernameIndex = 0
        for a in range(len(y)/4):
            
            if y[ctr] == self.recipient:
                usernameIndex = a
                self.userlist.append(y[ctr])
            else:
                self.userlist.append(y[ctr])
            
            ctr+=4
        
        self.value = StringVar()
        self.value.set(self.userlist[usernameIndex])
        self.drop = OptionMenu(self.top,self.value,*self.userlist)
        self.drop.config(bg="orange",fg="white")
        self.drop.place(width=200,height=30,x=130,y=100) 
        
        frame1 = Frame(self.top,relief="groove",width=460,height=145,border=5,bg="#81d1f7")
        frame1.place(x=20,y=170)         
    
        
        self.txtMessage = Text(self.top, borderwidth=3, relief="groove")
        self.txtMessage.config(font=("consolas", 12), undo=True, wrap='word')
        self.txtMessage.place(width=450,height=135,x=25,y=175)
    
        lblMessage = Label(self.top,text="Message: ",font=('Applemint',15),bg="#81d1f7")
        lblMessage.place(width=100,height=30,x=20,y=135) 
        
        btn = Button(self.top,text="Send Message", bg="orange",fg="white",command=self.sendPrivateMessage)
        btn.place(width=100,height=30,x=380,y=345)
        
        
    def sendPrivateMessage(self,*args):
        
        receiver = self.value.get()
        message =  self.txtMessage.get("1.0","end-1c")
        timestamp = datetime.now().strftime('%m-%d-%Y %H:%M')
        self.serverSendPM()
        if(os.path.isfile("database/"+receiver+".txt")):
            f = open("database/"+receiver+".txt","a")
            f.write(userUsername+"*"+message+"*"+timestamp+"*")
            f.close()
            self.txtMessage.delete("1.0",END)
            tkMessageBox.showinfo("PM to "+receiver, "Message sent successfully!")
            self.top.destroy()
            
        else:
            f = open("database/"+receiver+".txt","w")
            f.write(userUsername+"*"+message+"*"+timestamp+"*")
            f.close() 
            self.txtMessage.delete("1.0",END)
            tkMessageBox.showinfo("PM to "+receiver, "Message sent successfully!")
            self.top.destroy()     


    def sendReply(self,*args):
        
        receiver = self.xuser
        message =  self.txtMessageReply.get("1.0","end-1c")
        timestamp = datetime.now().strftime('%m-%d-%Y %H:%M')
        self.serverSendPmreply()
        if(os.path.isfile("database/"+receiver+".txt")):
            f = open("database/"+receiver+".txt","a")
            f.write(userUsername+"*"+message+"*"+timestamp+"*")
            f.close()
            self.txtMessageReply.delete("1.0",END)
            tkMessageBox.showinfo("PM to "+receiver, "Message sent successfully!")
            self.replywindow.destroy()
            self.messageReply(self.temp)
            
        else:
            f = open("database/"+receiver+".txt","w")
            f.write(userUsername+"*"+message+"*"+timestamp+"*")
            f.close() 
            self.txtMessageReply.delete("1.0",END)
            tkMessageBox.showinfo("PM to "+receiver, "Message sent successfully!")
            self.replywindow.destroy()
            self.messageReply(self.temp)

    def logout(self,*args):
        
        name = userUsername
        data = [4,name]
        data_string = pickle.dumps(data)
        self.client.send(data_string)

        f = open("database/onlinelist.txt","r")
        onlinelist = f.read().split()
        f.close()
        newlist = ""
        
        for a in onlinelist:
            if a == userUsername:
                pass
            else:
                newlist = newlist + a + " "
        
        f = open("database/onlinelist.txt","w")
        f.write(newlist)
        f.close()       
        self.root.destroy()
        Login()

    def sendMessage(self,*args):
        msg =  self.txtChatMessage.get()
        msg = filter(msg)
        if (msg != ""):
            name = userUsername
            timeStamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sendTo = "All"
            data = [0,name,msg,timeStamp,sendTo]
            data_string = pickle.dumps(data)
            self.chatbox.insert(END,userUsername+": "+msg)
            self.txtChatMessage.delete(0,END)
            self.chatbox.yview(END)   
            self.client.send(data_string)
            
        else:
            tkMessageBox.showinfo("ChatPinas", "Message is empty.")
            
            
    def serverSendPM(self):
            msg = self.txtMessage.get("1.0","end-1c")
            msg = filter(msg)
            name = userUsername
            timeStamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sendTo = self.value.get()
            data = [1,name,msg,timeStamp,sendTo]
            data_string = pickle.dumps(data)
            self.client.send(data_string)
    
    def serverSendPmreply(self):
            msg = self.txtMessageReply.get("1.0","end-1c")
            msg = filter(msg)
            name = userUsername
            timeStamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sendTo = self.xuser
            data = [1,name,msg,timeStamp,sendTo]
            data_string = pickle.dumps(data)
            self.client.send(data_string)
            
    def serverSendThemeChange(self,background):
            name = userUsername
            timeStamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            data = [2,name,background,timeStamp]
            data_string = pickle.dumps(data)
            self.client.send(data_string)
            
    def serverSendTyping(self,*args):
            name = userUsername
            data = [3,name]
            data_string = pickle.dumps(data)
            self.client.send(data_string)
    
    #4 leaves the chatroom
    def serverSendEmoticon(self,emoticon,*args):
            name = userUsername
            data = [5,name,emoticon]
            data_string = pickle.dumps(data)
            self.client.send(data_string)


            
class Signup:
    
    def __init__(self):
        self.root = Tk()
        self.root.title("Create an account")
        self.root.config(bg="#2cbcff")
        
        w = 800 
        h = 500 
    
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.resizable(width=False, height=False)
        self.entryText = StringVar()
        
        frame = Frame(self.root,relief="groove",width=300,height=460,border=5,bg="#e6f0f1")
        frame.pack(side=RIGHT,padx=45)
        
        btn = Button(self.root,text="Register", bg="orange",fg="white", command = self.registerAccount)
        btn.place(width=95,height=30,x=500,y=420)
        
        btn1 = Button(self.root,text="Go Back",bg="red",fg="white", command = self.backToLogin)
        btn1.place(width=95,height=30,x=610,y=420)
  
        name = Label(self.root,text="Name: ",bg="#e6f0f1")
        name.place(width=100,height=30,x=470,y=90)

        self.txtName = Entry(self.root,width=100,font=('Applemint',10),justify="center")
        self.txtName.place(width=200,height=25,x=500,y=120)
                
        username = Label(self.root,text="Username: ",bg="#e6f0f1")
        username.place(width=100,height=30,x=480,y=150)
        
        self.txtUsername = Entry(self.root,width=100,font=('Applemint',10),justify="center")
        self.txtUsername.place(width=200,height=25,x=500,y=180)
        self.txtUsername.bind('<FocusOut>',self.isUsernameExist)

        email = Label(self.root,text="Email: ",bg="#e6f0f1")
        email.place(width=100,height=30,x=470,y=210)
        
        self.txtEmail = Entry(self.root,width=100,font=('Applemint',10),justify="center",textvariable=self.entryText)
        self.txtEmail.place(width=200,height=25,x=500,y=240)
        self.txtEmail.bind('<FocusOut>',self.isEmailExist)

        password = Label(self.root,text="Password: ",bg="#e6f0f1")
        password.place(width=100,height=30,x=480,y=270)
        
        self.txtPassword = Entry(self.root,width=100,font=('Applemint',10),justify="center",show="*" )
        self.txtPassword.place(width=200,height=25,x=500,y=300)
        self.txtPassword.bind('<FocusOut>',self.validatePassword)
        
        cpassword = Label(self.root,text="Confirm Password: ",bg="#e6f0f1")
        cpassword.place(width=100,height=30,x=500,y=330)
        
        self.txtcPassword = Entry(self.root,width=100,font=('Applemint',10),justify="center",show="*" )
        self.txtcPassword.place(width=200,height=25,x=500,y=360)
        self.txtcPassword.bind('<Return>',self.registerAccount)
        
        label = Label(text="Register to ChatPinas",font=('Applemint',15),bg="#e6f0f1")
        label.place(width=200,height=30,x=500,y=45) 
        
        img = PhotoImage(file="img/logo.gif")
        placeholder = Label(image=img)
        placeholder.place(width=400,height=280,x=30,y=45)
        
        desc = Label(self.root,text="Meet thousand of people. Meet new friends, share the fun via \n public chatbox, private messaging and more. Enjoy laughter with everyone \n right here and right now. Start the journey to a new world of fun.\n")
        desc.config(font=('arial',8),bg="#2cbcff",fg="white")
        desc.place(x=50,y=350)
        
        desc1 = Label(self.root,text="Join us now!!!")
        desc1.config(font=('century gothic',12),bg="#2cbcff",fg="white")
        desc1.place(x=180,y=400)
        
        self.root.mainloop()
        
    def registerAccount(self,*args):
        
        n = self.txtName.get().lower().replace(" ","")
        un = self.txtUsername.get().lower().replace(" ","")
        em = self.txtEmail.get().lower().replace(" ","")
        pw = self.txtPassword.get().lower().replace(" ","")
        
        if (self.txtPassword.get() != self.txtcPassword.get()):
            tkMessageBox.showinfo("Registration Page", "Password do not match.")
            
        elif not self.isValidEmail(self.txtEmail.get().lower()):
            tkMessageBox.showinfo("Registration Page", "Please enter a valid email.")
            self.txtEmail.focus_set()
        
        elif (self.txtName.get() == "" or self.txtEmail.get() == "" or self.txtUsername.get() == "" or self.txtPassword.get() == "" or self.txtcPassword.get() == ""):

            tkMessageBox.showinfo("Registration Page", "Some contents are missing.")
        else:
            f = open("database/accounts.txt","a")
            f.write(n+" "+em+" "+un+" "+pw+" ");
            f.write("\n")
            f.close()
            self.txtName.delete(0,END);self.txtEmail.delete(0,END);self.txtUsername.delete(0,END);self.txtPassword.delete(0,END);self.txtcPassword.delete(0,END)
            tkMessageBox.showinfo("Registration Page", "Successfully Registered.\nClick the back button to login.")

    def isValidEmail(self,email):
        if re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)",email) != None:
            return True
        else:
            return False     
        
    def backToLogin(self):
        self.root.destroy()
        Login()
        
        
    def isUsernameExist(self,*args):
        userlist = []; 
        f = open("database/accounts.txt","r")
        y = f.read().split()
        f.close()
        
        ctr = 2
        for a in range(len(y)/4):
            userlist.append(y[ctr])
            ctr+=4
            
        if self.txtUsername.get().lower() in userlist:
            tkMessageBox.showinfo("Registration Page", "Username already exist.")
            self.txtUsername.focus_set()

    def isEmailExist(self,*args):
        emaillist = []
        f = open("database/accounts.txt","r")
        y = f.read().split()
        f.close()

        ctr = 1
        for a in range(len(y)/4):
            emaillist.append(y[ctr])
            ctr+=4

        if self.txtEmail.get().lower() in emaillist:
            tkMessageBox.showinfo("Registration Page", "Email address already exist.")
            self.entryText.set("")
            self.txtEmail.focus_set()

    def validatePassword(self,*args):
        if (len(self.txtPassword.get().lower()) >= 8 and len(self.txtPassword.get().lower()) <= 16):
            pass
        elif self.txtPassword.get() == "":
            pass
        else:
            tkMessageBox.showinfo("Registration Page", "Password must be 8-16 characters.")
            self.txtPassword.focus_set()          
 
             
class Login:
    
    username = ""
    
    def __init__(self):
        self.root = Tk()
        self.root.title("ChatPinas") 
        self.root.config(bg="#2cbcff")

        w = 800
        h = 500
        
        ws = self.root.winfo_screenwidth() 
        hs = self.root.winfo_screenheight() 
        
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.resizable(width=False, height=False)
        
        frame = Frame(self.root,relief="groove",width=300,height=400,border=5,bg="#e6f0f1")
        frame.pack(side=RIGHT,padx=45)
                
        btn = Button(self.root,text="Login", bg="red",fg="white",command = self.userLogin)
        btn.place(width=100,height=30,x=500,y=350)
        
        btn1 = Button(self.root,text="Register",bg="orange",fg="white",command = self.registerPage)
        btn1.place(width=100,height=30,x=610,y=350)
        
        username = Label(self.root,text="Username: ",bg="#e6f0f1")
        username.place(width=100,height=30,x=480,y=160)
        
        self.txtUsername = Entry(self.root,width=100,font=('Applemint',10),justify="center")
        self.txtUsername.bind('<Return>',self.userLogin)
        self.txtUsername.focus()
        self.txtUsername.place(width=200,height=30,x=500,y=190)

        password = Label(self.root,text="Password: ",bg="#e6f0f1")
        password.place(width=100,height=30,x=480,y=240)
        
        self.txtPassword = Entry(self.root,width=100,font=('Applemint',10),justify="center",show="*" )
        self.txtPassword.bind('<Return>',self.userLogin)
        self.txtPassword.place(width=200,height=30,x=500,y=270)
        
        label = Label(text="Login to ChatPinas",font=('Applemint',15),bg="#e6f0f1")
        label.place(width=200,height=30,x=500,y=100) 
        
        img = PhotoImage(file="img/logo.gif")
        placeholder = Label(image=img)
        placeholder.place(width=400,height=280,x=30,y=45)
        
        desc = Label(self.root,text="Meet thousand of people. Meet new friends, share the fun via \n public chatbox, private messaging and more. Enjoy laughter with everyone \n right here and right now. Start the journey to a new world of fun.\n")
        desc.config(font=('arial',8),bg="#2cbcff",fg="white")
        desc.place(x=50,y=350)
        
        desc1 = Label(self.root,text="Join us now!!!")
        desc1.config(font=('century gothic',12),bg="#2cbcff",fg="white")
        desc1.place(x=180,y=400)
         
        self.root.mainloop()
        
    def registerPage(self):
        self.root.destroy()
        Signup()

    def addToOnlineList(self):
        
        f = open("database/onlinelist.txt","r")
        onlinelist = f.read().split()
        f.close()
        if userUsername in onlinelist:
            return True
        else:
            f = open("database/onlinelist.txt","a")
            f.write(userUsername+" ")
            f.close()
            return False

    def userLogin(self,*args):
        global userUsername
        
        username = self.txtUsername.get().lower()
        password = self.txtPassword.get().lower()
        
        usernamelist = []; emaillist = []; passwordlist = []
        f = open("database/accounts.txt","r")
        y = f.read().split()
        f.close()
        
        ctr = 1
        for a in range(len(y)/4):
            emaillist.append(y[ctr])
            usernamelist.append(y[(ctr+1)])
            passwordlist.append(y[(ctr+2)])
            ctr+=4
          
        if username == "" and password == "":
            tkMessageBox.showinfo("Login Page", "Username/Password field is empty.")
            
        elif username in usernamelist:
            index = usernamelist.index(username)
            if passwordlist[index] == password:
                userUsername = usernamelist[index]
                if (self.addToOnlineList()):
                    tkMessageBox.showinfo("Login Page", "You're already logged in.")
                else:
                    self.root.destroy()
                    Client()
            elif password == "":
                tkMessageBox.showinfo("Login Page", "Password field is empty.")
            else:
                tkMessageBox.showinfo("Login Page", "Password is incorrect.")
        elif username in emaillist:
            index = emaillist.index(username)
            if passwordlist[index] == password:
                userUsername = usernamelist[index]
                if (self.addToOnlineList()):
                    tkMessageBox.showinfo("Login Page", "You're already logged in.")
                else:
                    self.root.destroy()
                    Client()
            elif password == "":
                tkMessageBox.showinfo("Login Page", "Password field is empty.")
            else:
                tkMessageBox.showinfo("Login Page", "Password is incorrect.")
        else:
            tkMessageBox.showinfo("Login Page", "Username not found.")

        #tkMessageBox.showinfo("Login", "Username and Password is Accepted")


if __name__ == '__main__':
    Login()