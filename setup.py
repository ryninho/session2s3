from setuptools import setup
setup(
  name = 'session2s3',
  packages = ['session2s3'],
  version = '0.1a1',
  description = 'Save your Python session to S3',
  author = 'Eric Rynerson',
  author_email = 'eric.rynerson@gmail.com',
  license='MIT',
  url = 'https://github.com/ryninho/session2s3',
  download_url = 'https://github.com/ryninho/session2s3/archive/0.1.tar.gz',
  keywords = ['s3', 'logging', 'debugging', 'session', 'rollback'],
  classifiers = [
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python :: 2.7'
  ],
  install_requires=['boto3', 'dill'],
  python_requires='==2.7.*',
)
