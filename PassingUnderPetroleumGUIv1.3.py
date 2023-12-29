import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPalette, QColor

class LapsCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create widgets
        self.laps_run_label = QLabel('Laps run:')
        self.laps_run_entry = QLineEdit()
        self.laps_run_entry.returnPressed.connect(self.focus_next)

        self.gal_start_label = QLabel('Gallons start:')
        self.gal_start_entry = QLineEdit()
        self.gal_start_entry.returnPressed.connect(self.focus_next)

        self.gal_rem_label = QLabel('Gallons remaining:')
        self.gal_rem_entry = QLineEdit()
        self.gal_rem_entry.returnPressed.connect(self.calculate_laps)

        self.calculate_button = QPushButton('Calculate')
        self.calculate_button.clicked.connect(self.calculate_laps)

        self.result_label = QLabel('')

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.laps_run_label)
        layout.addWidget(self.laps_run_entry)
        layout.addWidget(self.gal_start_label)
        layout.addWidget(self.gal_start_entry)
        layout.addWidget(self.gal_rem_label)
        layout.addWidget(self.gal_rem_entry)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        # Set up the main window
        self.setWindowTitle('PassingUnderPetroleum')

        # Set black background color
        self.setAutoFillBackground(True)
        self.setPalette(self.get_dark_palette())

    def calculate_laps(self):
        lapsRun = float(self.laps_run_entry.text())
        galStart = float(self.gal_start_entry.text())
        galRem = float(self.gal_rem_entry.text())

        galUsed = galStart - galRem
        lapGal = round((lapsRun / galUsed), 1)
        lapTank = round((lapGal * galStart), 1)

        self.result_label.setText(f'Laps per gallon: {lapGal}\nLaps per Tank: {lapTank}')

    def focus_next(self):
        # Move focus to the next input box
        current_widget = self.focusWidget()
        next_widget = current_widget.tabOrder()
        if next_widget:
            next_widget.setFocus()

    def get_dark_palette(self):
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(0, 0, 0))
        dark_palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 220))
        dark_palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Text, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))

        return dark_palette

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Set Fusion style for dark mode appearance
    calculator = LapsCalculator()
    calculator.show()
    sys.exit(app.exec_())


