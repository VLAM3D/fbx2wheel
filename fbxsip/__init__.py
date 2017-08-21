import importlib
from .fbxsip import *
globals().update(importlib.import_module('fbxsip.fbxsip').__dict__)