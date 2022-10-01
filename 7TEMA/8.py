for i in range(10,100):
    temp = i
    summ = 1
    while i > 0:
        last = i % 10
        summ *= last
        i //= 10
    summ *= 3
    
    if temp == summ:
        print(f'Число {temp} подходит')