testfingers = ['1','2','3','4']
testoffset = ['0','1','0','1']

zipped = zip(testfingers, testoffset)
blah = [''.join(zipped) for zipped in zipped]
print(blah)

fingOffsets = zip(*(testfingers, testoffset))

for x in fingOffsets:
  print(x)[0]

#
