import os
from VASP_JOB import *
from OUTCAR_HELPER import *

vasp_job = VASP_JOB(r"Data\Adsorption1a")
assert vasp_job.get_EDIFFG() == -0.01
vasp_job.print_forces_above_EDIFFG()