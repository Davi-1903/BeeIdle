from textual import on
from textual.app import ComposeResult
from textual.events import Key
from textual.screen import ModalScreen
from textual.widgets import Input


class OpenDirectoryModal(ModalScreen):    
    def compose(self) -> ComposeResult:
        yield Input(placeholder='Absolute path...')
    
    def on_key(self, event: Key):
        if event.key == 'escape':
            self.dismiss(None)
            return
        
        if event.key == 'enter':
            self.dismiss(self.query_one(Input).value)
            return
