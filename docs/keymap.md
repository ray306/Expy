http://pyglet.readthedocs.io/en/pyglet-1.2-maintenance/programming_guide/keyboard.html

The Latin-1 alphabet is simply the letter itself:
```
key_.A
key_.B
key_.C
...
```

The numeric keys have an underscore to make them valid identifiers:
```
key_._1
key_._2
key_._3
...
```
Various control and directional keys are identified by name:
```
key_.ENTER or key_.RETURN
key_.SPACE
key_.BACKSPACE
key_.DELETE
key_.MINUS
key_.EQUAL
key_.BACKSLASH

key_.LEFT
key_.RIGHT
key_.UP
key_.DOWN
key_.HOME
key_.END
key_.PAGEUP
key_.PAGEDOWN

key_.F1
key_.F2
...
```
Keys on the number pad have separate symbols:
```
key_.NUM_1
key_.NUM_2
...
key_.NUM_EQUAL
key_.NUM_DIVIDE
key_.NUM_MULTIPLY
key_.NUM_SUBTRACT
key_.NUM_ADD
key_.NUM_DECIMAL
key_.NUM_ENTER
```

Some modifier keys have separate symbols for their left and right sides (however they cannot all be distinguished on all platforms, including Mac OS X):
```
key_.LCTRL
key_.RCTRL
key_.LSHIFT
key_.RSHIFT
...
```
Key symbols are independent of any modifiers being held down. For example, lower-case and upper-case letters both generate the A symbol. This is also true of the number keypad.