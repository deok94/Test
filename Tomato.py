import sys
import queue
q = queue.Queue()
arr = []
ripe = []
unripe = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0

def rrripe() :
    global count
    while True :
        day_list = []
        for w in range(q.qsize()):
            rip = q.get()
            for z in range(4):
                r_y = rip[0] + dx[z]
                r_x = rip[1] + dy[z]
                if r_x >= 0 and r_x < n and r_y >= 0 and r_y < m:
                    if arr[r_y][r_x] == 0 :
                        arr[r_y][r_x] = 1
                        day_list.append([r_y,r_x])

            if q.qsize() == 0:
                count+=1
                for e in day_list:
                    q.put([e[0],e[1]])
                break

        if q.qsize() == 0:
            break

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0 :
                print(-1)
                quit()

    print(count-1)

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    for i in range(m):
        arr.append(list(map(int, sys.stdin.readline().split())))
    block = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                q.put([i, j])
            elif arr[i][j] == -1 :
                block +=1

    if q.qsize() + block == n*m :
        print(0)
        quit()
    else :
        rrripe()

