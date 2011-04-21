from setuptools import setup

setup(
    name='transmogrify.extract',
    entry_points = """
    [collective.transmogrifier]
    transmogrify.extract = transmogrify.extract
    """
)
