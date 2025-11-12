# grandpolar
DC2 proposition of reconstruction based on polarization of air shower EField

## Installation

* git clone https://github.com/grand-mother/grandpolar.git
* python -m pip install git+https://github.com/luckyjim/RadioShower.git@0.1.0
* cd grandpol
* source gpol_init.sh

## Data dc2_pol

on CCIN2P3:
* /sps/grand/simu/dc2_pol/v2

from DC2 simulation:
* /sps/grand/DC2Training/ZHAireS


### Efield

`efield_xx_yyyy.asdf` : Efield triggered
 * sampling at 2000 MHz
 * only polarized component
 * polar angle estimated

### Antenna voltage air shower

* `volt-ash_xx_yyyy.asdf` : GP300 response to Efield `efield_xx_yyyy.asdf`
    * sampling 500MHz
    * no noise

### Antenna voltage background 

GP300 response to Efield `efield_xx_yyyy.asdf` by changing the polarization angle and remove Cerenkov ring by 1/$r^2$ amplitude decrease.
 
* `volt-bkg-90_xx_yyyy.asdf` : by adding 90 to the polarization 

* `volt-bkg-rnd_xx_yyyy.asdf` : with random polarization angle 

## Models

#### Polar angle

#### Relative amplitude of the voltage along the direction

#### PSD Efield model with 4 parameters

#### PSD Efield along the direction and amplitude of the voltage

## Polar trigger

## Polar Wiener reconstruction of Efield
