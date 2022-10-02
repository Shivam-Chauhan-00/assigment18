print("program to convert two list into dictonary, item of  list 1 is the key and list 2 is the value")
l1=["name","class","age","city","state"]
l2=["shivam chauhan","bca","22","aligarh","uttar pradesh"]
d1={}
n=0

print("list firsr",l1,"\nlist second",l2)
while n<(len(l1)) :
   d1[l1[n]]=l2[n]    
   n=n+1

for e in d1 :
    print(e,d1[e])