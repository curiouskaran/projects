try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'My project',
        'author': 'Karan Sharma',
        'url': 'URL to get it at',
        'download_url': 'where to download it',
        'author_email': '01karan95@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'scripts': [],
        'name': 'projectname'
}

setup(**config)