from PyQt6.QtWidgets import QGridLayout,QWidget,QApplication,QLabel,QPushButton
import sys
from PyQt6.QtCore import Qt

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculator")

        #inital val
        self.current_input = "0"
        self.previous_input = ""
        self.current_operator = ""

        layout = QGridLayout()
        self.setLayout(layout)

        #Display
        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.display,0,0,1,4)

        #region Number Buttons
        buttons = [QPushButton(str(i)) for i in range(10)]
        
        for i,button in enumerate(buttons):
            # method takes 2 numbers and returns quotient and remainder as a tuple
            row,col = divmod(i,3)
            layout.addWidget(button,row+1,col)

        # Adding event handling to number buttons
        for button in buttons:
            button.clicked.connect(self.number_button_clicked)
        #endregion

        #region Operator Buttons
        operators = ["+","-","*","/"]
        operator_buttons = [QPushButton(op) for op in operators]

        for i,op_button in enumerate(operator_buttons):
            layout.addWidget(op_button,i+1,3)

        for button in operator_buttons:
            button.clicked.connect(self.operator_button_clicked)
        #endregion

        #region Equals and Clear
        self.equals_button = QPushButton("=")
        layout.addWidget(self.equals_button,4,1)
        self.equals_button.clicked.connect(self.calculate)

        self.clear_button = QPushButton("C")     
        layout.addWidget(self.clear_button,4,2)
        self.clear_button.clicked.connect(self.clear)
        #endregion

    
    # Method to handle number button clicked
    def number_button_clicked(self):
        digit = self.sender().text()

        if self.current_input == "0":
            self.current_input = digit
        else:
            self.current_input += digit
        self.display.setText(self.current_input)

    # Method to handle operator button clicked
    def operator_button_clicked(self):
        operator = self.sender().text()

        if self.current_operator == "":
            self.current_operator = operator
            self.previous_input = self.current_input
            self.current_input = "0"
        else:
            # calculate result of current stack
            self.calculate()
            self.current_operator = operator
            self.previous_input = self.current_input
            self.current_input = "0"

    def calculate(self):
        if self.current_operator == "+":
            result = float(self.previous_input) + float(self.current_input)
        elif self.current_operator == "-":
            result = float(self.previous_input) - float(self.current_input)
        elif self.current_operator == "*":
            result = float(self.previous_input) * float(self.current_input)
        elif self.current_operator == "/":
            if self.current_input == "0":
                result = "Error"
            else:
                result = float(self.previous_input) / float(self.current_input)
        else: 
            result = self.current_input
        self.display.setText(str(result))
        self.current_input = result
        self.current_operator = ""

    def clear(self):
        self.display.setText(self.current_input)
        self.current_input = "0"
        self.current_operator = ""
        self.previous_input = ""

app = QApplication(sys.argv)
# app.setStyle("windowsvista")
window = Window()
window.show()

sys.exit(app.exec())