import os
import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *


#============================  class 설정 부분  =======================================
def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('ui/label.ui')
form_class = uic.loadUiType(form)[0]

class WindowClass( QMainWindow, form_class):
    def __init__(self):
        super( ).__init__( )
        self.setupUi(self)
#==========================  Signal & Setting 부분  ===================================
        # setLineWidth / setMidLineWidth
        # setFrameShpae / setFrameShadow 여러 예시
        self.label.setLineWidth(2)
        self.label.setMidLineWidth(3)
        self.label.setFrameShape(QFrame.Box)
        self.label.setFrameShadow(QFrame.Raised)

        self.label_4.setLineWidth(1)
        self.label_4.setMidLineWidth(2)
        self.label_4.setFrameShape(QFrame.Panel)
        self.label_4.setFrameShadow(QFrame.Sunken)

        self.label_6.setLineWidth(3)
        self.label_6.setMidLineWidth(0)
        self.label_6.setFrameShape(QFrame.HLine)
        self.label_6.setFrameShadow(QFrame.Plain)

        # frameWidth 예시
        print("label - frameWidth : ",self.label.frameWidth())
        print("label_4 - frameWidth : ",self.label_4.frameWidth())
        print("label_6 - frameWidth : ",self.label_6.frameWidth())

        # setFrameRect 설정
        rect = QRect(10,10,100,100) #10,10위치에 100,100짜리 사각형 설정
        self.label_7.setLineWidth(1)
        self.label_7.setFrameShape(QFrame.Box)
        self.label_7.setFrameRect(rect)

        # setFrameStyle 예시
        print("label_6 - frameStyle : ",self.label_6.frameStyle())
        self.label_9.setFrameStyle(20) #shape, shadow만 설정

        # drawFrame 대체로 setPixmap 사용
        pixmap = QPixmap(self.label_10.size()) # label_6 크기로 QPixmap생성
        pixmap.fill(Qt.transparent) # pixmap을 투명하게 채움
        pt = QPainter(pixmap) # pixmap으로 QPainter객체 생성
        pt.setPen(QPen(Qt.red, 2, Qt.DashLine)) # 굵기2짜리 붉은 점선 지정
        pt.drawLine(0, 0, 70, 40) # 선 긋기
        pt.drawLine(70, 0, 0, 40)
        pt.setPen(QPen(Qt.black, 3)) # 굵기3짜리 검은선 지정
        pt.drawText(pixmap.rect(),Qt.AlignCenter,"라벨_6") # pixmap크기 사각형에 가운데 정렬로 글자 쓰기
        pt.end() # painter 종료
        self.label_10.setPixmap(pixmap) # label_6에 pixmap적용



#===============================  Slot 부분   =========================================

#==============================  app 실행 부분  =======================================
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass( )
    myWindow.show( )
    app.exec_( )