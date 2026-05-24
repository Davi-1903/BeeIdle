from textual.app import App, ComposeResult
from textual.widgets import Header, Footer


class Tidle(App):
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()


if __name__ == '__main__':
    Tidle().run()
