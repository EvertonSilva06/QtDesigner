import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from pnz import Ui_MainWindow  # Importa a interface gerada

class main_positivoNegativoZero(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.positivoNegativoZero)
        
    def positivoNegativoZero(self):
        n = int(self.ui.lineEdit.text())

        if n < 0:
            self.ui.resultado.setText("É negativo")
        elif n > 0:
            self.ui.resultado.setText("É positivo")
        else:
            self.ui.resultado.setText("É zero")
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_positivoNegativoZero()
    janela.show()
    sys.exit(app.exec_())