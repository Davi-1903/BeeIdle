from pathlib import Path
from textual import on
from textual.app import ComposeResult
from textual.widgets import TabPane, TextArea, Tab


class File(TabPane):
    def __init__(self, content: str, title: str, path: Path, **kwargs) -> None:
        super().__init__(title=title, id=title.replace('.', ''), **kwargs)
        self.path = path
        self.content = content
        self.original_title = title
        self.is_diferent = False

    def compose(self) -> ComposeResult:
        yield TextArea.code_editor(self.content, classes='code', language='python', theme='css', compact=True)

    def save_changes(self):
        if self.is_diferent:
            new_content = self.query_one(TextArea).text
            self.content = new_content
            self.is_diferent = False
            self.change_title(self.is_diferent)
            with open(self.path, 'w', encoding='utf-8') as f:
                f.write(self.content)

    def change_title(self, is_diferent: bool):
        try:
            tab_button = self.screen.query_one(f'#--content-tab-{self.id}', Tab)
            tab_button.label = f'{self.original_title}*' if is_diferent else self.original_title
            tab_button.refresh()
        except Exception:
            pass

    @on(TextArea.Changed)
    def changes(self, event: TextArea.Changed):
        self.is_diferent = event.text_area.text != self.content
        self.change_title(self.is_diferent)
