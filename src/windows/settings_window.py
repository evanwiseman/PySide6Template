
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QGridLayout, QVBoxLayout, QLabel, QCheckBox, QComboBox, QPushButton, QDialogButtonBox, QDialog
from qt_material import apply_stylesheet, list_themes
from utilities.settings import Settings
from utilities.logger import Logger



class SettingsWindow(QDialog):
    _logger = Logger(__name__).get_logger()
    _SETTINGS_LAYOUT_ALIGNMENT = Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft
    _SETTINGS_LAYOUT_PADDING = (0, 0, 0, 0)
    _SETTINGS_LAYOUT_SPACING = 0
    
    _BUTTON_BOX_LAYOUT_ALIGNMENT = Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight
    _BUTTON_BOX_LAYOUT_PADDING = (0, 0, 0, 0)
    _BUTTON_BOX_LAYOUT_SPACING = 0
    
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.settings = Settings()
        self.settings.load()
        self.init_ui()
        self.apply_theme(self.settings.theme)
        
    def init_ui(self):
        self.setWindowTitle('Settings')
        self.setGeometry(100, 100, 400, 200)
        
        self.theme_label = QLabel('Theme:')

        self.theme_combo = QComboBox()
        self.theme_combo.addItems(list_themes())
        self.theme_combo.setCurrentText(self.settings.theme)
        self.theme_combo.currentTextChanged.connect(self.on_theme_changed)
        
        self.button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Apply | 
            QDialogButtonBox.StandardButton.Ok | 
            QDialogButtonBox.StandardButton.Cancel
        )
        self.button_box.button(QDialogButtonBox.StandardButton.Apply).clicked.connect(lambda: self.apply_theme(self.settings.theme))
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        
        settings_layout = QGridLayout()
        settings_layout.setAlignment(self._SETTINGS_LAYOUT_ALIGNMENT)
        settings_layout.setContentsMargins(*self._SETTINGS_LAYOUT_PADDING)
        settings_layout.setSpacing(self._SETTINGS_LAYOUT_SPACING)
        settings_layout.addWidget(self.theme_label, 0, 0)
        settings_layout.addWidget(self.theme_combo, 0, 1)
        
        button_box_layout = QVBoxLayout()
        button_box_layout.setAlignment(self._BUTTON_BOX_LAYOUT_ALIGNMENT)
        button_box_layout.setContentsMargins(*self._BUTTON_BOX_LAYOUT_PADDING)
        button_box_layout.setSpacing(self._BUTTON_BOX_LAYOUT_SPACING)
        button_box_layout.addWidget(self.button_box)
        
        layout = QVBoxLayout()
        layout.addLayout(settings_layout)
        layout.addLayout(button_box_layout)
        self.setLayout(layout)
    
    def accept(self):
        self.apply_theme(self.settings.theme)
        self.settings.save()
        super().accept()
    
    def reject(self):
        super().reject()
    
    def on_theme_changed(self, theme):
        self.settings.theme = theme
    
    def apply_theme(self, theme):
        try:
            self._logger.info(f'Applying theme: {theme}')
            apply_stylesheet(QApplication.instance(), theme=theme)
        except Exception as e:
            self._logger.error(f'Failed to apply theme: {e}')
