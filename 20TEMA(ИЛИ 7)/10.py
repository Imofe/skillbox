def my_zip(str, num_tpl):
    return ((str[i], num_tpl[i]) for i in range(min(len(str), len(num_tpl))))

answer = my_zip("abcd", (10, 20, 30, 40))

print(answer)
print(*answer, sep='\n')
