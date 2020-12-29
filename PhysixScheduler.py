#the data has class number instead of points. class 1 has 2 points and class 2 has 1 point....so we need to swtich.
def switch(p):
	if p == 1:
		return '2'
	else:
		return '1'

def efficiency(d):
	#dList[i]: Record (in t/T/P format) of some task of some day of a participant 
	#dList[i][0]:t 		 dList[i][2]:T 	 	dList[i][4]:P 
	#sum(eList): sum of (ti/Ti). The whole expression is to calculate average. 
	dList = d.split()
	eList = []
	for i in dList:
		temp = i.split('/')
		t = temp[0]
		T = temp[1]
		p = switch (temp[2])
		eList.append( eval(t)/eval(T) )
	 
	return round((sum(eList)/len(eList)) * 100, 2)

def productivity(d):
	#dList[i]: Record (in t/T/P format) of some task of some day of a participant 
	#dList[i][0]:t 		 dList[i][2]:T 	 	dList[i][4]:P 
	#Numerator: sum of (ti*Pi). Denominator: sum of (Ti*Pi)
	dList = d.split()
	eList = []
	for i in dList:
		temp = i.split('/')
		t = temp[0]; T = temp[1]; p = switch (temp[2])
		eList.append(eval(t)*eval(p))
	numerator = sum(eList)
	eList.clear()#To clear the above data and make it usable for the next operations
	for i in dList:
		temp = i.split('/')
		t = temp[0]; T = temp[1]; p =switch (temp[2])
		eList.append(eval(T)*eval(p))
	denominator = sum(eList)
	return round((numerator/denominator) * 10, 2)

def progress():
	return None

#input Processing
#counting number of lines
participantsData = open ('participantsData.txt', 'r')
numberOfLines = 0
for lines in participantsData:
      if lines != '\n':
            numberOfLines += 1			

participantsData.seek(0)
participant = [] #to temporarly store a participant's efficiency and productivity until copied into allParticipants.
allParticipants = [] #

#Calculating e and p & storing them in allParticipants
for i in range(1, numberOfLines + 1):
	Input = participantsData.readline()
	e = efficiency (Input) #Efficiency of that day
	p = productivity (Input) #Efficiency of that day
	participant.append([e, p])	
	if i % 7 == 0:
		allParticipants.append(participant.copy())
		participant.clear()


#outputProcessing
#allParticipant is a 3d list with allParticipant[P][D][I]
#P: Which participant?	 D:what day?	I: Which info? Efficiency or Productivity?
days = ["Monday","Tuesday","Wednsday","Thursday","Friday","Saturday","Sunday"]
dayCount = 0
participantCount = 1

for participant in allParticipants:
      print ("Participant", participantCount, "Record")
      print ()
      print ("Day \t\t Efficiency \t Productivity")
      print ("-------------------------------------------------")
      for day in participant:
            print (days[dayCount], ' \t', day[0], '\t\t', day[1])
            dayCount += 1
      print (); print ()
      participantCount += 1
      dayCount = 0

participantsData.close()

#Comments on efficiency 

	# ti in the formula is t in the code
	# d[i][0] = t  d[i][1] = T  d[i][2] = point  ||  e = summation ( t * p )
	# dList[i] is the i'th task data. t/T/point
	# in the sheet its t/T/class. In the code its t/T/points
	# sum(elist) is equivalent to sum of ti in the formula.
