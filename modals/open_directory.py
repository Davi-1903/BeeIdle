from textual.app import ComposeResult
from textual.events import Key
from textual.screen import ModalScreen
from textual.widgets import Input


class OpenDirectoryModal(ModalScreen):
    AUTO_FOCUS = '#path-input'
    
    def compose(self) -> ComposeResult:
        yield Input(id='path-input', placeholder='Caminho absoluto...')
    
    def on_key(self, event: Key):
        if event.key == 'escape':
            self.dismiss(None)
            return
        
        path = self.query_one(Input).value
        if (path in ['./', '.'] or 'tidle' in path.lower()) and event.key == 'enter':
            self.notify('Diretório probido', severity='warning')
            return

        if event.key == 'enter':
            self.dismiss(path)
            return
