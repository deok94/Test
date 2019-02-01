import sys
arr = []


def slope(n,l):
    road_count = 0
    for i in range(n):
        not_road = False

        for y in range(n-l):
            pass_count = 0
            if not_road :
                break
            for z in range(1,l+1):
                if y+z < n:
                    if arr[i][y] - arr[i][y+z] == 0: # 같을때
                        pass
                    elif abs(arr[i][y] - arr[i][y+z]) == 1 :# 한칸차이 날때
                        pass_count +=1
                    else:
                        not_road = True
                        break
            if pass_count !=

        if not not_road :
            print(i)
            road_count += 1
    print('')
    print(road_count)

if __name__ == '__main__':
    n, l = map(int, sys.stdin.readline().split())
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))

    slope(n,l)