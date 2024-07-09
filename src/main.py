from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet
from utilities.logger import Logger
from utilities.settings import Settings
from windows.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    
    settings = Settings()
    settings.load()
    apply_stylesheet(app, theme=settings.theme)
    
    window.showMaximized()
    app.exec()