list = ["Aditi" , "Surat" , 20 , "SVIT" , "TY" , 7.5]
print(list)

#insert element "vasad" at index 5
list.insert(5,"vasad")
print(list)

#adding elemrnt at th end of the list
list.append("vadodara")
print(list)

#accesing elements of list
print(list[1])
print(list[3])

#removing element of the list(remove first accurance of element)
list.remove("SVIT")
print(list)

#remove the element at given index
list.pop(3)
print(list)

#delete the elemrnt of the given index
del list[2]
print(list)

#add multiple element at the end of the list
list.extend([1,2,3])
print(list)