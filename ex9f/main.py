import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from tabuada import Ui_MainWindow  # Importa a interface gerada

class main_tabuada(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.tabuada)
        
    def tabuada(self):
        num1 = int(self.ui.comboBox.currentText())
        resultado = 1
        tabuada = []

        for i in range(11):
            resultado = num1 * i
            tabuada.append(f"{num1} X {i} = {resultado}")
            
        resultadoFinal = "\n".join(tabuada)
        self.ui.resultado.setText(resultadoFinal)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_tabuada()
    janela.show()
    sys.exit(app.exec_())