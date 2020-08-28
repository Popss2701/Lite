x = 1
y = 5
step = 0


def cal(y):
    global step
    if x == y:
        print(step)
        return
    if y % 2:
        step += 1
    if (y + 1) // 2 >= x:
        step += 1
        cal((y + 1) // 2)
    else:
        step += x - (y + 1) // 2 + 1
        cal(x)


cal(y)
