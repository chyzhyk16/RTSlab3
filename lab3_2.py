import time


def calc2(learning_rate, maxtime, maxiter):
    iter = 0
    p = 4
    points = [[0, 6], [1, 5], [3, 3], [2, 4]]
    w1 = 0
    w2 = 0
    flag = False
    start = time.time()
    while iter < maxiter and maxtime > time.time() - start:
        y = points[iter % 4][0] * w1 + points[iter % 4][1] * w2
        delta = p - y
        w1 += delta * points[iter % 4][0] * learning_rate
        w2 += delta * points[iter % 4][1] * learning_rate
        iter += 1
        if points[0][0] * w1 + points[0][1] * w2 > p > points[2][0] * w1 + points[2][1] * w2 and points[1][0] * w1 + \
                points[1][1] * w2 > p > points[3][0] * w1 + points[3][1] * w2:
            flag = True
            return 'w1=' + str(w1)[:5] + ' w2=' + str(w2)[:5] + '\ntime=' + str(
                time.time() - start)+' num of iterations: '+str(iter)

            break
    if flag:
        return None
    else:
        return 'w1,w2 не розроховано до дедлайну'