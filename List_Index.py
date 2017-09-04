courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)

nums= [1,6,3,2,9,4,3,5,6]
print(nums)

print(courses.index('CompSci'))     # will provide the index location for this List

#print(courses.index('Art'))    # will give an Error: Art is not in List.

# To search specific value results in List.
print('Math' in courses)      # will return True
print('Art' in courses)       # will return False