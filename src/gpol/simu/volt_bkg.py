import pathlib
import re
from logging import getLogger
import logging

import submitit
import numpy as np

from proto.simu_dc2.simu_bkg import SimuBackground

out_dir = "/sps/grand/simu/dc2_polar/v2/"

def do_simu(pn_efield):
    logger = getLogger(__name__)
    TPL_FMT_LOGGER = "%(asctime)s.%(msecs)03d %(levelname)5s [%(name)s %(lineno)d] %(message)s"
    #datefmt="%d %H:%M:%S"
    datefmt="%H:%M:%S"
    logging.basicConfig(level=logging.INFO, format=TPL_FMT_LOGGER, datefmt=datefmt)
    sbkg = SimuBackground(pn_efield)
    sbkg.out_dir = out_dir
    sbkg.simu.params["fact_padding"] = 2.0
    sbkg.set_out_sampling_size(4, 1024)
    if False:
        sbkg.prefix = "volt-bgk-90_"
        sbkg.gen_polar_angle = np.deg2rad(90)
    else:
        sbkg.prefix = "volt-bgk-rnd_"
        sbkg.gen_polar_angle = "rand"
    sbkg.process_all_events_parallel_chunk(0, -1, 10)




pattern = re.compile(r"^efield")
l_efield = []
rep = pathlib.Path(out_dir)

for m_f in rep.iterdir():
    print(m_f)
    if m_f.is_file() and pattern.search(m_f.name):
        l_efield.append(str(m_f.absolute()))
            

print(l_efield)
print(len(l_efield))

executor = submitit.AutoExecutor(out_dir+"slurm_logs")
executor.update_parameters(cpus_per_task=4,timeout_min=10, nodes=1,slurm_mem="10GB")
executor.update_parameters(slurm_array_parallelism=20)
jobs = executor.map_array(do_simu, l_efield)
print(jobs)