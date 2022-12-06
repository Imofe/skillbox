count = 0
str = ''

with open('22tema/numbers.txt') as file:
    for row in file.readlines():
        str = row.strip()
        if str != '':
            count += int(str)

f = open('22tema/answer.txt', 'w')
f.write(str(count))
f.close()
