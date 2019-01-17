relation = [[100,"ryan","music",2],[200,"apeach","math",2],[300,"tube","computer",3],[400,"con","computer",4],[500,"muzi","music",3],[600,"apeach","music",2]]
result = 2

dic_test = {}
# dic_test['100'] = '0'
# dic_test['100'] = '0'
# dic_test['100'] = '0'
# dic_test['100'] = '0'
# dic_test[100] = 0
rl = [[]]

for i in range(len(relation)) :

    for y in range(len(relation[i])):

        rl[y].append(relation[i][y])
print(rl)

print(dic_test.items())
# for i,y in dic_test.items():
#     print(str(i),str(y))

# for i in relation :
#     for y in i:
#         print()