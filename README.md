# PulSort
#TODO directory names, update pulsort_combined, references.

## Introduction
PulSort uses two convolutional neural networks (CNNs) to predict whether a given PRESTO plot exhibits a pulsar signal or not. PulSort was trained on ~11000 images from the Pulsar Search Collaboratory (PSC) database, which contains Green Bank Telescope (GBT) observations at time intervals of 8.192 x 10<sup>-5</sup> and in observing frequency channels of 0.02 MHz<sup>1</sup>. Multiple trials were run with both CNNs to arrive at suitable hyperparameters for the models. 

<sup>1</sup> Lynch, Ryan. From the Telescope to the Collaboratory: Processing GBT Data. http://pulsarsearchcollaboratory.com/wp-content/uploads/2013/12/presto_guide.pdf

## Files on this repo
``initialise.py``: Installs packages required to run PulSort and creates a folder structure on the local machine.

``filter_get_plots.py``: This script logs into the PSC database and downloads prepfold plots that pass the dispersion measure (DM) and chi-squared filter. The use of the Selenium package allows the user to observe the iteration through plots visually. The DM/chi-squared filter usually rejects 80%-90% of the data it looks at.

``ra_finder.py``: PSC datasets are organised by right ascension (RA) with variable declination (Dec). This script takes advantage of this fact to return the RA values that have the most plots falling within a particular DM range (default is 2-400). *Deprecated with the release of* ``filter_get_plots.py``.

``crop.py``: Crops the pulse profile and frequency vs. phase subplots from the downloaded .pfd files.

``predict.py``: Returns a prediction (pulsar, not a pulsar, harmonic, etc.) for a given subplot. 

``prep_train_data.py``: A script to reshape cropped sections into a standard size for input to the neural networks and save features and labels in binary files.

``pulsort_combined.py``: Script combining ``filter_get_plots.py``, ``crop.py`` and ``predict.py``. 

``/Augmentation/brightening_images_script.py``: Given an image, generates 3 randomly brightened/darkened images.

``/Augmentation/flip.ps1``: Powershell script to flip images. 

``/Augmentation/flip.py``: Python script to flip images.

``/Models/pulse_profile_final``: Final pulse profile model.

``/Models/frequency_phase_final``: Final frequency vs. phase model.

``data.md``: Link to Google Drive folder containing train and test datasets.

## Notes
If you find any bugs, please submit an issue report.
September 2020 edit: The PSC database is undergoing updates, so ``filter_get_plots.py`` will not work. I may or may not maintain this code post the update.
