from setuptools import setup

setup(
    name='transmogrify.extract',
    install_requires='lxml',
    entry_points = """
    [collective.transmogrifier]
    transmogrify.extract = transmogrify.extract
    """
)
