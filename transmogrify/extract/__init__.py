import lxml
from collective.transmogrifier.interfaces import ISectionBlueprint, ISection
from zope.interface import classProvides, implements


class Extract(object):
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self.previous = previous

    def __iter__(self):
        for item in self.previous:
            text = item['text'].decode('utf-8')

            import pdb; pdb.set_trace()
            
            tree = lxml.html.fromstring(text)
            content = tree.xpath('//*[@id="content"]')
            # Look ma, no recursion! lxml iterates over nodes in "document
            # order"
            results = ''.join([lxml.etree.tostring(i) for i in content[0]])
            item['text'] = results
            yield item
