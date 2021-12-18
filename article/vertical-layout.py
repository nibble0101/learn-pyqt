from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QLabel,
    QWidget,
    QApplication,
    QVBoxLayout,
)

application = QApplication([])

mainWindow = QWidget()

mainWindow.setGeometry(0, 0, 350, 400)
mainWindow.setWindowTitle('Vertical Layout')

verticalLayout = QVBoxLayout()

for num in range(6):
    label = QLabel()
    pixmap = QPixmap('cat.jpg')
    label.setPixmap(pixmap)
    verticalLayout.addWidget(label)

mainWindow.setLayout(verticalLayout)
mainWindow.show()

application.exec()