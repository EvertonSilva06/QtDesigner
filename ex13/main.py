import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from e10e20 import Ui_MainWindow  # Importa a interface gerada

class main_entre10e20(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.entre10e20)
        
    def entre10e20(self):
        n = int(self.ui.lineEdit.text())
        list = [i for i in range(10,21)]

        if n in list:
            self.ui.resultado.setText("O número está entre 10 e 20")
        else:
            self.ui.resultado.setText("O número não está entre 10 e 20")
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_entre10e20()
    janela.show()
    sys.exit(app.exec_())