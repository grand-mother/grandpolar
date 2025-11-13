# Galactic Amplitude Spectrum Density (ASD) model

From file ASD_galaxy_ant_HFSS.npy

How reproduce this file ?

With function [save_asd_galaxy()](https://github.com/grand-mother/grand/blob/0a9de5b4e803078c8516b3b1be608bc274b8e50c/grand/sim/noise/galatic_ant_asd.py#L151) in GRANDLIB 

![psd gal](/docs/images/psd_gal_lst1.png)

# Global RF chain version DC2.1rc

From file TF_RF_Chain_DC2.1rc.npy

How reproduce this file ?

With script [extract_rf_chain.py](https://github.com/grand-mother/grand/blob/dev/scripts/extract_rf_chain.py) in GRANDLIB 

![rf chain](/docs/images/RF_chain_DC2.1rc.png)


# GP300 galactic response

Using both files, we can defined GP300 galactic response and compute for example sigma ADU for each direction and each hour of local sideral time.

![gal resp](/docs/images/sigma_galactic_ADU.png)
