import sys
import os

#print("you")
#fIO = open("test_data.txt", "r+")
#str = fIO.read(10);
#print(str)
#fIO.close()
myResultList = [0] * 15
#print(myResultList)

def initResultList():
    myResultList = [0] * 15
    
def updateSingleChar(*args):
    print("start fun test")
    if args[0] == 'Z':
         myResultList[0] += 1;
    print("end of fun")
 

with open("test_data.txt") as f:
    #content = f.readline()
    content = f.read().split("\n")

#content = [x.strip() for x in content]

print("Total size: " + str(len(content)))
f.close()

#for allL in range(len(content)):
#    strlist = list(content[allL])
#    funcX(strlist)
    #fullList = fullList + strlist
    #print(strlist)

fullList = list(content[50])
#print(strlist)


#def funcX(fullList = [],*args): 
for i in range(len(fullList)):
        #print(strlist[i])
        
        if fullList[i] == 'Z':
             myResultList[0] += 1;
        if fullList[i] == 'W':
             myResultList[1] += 1;
        if fullList[i] == 'U':
             myResultList[2] += 1;
        if fullList[i] == 'X':
             myResultList[3] += 1;
        if fullList[i] == 'G':
            myResultList[4] += 1;
        if fullList[i] == 'H':
            myResultList[5] += 1;
        if fullList[i] == 'F':
            myResultList[6] += 1;
        if fullList[i] == 'V':
            myResultList[7] += 1;
        if fullList[i] == 'S':
            myResultList[8] += 1;
        if fullList[i] == 'R':
            myResultList[9] += 1;
        if fullList[i] == 'T':
            myResultList[10] += 1;
        if fullList[i] == 'O':
            myResultList[11] += 1;
        if fullList[i] == 'N':
            myResultList[12] += 1;
        if fullList[i] == 'I':
            myResultList[13] += 1;
        if fullList[i] == 'E':
            myResultList[14] += 1;     
        i += 1
#print(myResultList)

def getResult():
    result = ""
    
    numX = 0

    if myResultList[0] >= 1:
        numX = myResultList[0]
        for i in range(numX):
            result = result + '0'
            myResultList[0]-=1
            myResultList[14]-=1
            myResultList[9]-=1
            myResultList[11]-=1
        numX = 0
    if myResultList[1] >= 1:
        numX = myResultList[1]
        for i in range(numX):
            result = result + '2'
            myResultList[10]-=1
            myResultList[1]-=1
            myResultList[11]-=1
        numX = 0
    if myResultList[2] >= 1:
        numX = myResultList[2]
        for i in range(numX):
            result = result + '4'
            myResultList[6]-=1
            myResultList[11]-=1
            myResultList[2]-=1
            myResultList[9]-=1
        numX = 0
    if myResultList[3] >= 1:
        numX = myResultList[3]
        for i in range(numX):
            result = result + '6'
            myResultList[8]-=1
            myResultList[13]-=1
            myResultList[3]-=1
        numX = 0
    if myResultList[4] >= 1:
        numX = myResultList[4]
        for i in range(numX):
            result = result + '8'
            myResultList[14]-=1
            myResultList[13]-=1
            myResultList[4]-=1
            myResultList[5]-=1
            myResultList[10]-=1
        numX = 0
    if myResultList[5] >= 1:
        numX = myResultList[5]
        for i in range(numX):
            result = result + '3'
            myResultList[10]-=1
            myResultList[5]-=1
            myResultList[9]-=1
            myResultList[14]-=1
            myResultList[14]-=1
        numX = 0
    if myResultList[6] >= 1:
        numX = myResultList[6]
        for i in range(numX):
            result = result + '5'
            myResultList[6]-=1
            myResultList[13]-=1
            myResultList[7]-=1
            myResultList[14]-=1
        numX = 0
    if myResultList[7] >= 1:
        numX = myResultList[7]
        for i in range(numX):
            result = result + '7'
            myResultList[8]-=1
            myResultList[14]-=1
            myResultList[7]-=1
            myResultList[14]-=1
            myResultList[12]-=1
        numX = 0
    if myResultList[11] >= 1:
        numX = myResultList[11]
        for i in range(numX):
            result = result + '1'
            myResultList[11]-=1
            myResultList[12]-=1
            myResultList[14]-=1
        numX = 0
    if myResultList[13] >= 1:
        numX = myResultList[14]
        for i in range(numX):
            result = result + '9'
            myResultList[12]-=1
            myResultList[13]-=1
            myResultList[12]-=1
            myResultList[14]-=1
        numX = 0
        
    print (result)
    #print (myResultList)
    
print ("start func convert")
getResult()
print ('end')

#refer to some test sample to the follwing link:
# https://www.codementor.io/sheena/essential-python-interview-questions-du107ozr6

def print_directory_contents(sPath):
    import os                                       
    for sChild in os.listdir(sPath):                
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)
            
print_directory_contents("..\Python")

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]

print(A0)
print(A1)
print(A2)
print(A3)
print(A4)
print(A5)
print(A6)

def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l) 

f(2)
f(3,[3,2,1])
f(3)

