import sys
import random
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Загрузка интерфейса из файла UI.ui
        uic.loadUi("UI.ui", self)
        self.setWindowTitle("Генератор окружностей")

        # Подключение кнопки к обработчику событий
        self.pushButton.clicked.connect(self.add_circle)

        # Список для хранения окружностей
        self.circles = []

    def add_circle(self):
        """Добавляет данные для новой окружности и перерисовывает виджет"""
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((x, y, diameter))
        self.update()  # Обновление интерфейса

    def paintEvent(self, event):
        """Рисует окружности на форме"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        for x, y, diameter in self.circles:
            painter.setBrush(QColor("yellow"))
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
