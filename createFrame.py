from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QGridLayout, QPushButton, QLabel

class crF():

    def createF(self, nameRecept):
        frame = QFrame()
        frame.resize(500,200)
        pBtn = QPushButton(frame)
        gridLayout_14 = QGridLayout(frame)
        gridLayout_14.setObjectName("gridLayout_14")
        pBtn.setMaximumSize(QSize(100, 30))
        pBtn.setObjectName(nameRecept)
        gridLayout_14.addWidget(pBtn, 0, 1, 1, 1)
        label = QLabel(frame)
        font = QFont()
        font.setFamily("Open Sans ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        label.setFont(font)
        label.setFrameShadow(QFrame.Sunken)
        label.setLineWidth(2)
        gridLayout_14.addWidget(label, 0, 0, 1, 1)
        label.setText(nameRecept)
        pBtn.setText("Открыть")
        pBtn.clicked.connect(lambda: self.receptWindow(nameRecept))
        return frame
