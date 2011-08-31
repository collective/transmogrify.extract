from collective.transmogrifier.interfaces import ISectionBlueprint, ISection
from lxml import etree, html
from zope.interface import classProvides, implements


class Extract(object):
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self.previous = previous
        if 'decode' in options:
            self.decode = options['decode']
        else:
            self.decode = 'utf-8'
        if 'encode' in options:
            self.encode = options['encode']
        else:
            self.encode = 'utf-8'
        if 'id' in options:
            self._id = options['id']
        else:
            self._id = "content"

    def __iter__(self):
        for item in self.previous:
            if 'text' in item.keys():
                try:
                    text = item['text'].decode(self.decode)
                except UnicodeDecodeError:
                    text = item['text']
                tree = html.fromstring(text)
                content = tree.xpath('//*[@id="%s"]' % self._id) or None
                if content is not None:
                    results = ''.join([etree.tostring(i) for i in content[0]])
                    try:
                        item['text'] = results.encode(self.encode)
                    except UnicodeEncodeError:
                        item['text'] = results
            yield item
