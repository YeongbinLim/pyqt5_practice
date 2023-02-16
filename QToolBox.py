import os
import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *


#============================  class 설정 부분  ========================================
def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('ui/QToolBox.ui')
form_class = uic.loadUiType(form)[0]

class WindowClass( QMainWindow, form_class):
    def __init__(self):
        super( ).__init__( )
        self.setupUi(self)
#==========================  Signal & Setting 부분  ============================================================
    #--------------------  QToolBox 생성 Settin 부분  -----------------------------------------------------------
        # QToolbox 객체 생성부
        self.toolbox = QToolBox(self)                   # QToolBox 생성
        self.toolbox.setGeometry(0,0,200,200)           # 위치 및 크기 지정
        self.toolbox.setFrameShape(QFrame.Box)          # 테두리 설정 (보기 쉽도록)

        # 페이지 생성부 [Designer에 객체가 있을때]
        self.page_1 = QWidget(self)                     # QWidget으로 page_1 생성
        self.label_1.setParent(self.page_1)             # label_1의 부모를 page_1로
        self.label_1.setGeometry(0,0,200,40)            # 위치 및 크기 지정
        self.btn_1.setParent(self.page_1)               # btn_1의 부모를 btn_1로
        self.btn_1.setGeometry(0,40,200,40)             # 위치 및 크기 지정

        # 페이지 생성부 [Designer에 객체가 없을때]
        self.page_2  = QWidget(self)                    # QWidget으로 page_2 생성
        self.label_2 = QLabel(self.page_2)              # page_2를 부모로 label_2 생성
        self.label_2.setGeometry(0,0,200,40)            # 위치 및 크기 지정
        self.label_2.setFrameShape(QFrame.Box)          # 테두리 설정
        self.label_2.setText("label_2")                 # 텍스트 설정
        self.label_2.setAlignment(Qt.AlignCenter)       # 가운데 정렬
        self.btn_2 = QPushButton(self.page_2)           # page_2를 부모로 btn_2 생성
        self.btn_2.setGeometry(0,40,200,40)             # 위치 및 크기 지정
        self.btn_2.setText("btn_2")                     # 텍스트 설정

        # 아이콘 설정부
        icon_red    = QIcon("test.png")              # 아이콘 설정
        icon_blue   = QIcon("test.png")             # 아이콘 설정

        # 페이지를 QToolBox 객체에 추가
        self.toolbox.addItem(self.page_1, icon_red,  'page_1')
        self.toolbox.addItem(self.page_2, icon_blue, 'page_2')
    #----------------------------------------------------------------------------------------------------------
        # setCurrentIndex (int) / setCurrentWidget (QWidget) [페이지 전환]
        self.btn_1.clicked.connect(self.fnc_btn_1)
        self.btn_2.clicked.connect(self.fnc_btn_2)

        # Signal : currentChanged [페이지 전환시 시그널 발생]
        self.toolbox.currentChanged.connect(self.fnc_changed)

        # widget [위젯의 인덱스] / indexOf [인덱스의 위젯] / count [페이지수]
        self.btn_chk.clicked.connect(self.fnc_btn_chk)

        # setItemEnabled [활성화 / 비활성화]
        self.btn_enable.clicked.connect(self.fnc_btn_enable)

        # insertItem [페이지 삽입] / setItemIcon [아이콘 설정]
        # setItemText [텍스트 설정] / setItemToolTip [툴팁 설정]
        self.btn_insert.clicked.connect(self.fnc_btn_insert)

        # removeItem [페이지 삭제]
        self.btn_remove.clicked.connect(self.fnc_btn_remove)


#===============================  Slot 부분   ==================================================================
    def fnc_btn_1(self):
        self.toolbox.setCurrentIndex(1)                 # Index 1번 페이지를 현재 페이지로
    def fnc_btn_2(self):
        self.toolbox.setCurrentWidget(self.page_1)      # page_1 페이지를 현재 페이지로

    def fnc_changed(self):
        print('changed')                                # 페이지가 바뀔경우 changed 출력

    def fnc_btn_chk(self):
        print("인덱스1번에 해당하는 위젯 :", self.toolbox.widget(1))
        print("page_1위젯의 해당하는 인덱스 :",self.toolbox.indexOf(self.page_1))
        print("페이지 수 :", self.toolbox.count())

    def fnc_btn_enable(self):
        if self.toolbox.isItemEnabled(1)==True:         # index 1페이지가 Enable 상태면
            self.toolbox.setItemEnabled(1, False)       # Disable 처리함
        else :                                          # index 1페이지가 Disable 상태면
            self.toolbox.setItemEnabled(1, True)        # Enable 처리함

    def fnc_btn_insert(self):
        self.page_3 = QWidget(self)                     # page_3을 QWidget으로 생성
        self.label_3.setParent(self.page_3)             # label_3의 부모를 page_3으로
        self.label_3.setGeometry(0,0,200,40)            # 위치 및 크기 설정
        self.btn_3.setParent(self.page_3)               # btn_3의 부모를 page_3으로
        self.btn_3.setGeometry(0,40,200,40)             # 위치 및 크기 설정
        self.toolbox.insertItem(1,self.page_3,"text")   # page_3을 index1번 위치에 추가
        icon_green = QIcon("test.png")             # 아이콘 생성
        self.toolbox.setItemIcon(1,icon_green)          # index 1번 페이지에 아이콘 설정
        self.toolbox.setItemText(1,"pa&ge_3")           # inedx 1번 텍스트를 Alt+G로 Page_3설정
        self.toolbox.setItemToolTip(1,"tool tip")       # index 1번 툴팁에 "tool tip" 설정

    def fnc_btn_remove(self):
        self.toolbox.removeItem(1)                      # index 1번 페이지 삭제

#==============================  app 실행 부분  =================================================================
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass( )
    myWindow.show( )
    app.exec_( )