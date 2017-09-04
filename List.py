# How to create a list

courses = ['History', 'Math', 'Physics', 'CompSci']

print(len(courses))           # Returns no of items or length of a list 

print(courses[1],courses[2])   # Will return Math and Physics

print(courses[-1])    #List items can be accessed through negative number locations as -1 for CompSci

print(courses[-2])    #Return Physics

#print(courses[4])     ## Error:  item out of range

print(courses[0:2])    # To access range of values
                     # First index 0 is inclusive but last 2 is not so will return item at 0 and 1.

print(courses[:2])     # It will assume start index as 0 to 2.

print(courses[2:])    # Same as it will assume index from 2 to till end which is 3

# To append items to our List we can perform append
courses.append('Art')
print(courses)            # New item is added to the List at the end.

#To insert item at a specific location use insert method
courses.insert(0,'Humanity')
print(courses)

courses.insert(2,'SocialScience')
print(courses)   # New item will be inserted to location 2 and existing item will be shifted to consecutive next locations.


courses_2 = ['Education','SoftwareDesign']

courses.insert(0,courses_2)   
# If here we use insert it will create courses_2 as sub list of List courses.
print(courses)
print(courses[0])  # will return sublist at location 0 as ['Education','SoftwareDesign']


#Remove values from List
courses.remove('Art')#,'SoftwareDesign')

# To add multiple items at once to a List, we use Extend method.
#courses.extend(courses_2)
print(courses)

courses.pop()   #automatically remove last item , behaves as stackwith List
print(courses)

popped=courses.pop()
print(popped)   #to see what items are removed
print(courses)

