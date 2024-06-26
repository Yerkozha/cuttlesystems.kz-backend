import typing

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject, Slot, Signal

from common.localisation import tran

from constructor_app.widgets.ui_selected_project_widget import Ui_SelectedProjectWidget

class SelectedProjectWidget(QWidget):
    activated_bot_signal = Signal(bool)
    def __init__(self, parent: typing.Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_SelectedProjectWidget()
        self._ui.setupUi(self)
        self._ui.switch_activated_bot.clicked.connect(self._switchBot)
        self._init_StyleSheet()
        # toDO: Добавить функцию инициализации QSS

    def _init_StyleSheet(self):
        # toDO: перенести все qssы в отдельный файлпроекта или для каждого окна сделать свой первострочный
        #  инициализатор qss
        self._ui.groupBox.setStyleSheet("QGroupBox{border-radius:22px; border:none; "
                                        "background-color:rgb(255,255,255);}")
        self._ui.open_in_redactor_button.setStyleSheet("QPushButton{background-color:rgb(57,178,146);border:none;"
                                                       "color:white;border-radius:8px;}")

    def _switchBot(self):
        # toDO: перенести все qssы в отдельный файлпроекта или для каждого окна сделать свой первострочный
        #  инициализатор qss и продумать грамотный флаг состояния бота
        if(self._ui.switch_activated_bot.isChecked()):
            self._ui.marker_state_bot.setStyleSheet("QLabel{border-radius:8px; border:none; color:white;"
                                                       "background-color:#4DAAFF;}")
            self._ui.marker_state_bot.setText(self._tr(u"Bot is enabled"))
            self.activated_bot_signal.emit(True)
        else:
            self._ui.marker_state_bot.setStyleSheet("QLabel{border-radius:8px; border:none; color:white;"
                                                       "background-color:#FF5F8F;}")
            self._ui.marker_state_bot.setText(self._tr(u"Bot is disabled"))
            self.activated_bot_signal.emit(False)

    def _tr(self, text: str) -> str:
        return tran('SelectedProjectWidget.manual', text)