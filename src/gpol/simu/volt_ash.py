'''
Created on 7 oct. 2025

@author: jcolley
'''

import pathlib
import re
from logging import getLogger
import logging

import submitit

from proto.simu_dc2.main_simu import SimuGrand

out_dir = "/sps/grand/simu/dc2_polar/v2/"

def do_simu(pn_efield):
    logger = getLogger(__name__)
    TPL_FMT_LOGGER = "%(asctime)s.%(msecs)03d %(levelname)5s [%(name)s %(lineno)d] %(message)s"
    #datefmt="%d %H:%M:%S"
    datefmt="%H:%M:%S"
    logging.basicConfig(level=logging.INFO, format=TPL_FMT_LOGGER, datefmt=datefmt)
    simu = SimuGrand(pn_efield)
    #simu.out_dir = "/sps/grand/colley/temp/"
    simu.out_dir = out_dir
    simu.set_out_sampling_size(4, 1024)
    simu.process_all_events_parallel_chunk(0, 1000, 10)


def list_directories(path):
    return [p for p in pathlib.Path(path).iterdir() if p.is_dir()]


path_data = "/sps/grand/DC2Training/ZHAireS"
l_data = list_directories(path_data)

pattern = re.compile(r"^efield.*L0")
l_efield = []
for rep in l_data:
    for m_f in rep.iterdir():
        if m_f.is_file() and pattern.search(m_f.name):
            l_efield.append(str(m_f.absolute()))
            break

print(l_efield)
print(len(l_efield))

executor = submitit.AutoExecutor(out_dir+"slurm_logs")
executor.update_parameters(cpus_per_task=4,timeout_min=10, nodes=1,slurm_mem="10GB")
executor.update_parameters(slurm_array_parallelism=20)
jobs = executor.map_array(do_simu, l_efield)
print(jobs)