import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
    QPushButton, QApplication, QLabel, QLineEdit,
    QTextEdit, QLCDNumber, QSlider, QVBoxLayout,
    QCompleter)

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, QStringListModel
from PyQt5.QtGui import QPalette, QColor


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        qle = QLineEdit(self)

        qle.move(60,100)
        self.lbl.move(60,40)

        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300,30,280,170)
        self.setWindowTitle('Search Bar')
        self.show()

    def onChanged(self,text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()
if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    dark_palette = QPalette()

    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(dark_palette)
    ex = Window()
    sys.exit(app.exec_())