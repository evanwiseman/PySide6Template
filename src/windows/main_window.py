from PySide6.QtWidgets import QMainWindow, QGridLayout, QWidget
from windows.settings_window import SettingsWindow

class MainWindow(QMainWindow):
    settings_window = None
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Main Window')
        
        menu_bar = self.menuBar()
        
        file_menu = menu_bar.addMenu('File')
        
        view_menu = menu_bar.addMenu('View')
        
        settings_menu = menu_bar.addMenu('Options')
        settings_menu.addAction('Settings', self.open_settings)
        
        layout = QGridLayout()
        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def open_settings(self):
        if self.settings_window is None:
            self.settings_window = SettingsWindow()
        self.settings_window.show()