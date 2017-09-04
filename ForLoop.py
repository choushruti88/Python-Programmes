#For loop define i variable for 1 to 10 range, have to put range from 1 to 11 as 11 is exclusive

for i in range(1, 11):
    print(i)


# While loop
x = 0

while x < 10:
    print(x)
    x += 1

#To create a finite loop and put exit after some number
x = 0 

while x < 10:
    if x == 5: 
        break
    print(x)
    x += 1

#to create an infinite loop we can replace numner condition with True
x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1


# To get out of an Infinite loop if you stuck then mostly cntrl+c will work to stop.

