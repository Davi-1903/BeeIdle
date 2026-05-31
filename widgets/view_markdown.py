from textual.app import ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import MarkdownViewer, TabPane


class ViewMarkDown(TabPane):
    def __init__(self, content: str, title: str, **kwargs) -> None:
        super().__init__(title=f'view mode: {title}', id=f'view-{title.replace(".", "")}', **kwargs)
        self.content = content
        self.original_title = title
        self.is_diferent = False
    
    def compose(self) -> ComposeResult:
        with ScrollableContainer():
            yield MarkdownViewer(
                markdown=self.content,
                name=self.original_title,
                open_links=True,
            )
