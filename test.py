import random 
shuffledNames = ['1','2','3']
names = ['1','3','2']

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