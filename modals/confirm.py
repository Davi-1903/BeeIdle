from textual.app import ComposeResult
from textual.events import Key
from textual.screen import ModalScreen
from textual.containers import Container, Grid, Horizontal
from textual.widgets import Button, Static


class ConfirmModal(ModalScreen):
    def __init__(
        self, message: str, name: str | None = None, id: str | None = None, classes: str | None = None
    ) -> None:
        super().__init__(name, id, classes)
        self.__message = message

    def compose(self) -> ComposeResult:
        with Grid():
            with Container(classes='forms'):
                yield Static(self.__message)

                with Horizontal():
                    yield Button('Ok', id='confirm-btn', variant='success')
                    yield Button('Cancelar', id='cancel-btn', variant='error')

    def on_key(self, event: Key):
        if event.key == 'escape':
            self.dismiss(False)

    def on_button_pressed(self, event: Button.Pressed):
        self.dismiss(event.button.id == 'confirm-btn')
