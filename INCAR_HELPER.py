from VASP_FILE import VASP_FILE

class INCAR(VASP_FILE):
    """docstring for INCAR"""

    def __init__(self, filename, filepath=None):
        super().__init__(filename, filepath=filepath)

        self.EDIFFG = None
        for line in self.filelines:
            if line.__contains__("EDIFFG"):
                self.EDIFFG = float(line.split("=")[1].split()[0])

        assert self.EDIFFG is not None
