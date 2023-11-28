num_list = [i for i in range(666, 3666666)]
result_list = [0]

for i in range(len(num_list)):
    if '666' in str(num_list[i]):
        result_list.append(num_list[i])

N = int(input())
print(result_list[N])
