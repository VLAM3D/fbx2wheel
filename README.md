# fbx2wheel
Setuptools setup script to make a platform wheel from the official FBX binaries

For internal convenience use only. Not to be used to push on PyPI. 

# How to use
- Download installer from official site
- Open exe with 7-zip and extract the fbxsip.pyd, fbx.pyd, FbxCommon.py 
- Put fbxsip.pyd in the fbxsip folder
- Put fbx.pyd, FbxCommon.py in the fbx folder
- python setup.py bdist_wheel

# Warning

Have a look at fbx/__init__.py file, it's pretty hacky. It might not work in all situations. 