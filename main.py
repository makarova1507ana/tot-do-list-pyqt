from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QListWidget, QListWidgetItem
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

class ToDoListApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List")

        # Настраиваем темный стиль
        self.set_dark_theme()

        # Создаем центральный виджет и layout
        widget = QWidget(self)
        main_layout = QVBoxLayout(widget)

        # Поле ввода для новых задач
        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Введите задачу")

        # Кнопка для добавления задач
        self.add_button = QPushButton("Добавить", self)
        self.add_button.clicked.connect(self.add_task)

        # Список задач (QListWidget)
        self.task_list = QListWidget(self)

        # Кнопка для удаления выбранных задач
        self.delete_button = QPushButton("Удалить выбранные", self)
        self.delete_button.clicked.connect(self.delete_task)

        # Добавляем виджеты в layout
        main_layout.addWidget(self.task_input)
        main_layout.addWidget(self.add_button)
        main_layout.addWidget(self.task_list)
        main_layout.addWidget(self.delete_button)

        # Устанавливаем общий стиль для всех элементов через setStyleSheet
        self.setStyleSheet("""
            QWidget {
                background-color: #1a1a1a;
            }

            QLineEdit {
                color: yellow; 
                background-color: #1a1a1a; 
                border: 1px solid #ffd700; 
                padding: 10px; 
                border-radius: 10px;
                font-size: 14px;
            }

            QLineEdit:hover {
                border-color: #fff700;
            }

            QPushButton {
                color: black; 
                background-color: #ffd700; 
                border-radius: 10px; 
                padding: 10px; 
                font-size: 14px;
                transition: background-color 0.3s ease;
            }

            QPushButton:hover {
                background-color: #fff44f;
            }

            QPushButton:pressed {
                background-color: #e0e000;
            }

            QListWidget {
                color: yellow; 
                background-color: #1a1a1a; 
                border: 1px solid #ffd700; 
                padding: 10px; 
                border-radius: 10px;
            }

            QListWidget::item {
                padding: 10px;
            }

            QListWidget::item:selected {
                background-color: #2a2a2a;
                color: #ffd700;
            }
        """)

        # Устанавливаем layout в основной виджет
        self.setCentralWidget(widget)

    def set_dark_theme(self):
        """Устанавливаем темную цветовую тему с желтыми элементами"""
        dark_palette = QPalette()
        
        # Цвет фона
        dark_palette.setColor(QPalette.ColorRole.Window, QColor(26, 26, 26))  # Темный фон
        dark_palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.yellow)

        # Цвет кнопок и фона кнопок
        dark_palette.setColor(QPalette.ColorRole.Button, Qt.GlobalColor.yellow)
        dark_palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.black)

        # Цвет текста и фона
        dark_palette.setColor(QPalette.ColorRole.Base, QColor(26, 26, 26))  # Цвет фона элементов
        dark_palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.yellow)

        # Цвет выделенных элементов
        dark_palette.setColor(QPalette.ColorRole.Highlight, Qt.GlobalColor.yellow)
        dark_palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)

        # Применяем палитру к приложению
        self.setPalette(dark_palette)

    def add_task(self):
        """Добавляем задачу в список"""
        task = self.task_input.text()
        if task:  # Проверяем, что задача не пустая
            list_item = QListWidgetItem(task)
            list_item.setFlags(list_item.flags() | Qt.ItemFlag.ItemIsUserCheckable)  # Делаем элемент отмечаемым
            list_item.setCheckState(Qt.CheckState.Unchecked)  # Состояние задачи: не выполнена
            self.task_list.addItem(list_item)
            self.task_input.clear()  # Очищаем поле ввода

    def toggle_task(self, item):
        """Зачеркивание выполненной задачи"""
        font = item.font()
        if item.checkState() == Qt.CheckState.Checked:
            font.setStrikeOut(True)  # Зачеркнуть текст, если задача выполнена
        else:
            font.setStrikeOut(False)  # Убрать зачеркивание, если задача не выполнена
        item.setFont(font)

    def delete_task(self):
        """Удаление выбранных задач"""
        for item in self.task_list.selectedItems():
            self.task_list.takeItem(self.task_list.row(item))  # Удаляем выбранные элементы


# Запуск приложения
app = QApplication([])

# Создаем главное окно
window = ToDoListApp()
window.show()

# Запуск цикла обработки событий
app.exec()
