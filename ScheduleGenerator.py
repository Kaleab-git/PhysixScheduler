class Schedule:
    def __init__(self):
    # Each day is a 2D least. The rows contain information of 1 task in 3 fields. When it starts(int), when it ends(int), and its name(string).
    # start and end time in military time. 13:00 would be 1300. There's a total of 2400 available time.
        self.Monday = [[],[],[],[],[],[],[]]
        self.Tuesday = [[],[],[],[],[],[],[]]
        self.Wednesday = [[],[],[],[],[],[],[]]
        self.Thursday = [[],[],[],[],[],[],[]]
        self.Friday = [[],[],[],[],[],[],[]]
        self.Saturday = [[],[],[],[],[],[],[]]
        self.Sunday = [[],[],[],[],[],[],[]]
        self.week = [self.Monday,self.Tuesday,self.Wednesday,self.Thursday,self.Friday,self.Saturday,self.Sunday]
    
    #unit: which unit of work time. 1-7
    def addTask(self, day, name, unit, startTime, endTime):
        if day == 'monday':
           self.Monday[unit-1].append(name); self.Monday[unit-1].append(startTime); self.Monday[unit-1].append(endTime)
        elif day == 'tuesday':
           self.Tuesday[unit-1].append(name); self.Tuesday[unit-1].append(startTime); self.Tuesday[unit-1].append(endTime)
        elif day == 'wedensday':
           self.Wednesday[unit-1].append(name); self.Wednesday[unit-1].append(startTime); self.Wednesday[unit-1].append(endTime)
        elif day == 'thursday':
           self.Thursday[unit-1].append(name); self.Thursday[unit-1].append(startTime); self.Thursday[unit-1].append(endTime)
        elif day == 'friday':
           self.Friday[unit-1].append(name); self.Friday[unit-1].append(startTime); self.Friday[unit-1].append(endTime)
        elif day == 'saturday':
           self.Saturday[unit-1].append(name); self.Saturday[unit-1].append(startTime); self.Saturday[unit-1].append(endTime)
        elif day == 'sunday':
           self.Sunday[unit-1].append(name); self.Sunday[unit-1].append(startTime); self.Sunday[unit-1].append(endTime)
        else:
            return 'incorrect Name'

    def generateSchedule(self):
        for i in self.week:
            count = 0
            taskCount = 0
            print ('Day')
            while taskCount < len(i):
                print ('       | Task', count, i)
                count += 1
                taskCount += 1
            print ()



physix = Schedule()

physix.addTask('thursday', 'SAT', 1, 730, 830)

#print (physix.Thursday)
physix.generateSchedule()





