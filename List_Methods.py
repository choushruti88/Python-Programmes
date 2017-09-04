courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)

# courses.reverse()   #to reverse items in list in alphabatical ascending order
# print(courses)

# courses.sort()
# print(courses)

nums= [1,6,3,2,9,4]

# nums.sort()           #to reverse numbers in ascending order
# print(nums)               

#to reverse the order we can use reverse method in sort with reverse=True
# courses.sort(reverse=True)
# nums.sort(reverse=True)
# print(courses,nums)

#If we do not want to order the original default order or arrangement of List then we can use sorted function on List.
sorted(courses)    # will not give sorted list but same because we have to assign this methos to a new variable

sorted_courses = sorted(courses)
print(sorted_courses)

print(min(nums))     # minimum number
print(max(nums))     # maximum number

print(sum(nums))    # sum of numbers in the list

