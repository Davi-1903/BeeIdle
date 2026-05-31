from pathlib import Path
from textual.app import ComposeResult
from textual.events import Key
from textual.screen import ModalScreen
from textual.widgets import Input, RadioSet, RadioButton


class OpenDirectoryModal(ModalScreen):
    AUTO_FOCUS = '#path-input'

    def __init__(self, path: Path | None):
        super().__init__()
        self.path = path if path is not None else Path('/')
    
    def compose(self) -> ComposeResult:
        yield Input(id='path-input', placeholder='Caminho absoluto...')
        yield RadioSet(*self.__get_directories(), id='directories-list')
    
    def on_key(self, event: Key):
        if event.key == 'escape':
            self.dismiss(None)
            return
        
        raw_path = self.query_one(Input).value
        radio_set = self.query_one(RadioSet)
        radio_value = radio_set.pressed_button
        if raw_path != '':
            path = Path(raw_path)
        elif radio_value is not None:
            path = Path(str(radio_value.label))
        else:
            path = self.path
        
        if event.key == 'enter':
            self.dismiss(path)
            return
    
    def __get_directories(self) -> list[RadioButton]:
        directories = [RadioButton(str(self.path.absolute().parent))]
        for path in self.path.glob('./*'):
            if path.name != '.git' and path.is_dir():
                directories.append(RadioButton(str(path)))
        return directories
