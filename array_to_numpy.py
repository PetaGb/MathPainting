import numpy as np
from PIL import Image

data = np.zeros((5, 4, 3), dtype=np.uint8)

data[:] = [255, 100, 90]

img = Image.fromarray(data, "RGB")
img.save('canvas.png')
print(data)