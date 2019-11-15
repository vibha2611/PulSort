# Pulsar-Search
This repository contains programs that optimize the search for pulsars among graphs containing pulsar signals, radio frequency interference and noise. 

chi-squared-filter.py filters out up to 80% of the noise in the data, based on chi-squared (NOT reduced chi-squared) and dispersion measure (DM) values for each plot. This serves as an initial filter.
Files ending in crop.py crop out the phase-subband subplot and pulses of best profile subplot from the graph. These are then fed into the artificial neural network and assigned a score on a scale of 1-3. The plots scored 3 are 95% likely to be a pulsar.

Note: At the time of this commit, this code is especially useful to PRESTO-generated plots and Pulsar Search Collaboratory (PSC) members. chi-squared-filter.py, for example, includes login and data download automation. I am working on adapting this code to other pulsar data, such as FAST and GBNCC data.

The repo will be updated with the neural network component soon.
As of November 2019, TensorFlow is only available for Python 3.7 64-bit. Download this release here: https://www.python.org/downloads/release/python-375/ if you are not using it already.
