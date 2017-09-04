nums = [1,2,3,4,5,6]

for num in nums:
    print(num)


#Search a certain number is our list
for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)


for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)


for num in nums:
    for letter in 'abc':
        print(num, letter)    #if u want to print a string put it in ''   





        