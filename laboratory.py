import queue

block = []
Virus = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]

a = input()
ay = int(a.split()[0])
ax = int(a.split()[1])
array = []
sizee=ay*ax
def array_reset() :
    array2 = []
    for i in range(len(array)):
        ary2_list =[]
        for y in range(len(array[i])):
            ary2_list.append(int(array[i][y]))
        array2.append(ary2_list)
    return array2

for i in range(int(ay)):
    c = input()
    idx = []
    for y in c.split():
        idx.append(int(y))
    array.append(idx)

array2 = array
one_size = 0
for i in range(len(array2)):
    for y in range(len(array2[i])):
        b_location = []
        v_location = []
        if array2[i][y] == 0:
            b_location.append(i)
            b_location.append(y)
            block.append(b_location)
        elif array2[i][y] ==2:
            v_location.append(i)
            v_location.append(y)
            Virus.append(v_location)
        else :
            one_size+=1

answer = 0
c_map = {}

for a in range(0,len(block)):
    for b in range(a+1,len(block)):
        for c in range(b+1,len(block)):
            b_array2 = array_reset()
            q = queue.Queue()
            b_array2[block[a][0]][block[a][1]] = 1
            b_array2[block[b][0]][block[b][1]] = 1
            b_array2[block[c][0]][block[c][1]] = 1
            duplicate = []
            for d in Virus:
                q.put(d)

            while True :
                count = 0

                for y in range(q.qsize()):
                        z_count = 0
                        point = q.get()
                        # if point in duplicate:
                        #     print(point)
                        #     continue
                        # duplicate.append(point)

                        for i in range(0,4):
                            bx = point[1]+dx[i]
                            by = point[0]+dy[i]
                            if bx >= 0 and by <= ay-1  and bx <=ax-1  and by >= 0:
                                ppp = b_array2[by][bx]

                                if ppp == 0:
                                    nv_location = []
                                    nv_location.append(by)
                                    nv_location.append(bx)
                                    b_array2[by][bx] = 2
                                    q.put(nv_location)

                if q.qsize() == 0:
                    # # print(sizee -( len(duplicate) + 3 + one_size))
                    # count = sizee -( len(duplicate) + 3 + one_size)
                    for i in b_array2:
                        for y in i:
                            if y == 0:
                                count += 1

                    c_map[count] = (count)
                    break


answer = max(c_map, key=c_map.get)
print(answer)





