import socket
import threading
import pickle

class ChatServer(threading.Thread):
    def __init__(self,dct,counter):
        self.dct=dct
        self.counter=counter
        threading.Thread.__init__(self)
        
    def run(self):
        self.messageContent = []
        print "\n Client",self.counter,"Connection Received"
        self.dct[self.counter].send("SERVER: You are now connected to the server.")
        self.code=0
        self.clientMess=0
        while self.code!=2:
            if self.clientMess=='exit':
                self.code+=2
            else:
                self.clientMess=self.dct[self.counter].recv(1024)
                try:
                    self.messageContent = pickle.loads(self.clientMess)
                    #messageContent = data = [1,name,msg,timeStamp,sendTo]
                    # 0: chat to all, 1: pm
                    if (self.messageContent[0] == 0): #chatbox 
                        try:
                            print self.messageContent[1] + " sends "+'"'+ self.messageContent[2] +'"'+ " to " + self.messageContent[4] + " at " + self.messageContent[3]
                        except:
                            pass
                        for client in self.dct:
                            if client == self.counter: 
                                pass # skip if the recepient is himself
                            else:
                                self.dct[client].send(str(self.counter)+" : "+self.messageContent[2]) #send message to all recepient
                    elif (self.messageContent[0] == 1): #private message
                        try:
                            print self.messageContent[1] + " sends "+'"'+ self.messageContent[2]+'"'+" to " + self.messageContent[4] + " at " + self.messageContent[3]
                        except:
                            pass
                    elif (self.messageContent[0] == 2):#change theme
                        try:
                            print self.messageContent[1] + " changed the background. Selected "+'"'+ self.messageContent[2]+'"'+ " at " + self.messageContent[3]
                        except:
                            pass
                        for client in self.dct:
                            if client == self.counter: 
                                pass # skip if the recepient is himself
                            else:
                                self.dct[client].send(self.messageContent[2]) #send message to all recepient
                                self.dct[client].send("!: "+self.messageContent[1]+" change the background.") #send message to all recepient


                    elif (self.messageContent[0] == 3): #typing
                        for client in self.dct:
                            if client == self.counter: 
                                pass # skip if the recepient is himself
                            else:
                                self.dct[client].send("!: " +self.messageContent[1] + " is typing...") #send message to all recepient
                    
                    elif (self.messageContent[0] == 4): #typing
                        try:
                            print self.messageContent[1] + " leave the chatroom and logout."
                        except:
                            pass
                        for client in self.dct:
                            if client == self.counter: 
                                pass # skip if the recepient is himself
                            else:
                                self.dct[client].send("SERVER: " +self.messageContent[1] + " exit the chatroom.") #send message to all recepient
                     
                    elif (self.messageContent[0] == 5): #emoticon
                        try:
                            print self.messageContent[1] + " sent an emoticon."
                        except:
                            pass
                        for client in self.dct:
                            if client == self.counter: 
                                pass # skip if the recepient is himself
                            else:
                                self.dct[client].send(self.messageContent[2]+"*"+self.messageContent[1]) #emoticon
                                self.dct[client].send("!: " +self.messageContent[1] + " sent an emoticon.") #send message to all recepient
                        
                        
                except:
                    pass
             
                
        server.close()
        
counter=0
host='127.0.0.1'
port=1024
serveradd=(host,port)
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(serveradd)
server.listen(3)
print "Server started on port",port,"\n"
while True:
    channel,addr=server.accept()
    name=channel.recv(1024)
    counter+=1
    if counter==1:
        dct={name:channel}
    else:
        dct[name]=channel
    ChatServer(dct,name).start()
