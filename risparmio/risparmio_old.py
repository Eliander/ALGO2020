'''

N: #luci totali (stdin)
M: #operazioni (stdin)

'''

def main():
    n, m = input('').split(' ')
    # n e m diventano interi
    int_n = int(n)
    int_m = int(m)
    list_op = []
    list_lights = []
    for i in range(0, int_m):
        list_op.append(input(''))
    for i in range(0, int_n + 1):
        list_lights.append(False)
    for op in list_op:
        list_lights = execute(op, list_lights)

def execute(op, list_lights):
    list_op = op.split(' ')
    if list_op[0] == "1":
        # inverti il valore nell'index
        list_lights[int(list_op[1])] = not list_lights[int(list_op[1])]
    else:
        # sequenze massime
        int_start = int(list_op[1])
        int_end = int(list_op[2])
        light = False
        count = 0
        for i in range(int_start, int_end + 1):
            if list_lights[i] and not light:
                count += 1
                light = True
            elif not list_lights[i]:
                light = False
        print(count)
    return list_lights


if __name__ == "__main__":
    main()