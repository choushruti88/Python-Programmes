a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   #  equal == will compare values from both variables a and b.

print(a is b)   # if we write a is b then it will return false



a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))
print(id(a) == id(b))
print(a is b)  # will return false as if for both variables will be different



a = [1, 2, 3]
b = a

print(id(a))
print(id(b))
print(id(a) == id(b))
print (a is b) 
print (a == b) # will return True because if for both variables will be same now




