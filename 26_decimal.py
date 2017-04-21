def aton(a):
    temp_aton = 0
    length = len(a)
    for i in range(length):
        temp_aton += (ord(a[length-i-1]) - ord('A')) * (26 ** i)
    return temp_aton


def compute(x, y, op):
    if op == '+':
        return [x + y]
    elif op == '-':
        return [x - y]
    elif op == '*':
        return [x * y]
    elif op == '/':
        return [int(x / y), x % y]

if __name__ == '__main__':

    # 入力例：DD + DD
    inp = input()
    temp = inp.split(' ')
    x, op, y = temp

    # 英字を数字に変換して計算
    x_d = aton(x)
    y_d = aton(y)
    result = compute(x_d, y_d, op)
    print('\n10\t: ' + str(x_d) + ' ' + op + ' ' + str(y_d) + ' = ' + str(result) + '\n')

    # 計算結果を26で割り続け、余りをリストに入れていく。割り切れなくなったら最後に商を入れる。
    lis = [[], []]
    for i in range(len(result)):
        result_t = result[i]
        while result_t > 25:
            lis[i].append(result_t % 26)
            result_t /= 26
            result_t = int(result_t)
        lis[i].append(result_t)

    # 26で割り続けた商と余りを数字に変換
    result_26 = ['', '']
    for i in range(2):
        if lis[i]:
            for j in range(len(lis[i])):
                result_26[i] += (chr(ord('A') + lis[i][len(lis[i]) - j - 1]))

    # 結果表示
    if op == '/':
        print('16\t: ' + x + ' ' + op + ' ' + y + ' = ' + result_26[0] + '+(' + result_26[1] + '/' + y + ')')
    else:
        print('16\t: ' + x + ' ' + op + ' ' + y + ' = ' + result_26[0])
