from VASP_FILE import VASP_FILE

class POSCAR(VASP_FILE):
    """docstring for OUTCAR"""

    def __init__(self, filename, filepath=None):
        super().__init__(filename, filepath=filepath)

        self.name = self.filelines[0]
        self.lattice_constant = self.filelines[1]
        self.lattice_a = [float(x) for x in self.filelines[2].split()]
        self.lattice_b = [float(x) for x in self.filelines[3].split()]
        self.lattice_c = [float(x) for x in self.filelines[4].split()]
        self.atom_names = self.filelines[5].split()
        self.atom_counts = [int(x) for x in self.filelines[6].split()]
        self.number_of_atoms = sum(self.atom_counts)
        self.coordinate_type = None
        #print("atom count: ", self.number_of_atoms)

        self.coord_start_line = False
        for n, line in enumerate(self.filelines):

            if not self.coord_start_line:
                if (line.__contains__("Direct") or line.__contains__("Cartesian")) and n != 0:
                    self.coord_start_line = n + 1
                    self.coordinate_type = line

        assert self.coord_start_line != None

        self.atom_info = [0]*self.number_of_atoms

        counter = 0
        for name, count in zip(self.atom_names, self.atom_counts):
            for c in range(count):
                line_number = counter + self.coord_start_line + c
                line = self.filelines[line_number]
                self.atom_info[c + counter] = {"atom_type": name, "atom_number": c + counter,
                                               "line_number": line_number,
                                               "x": float(line.split()[0]),
                                               "y": float(line.split()[1]),
                                               "z": float(line.split()[2])}
            counter += count



