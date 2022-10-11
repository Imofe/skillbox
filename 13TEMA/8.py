precision = float(input('Введите точность: '))
x = float(input('Введите число: '))

def row_summ(x, precision):
	summ = 1
	factorial = 1
	result = 1
	while abs(summ) > precision:
		summ *= (-1 * (x ** 2)) / (factorial * (factorial + 1))
		factorial += 2
		result +=summ
	print(f'Сумма ряда = {result}' )

row_summ(x, precision)