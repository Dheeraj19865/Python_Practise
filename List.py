#List 

lil = [10,20,44.45,True,'Kodnest']
print(lil, type(lil))

#append(): add ele to the end of the list
lil.append(300)
print(lil)

#insert() : to add ele at specified index
lil.insert(1,15)
print(lil)

#remove(): removes the first occurence of the  specific ele
lil.remove(20)
print(lil)

#in and not in operator
print(2000 in lil) #false
print('Kodnest' in lil) #true


#pop() without argument
lil.pop()
print(lil)

#pop() with argument
res = lil.pop(4)
print(res)
print(lil)


#del keyword:
del lil[1]
print(lil)