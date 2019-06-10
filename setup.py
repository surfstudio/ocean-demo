from setuptools import setup, find_packages


setup(name='crimes',
      version='0.0.1',
      description='',
      author='Surf',
      license='MIT',
      install_requires=["Sphinx", "mlflow"],
      packages=find_packages('.'),
      zip_safe=False)