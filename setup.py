import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()

with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()


setup(name='penelope.api',
      version='0.2',
      description='penelope.api',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      namespace_packages=['penelope'],
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires= [
          'setuptools',
          'Eve[sqlalchemy]',
          'penelope.models',
          'Flask-SQLAlchemy',
          'sqlalchemy',
          'psycopg2'
          ],
      test_suite="penelope.api",
      entry_points="""
      [console_scripts]
      eve = penelope.api:run
      """
      )

