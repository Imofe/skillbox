file = open('22tema\zen.txt', 'r')
str = file.readlines()
str.reverse()
print(''.join(str))
