import os
import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from time import sleep


#============================  class 설정 부분  ================================================================
def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('ui/QPlainTextEdit.ui')
form_class = uic.loadUiType(form)[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super( ).__init__( )
        self.setupUi(self)
#==========================  Signal & Setting 부분  ============================================================
        #[1] 복사 / 붙여넣기 / 잘라내기 / 취소 / 복구 / 전체선택 / 확대 / 축소 / 전체삭제 / 워터마크]
        # [copy / paste / cut / undo / redo / selectAll / zoomIn / zoomOut / clear/ setPlaceholderText]
        self.btn_copy.      clicked.connect(self.fnc_btn_copy)
        self.btn_cut.       clicked.connect(self.fnc_btn_cut)
        self.btn_paste.     clicked.connect(self.fnc_btn_paste)
        self.btn_undo.      clicked.connect(self.fnc_btn_undo)
        self.btn_redo.      clicked.connect(self.fnc_btn_redo)
        self.btn_all.       clicked.connect(self.fnc_btn_all)
        self.btn_zoomIn.    clicked.connect(self.fnc_btn_zoomIn)
        self.btn_zoomOut.   clicked.connect(self.fnc_btn_zoomOut)
        self.btn_clear.     clicked.connect(self.fnc_btn_clear)
        self.plain_1.setPlaceholderText("Place holder") # plain_1에 텍스트 없을때 워터마크 설정

        #[2] 붙여넣기 가능 확인 / 처음 보이는 줄 / 줄의 수 / 원점좌표 / 읽기 전용 / 텍스트 추가
        # / 텍스트 삽입 / 텍스트 변경 / 상호작용
        # [canPaste / firstVisibleBlock / blockCount / offset / setReadOnly / appendPlainText
        # / appendHtml /insert / setPlainText / setTextInteractionFlags]
        self.btn_canPaste.      clicked.connect(self.fnc_btn_canPaste)
        self.btn_firstVisible.  clicked.connect(self.fnc_btn_firstVisible)
        self.btn_blockCount.    clicked.connect(self.fnc_btn_blockCount)
        self.btn_offset.        clicked.connect(self.fnc_btn_offset)
        self.btn_readOnly.      clicked.connect(self.fnc_btn_readOnly)
        self.btn_append.        clicked.connect(self.fnc_btn_append)
        self.btn_insert.        clicked.connect(self.fnc_btn_insert)
        self.btn_plainText.     clicked.connect(self.fnc_btn_plainText)
        self.btn_flags.         clicked.connect(self.fnc_btn_flags)

        #[3]최대 줄수 / 커서 너비 / 덮어쓰기모드 / 탭 이동거리
        # [ setMaximumBlockCount / setCursorWidth / setOverwriteMode / setTabStopDistance ]
        self.plain_3.setMaximumBlockCount(8)        # 최대 줄 수
        self.plain_3.setCursorWidth(10)             # 커서 너비
        self.plain_3.setOverwriteMode(True)         # 덮어쓰기 모드 (insert키와 동일한 역할)
        # self.plain_3.setTabStopDistance(30)         # 탭 이동거리
        # 커서가 포함된 직사각형 / 좌표의 커서객체 반환 / 커서 조작 / 탭 역할 변경
        # [ cursorRect / cursorForPosition / moveCursor / setTabChangesFocus ]
        self.btn_cursorRect.    clicked.connect(self.fnc_btn_cursorRect)
        self.btn_move.          clicked.connect(self.fnc_btn_move)
        self.btn_tabFocus.      clicked.connect(self.fnc_btn_tabFocus)

        #[4] 자동 줄바꿈 / 배경표시 / 취소&복구 여부 / 스크롤 수직중앙
        # [ setLineWrapMode / setBackgroundVisible / setUndoRedoEnable / setCentralOnScroll ]
        self.plain_4.setLineWrapMode(QPlainTextEdit.NoWrap) # 자동 줄바꿈 하지 않음
        self.plain_4.setBackgroundVisible(True)             # 배경 표시
        self.plain_4.setUndoRedoEnabled(False)              # 취소&복구 여부
        self.plain_4.setCenterOnScroll(True)                # 줄 추가할때 커서가 항상 수직중앙에 위치하도록함
        # 특정 영역 설정 / 기본 메뉴 팝업 / 문자 찾기
        # [ExtraSelection / createStandardContextMenu / find]
        self.btn_extra.     clicked.connect(self.fnc_btn_extra)
        self.btn_menu.      clicked.connect(self.fnc_btn_menu)
        self.btn_find.      clicked.connect(self.fnc_btn_find)


        #[5] 줄 바꿈 모드 / 커서가 보이도록 수직 이동 / 커서가 보이도록 수직-수평 이동 / Doc객체 적용
        # 현재 선택 영역을 QMimeData 객체로 / QMimeData 객체를 입력 / QMimeData 객체가 입력 가능상태인지.
        # [setLineWrapMode / centerCursor / ensureCursorVisible / setDocument / setDocumentTitle
        # createMimeDataFromSelection / insertFromMimeData / canInsertFromMimeData
        self.plain_5.setLineWrapMode(QPlainTextEdit.NoWrap) # 자동 줄바꿈 해제
        self.btn_center.        clicked.connect(self.fnc_btn_center)
        self.btn_ensure.        clicked.connect(self.fnc_btn_ensure)
        self.btn_doc.           clicked.connect(self.fnc_btn_doc)
        self.btn_mime.          clicked.connect(self.fnc_btn_mime)

        # [6] 블록의 Geometry / 블록의 Rect / 커서이동 / 포맷 적용 / 현재 포맷에 새 포맷 추가
        # [blockBoundingGeometry / blockBoundingRect / setTextCursor / setCurrentCharFormat / mergeCurrentCharFormat
        self.btn_block.         clicked.connect(self.fnc_btn_block)
        self.btn_cursor.        clicked.connect(self.fnc_btn_cursor)
        self.btn_cursor.setText('&btn_cursor')  # 단축키 Alt+B 지정
        self.btn_format.        clicked.connect(self.fnc_btn_format)
        self.btn_merge.         clicked.connect(self.fnc_btn_merge)

        # [Signal]
        self.plain_1.undoAvailable.connect(self.fnc_undoAvailable)
        self.plain_1.redoAvailable.connect(self.fnc_redoAvailable)
        self.plain_2.copyAvailable.connect(self.fnc_copyAvailable)
        self.plain_3.blockCountChanged.connect(self.fnc_blockCountChanged)
        self.plain_3.modificationChanged.connect(self.fnc_modificationChanged)
        self.plain_4.cursorPositionChanged.connect(self.fnc_cursorPositionChanged)
        self.plain_5.textChanged.connect(self.fnc_textChanged)
        self.plain_6.selectionChanged.connect(self.fnc_selectionChanged)



#===============================  Slot 부분   ==================================================================
    #[1] 복사 / 붙여넣기 / 잘라내기 / 취소 / 복구 / 전체선택 / 확대 / 축소 / 전체삭제 / 워터마크]
    # [copy / paste / cut / undo / redo / selectAll / zoomIn / zoomOut / clearAll / setPlaceholderText]
    def fnc_btn_copy(self)      : self.plain_1.copy()
    def fnc_btn_cut(self)       : self.plain_1.cut()
    def fnc_btn_paste(self)     : self.plain_1.paste()
    def fnc_btn_undo(self)      : self.plain_1.undo()
    def fnc_btn_redo(self)      : self.plain_1.redo()
    def fnc_btn_all(self)       : self.plain_1.selectAll()
    def fnc_btn_zoomIn(self)    : self.plain_1.zoomIn(1)
    def fnc_btn_zoomOut(self)   : self.plain_1.zoomOut(1)
    def fnc_btn_clear(self)     : self.plain_1.clear()

    #[2] 붙여넣기 가능 확인 / 처음 보이는 줄 / 줄의 수 / 원점좌표 / 읽기 전용 / 텍스트 추가
    # / 텍스트 삽입 / 텍스트 변경 / 상호작용
    # [canPaste / firstVisibleBlock / blockCount / offset  / setReadOnly / appendPlainText
    # / appendHtml /insert/ setPlainText / setTextInteractionFlags]
    def fnc_btn_canPaste(self)      : print(self.plain_2.canPaste())
    def fnc_btn_firstVisible(self)  : print(self.plain_2.firstVisibleBlock().text())
    def fnc_btn_blockCount(self)    : print(self.plain_2.blockCount())
    def fnc_btn_offset(self)        : print(self.plain_2.contentOffset())       # 맨윗줄 좌표
    def fnc_btn_readOnly(self)      : self.plain_2.setReadOnly(True)
    def fnc_btn_append(self)        :
        self.plain_2.appendPlainText("Text")                # 텍스트 추가
        self.plain_2.appendHtml("<strong>Text<\strong>")    # html형식으로 텍스트 추가
    def fnc_btn_insert(self)        : self.plain_2.insertPlainText("[Text]")    # 커서 위치에 텍스트 삽입
    def fnc_btn_plainText(self)     : self.plain_2.setPlainText("setPlainText") # 텍스트 적용 
    def fnc_btn_flags(self)         :
        flags = self.plain_2.textInteractionFlags()     # plain_2의 현재 플래그 가져와서
        self.plain_2.setTextInteractionFlags(flags|Qt.TextSelectableByKeyboard) #키보드 입력 가능으로 변경


    #[3] 커서가 포함된 직사각형 / 좌표의 커서객체 반환 / 커서 조작 / 탭 역할 변경
    # [ cursorRect / cursorForPosition / moveCursor / setTabChangesFocus ]
    def fnc_btn_cursorRect(self):
        print("current cursor :",self.plain_3.cursorRect())     # 현재 커서가 포함된 Rect 출력
        cursor = self.plain_3.cursorForPosition(QPoint(10, 10)) # 10,10위치를 커서 객체로 지정
        print(cursor)
        print(self.plain_3.cursorRect(cursor))
    def fnc_btn_move(self):
        # KeepAnchor 상태(Shift누른 상태) 에서 커서를 아래로 이동
        self.plain_3.moveCursor(QTextCursor.Down, QTextCursor.KeepAnchor)   
    def fnc_btn_tabFocus(self): self.plain_3.setTabChangesFocus(True) # 탭 역할을 위젯 이동역할로 변경

    #[4] 특정 영역 설정 / 기본 메뉴 팝업 / 문자 찾기
    # [setExtraSelections / createStandardContextMenu / find]
    def fnc_btn_extra(self):
        selection = QTextEdit.ExtraSelection()                  # ExtraSelection 객체 생성
        color = QColor(Qt.yellow).lighter()                     # 색 지정(밝은노랑)
        selection.format.setBackground(color)                   # Extra객체에 배경색 지정
        selection.cursor = self.plain_4.textCursor()            # plain_4의 커서를 Extra객체의커서에 지정
        self.plain_4.setExtraSelections([selection])            # Extra 객체 적용
    def fnc_btn_menu(self):
        menu = self.plain_4.createStandardContextMenu()         # menu에 plain_4의 기본 메뉴 QMenu객체 부여
        menu.exec_()                                            # 메뉴 실행
    def fnc_btn_find(self):print(self.plain_4.find("AB"))       # plain_4에 "AB"가 있으면 True 반환

    # [5] 줄 바꿈 모드 / 커서가 보이도록 수직 이동 / 커서가 보이도록 수직-수평 이동 / Doc객체 적용
    # 현재 선택 영역을 QMimeData 객체로 / QMimeData 객체를 입력 / QMimeData 객체가 입력 가능상태인지.
    # [setLineWrapMode / centerCursor / ensureCursorVisible / setDocument / setDocumentTitle
    # createMimeDataFromSelection / insertFromMimeData / canInsertFromMimeData
    def fnc_btn_center(self):self.plain_5.centerCursor()        # 수직에 대해서만 커서이동
    def fnc_btn_ensure(self):self.plain_5.ensureCursorVisible() # 커서위치로 이동
    def fnc_btn_doc(self):
        doc = QTextDocument()                                   # QTextDocument 객체 생성
        doc.setPlainText('line1\nline2\nline3')                 # doc에 텍스트 입력
        doc.setDocumentLayout(QPlainTextDocumentLayout(doc))    # doc의 레이아웃을 기본으로
        self.plain_5.setDocument(doc)                           # doc를 plain_5에 지정
        self.plain_5.setDocumentTitle("Title")                  # plain_5의 doc객체 제목을 지정
        print(self.plain_5.documentTitle())                     # plain_5의 doc객체 제목 출력
    def fnc_btn_mime(self):
        data = self.plain_5.createMimeDataFromSelection()       # plain_5의 선택영역을 QMimeData객체로 생성
        print(self.plain_5.canInsertFromMimeData(data))         # QMimeData객체가 입력 가능상태인지 확인
        self.plain_6.insertFromMimeData(data)                   # QMimeData객체를 plain_6에입력

    #[6] 블록의 Geometry / 블록의 Rect / 커서이동 / 포맷 적용 / 현재 포맷에 새 포맷 추가
    # [blockBoundingGeometry / blockBoundingRect / setTextCursor / setCurrentCharFormat / mergeCurrentCharFormat
    def fnc_btn_block(self):
        doc = self.plain_6.document()                           # plain_6의 내용은 QDocument 객체로
        block_3 = doc.findBlockByNumber(3)                      # 3번째 줄 내용을 block_3에 QTextBlock객체로
        print(self.plain_6.blockBoundingGeometry(block_3))      # 3번째 줄 내용의 Geometry를 반환.
        print(self.plain_6.blockBoundingRect(block_3))          # 3번째 줄 내용의 Rect를 반환
    def fnc_btn_cursor(self):
        cursor = self.plain_6.cursorForPosition(QPoint(20,20))  # 20,20의 QTextCursor 객체로
        self.plain_6.setTextCursor(cursor)                      # QTextCursor의 위치로 커서 이동
    def fnc_btn_format(self):
        form = QTextCharFormat()                                # QTextCharFormat 객체 생성
        form.setFontPointSize(20)                               # 포맷에 폰트크기20 설정
        self.plain_6.setCurrentCharFormat(form)                 # plain_6에 포맷 적용
    def fnc_btn_merge(self):
        form = QTextCharFormat()                                # QTextCharFormat 객체 생성
        form.setFontUnderline(True)                             # 포맷에 밑줄 설정
        self.plain_6.mergeCurrentCharFormat(form)               # 기존 포맷에 새 포맷을 추가적용

    def fnc_undoAvailable(self)         : print("undoAvailable")
    def fnc_redoAvailable(self)         : print("redoAvailable")
    def fnc_copyAvailable(self)         : print("copyAvailable")
    def fnc_blockCountChanged(self)     : print("blockCountChanged")
    def fnc_modificationChanged(self)   : print("modificationChanged")
    def fnc_cursorPositionChanged(self) : print("cursorPositionChanged")
    def fnc_textChanged(self)           : print("textChanged")
    def fnc_selectionChanged(self)      : print("selectionChanged")

#==============================  app 실행 부분  =================================================================
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass( )
    myWindow.show( )
    app.exec_( )