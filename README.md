<h1> PulSort</h1>
<h2>Introduction</h2>
PulSort is a machine learning algorithm employing neural networks written to distinguish pulsar signals from noise and radio frequency interference data. The program filters (based chi-squared test values and dispersion measure) and downloads plots generated by the software PRESTO. It then crops out two sections (the pulses of best profile section and the phase vs. frequency section) of the plot, which are fed into two separate convolutional neural networks. These networks were trained on over 5000 pieces of manually classifed data and have been 100% successful in identifying known pulsars. This code was written using Keras in Python 3.7.

<h2>Instructions</h2>
<h3>Short version</h3>
1) Install Python.<br>
2) Run <tt>initialise.py</tt>.<br>
3) Run <tt>pulsort_combined.py</tt>. <br>
That's all!<br>
<b>Potential errors/questions</b>:<br>
Q1)<b> What value do I enter when prompted to enter a search ID?</b><br>
The URL of a PSC dataset has a sequence of numbers at the end. This sequence should be entered as the search ID. This is <i>not</i> the same as the dataset number.<br>
Q2) <b>What's a driver? Where do I get one?</b><br>
A driver (webdriver) can remotely control a web interface. You should be able to download a specific driver for your browser if you search something like "Chromedriver" online.<br>
Q3) <b>Why can't I log in?</b><br>
Unfortunately I haven't yet finished writing code to take your PSC username and password as inputs, so you will have to modify this directly in the program code. Substitute where it says <tt>your username</tt> and <tt>your password</tt> with your username and password.
<h2>Longer guide</h2>
<h3>filter_get_plots.py</h3>
This script uses Selenium to log in to the Pulsar Search Collaboratory database and download plots that pass a prescribed filter based on their values for dispersion measure (DM) and the chi-squared test. If no upper limit for DM is specified the default cutoff value is 400. Lowering the minimum chi-squared value allows a higher number of plots to pass through the filter. I would recommend using a value of 1.5 or above for this parameter.

<h4>Future focus areas and limitations</h4>
1. Security. Will probably incorporate some form of password concealment during entry and make the login process more user-friendly. <br>
2. Optimum value for chi-square is unknown.
