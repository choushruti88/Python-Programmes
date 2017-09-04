courses = ['History', 'Math', 'Physics', 'CompSci','Humanity','SocialSci']

for item in courses:
    print(item)


for course in courses:
    print(course)    # Item or course are variables, any name can be given


for index,course in enumerate(courses):
    print(index, course)   #will have access to index and course values


course_str = ', '.join(courses)
print(course_str)       # can be seperated thorugh space or comma or hyphen

course_str1 = ' - '.join(courses)
print(course_str1)

new_list = course_str.split(' - ')
print(course_str)
print(new_list)
 