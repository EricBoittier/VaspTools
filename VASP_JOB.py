import os
from OUTCAR_HELPER import *
from INCAR_HELPER import *
from POSCAR_HELPER import *
import sys

class VASP_JOB(object):
    """docstring for VASP_JOB"""

    def __init__(self, directory):
        super(VASP_JOB, self).__init__()
        self.directory = directory

        self.files = os.listdir(self.directory)

        assert "POSCAR" in self.files
        self.POSCAR = POSCAR("POSCAR", filepath=self.directory)
        self.atom_info = self.POSCAR.atom_info

        assert "INCAR" in self.files
        self.INCAR = INCAR("INCAR", filepath=self.directory)

        self.OUTCAR = None
        if "OUTCAR" in self.files:
            self.OUTCAR = OUTCAR("OUTCAR", filepath=self.directory)
            self.forces_above_EDIFFG = self.set_forces_above_EDIFFG()

    def get_EDIFFG(self):
        return self.INCAR.EDIFFG

    def get_atom_info(self):
        return self.POSCAR.atom_info

    def get_forces_above_EDIFFG(self, EDIFFG=None):
        return self.forces_above_EDIFFG

    def print_forces_above_EDIFFG(self, EDIFFG=None):
        for force in self.forces_above_EDIFFG:
            atom_number = force[0]
            s = "Atom {}, {}(".format(str(atom_number).rjust(4), self.atom_info[atom_number]["atom_type"].ljust(3))
            for number, F in enumerate(force[1:]):
                s += "{}: {}".format(F[0], F[1])
                if number+1 < len(force[1:]):
                    s += ", "
            print(s+")")

    def set_forces_above_EDIFFG(self, EDIFFG=None):
        if self.OUTCAR == None:
            print("Sorry, no OUTCAR file found, no forces to report")
            return None

        if EDIFFG == None:
            EDIFFG = self.get_EDIFFG()
        if EDIFFG == None:
            print("Sorry, no EDIFFG found, no forces to report")
            return None

        bad_forces = []

        for number, forces in enumerate(self.OUTCAR.forces):
            bad_force = [number]
            append = False
            for force in ["Fx", "Fy", "Fz"]:
                if abs(EDIFFG) < abs(forces[force]):
                    bad_force.append([force, forces[force]])
                    append = True
            if append:
                bad_forces.append(bad_force)

        return bad_forces

if __name__ == '__main__':
    current_dir = os.getcwd()
    vasp_job = VASP_JOB(current_dir)

    if sys.argv[0] == "bad_forces":
        vasp_job.print_forces_above_EDIFFG()







