import os
import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#==============================  Model 설정 부분  ===============================================================
class Model(QStandardItemModel):
    def __init__(self):
        QStandardItemModel.__init__(self)
        self.setHorizontalHeaderLabels(['col1','col2','col3','col4'])
        data = [
            {"type": "Name", "objects": ['A','B','C','D','E','F','G','H','I','J']},
            {"type": "Age", "objects": ['1','2','3','4','5','6','7','8','9','10']},]
        d = data[0]
        item = QStandardItem(d["type"])
        for i in range(len(d["objects"])):
            child = QStandardItem(d["objects"][i])
            item.appendRow(child)
        self.setItem(0, 0, item)

        d = data[1]
        item = QStandardItem(d["type"])
        for i in range(len(d["objects"])):
            child = QStandardItem(d["objects"][i])
            item.appendRow(child)
        self.setItem(1, 0, item)
#============================  class 설정 부분  ================================================================
def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('ui/QAbstractScrollArea.ui')
form_class = uic.loadUiType(form)[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super( ).__init__( )
        self.setupUi(self)
#==========================  Signal & Setting 부분  ============================================================
        # setVerticalScrollBarPolicy / setHorizontalScrollBarPolicy [스크롤 표시정책]
        self.table_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    # ↓
            # Qt.ScrollBarAsNeeded : 컨텐츠가 뷰포트보다 클때 스크롤바 생성(기본)
            # Qt.ScrollBarAlwaysOff : 스크롤바 항상 표시안함
            # Qt.ScrollBarAlwaysOn : 스크롤바 항상 표시

        # addScrollBarWidget [스크롤바에 위젯 추가] / setCornerWidget [코너에 위젯추가]
        self.btn_1 = QPushButton()
        self.btn_1.setText('btn_1')
        self.table_3.addScrollBarWidget(self.btn_1,Qt.AlignLeft)
        self.btn_2 = QPushButton()
        self.btn_2.setText('2')
        self.table_3.setCornerWidget(self.btn_2)

        # setVerticalScrollBar / setHorizontalScrollBa [스크롤바 적용]
        self.scroll_bar=QScrollBar(self)
        self.scroll_bar.setStyleSheet("background : black;")
        self.table_4.setVerticalScrollBar(self.scroll_bar)

        # maximumViewportSize [최대 뷰포트 크기 반환]
        print(self.table_4.maximumViewportSize())

        # setSizeAdjustPolicy [사이즈 조정 정책]
        self.table_5.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_5.resizeColumnsToContents()
            # QAbstractScrollArea.AdjustIgnored : 스크롤 영역 조정하지 않음
            # QAbstractScrollArea.AdjustToContent : 스크롤 영역을 내용물 기준 조정
            # QAbstractScrollArea.AdjustToContentsOnFirstShow : 처음에만 내용물 기준 조정

        # 비교용 원래 모습
        self.tree_6.setModel(Model())

        # setViewport [뷰포트에 위젯 삽입]
        self.scrollarea_1 = QAbstractScrollArea(self)
        self.scrollarea_1.setGeometry(self.tree_7.x(),self.tree_7.y(),self.tree_7.width(),self.tree_7.height())
        print(self.tree_7.height())
        print(self.tree_7.size())
        print(self.tree_7.width())
        self.scrollarea_1.setFrameShape(QFrame.Box)
        self.scrollarea_1.setorientation('Vertical')
        self.scrollarea_1.setViewport(self.tree_7)
        self.tree_7.setModel(Model())

        # setViewportMargins [뷰포트 여백]
        self.scrollarea_2 = QAbstractScrollArea(self)
        self.scrollarea_2.setGeometry(self.tree_8.x(),self.tree_8.y(),self.tree_8.width(),self.tree_8.height())
        self.scrollarea_2.setFrameShape(QFrame.Box)
        self.scrollarea_2.setViewportMargins(30, 0, 0, 0)
        self.tree_8.setParent(self.scrollarea_2.viewport())
        self.tree_8.setGeometry(0,0,217,174)
        self.tree_8.setModel(Model())

        # scrollContentsBy [뷰포트 내용 스크롤] / viewportSizeHint [권장 뷰포트 크기]
        self.tree_9.setModel(Model())
        self.btn_9.clicked.connect(self.fnc_btn_9)

#===============================  Slot 부분   ==================================================================
    def fnc_btn_9(self):
        self.tree_9.scrollContentsBy(100, 0)
        print(self.tree_9.viewportSizeHint())
#==============================  app 실행 부분  =================================================================
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass( )
    myWindow.show( )
    app.exec_( )