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
        #print("atom count: ", self.number_of_atoms)

        self.atom_info = [0]*self.number_of_atoms

        counter = 0
        for name, count in zip(self.atom_names, self.atom_counts):
            for c in range(count):
                self.atom_info[c + counter] = {"atom_type": name}
            counter += count


