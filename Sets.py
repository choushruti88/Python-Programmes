#Sets  : Sets throw away duplicates
# Sets dont care about orders : each time sequence of items will be different
cs_courses = {'History', 'Math', 'Physics', 'CompSci','Math'}
print(cs_courses)

print('Math' in cs_courses)

art_courses = {'History', 'Math','Art', 'Design'}

print(cs_courses.intersection(art_courses))  #To find out same courses in both sets

print(cs_courses.difference(art_courses))  # Find out different courses in cs
print(art_courses.difference(cs_courses))  # Find out different courses in art

print(cs_courses.union(art_courses))  ## Find out all courses

