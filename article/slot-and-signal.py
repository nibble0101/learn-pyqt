from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

application = QApplication([])

mainWindow = QWidget()
mainWindow.setGeometry(0, 0, 350, 400)
mainWindow.setWindowTitle('Slot and Signal')


def clickedSlot():
    print('The button has been clicked')


pushButton = QPushButton(parent=mainWindow, text='Click me')
pushButton.clicked.connect(clickedSlot)

mainWindow.show()

application.exec()
