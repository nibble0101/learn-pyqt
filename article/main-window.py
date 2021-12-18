from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Hello Wordl')
        self.setGeometry(0, 0, 350, 400)


if (__name__ == '__main__'):
    application = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    application.exec()