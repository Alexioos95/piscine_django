from elem import Elem, Text
from elements import *

class Page:
	def	__init__(self, elem):
		self.elem = elem

	def	__str__(self):
		code = str(self.elem)
		if isinstance(self.elem, Html):
			return "<!DOCTYPE html>\n" + code
		return (code)

	def write_to_file(self, filename):
		try:
			with open(filename + ".html", "w", encoding="utf-8") as file:
				file.write(f"{self.__str__()}")
		except Exception as e:
			print(f"Error: {e}")

	def	is_body_div_valid(self, elem):
		for content in elem.content:
			if isinstance(content, Text):
				continue
			if content.tag not in tags:
				return (False)
		return (True)

	def	is_valid(self):
		tags = {
			"html", "head", "body", "title", "meta", "img", "table", "th", "tr", "td",
			"ul", "ol", "li", "h1", "h2", "p", "div", "span", "hr", "br"
		}
		text_only = { "title", "h1", "h2", "li", "th", "td" }
		body = { "h1", "h2", "div", "table", "ul", "ol", "span", "text" }
		if not isinstance(self.elem, Elem) or self.elem.tag not in tags:
			return (False) 
		for content in self.elem.content:
			if isinstance(content, Text):
				continue
			elif isinstance(content, Elem):
				if not Page(content).is_valid():
					print("Fail Check on Childs")
					return (False)
				if isinstance(content, Html):
					clist = content.content
					if len(clist) != 2 or not isinstance(clist[0], Head) or not isinstance(clist[1], Body):
						print("Fail Check on HTML")
						return (False)
				elif isinstance(content, Head):
					if len(content.content) != 1 or not isinstance(content.content[0], Title):
						print("Fail Check on HEAD")
						return (False)
				elif isinstance(content, Body) or isinstance(content, Div):
					for elem in content.content:
						if isinstance(elem, Text):
							continue
						if elem.tag not in body:
							print("Fail Check on BODY")
							return (False)
				elif content.tag in text_only:
					if len(content.content) != 1 or not isinstance(content.content[0], Text):
						print("Fail Check on TEXT")
						return (False)
				elif isinstance(content, P):
					for elem in content:
						if not isinstance(elem, Text):
							print("Fail Check on P")
							return (False)
				elif isinstance(content, Span):
					for elem in content:
						if not isinstance(elem, Text) and not isinstance(elem, P):
							print("Fail Check on SPAN")
							return (False)
				elif isinstance(content, Ul) or isinstance(content, Ol):
					if len(content.content) < 1:
						print("Fail Check on UL")
						return (False)
					for elem in content.content:
						if not isinstance(elem, Li):
							print("Fail Check on UL")
							return (False)
				elif isinstance(content, Tr):
					if len(content.content) < 1:
						print("Fail Check on TR")
						return (False)
					first_type = type(content.content[0])
					for elem in content.content:
						if not isinstance(elem, Th) and not isinstance(elem, Td) or not type(elem) is first_type:
							print("Fail Check on TR")
							return (False)
				elif isinstance(content, Table):
					for elem in content.content:
						if not isinstance(elem, Tr):
							print("Fail Check on TABLE")
							return (False)
			else:
				return (False)
		return (True)

if __name__ == '__main__':
	true = Html(content=[
		Head(content=[
			Title(content=[Text("Success")])
		]),
		Body(content=[
			H1(content=[Text("TITLE")]),
			Table(content=[
				Tr(content=[
					Th(content=[Text("TH")])
				])
			])
		])
	])
	false = Html(content=[
		Head(content=[
			Div(content=[Text("Fail")])
		]),
	])
	print(f"{Page(true).is_valid()}")
	print(f"{Page(false).is_valid()}")
	print(f"{Page(true)}")
	Page(true).write_to_file("test")
