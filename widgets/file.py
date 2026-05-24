from textual.app import ComposeResult
from textual.widgets import TabPane, TextArea


class File(TabPane):
    def __init__(self, content: str, title: str = "Untitled", **kwargs) -> None:
        super().__init__(title=title, id=title.replace(r'.', ''), **kwargs)
        self.content = content
    
    def compose(self) -> ComposeResult:
        yield TextArea.code_editor(
            self.content,
            language='python',
            theme='css',
            compact=True
        )
