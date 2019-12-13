import os
from VASP_JOB import *
from OUTCAR_HELPER import *
from POSCAR_HELPER import *


def vasp_job_tests():
    vasp_job = VASP_JOB(r"Data\Adsorption1a")
    assert vasp_job.get_EDIFFG() == -0.01
    vasp_job.print_forces_above_EDIFFG()

def poscar_helper_tests():
    poscar = POSCAR("POSCAR", filepath=r"C:\Users\uqeboitt\PycharmProjects\VASP\Data\Matthew\IRC_1\START")
    print(poscar.coordinate_type)

poscar_helper_tests()