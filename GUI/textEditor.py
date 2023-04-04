import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QFileDialog

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btnOpen = QPushButton("Abrir", self)
        btnOpen.move(30,50)
        btnOpen.resize(btnOpen.sizeHint())
        btnOpen.clicked.connect(self.openArchive)

        btnSave = QPushButton("Salvar", self)
        btnSave.move(120,50)
        btnSave.resize(btnSave.sizeHint())
        btnSave.clicked.connect(self.saveArchive)

        self.textField = QPlainTextEdit(self)
        self.textField.setGeometry(20 , 100, 260, 200)

        self.setGeometry(300, 300, 300, 350)
        self.setWindowTitle("Editor de Texto")
        self.show()

    def openArchive(self):
        nameArchive, _ = QFileDialog.getOpenFileNames(self, "Abrir arquivo")
        if nameArchive:
            with open(nameArchive, 'r') as archive:
                text = archive.read()
                self.textField.setPlainText(text)

    def saveArchive(self):
        nameArchive, _ =QFileDialog.getSaveFileName(self, 'Salvar Arquivo')
        if nameArchive:
            with open(nameArchive, 'w') as archive:
                text = self.textField.toPlainText()
                archive.write(text)

if __name__=="__main__":
    app = QApplication(sys.argv)
    editor = TextEditor()
    sys.exit(app.exec_())