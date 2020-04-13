# PulSort
This repository contains programs that optimize the search for pulsars among graphs containing pulsar signals, radio frequency interference and noise. 

chi-squared-filter.py filters out up to 80% of the noise in the data, based on chi-squared (NOT reduced chi-squared) and dispersion measure (DM) values for each plot. This serves as an initial filter. As a preliminary measure, I have assigned the default upper limit DM as 400. In future, I will link this component to a galactic DM model.
crop.py crops out the phase-subband subplot and pulses of best profile subplot from the graph. These are then fed into the artificial neural network.

Note: At the time of this commit, this code is especially useful to PRESTO-generated plots and Pulsar Search Collaboratory (PSC) members. chi-squared-filter.py, for example, includes login and data download automation. 

<b>The complete code will be available by early May.</b>

As of November 2019, the latest Python release with which TensorFlow is compatible is Python 3.7 64-bit. Download this release here: https://www.python.org/downloads/release/python-375/ if you are not using it already.

A brief description of each of the files in this repo:

initialise.py installs required dependencies and sets up directories into which images will be loaded and classified. Run this program first.

chi-squared-filter.py identifies the most promising plots from all of the plots iterated through.

getplots.py is in development. It will download plots returned by dm-chi-square-filter.py onto the local system.

crop.py crops out the pulses of best profile and phase-subband sections of the plot, which are concatenated and used with the ANN model. PSC members enter 1 and GBNCC users enter 2 to select the correct pixel combination for cropping the phase-subband section of their respective plots.

