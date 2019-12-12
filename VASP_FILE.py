import os


class VASP_FILE(object):
    """docstring for INCAR"""

    def __init__(self, filename, filepath=None):
        self.filepath = filepath
        self.filename = filename

        #  Load the file safely
        self.filelines = None
        try:
            if self.filepath:
                self.filelines = open(os.path.join(filepath, filename)).readlines()
            else:
                self.filelines = open(filename).readlines()
        except IOError as err:
            print("OS error: {0}".format(err))
            raise Exception

        assert self.filelines is not None