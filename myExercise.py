import sys
namesdict={}
lista =[]
students = open(sys.argv[1],"r").readlines()
names = sys.argv[2].split(",")
for i in students:
    i =i.split(":")
    namesdict[i[0]] = i[1]
for i in names:
    try:
        print("Name: {}, University: {}".format(i,namesdict[i]), end="")
    except:
        print("No record of '{}' was found".format(i))
