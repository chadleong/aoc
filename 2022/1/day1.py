with open('input.txt') as f:
    data=f.readlines()
    f.close()

moose={}
moose_no=1
cals=0
for i, val in enumerate(data):
    # print(i, val)
    if val != "\n":
        cals += int(val)
        moose[moose_no]=cals
    else:
        cals=0
        moose_no+=1

print(moose)
max_moose=max(moose, key=moose.get)
print(moose[max_moose])