import sys
from PyQt5.QtWidgets import QApplication, QWidget
import random

list = []

# 학생 제외 번호
remove_list = []
#

# 주위에 있으면 안됨
no_partner = {}
no_partner[4] = 5
no_partner[7] = 8
no_partner[3] = 1

# 앉으면 안되는 자리
no_seat = []

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()

    def seat(n, m):
        # 학생 제외 번호 지우기
        for i in remove_list:
            list.remove(i)

        while True:
            arr = []

            # 자리 선정(랜덤으로)
            out = random.sample(list, len(list))
            out.reverse()

            # 자리 지정(배열로 표현)
            count = 0
            for i in range(n):
                tmp = []
                for y in range(m):
                    count += 1
                    if count not in no_seat:
                        tmp.append(out.pop())
                    else:
                        tmp.append(0)
                arr.append(tmp)

            # 해당 번호 주변으로 있으면 안되는 번호 Cheack
            b_count = 0
            for y in range(len(arr)):
                for x in range(len(arr[y])):
                    for i in range(8):
                        px = x + dx[i]
                        py = y + dy[i]
                        if px >= 0 and px < m and py >= 0 and py < n:
                            main_n = arr[y][x]
                            side_n = arr[py][px]
                            if int(main_n) in no_partner:
                                if int(no_partner[main_n]) == side_n:
                                    b_count += 1

            if b_count == 0:
                print('=============')
                return arr
            else:
                for i in arr:
                    print(i)
                print(' ')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())





