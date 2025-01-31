from PIL import Image
import numpy as np
import sys
import tempfile
import os

ULTRAHDR_BIN = os.environ.get('ULTRAHDR_BIN') or "./ultrahdr_app"

INPUT_IMAGE_1 = sys.argv[1]
INPUT_IMAGE_2 = sys.argv[2]
OUTPUT_IMAGE = sys.argv[3]

# image 1 must be a jpeg
if not (INPUT_IMAGE_1.endswith(".jpg") or INPUT_IMAGE_1.endswith(".jpeg")):
    print("Image 1 must be a jpeg")
    sys.exit(1)

image = Image.open(INPUT_IMAGE_2).convert("RGBA")
image_np = np.array(image).astype(np.float32) / 255.0
image_half = image_np.astype(np.float16)
_, tempfile = tempfile.mkstemp()
image_half.tofile(tempfile)

COMMAND = f"{ULTRAHDR_BIN} -m 0 -i {INPUT_IMAGE_1} -p {tempfile} -h {image_np.shape[0]} -w {image_np.shape[1]} -a 4 -t 0 -z {OUTPUT_IMAGE} -R 0 -s 1 -L 305 -Q 100" 
os.system(COMMAND)
os.remove(tempfile)
