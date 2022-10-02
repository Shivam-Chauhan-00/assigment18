print("program to create 3 dictionaries, then create one dictiionary that will contian the other three dict")
d1={"name":"Shivam","sirname":"Chauahn","gender":"male"}
d2={"class":"BCA","course":"web development"}
d3={"subject":"python","City":"Aligarh"}
d4=dict(a=d1,b=d2,c=d3)
print(d4)
print(d4["a"])
print(d4["b"])
print(d4["cs"])