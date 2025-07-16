from elem import Elem, Text

class Html(Elem):
    def __init__(self, content=None):
        super().__init__('html', content=content, tag_type='double')

class Head(Elem):
    def __init__(self, content=None):
        super().__init__('head', content=content, tag_type='double')

class Body(Elem):
    def __init__(self, content=None):
        super().__init__('body', content=content, tag_type='double')

class Title(Elem):
    def __init__(self, content=None):
        super().__init__('title', content=content, tag_type='double')

class Meta(Elem):
    def __init__(self, attr={}):
        super().__init__('meta', attr=attr, tag_type='simple')

class Img(Elem):
    def __init__(self, attr={}):
        super().__init__('img', attr=attr, tag_type='simple')

class Table(Elem):
    def __init__(self, content=None):
        super().__init__('table', content=content, tag_type='double')

class Th(Elem):
    def __init__(self, content=None):
        super().__init__('th', content=content, tag_type='double')

class Tr(Elem):
    def __init__(self, content=None):
        super().__init__('tr', content=content, tag_type='double')

class Td(Elem):
    def __init__(self, content=None):
        super().__init__('td', content=content, tag_type='double')

class Ul(Elem):
    def __init__(self, content=None):
        super().__init__('ul', content=content, tag_type='double')

class Ol(Elem):
    def __init__(self, content=None):
        super().__init__('ol', content=content, tag_type='double')

class Li(Elem):
    def __init__(self, content=None):
        super().__init__('li', content=content, tag_type='double')

class H1(Elem):
    def __init__(self, content=None):
        super().__init__('h1', content=content, tag_type='double')

class H2(Elem):
    def __init__(self, content=None):
        super().__init__('h2', content=content, tag_type='double')

class P(Elem):
    def __init__(self, content=None):
        super().__init__('p', content=content, tag_type='double')

class Div(Elem):
    def __init__(self, content=None):
        super().__init__('div', content=content, tag_type='double')

class Span(Elem):
    def __init__(self, content=None):
        super().__init__('span', content=content, tag_type='double')

class Hr(Elem):
    def __init__(self):
        super().__init__('hr', tag_type='simple')

class Br(Elem):
    def __init__(self):
        super().__init__('br', tag_type='simple')

if __name__ == '__main__':
    html = Html([
        Head(Title(Text("Hello ground!"))),
        Body([
            H1(Text("Oh no, not again!")),
            Img(attr={'src': "http://i.imgur.com/pfp3T.jpg"})
        ])
    ])
    print(html)
