#If else condition: Statement will print only if it is true
#if True:
#   print('Conditional was True')

#if False:
#    print('Conditional was True')

language = 'Python'

if language == 'Python':
    print('Conditional was True')

# Comparisons:
# Equal:             ==
# Not Equal:         !=
# Greater Than:      >
# Less Than:         <
# Greater or Equal:  >=
# Less or Equal:     <=
# Object Identity:   is


language = 'Java'

if language == 'Python':
    print('Conditional was True')
else:
    print('No Match')     


#If Else anf elif block
language = 'JavaScript'

if language == 'Python':
    print('Conditional was True')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No Match')           # Works as switch case operators in other language



# and  #or  #not
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')


#or operation
user = 'Admin'
logged_in = False

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')



#not operation
user = 'Admin'
logged_in = True

if not logged_in:
    print('Admin Page')
else:
    print('Welcome')

