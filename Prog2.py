greeting = 'Hello'
name = 'James'

message = greeting + name
message2 = greeting + ', ' + name + '.Welcome!'

print(message)
print(message2)

message3 = '{}, {}. Welcome!'.format(greeting, name)
print(message3)

message4 = f'{greeting}, {name}. WELCOME!'
print(message4)

message5 = f'{greeting}, {name.upper()}. WELCOME!'
print(message5)

