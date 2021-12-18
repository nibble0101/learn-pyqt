from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QLabel,
    QWidget,
    QApplication,
    QGridLayout,
)

application = QApplication([])

mainWindow = QWidget()

mainWindow.setGeometry(0, 0, 350, 400)
mainWindow.setWindowTitle('Grid Layout')

gridLayout = QGridLayout()

for row in range(3):
    for col in range(3):
        label = QLabel()
        pixmap = QPixmap('cat.jpg')
        label.setPixmap(pixmap)
        gridLayout.addWidget(label, row, col)

mainWindow.setLayout(gridLayout)
mainWindow.show()

application.exec()