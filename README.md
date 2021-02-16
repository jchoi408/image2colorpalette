# image2colorpalette
A Python package/tool that allows a user to extract a color palette from a given image. 

After the user selects the number of colors they'd like inside their palette, the program runs a clustering algorithm to automatically generate one.

These are the libraries that we will be dependent on to get this to work:

``` python
import numpy as np
import cv2
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

%matplotlib inline
```

After we `import image2colorpalette`, we need to use OpenCV to select an image from a directory and then convert it to RGB. In our example, we will be using Kanye West's _Graduation_ album cover.

Once the image is in RGB format, we can insert it into the `image2colorpalette()` function and store it as a variable.. The default `palette_size` is 10, but we are going to extract 20 colors. Higher resolution images and the large palette sizes can definitely affect performance and potentially increase run-time.

``` python
import image2colorpalette

# Select image with OpenCV, which is formatted in BGR
graduation_bgr = cv2.imread('../DATA/kanye_graduation_cover.png')

# Convert to RGB
graduation_rgb = cv2.cvtColor(graduation_bgr, cv2.COLOR_BGR2RGB)

# Generate color palette
graduation_palette = image2colorpalette(graduation_rgb, palette_size=20)
```

Print a preview of the palette, RGB, and HEX codes:
``` python
graduation_palette.show_palette()
```
![show_palette](./graduation_show_palette.JPG)

Return a nested array of RGB codes:
``` python
graduation_palette.get_rgb()
```

Return an array of HEX codes:
``` python
graduation_palette.get_hex()
```
