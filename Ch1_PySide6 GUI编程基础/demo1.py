import sys
from PySide6 import QtGui, QtCore, QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("demo_1")
    window.resize(500, 400)

    button = QtWidgets.QPushButton(window)
    button.setGeometry(150, 300, 150, 50)
    button.setText("关闭")

    label = QtWidgets.QLabel(window)
    label.setText("Hellow World\nPySide 6\nQt6")
    label.setGeometry(50, 10, 400, 300)
    font = QtGui.QFont()
    font.setPointSize(15)
    label.setFont(font)
    button.setFont(font)
    button.clicked.connect(window.close)
    window.show()
    sys.exit(app.exec())
