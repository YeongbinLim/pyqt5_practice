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

form = resource_path('main.ui')
form_class = uic.loadUiType(form)[0]

class WindowClass( QMainWindow, form_class):
    def __init__(self):
        super( ).__init__( )
        self.setupUi(self)
#==========================  Signal & Setting 부분  ============================================================

#--------------------  QStackedWidget객체 Setting 부분  ---------------------------------------------------------
    #StackedWidget 만들기
        # QStackedWidget 생성
        self.stack = QStackedWidget(self)                   # QStackedWidget 생성
        self.stack.setGeometry(0,0,200,300)                 # 위치 및 크기 지정
        self.stack.setFrameShape(QFrame.Box)                # 테두리 설정(보기 쉽게)

        # 입력할 page를 QWidget으로 생성
        self.page_1 = QWidget(self)                         # page_1 생성
        self.page_2 = QWidget(self)                         # page_2 생성

    # page에 위젯 추가하기
        # 객체가 Designer에 존재할 경우 page를 부모위젯으로 설정
        self.label_1.setParent(self.page_1)                 # page_1을 label_1의 부모위젯으로 설정
        self.label_1.setGeometry(0,0,200,40)                # 위치 및 크기 지정
        self.btn_1.setParent(self.page_1)
        self.btn_1.setGeometry(0,40,200,40)

        # 객체가 Designer에 없을경우 생성시 부모로 page를 설정
        self.label_2 = QLabel(self.page_2)                  # page_2를 부모로 label_2 생성
        self.label_2.setFrameShape(QFrame.Box)              # 테두리 설정(보기 쉽게)
        self.label_2.setText('label_2')                     # 내용은 'label_2'로
        self.label_2.setAlignment(Qt.AlignCenter)           # 가운데 정렬
        self.label_2.setGeometry(0,0,200,40)                # 위치 및 크기 지정
        self.btn_2 = QPushButton(self.page_2)               # pager_2를 부모로 btn_2 생성
        self.btn_2.setText('btn_2')                         # 내용은 'btn_2'로
        self.btn_2.setGeometry(0,40,200,40)                 # 위치 및 크기 지정

    # 내용입력이 완료된 페이지를 QStackedWidget객체에 추가
        self.stack.addWidget(self.page_1)                   # stack에 page_1 추가
        self.stack.addWidget(self.page_2)                   # stack에 page_2 추가
#--------------------------------------------------------------------------------------------------------------

        # setCurrentIndex / setCurrentWidget [페이지 전환]
        self.btn_1.clicked.connect(self.fnc_btn_1)          # btn_1 누르면 fnc_btn_1 호출
        self.btn_2.clicked.connect(self.fnc_btn_2)          # btn_2 누르면 fnc_btn_2 호출

        # insertWidget [페이지 삽입]
        self.btn_insert.clicked.connect(self.fnc_btn_insert)

        # indexOf [페이지의 인덱스값] / widget [인덱스 값인 페이지] / count [페이지수]
        self.btn_chk.clicked.connect(self.fnc_btn_chk)      # btn_chk누르면 fnc_btn_chk호출

        # removeWidget [페이지 삭제]
        self.btn_remove.clicked.connect(self.fnc_btn_remove)# btn_remove누르면 fnc_btn_remove호출

        # Signals
        # currentChanged [페이지 변경시] / widgetRemoved [페이지 삭제시]
        self.stack.currentChanged.connect(self.fnc_changed) # 페이지 변경시 fnc_changed호출
        self.stack.widgetRemoved.connect(self.fnc_removed)  # 페이지 삭제시 fnc_removed호출
#===============================  Slot 부분   ==================================================================
    def fnc_btn_1(self):
        self.stack.setCurrentIndex(1)                       # 현재 Index(페이지)를 1로

    def fnc_btn_2(self):
        self.stack.setCurrentWidget(self.page_1)            # 현재 Widget(페이지)를 page_1로

    def fnc_btn_insert(self):
        self.page_3 = QWidget(self)                         # page_3 위젯 생성
        self.label_3.setParent(self.page_3)                 # label_3의 부모를 page_3으로
        self.label_3.setGeometry(0,0,200,40)                # 위치 및 크기 지정
        self.btn_3.setParent(self.page_3)                   # btn_3의 부모를 page_3으로
        self.btn_3.setGeometry(0,40,200,40)                 # 위치 및 크기 지정
        self.stack.insertWidget(1,self.page_3)              # index 1번 위치에 page_3 삽입
        self.stack.setCurrentIndex(1)                       # index 1페이지 전환

    def fnc_btn_chk(self):
        print('page_2의 index는   :',self.stack.indexOf(self.page_2))
        print('index가 0인 page는 :',self.stack.widget(0))
        print('페이지 수는 :',self.stack.count())

    def fnc_btn_remove(self):
        self.stack.removeWidget(self.page_3)

    def fnc_changed(self):
        print("changed")
    def fnc_removed(self):
        print("removed")
#==============================  app 실행 부분  =================================================================
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass( )
    myWindow.show( )
    app.exec_( )