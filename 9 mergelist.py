print("program to merge two python dictionaries into one dictionary")
d1={"name": "aman","class":"mca","book":"java"}
d2={"city":"aligarh","fathername":"rakesh chauhan","friendname":"shivam"}
print("d1=",d1,"\nd2=",d2)
for e in d2 :
    d1[e]=d2[e]

print("now d1 is..",d1)

