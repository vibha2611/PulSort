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

parents=[r"C:\ProgramFiles\Phase Subband", r"C:\ProgramFiles\Pulse Profile"]
for path in parents:
    if not os.path.exists(path):
        os.makedirs(path)

children=[r"\Pulsar", r"\Not a pulsar"]

for child in children:
    for parent in parents:
        path=parent+child
        if not os.path.exists(path):
            os.makedirs(path)
