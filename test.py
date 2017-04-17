def aton(a):
    temp_aton = 0
    length = len(a)
    for j in range(length):
        temp_aton += (ord(a[length-j-1]) - ord('A')) * (26 ** j)
    return temp_aton


def compute(x, y, op):
    if op == '+':
        return x + y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y
    elif op == '-':
        return x - y

if __name__ == '__main__':
    inp = input()
    temp = inp.split(' ')

    x, op, y = temp

    x_d = aton(x)
    y_d = aton(y)
    result = compute(x_d, y_d, op)
    print(str(x_d) + op + str(y_d) + ' = ' + str(result))

    lis = []
    while result > 25:
        lis.append(result % 26)
        result /= 26
        result = int(result)
        print(result)
    lis.append(result)

    result_16 = ''
    for i in range(len(lis)):
        result_16 += (chr(ord('A') + lis[len(lis) - i - 1]))
    print(result_16)
