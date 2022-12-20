#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python 3.7

# @Time   : 2022/12/20 18:21
# @Author : 'Lou Zehua'
# @File   : xml_json_transformer.py

import os
import json
import xmltodict

from lxml import etree


def xml2json(xml_str):
    xml_str = xml_str.replace(r"&|*|'|(|)|;|:|@|&|=|+|$|,|/|?|#|[|]", " ")
    data_ordered_dict = xmltodict.parse(xml_str, encoding='utf-8')  # <class 'collections.OrderedDict'>
    json_dict = json.loads(json.dumps(data_ordered_dict))
    return json_dict


def json2xml(json_dict):
    xml_str = xmltodict.unparse(json_dict)
    xml_root_elem = etree.fromstring(xml_str.encode('utf-8'))
    return xml_root_elem


if __name__ == '__main__':
    encoding = "utf-8"
    BASE_DIR = os.getcwd()

    xml_path = os.path.join(BASE_DIR, 'data/gexf_example.gexf')
    xml_path_new = os.path.join(BASE_DIR, 'data/gexf_example_new.gexf')
    json_path = os.path.join(BASE_DIR, 'data/gexf2json.json')

    # xml_path = os.path.join(BASE_DIR, 'data/gexf_example_simple_graph_part.xml')
    # xml_path_new = xml_path
    # json_path = os.path.join(BASE_DIR, 'data/gexf2json_simple_graph_part.json')

    # xml_path = os.path.join(BASE_DIR, 'data/gexf_example_multiattrs.gexf')
    # xml_path_new = xml_path
    # json_path = os.path.join(BASE_DIR, 'data/gexf2json_multiattrs.json')

    # xml to json
    with open(xml_path, 'r', encoding=encoding) as f_xml:
        xml_str = f_xml.read()
    json_dict = xml2json(xml_str)
    json_pretty_str = json.dumps(json_dict, indent=1)
    with open(json_path, 'w', encoding=encoding) as f_json:
        f_json.write(json_pretty_str)

    # json to xml
    with open(json_path, 'r', encoding=encoding) as f_json:
        json_dict = json.load(f_json)
    xml_root_elem = json2xml(json_dict)
    xml_pretty_str = etree.tostring(xml_root_elem, pretty_print=True).decode()
    with open(xml_path_new, 'w', encoding=encoding) as f_xml:
        xml_str = f_xml.write(xml_pretty_str)
