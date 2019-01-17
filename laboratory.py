# input_array = input()
# array_size = input_array.split(' ')
# array = [[]*int(array_size[1])]*int(array_size[0])
# print(array)
# inputp =input()
# print(inputp)
# ax = 7
# ay =7
# array = [[2,0,0,0,1,1,0]
# ,[0,0,1,0,1,2,0]
# ,[0,1,1,0,1,0,0]
# ,[0,1,0,0,0,0,0]
# ,[0,0,0,0,0,1,1]
# ,[0,1,0,0,0,0,0]
# ,[0,1,0,0,0,0,0]]

# ax = 8
# ay = 8
# array = [[2,0,0,0,0,0,0,2]
# ,[2,0,0,0,0,0,0,2]
# ,[2,0,0,0,0,0,0,2]
# ,[2,0,0,0,0,0,0,2]
# ,[2,0,0,0,0,0,0,2]
# ,[0,0,0,0,0,0,0,0]
# ,[0,0,0,0,0,0,0,0]
# ,[0,0,0,0,0,0,0,0]]
block = []
# ax=6
# ay=4
# array = [[0,0,0,0,0,0]
# ,[1,0,0,0,0,2]
# ,[1,1,1,0,0,2]
# ,[0,0,0,0,0,2]]

a = input()
ay = int(a.split()[0])
ax = int(a.split()[1])

array = []
for i in range(int(ay)):
    c = input()
    idx = []
    for y in c.split():
        idx.append(y)
    array.append(idx)


for i in range(len(array)):
    for y in range(len(array[i])):
        location = []
        if array[i][y] == 0:
            # print(i,y,array[i][y])
            location.append(i)
            location.append(y)
            block.append(location)
#
print(len(block))
count = 0
block_list = []
# for x in range(0,len(block)):
#     for y in range(x+1,len(block)):
#         for z in range(y+1,len(block)):
#             print(block[x][0],block[x][1])
#             print(block[y][0],block[y][1])
#             print(block[z][0],block[z][1])
#
#             print(block[x],block[y],block[z])
#             print('')
# #
# print(count)



# print(array)
dx = [0,1,0,-1]
dy = [1,0,-1,0]
pre_count = 0

# ax = 6
# ay =4
# array = [[0,0,0,0,0,0]
# ,[1,0,0,0,0,2]
# ,[1,1,1,0,0,2]
# ,[0,0,0,0,0,2]]
print(array)
print('')
countt = 0
count_list = []
for a in range(0,len(block)):
    for b in range(a+1,len(block)):
        for c in range(b+1,len(block)):
            countt+=1
            # print(XXX)
            b_array = array
            # print(b_array)
            b_array[block[a][0]][block[a][1]] = 1
            b_array[block[b][0]][block[b][1]] = 1
            b_array[block[c][0]][block[c][1]] = 1
            print(XXX)
            print(b_array)
            while True :
                count = 0
                for y in range(len(b_array)):
                    # print(y)s
                    for x in range(len(b_array[y])):
                        # print(array[y][x], y,x)
                        # print('----------------------')
                        if b_array[y][x] == 2:
                            for i in range(0,4):
                                # print('i :' + str(i))

                                bx = x+dx[i]
                                by = y+dy[i]
                                # print(dy[i], dx[i])
                                # print(by,ax-1, bx,ay-1)

                                if bx >= 0 and by <= ay-1  and bx <=ax-1  and by >= 0:
                                    ppp = b_array[by][bx]
                                    # print('ppp:'+str(ppp))
                                    # print(i,i,i,i,i,i,i,i,i,i,i,i)
                                    if ppp == 0:
                                        b_array[by][bx] = 2
                for i in b_array:
                    for y in i:
                        if y == 2:
                            count +=1

                # for i in array:
                #     # print(i)

                if count == pre_count:

                    zero_count = 0
                    for i in b_array:
                        # print(i)
                        for y in i:
                            if y == 0:
                                zero_count+=1
                    # print(block[a], block[b], block[c],zero_count)
                    count_list.append(zero_count)
                    # count_list[zero_count] = str(block[a]) +',' + str(block[b])
                    # print(zero_count)
                    print(' ')
                    # count_list[block[a],block[b],block[c]] = count
                    break
                pre_count = count

count_list.sort(reverse=True)
print(countt)
print(count_list[0])


