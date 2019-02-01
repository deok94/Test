import sys
import copy
n = 0
m = 0
arr = []
iceberg = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]
years = {}

def Melt() :
    for i in range(2):



        for i in iceberg:
            p_x = i[0]
            p_y = i[1]
            ice = arr[p_x][p_y]
            for j in range(4):
                x = p_x + dx[j]
                y = p_y + dy[j]
                if x >=0 and x < n and y >=0 and y < m:
                    if arr[x][y] == 0 :
                        if ice != 0:
                            ice -= 1
            years[p_x,p_y] = ice


        judg = []
        for i in years:
            if years[i] != 0:
                judg.append([i[0],i[1]])
            arr[i[0]][i[1]] = years[i]
        arr2 = arr.copy()
        dfs(judg)

        for i in arr:
            print(i)
        print()

def dfs(judg):
    count = 0
    print(judg)
    print()


    for i in judg:
        if len(judg) == 0:
            break
        x = i[0]
        y = i[1]
        for j in range(4):
            xx = x + dx[j]
            yy = y + dy[j]

            if arr[xx][yy] != 0 :
                judg.remove([x,y])

                dfs(judg)















if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))

    for i in range(len(arr)) :
        for y in range(len(arr[i])):
            if arr[i][y] != 0:
                iceberg.append([i,y])
    for i in arr:
        print(i)
    print()
    Melt()


