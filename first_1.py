'''
Created on Feb 1, 2018

@author: Justin
'''
import itertools

fingers = ['1','2','3','4']
for y in itertools.permutations(fingers, 4):
    print(y)



offset = ['0','1','2','3','4','5']
print(offset)

for x in itertools.product(offset, repeat=4):
    print(x)

#zip fingers and offset

    
testfingers = ['1','2','3','4']
testoffset = ['0','1','0','1']

zipped = zip(testfingers, testoffset)
blah = [''.join(zipped) for zipped in zipped]
print(blah)

activestring = 1
fullstring = ''
finished=False

mystring = blah[3][:1]+str((int(blah[3][-1:])+int(1)))
print(mystring)

#activestring is level
#create finger/string pair four times
#increment activestring
#^^
#if we hit string 6, finish after this set of 4

#need to change this to list rather than string

while finished == False:
    for i in range(0,4):
        mystring = blah[i][:1]+str((int(blah[i][-1:])+int(activestring)))
        if int(int(blah[i][-1:])+int(activestring)) == 6:
            finished = True
        fullstring = fullstring + mystring + ","
        i += 1
        continue
    activestring += 1 #not getting to this line for some reason


#once we get here, go back down the strings

activestring = 6
finished = False

while finished == False:
    for i in range(3,-1,-1):
        mystring = blah[i][:1]+str((int(activestring)-int(blah[len(blah)-i-1][-1:])))
        if int(int(activestring)-int(blah[i][-1:])) == 1:
            finished = True
        fullstring = fullstring + mystring + ","
        i -= 1
        continue
    activestring -= 1
print(fullstring[:-1:])


#print in tab format

#from 6 to 1:
    #get the index of every 6
    #loop the number of 6's we find
    #place dashes based on index of 6's - subtract indexes for sequential items

print("--" + "-"*fullstring.find("2"))



