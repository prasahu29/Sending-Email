import smtplib as s
from email import message

ob = s.SMTP("smtp.gmail.com",587) # setup port

ob.starttls()
ob.login("trumpprashant29@gmail.com","your email password") #whose email id send by mail 
subject = "486a"   #email subject 
body = "Hello puneet 10 INR "  # email msg 
message = "Subject:{}\n\n{}".format(subject,body)

list_of_address = [ "punitrock11@gmail.com"] #whose msg send
ob.sendmail("trumpprashant29",list_of_address,message)
print("send successfully")
ob.quit()