from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from googletrans import Translator

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.trans = Translator()
        self.dictionary = { "англійська": "en",
                           "французька": "fr",
                           "іспанська": "es"}
    
        self.ui.comboBox.addItems(self.dictionary.keys())
        self.ui.pushButton.clicked.connect(self.translate_text)
        
    def translate_text(self):
        text = self.ui.textEdit.toPlainText()
        t = self.ui.comboBox.currentText()
        if text: 
            result = self.trans.translate(text,dest=self.dictionary[t])
            self.ui.textEdit_2.setPlainText(result.text)


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()

