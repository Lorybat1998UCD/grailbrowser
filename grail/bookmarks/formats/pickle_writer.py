"""Writer for Grail's pickled bookmarks."""

__version__ = '$Revision: 1.4 $'


from .. import BookmarkWriter                        # from parent
import pickle


class Writer(BookmarkWriter):
    HEADER_STRING = "# GRAIL-Bookmark-file-4 (cache pickle format)\n"
    _filetype = "pickle"

    __filename = ""
    __mtime = 0

    def __init__(self, root):
        self.__root = root

    def set_original_filename(self, filename):
        self.__filename = filename

    def set_original_mtime(self, mtime):
        self.__mtime = mtime

    def write_tree(self, fp):
        try:
            fp.write(self.HEADER_STRING)
            fp.write(self.__filename + "\n")
            fp.write("{}\n".format(self.__mtime))
            pickle.dump(self.__root, fp, 1)
        finally:
            fp.close()