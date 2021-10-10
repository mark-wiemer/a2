import logging
import typing
from singlesiding import QSingleApplication
from a2qt import QtWidgets
import a2db
import a2modsource

A2DEFAULT_HOTKEY: str
EDIT_DISCLAIMER: str
NAME: str

class A2Obj:
    """Non-Ui a2 backend object."""

    _instance: object

    app: typing.Optional[QSingleApplication] = None
    win: typing.Optional[QtWidgets.QMainWindow] = None
    paths: Paths
    urls: URLs
    db: a2db.A2db

    enabled: typing.Dict[str, typing.List[str]]
    module_sources: typing.Dict[str, a2modsource.ModSource]

    def __init__(self) -> None: ...
    @classmethod
    def inst(cls) -> A2Obj: ...
    def start_up(self) -> None: ...
    def fetch_modules(self) -> None: ...


class Paths:
    """Aquires and hosts common paths around a2."""

    a2: str
    autohotkey: str
    data: str
    defaults: str
    includes: str
    lib: str
    def set_data_path(self, str): ...
    def write_user_include(self): ...


class URLs:
    a2: str
    help: str
    wiki: str
    helpEditCtrl: str
    helpHotkey: str
    helpCheckbox: str
    help_scopes: str
    help_string: str
    help_number: str
    help_path: str
    help_report_issue: str
    security: str
    ahk: str
    ahk_commands: str
    ahk_run: str
    ahk_send: str
    ahkWinActive: str
    ahk_builtin_vars: str
    ahkWinTitle: str


def get_logger(str) -> logging.Logger: ...

def tags() -> dict[str, str]:
    """Return tags dictionary with shortnames/english desctiptions."""
