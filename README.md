# circutpython_sim

Import `Pixel` from sim and use it as you would `neopixel.NeoPixel()`, except `Pixel()` only need the number of pixels to draw.
For example to create 22 pixels:

```python
from sim import Pixel
pixels = Pixels(22)
```
See `main.py` for an example.

_Note: You have to control + c from the running terminal to kill the process since I don't check for quit events from the window's x_