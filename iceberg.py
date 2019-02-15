import sys
n = 0
m = 0
arr = []
iceberg = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]

year = 0
def Melt() :

    while True :
        years = {}
        for z in iceberg:
            p_x = z[0]
            p_y = z[1]
            ice = arr[p_x][p_y]
            for j in range(4):
                x = p_x + dx[j]
                y = p_y + dy[j]
                if x >=0 and x < n and y >=0 and y < m:
                    if arr[x][y] == 0 and ice > 0:
                        ice -= 1
            #녹는 맵 생성
            years[p_x,p_y] = ice

        ices = []
        for i in years:
            x = i[0]
            y = i[1]
            if years[i] != 0:
                ices.append([x,y])
            arr[x][y] = years[i]

        if len(ices) == 0:
            print(0)
            quit()
        for i in arr:
            print(i)
        print()

        bfs(ices)


def bfs(ices):
    global year
    year +=1
    queue = [ices[0]]
    check = []

    while queue :
        q = queue.pop(0)
        if q not in check:
            check.append(q)
            for i in range(4):
                x = q[0] + dx[i]
                y = q[1] + dy[i]
                if x >= 0 and x < n and y >= 0 and y < m:
                    #  체크 되지않은 queue 쌓기
                    if arr[x][y] != 0 and [x,y] not in check :
                        queue.append([x,y])

    if len(ices) != len(check) :
        print(year)
        quit()


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))

    for x in range(len(arr)) :
        for y in range(len(arr[x])):
            if arr[x][y] != 0:
                iceberg.append([x,y])
    Melt()


