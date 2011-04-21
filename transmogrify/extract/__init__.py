
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
            yield item


#            root = lxml.html.fromstring(item['text'])
#            text = """<div id="content">"""
#            for tag in [i for i in root.iter()]:
#                tag_id = tag.get('id')
#                if tag_id is not None:
#                    if tag.get('id') == 'content':
#                        children = tag.getchildren()
#                        for child in children:
#                            if child.text is not None:
#                                try:
#                                    text += '<%s>%s</%s>' % (
#                                        child.tag, child.text.decode('utf-8'), child.tag)
#                                except:
#                                    pass
#                        
#            text += """</div>"""
#            item['text'] = text
#            yield item
