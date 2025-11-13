import matplotlib.pyplot as plt

from rshower.io.rf_fmt import plot_global_rf_chain, read_TF_numpy_fmt


plot_global_rf_chain("TF_RF_Chain_DC2.1rc.npy", read_TF_numpy_fmt,"RF chain DC2.1rc")

plt.show()