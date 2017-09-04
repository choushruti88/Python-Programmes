# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence.For example, '', {}, [].
# Any empty mapping. For example, {}.

condition =  None

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')



condition = 10
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')



condition = {}          #Empty dictionary will lead to false
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')



condition = 'Test'          #Empty dictionary will lead to false
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')