import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QLineEdit
from PyQt5.QtCore import Qt

from jisho_apiCall import *

class kirara(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kirara Dictionary")
        self.resize(250, 100) 

        layout = QVBoxLayout()

        self.label = QLabel("Created by Bunkai\n&\nPowered by the Jisho API")
        self.label.setStyleSheet("color:black; font-size:14px;")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Introduce texto")
        self.input.returnPressed.connect(self.comando_dic)
        layout.addWidget(self.input)

        self.setLayout(layout)

    def comando_dic(self):
        texto = self.input.text()
        result = jisho_Dic(texto)
        self.label.setText(result)
        self.input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = kirara()
    ventana.show()
    sys.exit(app.exec_())