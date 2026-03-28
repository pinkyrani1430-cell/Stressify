import sys
import time
import random
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QTextEdit, QPushButton, QHBoxLayout
)
from PySide6.QtCore import Qt


class BurnoutApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Employee Burnout Detector")
        self.showMaximized()

        self.start_time = None
        self.dark_mode = False

        layout = QVBoxLayout()

        # ---------------- MESSAGES ---------------- #
        self.low_messages = [
            "Hey, looks like a calm day 😊",
            "You're doing great, keep going!",
            "Nice pace! Stay relaxed ✨",
            "I think today is a cool day for you 😎",
            "Everything is under control, keep smiling!",
            "You're typing like a peaceful monk 🧘‍♂️",
            "Chill mode activated 😌",
            "No stress detected... are you even human? 😄"
        ]

        self.medium_jokes = [
            "Why do programmers hate nature? Too many bugs 🐛",
            "Why did the computer get cold? It forgot to close Windows 😂",
            "Why do Java developers wear glasses? Because they don't C# 😆",
            "I told my computer I needed a break... it froze 🥶",
            "Why was the keyboard so tired? Too many shifts 😴",
            "Debugging: being the detective in a crime movie where you are also the criminal 😅",
            "My code doesn’t work, I have no idea why. My code works, I have no idea why 🤯",
            "Why did the developer go broke? Because he used up all his cache 💸",
            "There are only 10 types of people: those who understand binary and those who don’t 😄"
        ]

        self.high_jokes = [
            "STOP! Breathe 😤... you’re not fighting a boss battle 😂",
            "Relax! Even Google takes seconds to load sometimes 😄",
            "Your keyboard is not your enemy... be gentle 😅",
            "Warning: Overheating human detected 🔥😂",
            "Take a break before your brain files a complaint 🧠📢",
            "If stress burned calories, you'd be a superhero by now 💪😂",
            "Calm down... even bugs have feelings 🐛❤️",
            "You’re typing so fast even WiFi is confused 😳",
            "System alert: Human needs snacks 🍕 immediately!",
            "Don’t worry... even errors need love 💻❤️",
            "Your brain: 100 tabs open, 99 not responding 😂",
            "Take a deep breath… you're doing better than your code 😏"
        ]

        # ---------------- UI ---------------- #

        # Title
        self.title = QLabel("Burnout Detector")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("font-size: 22px; font-weight: bold;")

        # Text Box
        self.text_box = QTextEdit()
        self.text_box.setPlaceholderText("Start typing here...")

        # Labels
        self.speed_label = QLabel("Typing Speed: 0 WPM")
        self.stress_label = QLabel("Stress: Idle")

        self.message_label = QLabel("")
        self.message_label.setAlignment(Qt.AlignCenter)
        self.message_label.setStyleSheet("font-size: 14px; font-style: italic;")

        self.speed_label.setAlignment(Qt.AlignCenter)
        self.stress_label.setAlignment(Qt.AlignCenter)

        # Buttons
        self.start_btn = QPushButton("Start Monitoring")
        self.stop_btn = QPushButton("Stop Monitoring")
        self.theme_btn = QPushButton("Toggle Theme")

        # Button layout
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.stop_btn)

        # Add widgets to layout
        layout.addWidget(self.title)
        layout.addWidget(self.text_box)
        layout.addWidget(self.speed_label)
        layout.addWidget(self.stress_label)
        layout.addWidget(self.message_label)
        layout.addLayout(btn_layout)
        layout.addWidget(self.theme_btn)

        self.setLayout(layout)

        # Connections
        self.start_btn.clicked.connect(self.start_monitoring)
        self.stop_btn.clicked.connect(self.stop_monitoring)
        self.text_box.textChanged.connect(self.calculate_speed)
        self.theme_btn.clicked.connect(self.toggle_theme)

        self.apply_light_theme()

    def start_monitoring(self):
        self.start_time = time.time()
        self.text_box.clear()
        self.speed_label.setText("Typing Speed: 0 WPM")
        self.stress_label.setText("Stress: Idle")
        self.message_label.setText("")

    def stop_monitoring(self):
        self.start_time = None

    def calculate_speed(self):
        if not self.start_time:
            return

        text = self.text_box.toPlainText()
        char_count = len(text)

        elapsed_time = time.time() - self.start_time

        if elapsed_time <= 0 or char_count == 0:
            return

        # WPM calculation
        wpm = (char_count / 5) / (elapsed_time / 60)

        self.speed_label.setText(f"Typing Speed: {wpm:.2f} WPM")

        # Stress Logic + Messages
        if wpm < 40:
            stress = "Low Stress"
            color = "green"
            message = random.choice(self.low_messages)

        elif wpm < 60:
            stress = "Medium Stress"
            color = "orange"
            message = random.choice(self.medium_jokes)

        else:
            stress = "High Stress"
            color = "red"
            message = random.choice(self.high_jokes)

        self.stress_label.setText(f"Stress: {stress}")
        self.stress_label.setStyleSheet(f"font-weight: bold; color: {color};")

        # Show message/joke
        self.message_label.setText(message)

    # ---------------- THEME ---------------- #

    def toggle_theme(self):
        if self.dark_mode:
            self.apply_light_theme()
        else:
            self.apply_dark_theme()

        self.dark_mode = not self.dark_mode

    def apply_light_theme(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
                color: black;
            }
            QTextEdit {
                background-color: white;
                border: 1px solid gray;
                padding: 5px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 6px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: white;
            }
            QTextEdit {
                background-color: #2e2e2e;
                color: white;
                border: 1px solid gray;
                padding: 5px;
            }
            QPushButton {
                background-color: #007acc;
                color: white;
                padding: 6px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #005f99;
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BurnoutApp()
    window.show()
    sys.exit(app.exec())