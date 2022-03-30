from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='wiredcalc',
  version='0.0.2',
  description='an weird calulator',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url = 'https://github.com/L-e-o-linux-das/wiredcalc/',
  download_url = 'https://github.com/L-e-o-linux-das/wiredcalc/archive/refs/tags/V_02.tar.gz',
  author='Leo Mux',
  author_email='leo.das.nirjhar@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='calc', 
  packages=find_packages(),
  install_requires=[''] 
)