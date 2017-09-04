# Tuples are different from List because Tuples are immutable (changable)

# courses = ['History','Math','Physics','CompSci','Humanity']

#Mutable
#list_1 = ['History','Math','Physics','CompSci','Humanity']
#list_2 = list_1

#print(list_1)
#print(list_2)

# list_1[0] = 'Art'    #Muttable objects as list will change the value for list_2 items too.

# print(list_1)
# print(list_2)

# Immutable objects as Tuple will not make changes the value for list_2 items too.
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)   

tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)