# Print Welcome Message
print('Hello World')

message = 'Hello Shruti\'s World'
message2 = "Hello Shruti's World"
message3 = """HELLO 'BEAUTIFUL WORLD - SHRUTI YOGESH"""

#String Length
print(len(message3))

print(message)
print(message2)
print(message3)

#String print
print(message[6])
print(message[0:7])
print(message[5:20])

# Methods 
print(message.lower())
print(message.upper())

#Method is function belongs to an Object
print(message.count('Hello'))
print(message.count('l'))

print(message.find('World'))
print(message.find('universe'))

print(message2.replace('World','Universe'))

new_message = message.replace('World','Universe')
print(message2)
print(new_message)