from pathlib import Path
from typing import Iterable
from textual.widgets import DirectoryTree


class FilteredDirectoryTree(DirectoryTree):
    show_root = False
    show_guides = False
    guide_depth = 2
    ignore_files = ['.git']

    def filter_paths(self, paths: Iterable[Path]) -> Iterable[Path]:
        return [path for path in paths if path.name not in self.ignore_files]
