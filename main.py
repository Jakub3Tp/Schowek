import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.text = ""
        self.ui.copy.clicked.connect(self.copy)
        self.ui.paste.clicked.connect(self.paste)

    def copy(self):
        self.text = self.ui.dataLine.text()

    def paste(self):
        self.ui.result.setText(self.text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())