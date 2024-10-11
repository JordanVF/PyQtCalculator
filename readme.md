# PyQt Calculator

## Description
A simple calculator application built using `PyQt6`. This calculator allows users to perform basic arithmetic operations like addition, subtraction, multiplication, and division. It features a clear display and responsive buttons for digits and operators.

## Installation 
1. Clone the repository:
   ```bash
   git clone https://github.com/JordanVF/pyQtCalculator.git
2. Navigate to the project directory: 
```bash
cd pyQtCalculator
```
3. Install the required dependencies:
```bash
pip install PyQt6
```
 
## Usage
1. Run the application
2. Features:
   - Digits (0-9): Input numbers by clicking the corresponding buttons.
   - Operators (+, -, *, /): Perform basic arithmetic operations.
   - Equals (=): Calculate the result of the operation.
   - Clear (C): Clear the current input and reset the calculator.

## How it works
- Display: The current input or result is displayed using a QLabel aligned to the right for a clean look.
- Buttons: Buttons for digits and operators are created dynamically and added to a QGridLayout for a simple calculator-like layout.
- Event Handling: Each button click triggers connected functions. Number buttons append digits to the current input, operator buttons store the operation to be performed, and the equals button calculates and displays the result.
- Arithmetic: The calculate method handles the arithmetic based on the selected operator. It checks for division by zero and outputs an error if this occurs.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

