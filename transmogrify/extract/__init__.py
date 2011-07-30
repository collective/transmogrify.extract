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
