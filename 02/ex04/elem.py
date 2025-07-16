#!/usr/bin/python3

class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        res = super().__str__()
        res = res.replace("&", "&amp;")
        res = res.replace("<", "&lt;")
        res = res.replace(">", "&gt;")
        res = res.replace("\"", "&quot;")
        return res.replace('\n', '\n<br />\n')

class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    class ValidationError(Exception):
        def __init__(self):
            Exception.__init__(self, "Something went wrong.")

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        self.tag = tag
        self.attr = attr
        self.tag_type = tag_type
        if content is None:
            self.content = []
        elif isinstance(content, list):
            if not all([self.check_type(c) for c in content]):
                raise self.ValidationError
            self.content = content
        elif self.check_type(content):
            self.content = [content]
        else:
            raise self.ValidationError

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        result = f"<{self.tag}{self.__make_attr()}"
    
        if self.tag_type == 'double':
            result += ">"
            content = self.__make_content()
            if content:
                result += f"\n  {content}\n"
            result += f"</{self.tag}>"
        elif self.tag_type == 'simple':
            result += "/>"
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''
        result = ''
        for elem in self.content:
            if str(elem).strip():
                str_elem = str(elem).replace("\n", "\n  ").strip()
                result += f"\n  {str_elem}"
        return result.strip()

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))

if __name__ == '__main__':
    title = Text("Hello ground!")
    h1 = Text("Oh no, not again!")
    img = Elem(tag='img', attr={'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')
    html = Elem(tag='html', content=[
        Elem(tag='head', content=[
            Elem(tag='title', content=[title], tag_type='double')
        ], tag_type='double'),
        Elem(tag='body', content=[
            Elem(tag='h1', content=[h1], tag_type='double'),
            img
        ], tag_type='double')
    ], tag_type='double')
    print(html)
