def f(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


s = int(input())

a = []

for i in range(1, 1000000):
    if i == 1:
        a.append(s)
    else:
        ai = f(a[-1])
        if ai in a:
            print(i)
            break
        else:
            a.append(ai)


def f(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


s = int(input())

a = [s]

for i in range(2, 1000001):
    ai = f(a[-1])
    if ai in a:
        print(i)
        break
    else:
        a.append(ai)


