"""
Created on 7 oct. 2025

@author: jcolley
"""

import numpy as np
import matplotlib.pyplot as plt


from rshower.simu.gal_resp import GalacticRespDetectorGenerator

from gpol import get_path_gp300


class GalacticRespGP300(GalacticRespDetectorGenerator):
    def __init__(self):
        pn_fmodel = get_path_gp300()
        pn_tf_elec = pn_fmodel / "TF_RF_Chain_DC2.1rc.npy"
        pn_asd_galactic = pn_fmodel / "ASD_galaxy_ant_HFSS.npy"
        super().__init__(pn_tf_elec, pn_asd_galactic)


def do_sigma_galactic():
    from rshower.basis.traces_event import Handling3dTraces

    size_out = 1024
    fs_mhz = 500
    nb_du = 1000
    gresp = GalacticRespGP300()
    gresp.set_paramters_simu(fs_mhz, size_out)
    sigma_lst = np.zeros((24, 3), dtype=np.float32)
    for lst in range(24):
        evt = gresp.get_galactic_event(nb_du, lst)
        assert isinstance(evt, Handling3dTraces)
        # for ADU
        # evt.to_digit(True, np.float64)
        traces = evt.traces
        sigma_lst[lst] = np.std(traces[:, :, -100:], axis=-1).mean(axis=0)
    # to mV
    sigma_lst /= 1000
    plt.figure()
    plt.title("Sigma galactic GP300 response simulation\n1000 traces by point")
    plt.plot(sigma_lst[:, 0], label="NS", color="k")
    plt.plot(sigma_lst[:, 1], label="WE", color="y")
    plt.plot(sigma_lst[:, 2], label="Up", color="b")
    plt.grid()
    plt.xlabel("Local sideral time [h]")
    # plt.ylabel(r'${\mu V}^2$')
    # plt.ylabel(r'ADU')
    plt.ylabel(r"mV")
    plt.legend()


if __name__ == "__main__":
    do_sigma_galactic()
    plt.show()
