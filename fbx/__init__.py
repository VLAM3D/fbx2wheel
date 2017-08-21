import importlib
import sys
import os
from .fbx import *
# add this folder to the system path to allow import FbxCommon to work
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
globals().update(importlib.import_module('fbx.fbx').__dict__)
