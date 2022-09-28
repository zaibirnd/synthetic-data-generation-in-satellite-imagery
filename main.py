# Master Script
from stl_png_loop import rotation
from stl_png_loop_tilt import rotation_tilt
from tran_png import transparent_overlayimg
from overlay_img import overlayimg_make


# Running Loop Script
filename = 'airplane.stl'
deg = 45
# rotation(filename,deg)
rotation_tilt(filename,deg)

# Genreating Transperent Overlay Images
transparent_overlayimg()

# Paste Transperent Overlay on Satilite Imagery
overlayimg_make()

# Bounding Box Generation







