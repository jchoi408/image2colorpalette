# image2colorpalette
A Python package/tool that allows a user to extract a color palette from a given image.

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

After we `import image2colorpalette`, we need to use OpenCV to select an image from a directory and then convert it to RGB. In our example, we will be using Kanye West's Graduation album cover.

Once the image is in RGB format, we can insert it into the `image2colorpalette()` function and store it as a variable.. The default `palette_size` is 10, but we are going to extract 20 colors.

``` python
import image2colorpalette

# Select image with OpenCV, which is formatted in BGR
graduation_bgr = cv2.imread('../DATA/kanye_graduation_cover.png')

# Convert to RGB
graduation_rgb = cv2.cvtColor(graduation_bgr, cv2.COLOR_BGR2RGB)

# Generate color palette
graduation_palette = image2colorpalette(graduation_rgb, palette_size=20)
```
