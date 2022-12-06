def challenge(end, start=1):
    if start <= end:
        print(start)
        challenge(end, start + 1)

challenge(int(input('Введите num: ')))
