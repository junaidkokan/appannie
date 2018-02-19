from setuptools import setup

setup(name='appannie',
      version='0.1',
      description='Client library to download data from appannie API',
      url='https://github.com/junaidkokan/appannie',
      author='Junaid Kokan',
      author_email='junaid.kokan13@gmail.com',
      license='Apache License 2.0',
      packages=['appannie'],
      install_requires=[
          'markdown',
          urllib2,
          urllib,
          time,
          json,
          datetime,
          retrying
      ],
      zip_safe=False)
