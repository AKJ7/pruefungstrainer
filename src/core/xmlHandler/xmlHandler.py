import os
import xml.etree.ElementTree as ET

# TODO: CRUD (Create, Read, Update, Delete)
# TODO: ADD ERRORHANDLER


class XMLHandler:
    def __init__(self, file_name: str):
        self._fileName = file_name
        if not os.path.exists(file_name):
            open(self._fileName, 'w')
        self._tree = None
        self.root = None
        self.parse_file()

    def parse_file(self):
        try:
            self._tree = ET.parse(self._fileName)
        except ET.ParseError as xml_parse_error:
            open(self._fileName, 'w').write('<?xml version="1.0"?><data></data>')
            self._tree = ET.parse(self._fileName)
        self.root = self._tree.getroot()
        assert self.root.tag == 'data', 'Invalid root tag!'

    def __getitem__(self, item: str):
        for child in self.root:
            if child.attrib['name'] == item:
                return child
        raise NameError('Could not find: ' + item)

    def __setitem__(self, key: str, value: str):
        for child in self.root:
            if child.attrib['name'] == key:
                print(key, value)

    def insert_question(self, into: str, value: str):
        last_digit = 0
        for child in self.root:
            if child.attrib['name'] == into:
                for element in child:
                    last_digit = int(element.attrib['id'])
                ET.SubElement(child, 'question', {'id': str(last_digit + 1)}).text = value
                self._tree.write(self._fileName, encoding='utf8', xml_declaration=True)
                return
        raise NameError(into + ' not found')

    def insert_subject(self, value: str):
        for child in self.root:
            if child.attrib['name'] == value:
                raise NameError(value + ' already exists!')
        a = ET.SubElement(self.root, 'course', {'name': value})
        self._tree.write(self._fileName, encoding='utf8', xml_declaration=True)

    def remove_subject(self, value: str):
        for child in self.root:
            if child.attrib['name'] == value:
                self.root.remove(child)
                self._tree.write(self._fileName, encoding='utf8', xml_declaration=True)
                return
        raise NameError(value + ' not found')

    def remove_question(self, name: str, id: int):
        for child in self.root:
            if child.attrib['name'] == name:
                for element in child:
                    if int(element.attrib['id']) == id:
                        child.remove(element)
                        self._tree.write(self._fileName, encoding='utf8', xml_declaration=True)
                        return
                raise NameError('Element with id: ' + str(id) + ' not found')
            raise NameError('Child with attribute: ' + name + ' not found')


x = XMLHandler('xmlsTest.xml')
# print(x['Panama'][1].text)
# x['Panama'] = 'test'
# x.insert_question('Panama', 'this is a test')
# x.insert_subject('math')
x.insert_question('math', 'Another test in math2')
# x.remove_subject('math')
# x.remove_question('math', 3)
