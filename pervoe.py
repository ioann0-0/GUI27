import sys
import requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QLineEdit, QVBoxLayout, QWidget, QFileDialog

class JsonPlaceholderClient(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('JSON Placeholder Client')
        self.setGeometry(100, 100, 600, 400)

        self.url_input = QLineEdit(self)
        self.url_input.setText('https://jsonplaceholder.typicode.com/posts')

        self.get_data_button = QPushButton('Получить данные', self)
        self.get_data_button.clicked.connect(self.get_data)

        self.save_data_button = QPushButton('Сохранить данные', self)
        self.save_data_button.clicked.connect(self.save_data)

        self.result_text_edit = QTextEdit(self)
        self.result_text_edit.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.url_input)
        layout.addWidget(self.get_data_button)
        layout.addWidget(self.result_text_edit)
        layout.addWidget(self.save_data_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def get_data(self):
        url = self.url_input.text()
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            self.result_text_edit.setPlainText(str(data))
        except requests.RequestException as e:
            self.result_text_edit.setPlainText(f'Ошибка: {e}')

    def save_data(self):
        data = self.result_text_edit.toPlainText()
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить данные", "", "JSON Files (*.json);;All Files (*)", options=options)
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(data)
            except Exception as e:
                self.result_text_edit.setPlainText(f'Ошибка при сохранении: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = JsonPlaceholderClient()
    window.show()
    sys.exit(app.exec())
