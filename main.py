# Master Script
from stl_png_loop import rotation
from tran_png import overlayimg
from overlay_img import overlayimg_make


# Running Loop Script
filename = 'airplane.stl'
deg = 45
rotation(filename,deg)

# Genreating Transperent Overlay Images
overlayimg()

# Paste Transperent Overlay on Satilite Imagery
overlayimg_make()

# Bounding Box Generation







