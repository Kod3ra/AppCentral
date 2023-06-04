import sys
import subprocess
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QTextEdit, QGridLayout, QComboBox, QDialog, QLabel, QInputDialog

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AppCentral | V1.0 | Made By Kod3ra")
        self.resize(750, 450)  # Définition des dimensions de la fenêtre

        self.layout = QVBoxLayout()
        self.console = QTextEdit()
        self.console.setReadOnly(True)
        self.layout.addWidget(self.console)

        buttons_layout = QGridLayout()

        self.buttons = []
        for i in range(4):
            button = QPushButton("Add an application")
            button.clicked.connect(self.launch_application)
            self.buttons.append(button)
            button.setMaximumWidth(150)  # Définir une largeur maximale pour les boutons
            buttons_layout.addWidget(button, i, 0)

        for i in range(4):
            button = QPushButton("Add an application")
            button.clicked.connect(self.launch_application)
            self.buttons.append(button)
            button.setMaximumWidth(150)  # Définir une largeur maximale pour les boutons
            buttons_layout.addWidget(button, i, 1)

        buttons_layout.setColumnStretch(2, 1)  # Permet aux boutons de rester collés à gauche

        reset_button = QPushButton("Reset")
        reset_button.clicked.connect(self.reset_applications)
        buttons_layout.addWidget(reset_button, 0, 2)  # Bouton "Reset" positionné en haut à droite

        theme_button = QPushButton("Thème")
        theme_button.clicked.connect(self.show_theme_options)
        buttons_layout.addWidget(theme_button, 1, 2)  # Bouton "Thème" positionné en bas à droite

        settings_button = QPushButton("Settings")
        settings_button.clicked.connect(self.open_settings_dialog)
        buttons_layout.addWidget(settings_button, 2, 2)  # Bouton "Settings" positionné en bas à droite

        self.layout.addLayout(buttons_layout)

        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

    def launch_application(self):
        button = self.sender()
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Applications (*.exe *.py *.pyw)")
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            application_name = os.path.basename(file_path)
            button.setText(application_name)
            button.clicked.disconnect()
            button.clicked.connect(lambda: self.launch_application_from_button(file_path))

    def launch_application_from_button(self, file_path):
        try:
            subprocess.Popen(file_path)
            self.console.append(f"Application launched: {file_path}")
        except OSError:
            self.console.append(f"Failed to launch application: {file_path}")

    def reset_applications(self):
        for button in self.buttons:
            button.setText("Add an application")
            button.clicked.disconnect()
            button.clicked.connect(self.launch_application)

    def show_theme_options(self):
        theme_options = ["Default", "Dark", "Light", "Multicolore", "Red", "Green", "Blue"]

        theme, ok = QInputDialog.getItem(self, "Select Theme", "Choose a theme:", theme_options)

        if ok and theme:
            if theme == "Default":
                self.setStyleSheet("")
            elif theme == "Dark":
                self.setStyleSheet("background-color: #1e1e1e; color: #ffffff;")
            elif theme == "Light":
                self.setStyleSheet("background-color: #f0f0f0; color: #000000;")
            elif theme == "Multicolore":
                self.setStyleSheet("background-color: #ff0000;"
                                   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #ff0000, stop:0.17 #ff8000, stop:0.33 #ffff00, stop:0.5 #00ff00, stop:0.67 #00ffff, stop:0.83 #0000ff, stop:1 #8000ff);"
                                   "color: #ffffff;")
            elif theme == "Red":
                self.setStyleSheet("background-color: #ff0000; color: #ffffff;")
            elif theme == "Green":
                self.setStyleSheet("background-color: #00ff00; color: #ffffff;")
            elif theme == "Blue":
                self.setStyleSheet("background-color: #0000ff; color: #ffffff;")

    def open_settings_dialog(self):
        settings_dialog = QDialog(self)
        settings_dialog.setWindowTitle("Settings")

        layout = QVBoxLayout()

        language_label = QLabel("Language:")
        layout.addWidget(language_label)

        language_combo = QComboBox()
        language_combo.addItem("English")
        language_combo.addItem("Français")
        layout.addWidget(language_combo)

        save_button = QPushButton("Save")
        save_button.clicked.connect(settings_dialog.accept)
        layout.addWidget(save_button)

        settings_dialog.setLayout(layout)
        settings_dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
