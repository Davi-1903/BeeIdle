from typing import Callable
from textual.app import ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Static, TabPane, Button


class WelcomePane(TabPane):
    CONTENT = """[bold $primary]
       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠀⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
       ⠀⠀⢀⡀⢻⣷⣦⣄⡀⠀⠀⢰⢶⣬⣿⣶⣾⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀       
       ⠀⠀⠻⣿⣿⣿⣿⣿⣿⣶⣄⠀⢸⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀       
       ⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠙⢿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀       
       ⠀⠈⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠙⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀       
       ⠀⠀⠘⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡈⢻⣿⡇⠀⠀⢠⣤⣀⣀⠀⠀⠀⠀       
       ⠀⠀⠀⠀⠈⠙⠋⢨⣿⡿⢿⣿⣿⣿⣿⣿⣷⡄⢀⣄⡀⠀⠘⣿⠈⠙⢷⣄⠀⠀       
       ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠘⠛⠁⠼⠿⠿⠿⣿⣶⣿⣿⣆⣀⣿⣧⣤⡀⠙⠓⠀       
       ⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣦⣤⣄⣀⣦⣤⣤⣼⣿⣿⣿⣿⣿⠉⠙⢿⣿⡄⠀⠀       
       ⠀⠀⠀⠀⢠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⠻⣿⣄⣀⣸⣿⠃⠀⠀       
       ⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀⠙⣿⠛⢻⣿⠀⠙⠛⠿⠛⠋⠀⠀⠀       
       ⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⢻⣆⠀⢿⣦⡈⠛⠻⠶⣦⠄⠀⠀⠀⠀⠀       
       ⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠈⠁⠀⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀       
       ⠀⠈⠛⠻⠿⠿⠿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀       

██████╗ ███████╗███████╗██╗██████╗ ██╗     ███████╗
██╔══██╗██╔════╝██╔════╝██║██╔══██╗██║     ██╔════╝
██████╔╝█████╗  █████╗  ██║██║  ██║██║     █████╗  
██╔══██╗██╔══╝  ██╔══╝  ██║██║  ██║██║     ██╔══╝  
██████╔╝███████╗███████╗██║██████╔╝███████╗███████╗
╚═════╝ ╚══════╝╚══════╝╚═╝╚═════╝ ╚══════╝╚══════╝[/bold $primary]
"""

    def __init__(self, action_select_folder: Callable):
        super().__init__(title='Welcome to BeeIdle', name='welcome', id='welcome-pane')
        self.action = action_select_folder

    def compose(self) -> ComposeResult:
        with ScrollableContainer():
            yield Static(self.CONTENT)
            yield Button('Open a project', variant='primary')

    def on_button_pressed(self):
        self.action()
