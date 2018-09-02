import itertools


fingerPerms = itertools.permutations(['1','2','3','4'], 4)
offsets = itertools.product(['0', '1', '2', '3', '4', '5'], repeat=4)



# fingOffset = dict(zip(fingerPerms, offsets)) --zipping full arrays together

# for each item in fingerperms
    #for each in offsets
        #zip x,y

# for x,y in fingerPerms, offsets:
#     print(itertools.zip_longest(x,y))

# for x in fingerPerms:
#     for y in offsets:
#         result = dict(zip(x,y))
#         for z in result:
#             print(z)
# for z in result:
#     print(z)


for x in fingerPerms:
    for y in offsets:
        print('x: ', x, 'y: ', y)
        for z in dict(zip(x,y)):
            print(z)


fingOffsets = zip(*(fingerPerms, offsets))

# for x in fingOffset:
#     print(x)

# def toTab(fingOffset):
