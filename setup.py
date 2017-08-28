from __future__ import print_function
from setuptools import setup, find_packages
import pip
import os
import sys
import io
import platform
from shutil import copyfile

with io.open('README.rst', encoding="utf-8") as f:
    long_description = f.read()

def check_copy(src, dst):    
    if not os.path.exists(src):
        raise RuntimeError('%s not found' % src)        
    print('Copying %s to %s' % (src,dst))
    copyfile(src, dst)

# From https://github.com/skvark/opencv-python/blob/master/setup.py
# This creates a list which is empty but returns a length of 1.
# Should make the wheel a binary distribution and platlib compliant.
class EmptyListWithLength(list):
    def __len__(self):
        return 1

if not ((sys.version_info[0] == 2 and sys.version_info[1] == 7) or
        (sys.version_info[0] == 3 and sys.version_info[1] == 3)):
    raise RuntimeError('No binaries available for Python %s.%s' % (sys.version_info[0], sys.version_info[1]) )

machine2suffix = {'i386' : 'x86', 'AMD64' : 'x64'}
src_folder = 'Python%s%s_%s' % (sys.version_info[0], sys.version_info[1], machine2suffix[platform.machine()])
check_copy(os.path.join(src_folder, 'fbxsip.pyd'), os.path.join('./fbxsip', 'fbx.pyd'))
check_copy(os.path.join(src_folder, 'fbx.pyd'), os.path.join('./fbx', 'fbx.pyd'))
check_copy(os.path.join(src_folder, 'FbxCommon.py'), os.path.join('./fbx', 'FbxCommon.py'))

package_data = {}
package_data['fbxsip'] = ['fbxsip.pyd']
package_data['fbx'] = ['fbx.pyd', 'FbxCommon.py']

setup(name='fbx',
      version='2018.1.1',
      url='https://github.com/VLAM3D/fbx2wheel',
      license='MIT',
      description='Setup tools script to make a wheel file for FBX.',
      long_description=long_description,
      packages=['fbxsip','fbx'],
      package_data=package_data,
      maintainer="Mathieu Lamarre",
      include_package_data=True,
      ext_modules=EmptyListWithLength(),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        #'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        #'Operating System :: POSIX',
        #'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: C++',
        'Programming Language :: Python :: Implementation :: CPython',
        #'Topic :: Scientific/Engineering',
        #'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Software Development',
        ]
      )