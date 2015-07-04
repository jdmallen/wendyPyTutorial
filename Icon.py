# __author__ = 'Jesse'

import sys

from PyQt4 import QtGui

class Icon(QtGui.QWidget):

    def __init__(self):
        super(Icon, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('web.png'))

        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Icon()
    sys.exit(app.exec_())

if __name__ == '__main__':
    
    main()
