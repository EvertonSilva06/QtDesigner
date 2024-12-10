import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from primo import Ui_MainWindow  # Importa a interface gerada

class main_primo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.primo)
        
    def primo(self):
        num1 = int(self.ui.lineEdit.text())

        if num1 > 1:
            for i in range(2,num1):
                if num1 % i == 0:
                    self.ui.resultado.setText("Não é primo")
                    break
                else:
                    self.ui.resultado.setText("É primo")
                    break
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_primo()
    janela.show()
    sys.exit(app.exec_())