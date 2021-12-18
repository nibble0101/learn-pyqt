from PyQt5.QtWidgets import QWidget, QApplication

app = QApplication([])

main_window = QWidget()

main_window.setGeometry(0, 0, 350, 400)
main_window.setWindowTitle('Hello World')

main_window.show()

app.exec()
