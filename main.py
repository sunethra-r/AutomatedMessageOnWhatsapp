import pywhatkit
num=input("Enter receiver's Phone No. (including country code): ")
msg=input("Enter the message you you want to send: ")
hr=int(input("Enter at which hour of time you want to send message: "))
mt=int(input("Enter at which minute of that hour you want to send message: "))
pywhatkit.sendwhatmsg(num,msg,hr,mt)
print("Message Sent :)")