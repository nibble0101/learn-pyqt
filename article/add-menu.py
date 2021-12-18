from PyQt5.QtWidgets import QMainWindow, QApplication, QAction


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Dropdown Menu')
        self.setGeometry(0, 0, 350, 400)
        self.addMenu()

    def addMenu(self):

        # Create menu bar
        menuBar = self.menuBar()

        # Add menu items
        fileMenu = menuBar.addMenu('File')
        helpMenu = menuBar.addMenu('Help')

        # Create actions

        visitWebsiteAction = QAction('Visit Our Website', self)
        fileBugReportAction = QAction('File a Bug Report', self)

        # Add dropdown menu items on the Help menu
        
        helpMenu.addAction(visitWebsiteAction)
        helpMenu.addAction(fileBugReportAction)

        # Add 'Follow Us' dropdown menu item on the Help menu
       
        followUs = helpMenu.addMenu('Follow Us')

        # Social media actions

        twitterAction = QAction('Twitter', self)
        githubAction = QAction('GitHub', self)

        # Add actions

        followUs.addAction(twitterAction)
        followUs.addAction(githubAction)



if (__name__ == '__main__'):
    application = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    application.exec()