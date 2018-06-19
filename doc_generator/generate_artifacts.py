import json
import random
import inspect
from xml.dom.minidom import parseString
import xml

from words import nouns
from libs.dicttoxml import dicttoxml as DictToXML


def _getRandWord():
    noun_count = len(nouns)
    return nouns[random.randrange(0, noun_count)]


def _writeDocument(name, data, document_type='json'):
    print(data)
    xml_dir = './xmls/'
    json_dir = './jsons/'
    if document_type in ['json', 'both']:
        with open(json_dir + name + ".json", 'w') as out:
            json.dump(data, out, indent=4)
    if document_type in ['xml', 'both']:
        with open(xml_dir + name + ".xml", 'w') as out:
            if not isinstance(data, xml.dom.minidom.Document):
                flat_xml = DictToXML(data).decode("UTF-8")
                xml_dom = parseString(flat_xml)
            else:
                xml_dom = data
            out.write(xml_dom.toprettyxml())

# JSON Attacks


def maxPropertyCount(count, name=None, document_type='json'):
    name = inspect.stack()[0][3] if name == None else name
    sample = {}
    for _ in range(count):
        key = _getRandWord()
        val = _getRandWord()
        sample[key] = val
    _writeDocument(name, sample, document_type)


def maxStringLength(length):
    name = inspect.stack()[0][3]
    sample = {
        _getRandWord(): _getRandWord()*length
    }
    _writeDocument(name, sample)


def maxArrayElementCount(ar_count):
    name = inspect.stack()[0][3]
    sample = {
        _getRandWord(): nouns[:ar_count]
    }
    _writeDocument(name, sample)


def maxKeyLength(length):
    name = inspect.stack()[0][3]
    sample = {
        _getRandWord()*length: _getRandWord()
    }
    _writeDocument(name, sample)


def maxElementDepth(depth, name=None, document_type='json'):
    sample = nestedJSON(depth)
    name = inspect.stack()[0][3] if name == None else name
    _writeDocument(name, sample, document_type)


def nestedJSON(depth):
    if depth <= 1:
        return {_getRandWord(): _getRandWord()}
    return {_getRandWord(): nestedJSON(depth-1)}

# JSON Attacks --end

# XML Attacks


def maxXMLDepth(depth):
    name = inspect.stack()[0][3]
    maxElementDepth(depth, name, 'xml')


def maxElementCount(count):
    name = inspect.stack()[0][3]
    maxPropertyCount(count, name, 'xml')


def maxAttributeCount(count):
    name = inspect.stack()[0][3]
    sample = {_getRandWord(): _getRandWord()}
    sample_xml = DictToXML(sample).decode("UTF-8")
    xml_dom = parseString(sample_xml)
    for _ in range(count):
        xml_dom.firstChild.firstChild.setAttribute(
            _getRandWord(), _getRandWord())
    _writeDocument(name, xml_dom, 'xml')


def maxAttributeLength(length):
    name = inspect.stack()[0][3]
    sample = {_getRandWord(): _getRandWord()}
    sample_xml = DictToXML(sample).decode("UTF-8")
    xml_dom = parseString(sample_xml)
    xml_dom.firstChild.firstChild.setAttribute(
        _getRandWord()*length, _getRandWord())
    _writeDocument(name, xml_dom, 'xml')


def maxChildrenPerElement(count):
    name = inspect.stack()[0][3]
    child = _getRandWord()
    sample = {child: {}}
    for _ in range(count):
        key = _getRandWord()
        val = _getRandWord()
        sample[child][key] = val
    _writeDocument(name, sample, 'xml')


def entityExpansionLimit(limit):
    pass

# XML Attacks --end


def main():
    print('Generating bogus Documents')
    maxPropertyCount(150)
    maxStringLength(101)
    maxArrayElementCount(101)
    maxKeyLength(101)
    maxElementDepth(101)
    #  XML Docs
    maxAttributeCount(101)
    maxChildrenPerElement(102)
    maxAttributeLength(102)
    maxElementCount(103)
    maxXMLDepth(105)


if __name__ == '__main__':
    main()
