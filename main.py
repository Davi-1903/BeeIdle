from pathlib import Path
from textual import on
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive
from textual.widgets import DirectoryTree, Header, Footer, TabbedContent, Button

from modals.confirm import ConfirmModal
from modals.create_name_file import CreateNameFile
from modals.open_directory import OpenDirectoryModal
from modals.select_directory import SelectDirectory
from widgets.directory_tree_filtered import FilteredDirectoryTree
from widgets.file import File


class Tidle(App):
    CSS_PATH = 'styles/app.tcss'
    BINDINGS = [
        Binding('ctrl+r', 'select_folder', 'Selecionar diretórios', show=True),
        Binding('ctrl+w', 'close_file', 'Fechar arquivo', show=True),
        Binding('ctrl+b', 'toggle_nav', 'Abrir/fechar árvore de arquivos', show=True),
        Binding('ctrl+s', 'save_changes', 'Salvar alterações', show=True)
    ]
    AUTO_FOCUS = ''

    directory = reactive(None)

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Horizontal():
            with Vertical(id='sidebar-container', classes='open'):
                with Horizontal(id='actions-content'):
                    yield Button('Create', id='create-btn', variant='success')
                    yield Button('Delete', id='delete-btn', variant='error')
                with Vertical(id='sidebar-content'):
                    yield Button('Abrir diretório', id='open-directory-btn', variant='primary')
            yield TabbedContent(id='code-container')
        yield Footer()

    def render_directory(self):
        sidebar = self.query_one('#sidebar-content')
        sidebar.remove_children()
        if self.directory is None:
            sidebar.mount(Button('Abrir diretório', id='open-directory-btn', variant='primary'))
        else:
            sidebar.mount(FilteredDirectoryTree(self.directory))

    def open_file(self, content: str, title: str, path: Path):
        tabbed_content = self.query_one('#code-container', TabbedContent)
        try:
            tabbed_content.get_pane(title.replace('.', ''))
            tabbed_content.active = title.replace('.', '')
            return
        except:
            pass

        file_tab = File(content=content, title=title, path=path)
        tabbed_content.add_pane(file_tab)
        tabbed_content.active = title.replace('.', '')
    
    def create_file(self, name_file: str, path: Path):
        if Path(path).joinpath(name_file).exists():
            self.notify(f'O arquivo {name_file} já existe nesse diretório', severity='error')
            return
        
        try:
            with open(Path(path).joinpath(name_file), 'w', encoding='utf-8') as f:
                f.write('')
                self.notify(f'Arquivo {name_file} criado com sucesso')
                self.render_directory()
        except:
            self.notify('Ocorreu um erro ao criar o arquivo', severity='error')

    # ==================================== ACTIONS ====================================
    @on(Button.Pressed, '#open-directory-btn')
    def action_select_folder(self):
        def set_directory(path: str | None):
            if path is not None:
                self.directory = path
                self.render_directory()
        
        self.push_screen(OpenDirectoryModal(), set_directory)
    
    def action_close_file(self):
        tabbed_content = self.query_one('#code-container', TabbedContent)
        current_pane = tabbed_content.active_pane
        if current_pane:
            tabbed_content.remove_pane(current_pane.id) # type: ignore
    
    def action_toggle_nav(self):
        sidebar = self.query_one('#sidebar-container')
        sidebar.toggle_class('open')
    
    def action_save_changes(self):
        tabbed_content = self.query_one('#code-container', TabbedContent)
        current_pane = tabbed_content.active_pane
        if isinstance(current_pane, File):
            current_pane.save_changes()
    
    # ==================================== EVENTS ====================================
    @on(DirectoryTree.FileSelected)
    def handle_file_selected(self, event: DirectoryTree.FileSelected):
        try:
            with open(event.path, encoding='utf-8') as f:
                content = f.read()
                self.open_file(content, event.path.name, event.path)
        except:
            self.notify(f'O correu um erro ao abrir o arquivo {event.path.name}', severity='error')
    
    @on(Button.Pressed, '#create-btn')
    def handle_create_file(self):
        def create_file(path: Path | None):
            if path is not None:
                self.__handle_create_file_get_name(path)
        
        self.query_one('#create-btn').blur()
        self.push_screen(SelectDirectory(), create_file)
    
    def __handle_create_file_get_name(self, path: Path):
        def get_name(name: str | None):
            if name is not None:
                self.create_file(name, path)
        
        self.push_screen(CreateNameFile(), get_name)
    
    @on(Button.Pressed, '#delete-btn')
    def handle_delete_file(self):
        def confirm_delete(confirmed: bool | None, current_pane: File, tabbed_content: TabbedContent):
            if confirmed is not None:
                self.__handle_delete_file_confirm(confirmed, current_pane, tabbed_content)
        
        tabbed_content = self.query_one('#code-container', TabbedContent)
        current_pane = tabbed_content.active_pane
        if isinstance(current_pane, File):
            self.push_screen(ConfirmModal('Tem certeza que deseja deletar esse arquivo?'), lambda result: confirm_delete(result, current_pane, tabbed_content))
    
    def __handle_delete_file_confirm(self, confirmed: bool, current_pane: File | None = None, tabbed_content: TabbedContent | None = None):
        if not confirmed or current_pane is None or tabbed_content is None:
            return
        
        try:
            Path(current_pane.path).unlink()
            tabbed_content.remove_pane(current_pane.id) # type: ignore
            self.notify(f'Arquivo {current_pane._title} deletado com sucesso')
            self.render_directory()
        except:
            self.notify(f'Ocorreu um erro ao deletar o arquivo {current_pane._title}', severity='error')


if __name__ == '__main__':
    Tidle().run()
