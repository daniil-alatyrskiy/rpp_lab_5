import os


class DirectoryScanner:
    """
    This class helps to work with directories
    """
    def __init__(self, path):
        self.__setattr__('path', path)
        self._files = None

    def __setattr__(self, name, value):
        if name == 'path':
            if not os.path.isdir(value):
                raise ValueError(f"Некорректная директория: {value}")
            object.__setattr__(self, name, value)
            self._files = None
        else:
            object.__setattr__(self, name, value)

    def __iter__(self):
        self._files = os.listdir(self.path)
        self._index = 0
        return self

    def __next__(self):
        while self._index < len(self._files):
            filename = self._files[self._index]
            self._index += 1
            full = os.path.join(self.path, filename)
            if os.path.isfile(full):
                return filename
        raise StopIteration

    def count_files(self):
        return sum(1 for _ in self)

    def __repr__(self):
        return f"<DirectoryScanner path='{self.path}'>"
