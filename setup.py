from setuptools import setup, find_packages
import pip
import os
import sys
import io

with io.open('README.rst', encoding="utf-8") as f:
    long_description = f.read()

# From https://github.com/skvark/opencv-python/blob/master/setup.py
# This creates a list which is empty but returns a length of 1.
# Should make the wheel a binary distribution and platlib compliant.
class EmptyListWithLength(list):
    def __len__(self):
        return 1

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