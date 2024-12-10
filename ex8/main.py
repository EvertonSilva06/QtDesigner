import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from quadrado import Ui_MainWindow  # Importa a interface gerada

class main_quadrado(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.quadrado)
    
    def quadrado(self):
        num1 = int(self.ui.lineEdit.text())
        quadrado = num1 * num1
        self.ui.resultado.setText(f"Resultado: {quadrado}")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_quadrado()
    janela.show()
    sys.exit(app.exec_())