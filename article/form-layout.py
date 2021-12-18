from PyQt5.QtWidgets import (
    QGroupBox,
    QLabel,
    QLineEdit,
    QPlainTextEdit,
    QRadioButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
    QApplication,
    QFormLayout,
)

application = QApplication([])

mainWindow = QWidget()

mainWindow.setGeometry(0, 0, 350, 400)
mainWindow.setWindowTitle('Form Layout')

formLayout = QFormLayout()

nameLabel = QLabel('Name')
nameField = QLineEdit()

ageLabel = QLabel('Age')
ageField = QSpinBox()
ageField.setMinimum(0)
ageField.setMaximum(130)


sexLabel = QLabel('Sex')
sexGroup = QGroupBox()
verticalLayout = QVBoxLayout()

for sex in ['Male', 'Female', 'Other']:
    radioButton = QRadioButton(sex)
    verticalLayout.addWidget(radioButton)

sexGroup.setLayout(verticalLayout)

commentLabel = QLabel('Comments')
commentField = QPlainTextEdit()


formLayout.addRow(nameLabel, nameField)
formLayout.addRow(ageLabel, ageField)
formLayout.addRow(sexLabel, sexGroup)
formLayout.addRow(commentLabel, commentField)

mainWindow.setLayout(formLayout)
mainWindow.show()

application.exec()