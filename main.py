from textual import on
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive
from textual.widgets import DirectoryTree, Header, Footer, TabbedContent

from widgets.directory_tree_filtered import FilteredDirectoryTree
from widgets.file import File


class Tidle(App):
    CSS_PATH = 'styles/app.tcss'
    BINDINGS = [
        Binding('ctrl+r', 'select_folder', 'Selecionar diretórios', show=True, key_display='ctrl+r'),
        Binding('ctrl+w', 'close_file', 'Fechar arquivo', show=True, key_display='ctrl+w')
    ]
    theme = 'dracula' # type: ignore

    directory = reactive('./')

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Horizontal():
            yield Vertical(id='nav')
            yield TabbedContent(id='code-container')
        yield Footer()
    
    def on_mount(self):
        self.render_directory()
    
    def render_directory(self):
        if self.directory is not None:
            nav = self.query_one('#nav')
            nav.remove_children()
            nav.mount(FilteredDirectoryTree(self.directory))
    
    def action_select_folder(self):
        self.notify('Opa!')
    
    def action_close_file(self):
        tabbed_content = self.query_one('#code-container', TabbedContent)
        current_pane = tabbed_content.active_pane
        if current_pane:
            tabbed_content.remove_pane(current_pane.id) # type: ignore
    
    @on(DirectoryTree.FileSelected)
    def handle_file_selected(self, event: DirectoryTree.FileSelected):
        try:
            with open(event.path, encoding='utf-8') as f:
                content = f.read()
                self.__open_new_file(content, event.path.name)
        except:
            self.notify(f'O correu um erro ao abrir o arquivo {event.path.name}', severity='error')
        
    def __open_new_file(self, content: str, title: str):
        tabbed_content = self.query_one('#code-container', TabbedContent)
        try:
            tabbed_content.get_pane(title.replace(r'.', ''))
            return
        except:
            pass

        file_tab = File(content=content, title=title)
        tabbed_content.add_pane(file_tab)


if __name__ == '__main__':
    Tidle().run()
