import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from contagem import Ui_MainWindow  # Importa a interface gerada

class main_contagemRegressiva(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
       
        self.ui.pushButton.clicked.connect(self.contagemRegressiva)
       
    def contagemRegressiva(self):    
        n = 10
        resultado = ""
        for i in range(11):
            resultado += f"{n}\n"
            n -= 1
         
        self.ui.resultado.setText(resultado)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_contagemRegressiva()
    janela.show()
    sys.exit(app.exec_())