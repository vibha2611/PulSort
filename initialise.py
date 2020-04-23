import os, subprocess, sys

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

install('tensorflow')
install('Keras')
install('opencv-python')
install('scipy')
install('Pillow')
install('matplotlib')
install('numpy')
install('pandas')
install('selenium')

parent=r"C:\Program Files\PulSort"
if not os.path.exists(parent):
    os.makedirs(parent)

children=[r"\phase_subband", r"\pulse_profile"]

for child in children:
        path=parent+child
        if not os.path.exists(path):
            os.makedirs(path)
