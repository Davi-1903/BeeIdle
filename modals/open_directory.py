from textual.app import ComposeResult
from textual.events import Key
from textual.screen import ModalScreen
from textual.widgets import Input


class OpenDirectoryModal(ModalScreen):    
    def compose(self) -> ComposeResult:
        yield Input(placeholder='Caminho absoluto...')
    
    def on_key(self, event: Key):
        path = self.query_one(Input).value
        if path == './':
            self.notify('Caminho inválido', severity='warning')
            return
        
        if event.key == 'escape':
            self.dismiss(None)
            return
        
        if event.key == 'enter':
            self.dismiss(path)
            return
