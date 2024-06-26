import typing

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject, Slot, Signal, QThread

from common.localisation import tran

from constructor_app.widgets.ui_login_widget import Ui_LoginWidget

class LoginWidget(QWidget):
    # сигнал, что пользователь авторизовался
    log_in = Signal()
    registrated_state_signal = Signal(bool)
    def __init__(self, parent: typing.Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_LoginWidget()
        self._ui.setupUi(self)

        # подключаю кнопку ентерПользователя с переходом на мейнОкно
        self._ui.enter_button.clicked.connect(self._clicked_login)
        # toDO: Добавить функцию инициализации QSS

    def _clicked_login(self):
        self.log_in.emit()

    def _switch_login(self):
        # toDO: перенести все qssы в отдельный файлпроекта или для каждого окна сделать свой
        #  первострочный инициализатор qss и доработать режим входа/регистрации
        #if (self._ui.switchActivatedBot.isChecked()):
        #    self._ui.markerActivisionBot.setStyleSheet("QLabel{border-radius:8px; border:none; color:white;"
        #                                                   "background-color:#4DAAFF;}")
        #    self._ui.markerActivisionBot.setText(u"Бот запущен")
        #    self.ActivatedBotSignal.emit(True)
        #else:
        #    self._ui.markerActivisionBot.setStyleSheet("QLabel{border-radius:8px; border:none; color:white;"
        #                                                   "background-color:#FF5F8F;}")
        #    self._ui.markerActivisionBot.setText(u"Бот не активен")
        self.registrated_state_signal.emit(False)

    def _tr(self, text: str) -> str:
        return tran('LoginWidget.manual', text)