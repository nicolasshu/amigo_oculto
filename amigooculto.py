##############################################################
#
##############################################################


'''
NOTE: This python script has to be used with Python3
i.e. On Terminal, run the command:
	$ python3 amigooculto.py

'''
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random

MY_ADDRESS = "nicolas.s.shu@gmail.com"
PASSWORD = "enter_password_here"

#Port Numbers for Gmail
portSSL = 465
portTLS = 587

s = smtplib.SMTP(host='smtp.gmail.com',port = 587)
s.starttls()
s.login(MY_ADDRESS,PASSWORD)
#######################################################################################################
#######################################################################################################
# HELPER FUNCTIONS
#######################################################################################################
#######################################################################################################
#Extract information about template
def read_template(filename):
	with open(filename,'r',encoding='utf-8') as template_file:
		template_file_content = template_file.read()

	return Template(template_file_content)

#######################################################################################################
#Extract information about contacts
def get_contacts(filename):
	names = []
	emails = []
	shuffledNames = []

	with open(filename,mode='r',encoding = 'utf-8') as contacts_file:
		for a_contact in contacts_file:
			names.append(a_contact.split()[0]+" "+a_contact.split()[1])
			shuffledNames.append(a_contact.split()[0]+" "+a_contact.split()[1])
			emails.append(a_contact.split()[2])
		return names,shuffledNames,emails

#######################################################################################################
#######################################################################################################
names,shuffledNames,emails = get_contacts('./mycontacts.txt')
message_template = read_template('./mytemplate.txt')

#######################################################################################################
#Shuffle the names in one of the lists
random.shuffle(shuffledNames)

#######################################################################################################
# Make sure that no one got him/herself

Pass = False
crap = 0
while Pass is not True:
	print ('Enter while loop')
	crap = 0
	for k,item in enumerate(shuffledNames):
		if shuffledNames[k] == names[k]:
			crap = crap + 1
			print('mistake')
	if crap != 0:
		print ("Shuffle them")
		random.shuffle(shuffledNames)
	else:
		Pass = True
	print ("Names:")
	print (names)
	print ("Shuffled Names:")
	print (shuffledNames)
	print ("############################")

print ("FINALLY!!!!")
print ("Crap = "+str(crap))
print (names)
print (shuffledNames)

###########################################################################
print (names)
print (shuffledNames)
print (emails)



for sender,sender_email,recipient in zip(names,emails,shuffledNames):
	#For book keeping 
	print (sender,"|",sender_email,"|",recipient)
	
	#Initialize the message handle
	msg_handle = MIMEMultipart()

	#Setting up parameters of the email handle
	msg_handle['From']=MY_ADDRESS
	msg_handle['To']=sender_email
	msg_handle['Subject']="Testing testing"
	
	#Making substitution of variables in message template
	message = message_template.substitute(NOEL = sender.title(),RECIPIENTE = recipient.title())
	
	#Adding the message body
	msg_handle.attach(MIMEText(message,'plain'))
	#s.send_message(msg_handle)
	del msg_handle

s.quit()
print ("Code Finished.")
