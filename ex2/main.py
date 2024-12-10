import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from parImpar import Ui_MainWindow  # Importa a interface gerada

class main_par_impar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.verificacao)
    
    def verificacao(self):
        num1 = int(self.ui.lineEdit.text())
        
        if num1 % 2 == 0:
            self.ui.resultado.setText("É par")
        else:
            self.ui.resultado.setText("É impar")
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_par_impar()
    janela.show()
    sys.exit(app.exec_())