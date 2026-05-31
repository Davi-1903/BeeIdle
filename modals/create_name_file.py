from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.events import Key
from textual.widgets import Input


class CreateNameFile(ModalScreen):
    AUTO_FOCUS = '#file-input'
    
    def compose(self) -> ComposeResult:
        yield Input(id='file-input', placeholder='Nome do arquivo...')
    
    def on_key(self, event: Key):
        if event.key == 'escape':
            self.dismiss(None)
            return
        
        path = self.query_one(Input).value
        if event.key == 'enter':
            self.dismiss(path)
