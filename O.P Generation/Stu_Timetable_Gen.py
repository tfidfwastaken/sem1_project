import json
import os



listOfClasses = ['1A','1B','1C','2A','2B']      #Expected to be gathered at input
listOfDays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']   #Expected to be gathered at input




def __retrJSON(jsonFileName):         #Loads the Origin file(JSON) - 1 arg
    with open('{}.json'.format(jsonFileName)) as temp:
        jsonFile = json.load(temp)
    return jsonFile

def __tableBorder():            #Creates the bottom and top lines of the table
    tempStr = '+---------'*10 + '+' + '\n'
    return tempStr

def __colNum():       #Creates 10 Columns - first column empty, 
    tempStr = '|' + ' '*9 + '|'
    for i in range(1,10):
        tempStr +=  '{:<9}'.format(i) + '|'
    tempStr += '\n'
    return tempStr

def __subLine(day,periodList):        #Given a list containing periods of a day, returns a string
    day = day[0:3].capitalize()     #Truncates day string to 3 letters
    tempStr = '|' + '{:<9}'.format(day) + '|'
    for period in periodList:
        tempStr += '{:<9}'.format(period) + '|'
    tempStr += '\n'
    return tempStr

def __rowsep():                 # Creates row seperators
    tempStr = '|---------' + '+---------'*9+ '|' + '\n'
    return tempStr





    
def genClassTt(jsonFileName):       #Generates the class timetable
    data = __retrJSON(jsonFileName)

    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') #Var assigned 'path of Desktop' (code for windows)
    # desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')              # Code for Unix
    dirStr = '{}\\{}'.format(desktop,'Student Timetables')
    try:
        os.mkdir(dirStr)                                                                #This Directory to be created in another directory called Timetables (If there is time)
    except FileExistsError:
        print('Directory already exists. Will do ammendments in the directory.')

#For eachClass iterates over JSON file to retrieve timetable the particular class,
#And generates a timetable for each class as a text file
#And stores them in a directory named 'Student Timetables' on the desktop.
    for eachClass in listOfClasses:
        rawClassTt = []
        for Day in data:                #Appends each day's periods to rawClasTt[]
            rawClassTt.append(data[Day][eachClass])
        
        with open('{}\\{}.txt'.format(dirStr,eachClass), mode='w') as file:        
            tempStr = __tableBorder()
            file.write(tempStr)
            tempStr = __colNum()
            file.write(tempStr)
            for i in range(5):
                tempStr = __rowsep()
                file.write(tempStr)
                tempStr = __subLine(listOfDays[i], rawClassTt[i])
                file.write(tempStr)
            tempStr = __tableBorder()
            file.write(tempStr)







                
genClassTt('jsonSample')



