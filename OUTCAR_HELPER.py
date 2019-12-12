from VASP_FILE import VASP_FILE

class OUTCAR(VASP_FILE):
    """docstring for OUTCAR"""

    def __init__(self, filename, filepath=None):
        super().__init__(filename, filepath=filepath)


        for number, line in enumerate(self.filelines):
            if line.startswith(" POSITION                                       TOTAL-FORCE (eV/Angst)"):
                self.forces_start_slice = number + 2
            if line.startswith("    total drift: "):
                self.forces_end_slice = number - 2

        self.forces_lines = self.filelines[self.forces_start_slice: self.forces_end_slice+1]
        self.forces = [0]*len(self.forces_lines)

        for number, line in enumerate(self.forces_lines):
            self.forces[number] = {}
            spl = line.split()
            self.forces[number]["x"] = float(spl[0])
            self.forces[number]["y"] = float(spl[1])
            self.forces[number]["z"] = float(spl[2])
            self.forces[number]["Fx"] = float(spl[3])
            self.forces[number]["Fy"] = float(spl[4])
            self.forces[number]["Fz"] = float(spl[5])




