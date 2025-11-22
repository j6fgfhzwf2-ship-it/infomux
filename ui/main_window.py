import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QComboBox, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from ai.model import AIModel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Infomux")
        self.setGeometry(200, 200, 600, 500)

        self.ai = AIModel()

        self.text_area = QTextEdit(self)
        self.text_area.setReadOnly(True)
        self.input_area = QTextEdit(self)
        self.input_area.setFixedHeight(50)

        self.persona_box = QComboBox(self)
        self.persona_box.addItems(["normal", "sans_filtre", "siri", "sombre"])
        self.persona_box.currentTextChanged.connect(self.change_persona)

        self.send_button = QPushButton("Envoyer", self)
        self.send_button.clicked.connect(self.send_message)

        layout = QVBoxLayout()
        layout.addWidget(self.text_area)
        layout.addWidget(self.input_area)
        layout.addWidget(self.persona_box)
        layout.addWidget(self.send_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def change_persona(self, text):
        self.ai.set_persona(text)

    def send_message(self):
        user_message = self.input_area.toPlainText()
        if user_message.strip() == "":
            return
        self.text_area.append(f"Vous: {user_message}")
        response = self.ai.ask(user_message)
        self.text_area.append(f"Infomux: {response}")
        self.input_area.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

