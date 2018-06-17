name = input('Please input your name: ')
file = open('file.txt', mode='w')
file.write(name)
file.close()

file = open('file.txt', mode='r')
name = file.read()
print(name)
file.close()
