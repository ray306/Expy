# Overview

[![PyPI Version][pypi-v-image]][pypi-v-link]

[pypi-v-image]: https://img.shields.io/pypi/v/expy.png
[pypi-v-link]: https://pypi.python.org/pypi/expy

Expy is an easy-yet-powerful experiment framework builder for psychology. It's aimed at setting up an experiment without struggling with the manual production of stimuli, data loading and storing, or the other time-consuming works, by using various module functions.
Expy is designed for psycholinguistic experiments, but it's also suitable for any other experiments.

**Advantanges**:

- Various stimuli modules (not need for preparation of massive stimuli pictures).
- Various procedure-controlling modules (instruction, alert, rest-stage, etc.)
- Convenient for stimuli loading and responses recording.
- Getting participants' response data (from keyboard, mouse, or joystick) by one function.
- Sending triggers easily.
- Easy pause or exit from the program.

**Disadvantages**:

- Not good at drawing complex shape (e.g.,grating) as stimuli (however, you could draw them as loaded pictures).
- Not good at video playing.

---
## Documentation
See http://expy.readthedocs.io/en/latest/ for introduction, tutorials, and reference manual.

---
# Installation instructions

Expy has been tested on Python3.5 64bit.
(Current it might be unfit for older versions like Python2.7. But since Python2 will become obsolete in the years to come, why not drop it anyaway and take Python3 instead?)

The simplest way to install Expy is through the Python Package Index (PyPI), which ensures that all required dependencies are established. This can be achieved by executing the following command:

```
pip install expy
```
or:
```
sudo pip install expy
```

The command of getting update:
```
pip install --upgrade expy
```
or:
```
sudo pip install --upgrade expy
```

###*Required Dependencies*

- numpy
- pandas
- scipy
- pygame
- pyaudio
- wave
- pyserial