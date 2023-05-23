# manually add File into it 

# __all__=[
#     "user_controler",
#     "product_controller"
# ]

# solution for that

import os
import glob

__all__ = [os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__)+ "/*.py")]