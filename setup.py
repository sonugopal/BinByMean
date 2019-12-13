from distutils.core import setup
setup(
  name = 'BinByMean',         # How you named your package folder (MyLib)
  packages = ['BinByMean'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Performs Bin By mean in your dataset.',   # Give a short description about your library
  author = 'SONU GOPAL',                   # Type in your name
  author_email = 'sonu.g@mca.christuniversity.in',      # Type in your E-Mail
  url = 'https://github.com/sonugopal/BinByMean.git',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/sonugopal/BinByMean/archive/v0.1.tar.gz',    # I explain this later on
  keywords = ['Bin By Mean', 'Noise Reduction', 'python'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
          'numpy',
      'statistics',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which python versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
