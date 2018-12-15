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


'''
--------------------------------------
BEFORE TESTING
Names:
['Priscilla Chan', 'Derek Chan', 'Jack Shu', 'Jane Shu', 'Katia Chang', 'Leandro Chan', 'Natalia Shu', 'Nicolas Shu', 'Simone Chang', 'Tzu Ming', 'Wilson Chung', 'Jaime Shu', 'Jine Shu']
Shuffled Names:
['Leandro Chan', 'Jaime Shu', 'Derek Chan', 'Jane Shu', 'Priscilla Chan', 'Wilson Chung', 'Natalia Shu', 'Jack Shu', 'Katia Chang', 'Nicolas Shu', 'Simone Chang', 'Tzu Ming', 'Jine Shu']
--------------------------------------
Enter while loop
mistake
mistake
mistake
Shuffle them
Names:
['Priscilla Chan', 'Derek Chan', 'Jack Shu', 'Jane Shu', 'Katia Chang', 'Leandro Chan', 'Natalia Shu', 'Nicolas Shu', 'Simone Chang', 'Tzu Ming', 'Wilson Chung', 'Jaime Shu', 'Jine Shu']
Shuffled Names:
['Natalia Shu', 'Nicolas Shu', 'Priscilla Chan', 'Jane Shu', 'Jine Shu', 'Jaime Shu', 'Tzu Ming', 'Jack Shu', 'Derek Chan', 'Simone Chang', 'Wilson Chung', 'Leandro Chan', 'Katia Chang']
############################
Enter while loop
mistake
mistake
Shuffle them
Names:
['Priscilla Chan', 'Derek Chan', 'Jack Shu', 'Jane Shu', 'Katia Chang', 'Leandro Chan', 'Natalia Shu', 'Nicolas Shu', 'Simone Chang', 'Tzu Ming', 'Wilson Chung', 'Jaime Shu', 'Jine Shu']
Shuffled Names:
['Simone Chang', 'Jaime Shu', 'Katia Chang', 'Natalia Shu', 'Jine Shu', 'Derek Chan', 'Jane Shu', 'Priscilla Chan', 'Wilson Chung', 'Tzu Ming', 'Nicolas Shu', 'Leandro Chan', 'Jack Shu']
############################
Enter while loop
mistake
Shuffle them
Names:
['Priscilla Chan', 'Derek Chan', 'Jack Shu', 'Jane Shu', 'Katia Chang', 'Leandro Chan', 'Natalia Shu', 'Nicolas Shu', 'Simone Chang', 'Tzu Ming', 'Wilson Chung', 'Jaime Shu', 'Jine Shu']
Shuffled Names:
['Natalia Shu', 'Derek Chan', 'Jane Shu', 'Wilson Chung', 'Jine Shu', 'Tzu Ming', 'Leandro Chan', 'Katia Chang', 'Jaime Shu', 'Jack Shu', 'Simone Chang', 'Nicolas Shu', 'Priscilla Chan']
############################
Enter while loop
mistake
Shuffle them
Names:
['Priscilla Chan', 'Derek Chan', 'Jack Shu', 'Jane Shu', 'Katia Chang', 'Leandro Chan', 'Natalia Shu', 'Nicolas Shu', 'Simone Chang', 'Tzu Ming', 'Wilson Chung', 'Jaime Shu', 'Jine Shu']
Shuffled Names:
['Derek Chan', 'Wilson Chung', 'Jine Shu', 'Leandro Chan', 'Tzu Ming', 'Jaime Shu', 'Katia Chang', 'Jane Shu', 'Jack Shu', 'Priscilla Chan', 'Simone Chang', 'Nicolas Shu', 'Natalia Shu']
############################
Enter while loop
Names:
['Priscilla Chan', 'Derek Chan', 'Jack Shu', 'Jane Shu', 'Katia Chang', 'Leandro Chan', 'Natalia Shu', 'Nicolas Shu', 'Simone Chang', 'Tzu Ming', 'Wilson Chung', 'Jaime Shu', 'Jine Shu']
Shuffled Names:
['Derek Chan', 'Wilson Chung', 'Jine Shu', 'Leandro Chan', 'Tzu Ming', 'Jaime Shu', 'Katia Chang', 'Jane Shu', 'Jack Shu', 'Priscilla Chan', 'Simone Chang', 'Nicolas Shu', 'Natalia Shu']
############################
FINALLY!!!!
Crap = 0
['Priscilla Chan', 'Derek Chan', 'Jack Shu', 'Jane Shu', 'Katia Chang', 'Leandro Chan', 'Natalia Shu', 'Nicolas Shu', 'Simone Chang', 'Tzu Ming', 'Wilson Chung', 'Jaime Shu', 'Jine Shu']
['Derek Chan', 'Wilson Chung', 'Jine Shu', 'Leandro Chan', 'Tzu Ming', 'Jaime Shu', 'Katia Chang', 'Jane Shu', 'Jack Shu', 'Priscilla Chan', 'Simone Chang', 'Nicolas Shu', 'Natalia Shu']
['Priscilla Chan', 'Derek Chan', 'Jack Shu', 'Jane Shu', 'Katia Chang', 'Leandro Chan', 'Natalia Shu', 'Nicolas Shu', 'Simone Chang', 'Tzu Ming', 'Wilson Chung', 'Jaime Shu', 'Jine Shu']
['Derek Chan', 'Wilson Chung', 'Jine Shu', 'Leandro Chan', 'Tzu Ming', 'Jaime Shu', 'Katia Chang', 'Jane Shu', 'Jack Shu', 'Priscilla Chan', 'Simone Chang', 'Nicolas Shu', 'Natalia Shu']
['primey88@gmail.com', 'dkschan@poli.ufrj.br', 'jkshu@hotmail.com', 'jylshu@gmail.com', 'katiahopow@gmail.com', 'lechan56@gmail.com', 'nataliapshu@gmail.com', 'nicolas.s.shu@gmail.com', 'simonehpchang@gmail.com', 'hutzuming@hotmail.com', 'wleec@yahoo.com', 'jshu@oi.com.br', 'shu.jine@gmail.com']
Priscilla Chan | primey88@gmail.com | Derek Chan
Derek Chan | dkschan@poli.ufrj.br | Wilson Chung
Jack Shu | jkshu@hotmail.com | Jine Shu
Jane Shu | jylshu@gmail.com | Leandro Chan
Katia Chang | katiahopow@gmail.com | Tzu Ming
Leandro Chan | lechan56@gmail.com | Jaime Shu
Natalia Shu | nataliapshu@gmail.com | Katia Chang
Nicolas Shu | nicolas.s.shu@gmail.com | Jane Shu
Simone Chang | simonehpchang@gmail.com | Jack Shu
Tzu Ming | hutzuming@hotmail.com | Priscilla Chan
Wilson Chung | wleec@yahoo.com | Simone Chang
Jaime Shu | jshu@oi.com.br | Nicolas Shu
Jine Shu | shu.jine@gmail.com | Natalia Shu
Code Finished.

'''
