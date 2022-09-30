# Master Script for the project
# from stl_png_loop import rotation
from stl_png_loop_tilt import rotation_tilt
from tran_png import transparent_overlayimg
from overlay_img import overlayimg_make
import time

st = time.time()
# Running Loop Script
filename = 'airplane.stl'
deg = 45
# rotation(filename,deg)
rotation_tilt(filename,deg)

# Genreating Transperent Overlay Images
transparent_overlayimg()

# Paste Transperent Overlay on Satilite Imagery
offset = 5
overlayimg_make(offset)

# Bounding Box Generation


# get the end time
et = time.time()
# get the execution time
elapsed_time = et - st
print('\nExecution time:', round(elapsed_time,2), 'seconds')







