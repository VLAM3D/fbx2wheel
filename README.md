# fbx2wheel
Setuptools setup script to make a platform wheel from the official FBX binaries

For internal convenience use only. Not to be used to push on PyPI. 

# How to use
- Download installer from official site
- Open exe with 7-zip and extract the lib folder to this folder, ex: for 2018.1
    - Python27_x64
    - Python27_x86
    - Python33_x64
    - Python33_x86
- python setup.py bdist_wheel

# Warning

The official FBX Windows binaries only support the four Python versions listed above. 

Have a look at fbx/__init__.py file, it's pretty hacky. It might not work in all situations. 