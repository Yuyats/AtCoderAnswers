def main():
    global result, S
    S = int(input())
    result = 0
    bfs(0, '')
    print(result)


def bfs(i, s):
    global result, S
    if s != '' and int(s) <= S and len(set(s)) == 3:
        result += 1
    if i == len(str(S)):
        return
    i += 1
    bfs(i, s + '3')
    bfs(i, s + '5')
    bfs(i, s + '7')


if __name__ == '__main__':
    main()
