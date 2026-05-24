from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, TabbedContent


class Tidle(App):
    DEFAULT_CSS = '''
    #nav {
        width: 2fr;
    }

    #code-container {
        width: 8fr;
        height: 100%;
    }

    .code:focus {
        border: none;
    }
    '''

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Horizontal():
            yield Vertical(id='nav')
            yield TabbedContent(id='code-container')
        yield Footer()


if __name__ == '__main__':
    Tidle().run()
