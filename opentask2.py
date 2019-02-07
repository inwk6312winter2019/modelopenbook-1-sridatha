fin=open("Street_Centrelines.csv","r")
def easy(fin):
	list1=[]
	for line in fin:
		line=line.split(",")
		list1.append((line[2],line[4],line[6],line[7]))
	return list1

print(easy(fin)) 

def maintenance():
    hist = dict()
    for fun in fin:
        fun = fun.split(",")
        if fun[12] not in hist:
            hist[fun[12]] = 1
        else :
            hist[fun[12]] += 1
    print(hist)


def unique():
    own_list = fin[11]
    new_list = []
    for u in fin:
        u = u.split(",")
        if u[11] not in new_list:
            new_list.append(u[11])
    print(new_list)

def street_classes():
	street_class={}
	for data in fin:
		if data[10] not in street_class:
			street_class[data[10]]=data[2]
		else:
			street_class[data[10]].join(fin[2])
	return street_class

street_classes()
maintenance()
unique()
