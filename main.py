import random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
import sqlite3
import sys


class CoffeeViewer(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        connection = sqlite3.connect('coffee_sqlite.db')
        curs = connection.cursor()
        self.res = curs.execute('''select * from coffee''').fetchall()
        self.coffee_btn.clicked.connect(self.show_coffee)

    def show_coffee(self):
        coffee = self.res[random.randint(0, len(self.res) - 1)]
        self.coffee_shower.setText(f"id: {coffee[0]}, {', '.join(coffee[1:-2])}, {coffee[-2]} рублей за {coffee[-1]}кг")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = CoffeeViewer()
    ex.show()
    sys.exit(app.exec())