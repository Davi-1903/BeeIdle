from pathlib import Path
from typing import Iterable
from textual.widgets import DirectoryTree


class FilteredDirectoryTree(DirectoryTree):
    CSS_PATH = '../style/directory_tree_filtered.tcss'
    show_root = False
    show_guides = False
    guide_depth = 2
    
    def filter_paths(self, paths: Iterable[Path]) -> Iterable[Path]:
        return [path for path in paths if path.name != '.git']
