# Dictionary works on key value concepts

student = {'name':'John', 'age': 25, 'courses': ['Math','ComputSci']}

print(student['courses'])
#print(student['phone']) # when we try to access the key which doesnt exist it gives KeyError


# we can access the key with 1
#student = {1:'John', 'age': 25, 'courses': ['Math','ComputSci']}
#print(student[1])

#If we donot want to get KeyError but None or any default value
# "get" method can be used as below
print(student.get('name'))
print(student.get('phone'))  # None

print(student.get('phone', 'Not Found'))  # specify message to be recieved


# New entry to the Dictionary
student['phone'] = '555-5555'
print(student['phone'])

#Update an value for key
student['name'] = 'Jane'
print(student)

#Update multiple values at a time
student.update({'name':'Josh','age':27,'phone':'558-2577'})
print(student)

#Delete specific key and values
#del student['age']
# print(student)

#or can be done with POP method
#age= student.pop('age')
#print(student)

#To find out length of our KEy and Value
print(len(student))

print(student.keys())    #Keys
print(student.values())  #Values
print(student.items())   #Key-value pairs wll be visible

for key in student:
    print(key)

for key,value in student.items():
    print(key,value)