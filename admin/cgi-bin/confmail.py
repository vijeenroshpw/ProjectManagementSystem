#This script will send comformation Mail to the users and guides
import smtplib
import string
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText 
def mail()
	passwd=raw_input("Enter password ");
	server = smtplib.SMTP("smtp.gmail.com:587")
	server.starttls()
	server.login("gecgitrepository@gmail.com",passwd)
	while row:
		server = smtplib.SMTP("smtp.gmail.com:587")
		server.starttls()
		server.login("gecgitrepository@gmail.com",passwd)
		handle=MIMEMultipart()
		handle["From"]="gecgitrepoitory@gmail.com"
		handle["Subject"]=" Confirmation Email from  GEC Git Repo "
		handle["To"]=row[3]
		message='''This is a computer generated Email.Please note That 
				   reply to this address may not be monitered.
                   You have received this mail  as you have requested 
				   for confirmation code of GEC GitRepository.

		    	   Here are your account details:
			       Username          : ''' + row[0] +'''
		    	   Confirmation Code : ''' + randword + ''' 
	        

	    		   if you have no idea what is happening,please ignore
				   this mail.Some body might have entered your Mail Id
				   by mistake. '''
	
		handle.attach(MIMEText(message))
		server.sendmail("gecgitrepository@gmail.com",row[3],handle.as_string())
		message=""
		print "Mail sent to "+row[3]
		row = cursor.fetchone()
		server.quit()