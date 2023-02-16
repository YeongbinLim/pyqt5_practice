import os
import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *


# ============================  class 설정 부분  ================================================================
def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


form = resource_path('main.ui')
form_class = uic.loadUiType(form)[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # ==========================  Signal & Setting 부분  ============================================================
        # 각 버튼의 시그널-슬롯 연결
        # addSubWindow [위젯(창) 추가] / removeSubWindow [위젯(창) 제거]
        self.btn_add.clicked.connect(self.fnc_btn_add)  # 창과 위젯 추가
        self.btn_remove.clicked.connect(self.fnc_btn_remove)  # 창의 위젯 삭제 (창 삭제 아님)

        # cascadeSubWindows [계단식 정렬] / tileSubWindows [바둑판식 정렬]
        self.btn_cascade.clicked.connect(self.fnc_btn_cascade)  # 계단식 정렬
        self.btn_tile.clicked.connect(self.fnc_btn_tile)  # 바둑판식 정렬

        # currentSubWindow [현재 창] / setActiveSubWindow [창 활성화]
        # activatePreviousSubWindow [이전창] / activateNextSubWindow [다음창]
        self.btn_current.clicked.connect(self.fnc_btn_current)  # 현재 창(위젯)
        self.btn_pre.clicked.connect(self.fnc_btn_pre)  # 이전 창(위젯)
        self.btn_next.clicked.connect(self.fnc_btn_next)  # 다음 창(위젯)
        self.btn_active.clicked.connect(self.fnc_btn_active)  # 특정 창 활성화

        # setViewMode [창/탭모드] / setTabPosition [탭 위치]
        # setTabShape [탭 모양] / setTabsClosable [탭 닫기버튼] / setTabsMovable [탭 이동가능여부]
        self.btn_mode.clicked.connect(self.fnc_btn_mode)  # 창보기-탭보기 모드 설정
        self.btn_pos.clicked.connect(self.fnc_btn_pos)  # 탭 위치
        self.btn_shape.clicked.connect(self.fnc_btn_shape)  # 탭 모양
        self.btn_closable.clicked.connect(self.fnc_btn_closable)  # 탭 닫기 가능 여부
        self.btn_move.clicked.connect(self.fnc_btn_move)  # 탭 이동 여부

        # closeActiveSubWindow [현재창 닫기] / closeAllSubWindows [모든창 닫기]
        self.btn_close.clicked.connect(self.fnc_btn_close)  # 창 닫기
        self.btn_closeA.clicked.connect(self.fnc_btn_closeA)  # 모든창 닫기

        # setBackground [배경색 설정]
        self.mdi.setBackground(QBrush(QColor("black")))

        # 위젯을 mdi 하위창으로 추가
        subwindow_1 = QMdiSubWindow()
        subwindow_1.setWidget(self.tool_1)
        self.mdi.addSubWindow(subwindow_1)

        subwindow_2 = QMdiSubWindow()
        subwindow_2.setWidget(self.tool_2)
        self.mdi.addSubWindow(subwindow_2)

        subwindow_3 = QMdiSubWindow()
        subwindow_3.setWidget(self.tool_3)
        self.mdi.addSubWindow(subwindow_3)

    # ===============================  Slot 부분   ==================================================================
    # ----- 창 추가 및 제거 -------------------------------------------------
    def fnc_btn_add(self):
        self.mdi.addSubWindow(self.tool_4)  # tool_4를 서브윈도우로 설정
        self.tool_4.show()  # tool_4 보기

    def fnc_btn_remove(self):
        self.mdi.removeSubWindow(self.tool_4)  # tool_4 제거

    # ----- 창 정렬 --------------------------------------------------------
    def fnc_btn_cascade(self):
        self.mdi.cascadeSubWindows()  # 계단식으로 정렬

    def fnc_btn_tile(self):
        self.mdi.tileSubWindows()  # 바둑판식으로 정렬

    # ----- 창 확인 및 활성화 -----------------------------------------------
    def fnc_btn_current(self):
        # 현재 활성창의 위젯의 위젯명 출력
        print(self.mdi.currentSubWindow().widget().objectName())

    def fnc_btn_pre(self):
        self.mdi.activatePreviousSubWindow()        # 이전 창 활성화

    def fnc_btn_next(self):
        self.mdi.activateNextSubWindow()            # 다음 창 활성화

    def fnc_btn_active(self):
        mdi_list = self.mdi.subWindowList()         # 현재 창 리스트
        print(mdi_list)                             # 출력
        self.mdi.setActiveSubWindow(mdi_list[1])    # 1번(2번째) 창 활성화

    # ----- 탭 모드 설정 ----------------------------------------------
    def fnc_btn_mode(self):                             # 모드 0 <-> 1 변경
        if self.mdi.viewMode() == 0:                    # 현재 모드가 창모드(0) 이면
            self.mdi.setViewMode(1)                     # 탭모드(1)로 변경
        else:
            self.mdi.setViewMode(0)                     # 아니면 창모드(0)로 변경
        print("ViewMode :", self.mdi.viewMode())        # 현재 모드상태 출력

    def fnc_btn_pos(self):                              # 누를때 마다 position 변경 
        x = self.mdi.tabPosition()                      # x에 현재 tabPositions값 입력
        if x < 3:                                       # x가 3보다 작으면(position이 0,1,2,3이므로)
            self.mdi.setTabPosition(x + 1)              # x+1 포지션으로 변경
        else:
            self.mdi.setTabPosition(0)                  # 3보다 크면 다시 0으로
        print("TabPosition :", self.mdi.tabPosition())  # 현재 position값 출력

    def fnc_btn_shape(self):                            # 탭 모양 0 <-> 1 변경
        if self.mdi.tabShape() == 0:                    # 탭 모양이 네모(0)이면
            self.mdi.setTabShape(1)                     # 탭 모양 세모(1)로 변경
        else:
            self.mdi.setTabShape(0)                     # 아니면 네모(0)으로 변경
        print("TabShape :", self.mdi.tabShape())        # 현재 탭 모양 출력

    def fnc_btn_closable(self):                         # 탭 닫기 버튼 설정 
        if self.mdi.tabsClosable() == False:            # tabclose가 불가 상태면
            self.mdi.setTabsClosable(True)              # 가능하도록 변경
        else:                                   
            self.mdi.setTabsClosable(False)             # 가능상태면 불가능하도록 변경
        print("TabsClosable :", self.mdi.tabsClosable())# 현재 탭 닫기가능 여부 출력

    def fnc_btn_move(self):                             # 탭 이동 가능여부 변경
        if self.mdi.tabsMovable() == False:             # 탭이 이동불가 상태면
            self.mdi.setTabsMovable(True)               # 탭 이동 가능으로 변경
        else:                                       
            self.mdi.setTabsMovable(False)              # 탭 이동 가능 상태면 불가로 변경
        print("TabsMovable :", self.mdi.tabsMovable())  # 탭 이동 가능여부 출력

    # ----- 창 닫기 ----------------------------------------------------
    def fnc_btn_close(self):                    
        self.mdi.closeActiveSubWindow()                 # 활성상태의 창 닫기

    def fnc_btn_closeA(self):
        self.mdi.closeAllSubWindows()                   # 전체 창 닫기


# ==============================  app 실행 부분  =================================================================
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()