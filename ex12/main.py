import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from maior import Ui_MainWindow  # Importa a interface gerada

class main_maioNumero(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.maiorNumero)
        
    def maiorNumero(self):
        n1 = int(self.ui.lineEdit.text())
        n2 = int(self.ui.lineEdit_2.text())
        n3 = int(self.ui.lineEdit_3.text())

        if n1 > n2 and n1 > n3:
            self.ui.resultado.setText(f"{n1} é o maior número")
        elif n2 > n1 and n2 > n3:
            self.ui.resultado.setText(f"{n2} é o maior número")
        elif n3 > n1 and n3 > n2:
            self.ui.resultado.setText(f"{n3} é o maior número")
        else:
            self.ui.resultado.setText("Nenhum número é maior")
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_maioNumero()
    janela.show()
    sys.exit(app.exec_())