
f=open("running-config.cfg","rt") 
f=f.read()
f=f.split("\n")
final_list=list()
interface_list=list()
intdict=dict()
vlancheck=0
def listoftup():
	for value in f:
		if "interface" in value:
			value=value.split()
			interface_list.append(value[1])
		if "nameif" in value:
			value=value.split()
			if "no" in value[0]:
				interface_list.append("null")
				final_list.append(tuple(interface_list))
				del  interface_list[:]
			else:
				interface_list.append(value[1])
				final_list.append(tuple(interface_list))
				del interface_list[:]
	return final_list
print (listoftup())

