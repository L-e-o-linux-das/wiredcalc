from distutils.core import setup
setup(
  name = 'wiredcalculator',         
  packages = ['wiredcalculator'],   
  version = '0.1',      
  license='MIT',        
  description = 'lol this is a calculator',   
  author = 'leomux',                  
  author_email = 'leo.das.mux@gmail.com',      
  url = 'https://github.com/user/reponame',   
  download_url = '',  
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   
  install_requires=[           
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)