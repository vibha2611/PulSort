# Pulsar-Search
This repository contains programs that optimize the search for pulsars among graphs containing pulsar signals, radio frequency interference and noise. 

chi-squared-filter.py filters out up to 80% of the noise in the data, based on chi-squared (NOT reduced chi-squared) and dispersion measure (DM) values for each plot. This serves as an initial filter.
Files ending in crop.py crop out the phase-subband subplot and pulses of best profile subplot from the graph. These are then fed into the artificial neural network and assigned a score on a scale of 1-3. The plots scored 3 are 95% likely to be a pulsar.

Note: At the time of this commit, this code is especially useful to PRESTO-generated plots and Pulsar Search Collaboratory (PSC) members. chi-squared-filter.py, for example, includes login and data download automation. 

The repo will be updated with the neural network component soon.

As of November 2019, the latest Python release with which TensorFlow is compatible is Python 3.7 64-bit. Download this release here: https://www.python.org/downloads/release/python-375/ if you are not using it already.

A brief description of each of the files in this repo:

initialise.py installs required dependencies and sets up directories into which images will be loaded and classified. Run this program first.

chi-squared-filter.py identifies the most promising plots from all of the plots iterated through.

getplots.py is in development. It will download plots returned by chi-squared-filter.py onto the local system.

phase-subband-crop.py crops out the phase-subband section of the pulsar graph. PSC members (GBT data users) should enter 1 when prompted; GBNCC users enter 2. 

pulse-profile-crop.py crops out the pulses of best profile section. Again, PSC members enter 1 and GBNCC users enter 2.

