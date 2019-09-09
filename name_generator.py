import json, random

with open("names.json", "r") as readfile:
	names=json.load(readfile)
#	print("names should be laoded!")

first_list=[]

for i in names:
#	print (i)
#	print (names[i])
	#if names[i]["type"]=="first":
	#	first_list.append(i)
#	if i in names.values():
#		first_list.append(i)
#	print (names[i]["type"])
	if "first" in names[i]["type"]:
#		print ("yes")
		first_list.append(i)
	
#for i in first_list:
#	print (i)
first_name=random.choice(first_list)
#print (first_name)


last_list=[]

for i in names:
#	print (i)
#	print (names[i])
	#if names[i]["type"]=="first":
	#	first_list.append(i)
#	if i in names.values():
#		first_list.append(i)
#	print (names[i]["type"])
	if "last" in names[i]["type"]:
#		print ("yes")
		last_list.append(i)
	
#for i in first_list:
#	print (i)
last_name=random.choice(last_list)
#print (last_name)
print ("Your name is", first_name, last_name)