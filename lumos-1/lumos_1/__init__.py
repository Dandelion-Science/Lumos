import sys
import os

# Add this directory to sys.path so that the inference scripts' flat imports
# (e.g., `from model.utils import ...`, `from data.item_processor import ...`)
# resolve correctly when this package is installed via pip.
_here = os.path.dirname(os.path.abspath(__file__))
if _here not in sys.path:
    sys.path.insert(0, _here)
