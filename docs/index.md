# Overview

[![PyPI Version][pypi-v-image]][pypi-v-link]

[pypi-v-image]: https://img.shields.io/pypi/v/expy.png
[pypi-v-link]: https://pypi.python.org/pypi/expy

Expy is an simple-yet-powerful experiment framework builder for cognitive tasks. It's aimed at setting up an experiment without struggling with the manual production of stimuli, data loading and storing, or the other time-consuming works.

**Highlights**:

- Various stimuli modules (not need for preparation of massive stimuli pictures).
- Various procedure-controlling modules (instruction, tip, rest-stage, etc.)
- Convenient for stimuli loading and responses recording.
- Convenient for getting participants' response data (from keyboard, mouse, or joystick).
- Sending triggers easily.
- Easy pause or exit from the program.

**Limitation**:

- Not good at drawing complex shape (e.g.,grating) as stimuli (however, you could draw them as loaded pictures).

---
## Documentation
See http://expy.readthedocs.io/en/latest/ for introduction, tutorials, and reference manual.

---
# Installation instructions

The simplest way to install Expy is through the Python Package Index (PyPI), which ensures that all required dependencies are established. This can be achieved by executing the following command:

```
pip install expy
```
or:
```
sudo pip install expy
```

If you have Anaconda installed and meet compile issue when install resampy, please run the following command:
```
conda install -c conda-forge resampy
```

If you are using Mac, please run the following commands in your terminal:
```
xcode-select --install
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install portaudio
```


The command of getting update:
```
pip install --upgrade expy --no-deps
```
or:
```
sudo pip install --upgrade expy --no-deps
```

If you want to play video in Expy, you should install AVbin (https://avbin.github.io/AVbin/Download.html)
If you want to play a lot of media formats (e.g. mp3) in Expy, you installed FFmpeg (https://ffmpeg.org/download.html)


### *Required Dependencies*

- numpy
- pandas
- scipy
- pyglet
- pyaudio
- librosa
- pyserial