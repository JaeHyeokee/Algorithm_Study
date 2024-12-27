for i in range(int(input())):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    turn = 0
    while True:
        skip = False
        for j in range(1, len(queue)):
            if queue[0] < queue[j]:
                queue.append(queue.pop(0))
                if M == 0: M = len(queue) - 1
                else: M -= 1
                skip = True
                break
        if skip == False:
            queue.pop(0)
            turn += 1
            if M == 0: break
            M -= 1
    print(turn)