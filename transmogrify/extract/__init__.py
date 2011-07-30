<<<<<<< HEAD
from collective.transmogrifier.interfaces import ISectionBlueprint, ISection
from lxml import etree, html
from zope.interface import classProvides, implements


class Extract(object):
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self.previous = previous
        self.decode = options['decode']
        self.encode = options['encode']

    def __iter__(self):
        for item in self.previous:
            try:
                text = item['text'].decode(self.decode)
            except UnicodeDecodeError:
                text = item['text']
            tree = html.fromstring(text)
            content = tree.xpath('//*[@id="content"]')
            results = ''.join([etree.tostring(i) for i in content[0]])
            try:
                item['text'] = results.encode(self.encode)
            except UnicodeEncodeError:
                item['text'] = results
            yield item
=======
# See http://peak.telecommunity.com/DevCenter/setuptools#namespace-packages
try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    from pkgutil import extend_path
    __path__ = extend_path(__path__, __name__)
>>>>>>> e8902591032205128e6c6840a8b61517f56724a5
