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
testoffset = ['0','0','0','0']

zipped = zip(testfingers, testoffset)
blah = [''.join(zipped) for zipped in zipped]
print(blah)

activestring = 1
fullstring = ''
full_list = list()
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
        full_list.append(mystring)
        i += 1
        continue
    activestring += 1 #not getting to this line for some reason


#once we get here, go back down the strings

full_list.extend(reversed(full_list))


print(",".join(full_list))



#print in tab format

#from 6 to 1:
    #get the index of every 6
    #loop the number of 6's we find
    #place dashes based on index of 6's - subtract indexes for sequential items

#print("--" + "-"*fullstring.find("2"))


indices = [i for i, s in enumerate(full_list) if s.endswith('6')]
print(indices)


dashes = [y - x for x,y in zip(indices,indices[1:])]
print(dashes)

poop = ['17','2','1','2']
print(poop)
print(len(indices))
print(len(poop))

tabstring = ''
for z in range(0,4):
    tabstring = tabstring + '-' * int(poop[z]) + str(full_list[indices[z]][:1])
    #print(tabstring)

tabstring = ''
sup = []
for q in range(1,3):
    indices = [i for i, s in enumerate(full_list) if s.endswith(str(q))]
    dashes = [y - x for x,y in zip(indices,indices[1:])]
    print('q = ', q)
    print('indices[0] = ', indices[0])
    print('dashes = ', dashes)
    sup = [indices[0]] + dashes
    print('sup = ',sup)
    
    #maybe run once first, then loop from 1 to len, so we get the correct number of dashes first
    for z in range(0,len(sup)):
        tabstring = tabstring + '-' * int(sup[z]) + str(full_list[indices[z]][:1])
        #need to also do something about the dashes in between
    tabstring = tabstring + '\n'
print(tabstring)
    
print(",".join(full_list))    
    
#we won't always have every string played...
#check if indices list is empty - if so, just add dashes
#print('-' * indices[0] + full_list[indices[0]][:1])

#print(indices[0]-indices[-1])


