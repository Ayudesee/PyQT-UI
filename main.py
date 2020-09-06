import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import pyautogui as pgui
import Xclipboard as cb


class MainPage(QDialog):
    posStatusCompleted = "1290, 237"
    posStatusClosed = "904, 286"
    posWriteAndClose = "143, 171"
    posFirstAppeal = "232, 250"
    countAppeal = 2
    countPause = 2
    countMouseMovementTime = 0.6
    qwerty = """qwertyuiop[]asdfghjkl;'zxcvbnm,.?/QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>"""
    ycuken = """йцукенгшщзхъфывапролджэячсмитьбю,.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"""
    minfo = 0
    tr = dict(zip(ycuken, qwerty))

    def translate(self, key):
        """Returns qwerty key or the given key itself if no mapping found"""
        return "".join(map(lambda x: self.tr.get(x, x), key))

    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('for_work.ui', self)
        self.lineEdit.setText(self.posStatusCompleted)
        self.lineEdit_2.setText(self.posStatusClosed)
        self.lineEdit_3.setText(self.posWriteAndClose)
        self.lineEdit_4.setText(self.posFirstAppeal)
        self.lineEdit_5.setText(str(self.countAppeal))
        self.lineEdit_6.setText(str(self.countPause))
        self.lineEdit_7.setText(str(self.countMouseMovementTime))
        self.pushButton.clicked.connect(self.func1)
        self.pushButton_2.clicked.connect(self.func2)
        self.pushButton_3.clicked.connect(self.func3)
        self.pushButton_4.clicked.connect(self.func4)
        self.pushButton_5.clicked.connect(self.func5)

        self.pushButton_7.clicked.connect(self.func7)
        self.pushButton_8.clicked.connect(self.func8)
        self.pushButton_9.clicked.connect(self.func9)
        self.mouseInfoButton.clicked.connect(self.mouseInfo)

    # def closeEvent(self, event):
    #     pass
        #if type(self.minfo) == :
            #self.minfo.closeEvent(self)

    def func1(self):
        #pgui.moveTo(1336, 427, 3)
        #pgui.click()
        #pgui.typewrite(self.translate('проконтролировано'), interval=0.1)
        pgui.sleep(2)
        cb.copy("проконтролировано")
        #cb.paste()
        pgui.hotkey('ctrl', 'v')

    def func2(self):
        print('2')

    def func3(self):
        print('3')

    def func4(self):
        print('4')

    def func5(self):
        self.countAppeal = int(self.lineEdit_5.text())
        print(type(self.countAppeal))
        print(self.countAppeal)
        self.lineEdit_5.setText(str(self.countAppeal - 5))

    def func6(self):
        pass

    def func7(self):
        pgui.sleep(2)
        self.countMouseMovementTime = float(self.lineEdit_7.text())
        self.countAppeal = int(self.lineEdit_5.text())
        self.countPause = float(self.lineEdit_6.text())
        x = self.countAppeal
        while x > 0:
            pgui.sleep(float(self.countPause))
            pgui.moveTo(int(self.posStatusCompleted.split(", ")[0]), int(self.posStatusCompleted.split(", ")[1]),
                        self.countMouseMovementTime)
            pgui.sleep(0.2)
            pgui.click(duration=0.1)
            pgui.sleep(float(self.countPause))
            pgui.moveTo(int(self.posStatusClosed.split(", ")[0]), int(self.posStatusClosed.split(", ")[1]),
                        self.countMouseMovementTime)
            pgui.sleep(0.2)
            pgui.click(duration=0.1)
            pgui.sleep(float(self.countPause))
            pgui.moveTo(int(self.posWriteAndClose.split(", ")[0]), int(self.posWriteAndClose.split(", ")[1]),
                        self.countMouseMovementTime)
            pgui.sleep(0.2)
            pgui.click(duration=0.1)

            pgui.sleep(float(self.countPause) + 2)
            pgui.press('down')
            pgui.sleep(float(self.countPause))
            pgui.press('enter')
            x -= 1
            self.lineEdit_5.setText(str(x))
            self.repaint()

    def func8(self):
        self.label_5.setText(self.lineEdit.text())
        self.label_6.setText(self.lineEdit_2.text())
        self.label_7.setText(self.lineEdit_3.text())
        self.label_8.setText(self.lineEdit_4.text())
        self.posStatusCompleted = self.lineEdit.text()
        self.posStatusClosed = self.lineEdit_2.text()
        self.posWriteAndClose = self.lineEdit_3.text()
        self.posFirstAppeal = self.lineEdit_4.text()

    def func9(self):
        self.lineEdit.setText(self.posStatusCompleted)
        self.lineEdit_2.setText(self.posStatusClosed)
        self.lineEdit_3.setText(self.posWriteAndClose)
        self.lineEdit_4.setText(self.posFirstAppeal)
        self.func8()

    def mouseInfo(self):
        self.minfo = pgui.mouseInfo()
        print(type(self.minfo))


app = QApplication(sys.argv)
widget = MainPage()
widget.show()
widget.setWindowTitle("For Itilium")
sys.exit(app.exec_())


