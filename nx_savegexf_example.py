#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python 3.7

# @Time   : 2022/12/20 21:27
# @Author : 'Lou Zehua'
# @File   : nx_savegexf_example.py

import networkx as nx
import pandas as pd


def set_node_default_value_inplace(G, attr_default_pairs=None, nodes=None):
    nodes = nodes or G.nodes
    if not attr_default_pairs:
        return G
    if len(attr_default_pairs):
        if type(attr_default_pairs) is dict:
            attr_default_pairs = list(attr_default_pairs.items())
        for attr, default in attr_default_pairs:
            if not attr:
                print("Bad attr name, which may be regarded as False to update! Skipped...")
                continue
            for n in nodes:
                G.nodes[n][attr] = G.nodes.data(attr, default=default).__getitem__(n)
    return G


def set_edge_default_value_inplace(G, attr_default_pairs=None, edges=None):
    edges = edges or G.edges
    if not attr_default_pairs:
        return G
    if len(attr_default_pairs):
        if type(attr_default_pairs) is dict:
            attr_default_pairs = list(attr_default_pairs.items())
        for attr, default in attr_default_pairs:
            if not attr:
                print("Bad attr name, which may be regarded as False to update! Skipped...")
                continue
            for dd in list(zip(*edges.data(data=True)))[-1]:
                dd[attr] = dict(dd).get(attr, default)
    return G


if __name__ == '__main__':
    graph = nx.DiGraph(name="my graph")

    graph.add_node(0, id="32446707", weight=100, nodetype='repo', name="soimort/mono")
    graph.add_node(1, id="342945", weight=10, nodetype='actor', name="soimort")
    graph.add_nodes_from([(2, dict(id="repo1")), (3, dict(id="repo2"))], nodetype='repo')  # share attribute nodetype
    # batch way
    # default key attribute: "label"
    data = zip(range(4, 6), ["actor1", "actor2"])
    data_items = pd.DataFrame(data, columns=["label", "id"]).set_index("label")[["id"]].to_dict('index').items()
    graph.add_nodes_from(data_items, nodetype='actor')

    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 0)
    graph.add_edge(2, 1)
    graph.add_edge(0, 3)

    default_node_settings = {"weight": 2}
    need_set_default_nodes = [2, 3, 4, 5]
    # need_set_default_nodes = range(2, len(graph.nodes))
    graph = set_node_default_value_inplace(graph, default_node_settings, need_set_default_nodes)
    print(graph.nodes.data(data=True))

    default_edge_settings = {"weight": 1}
    graph = set_edge_default_value_inplace(graph, default_edge_settings)
    print(graph.edges.data(data=True))

    nx.write_gexf(graph, "./data/gexf_example.gexf")  # See details about gexf: http://gexf.net/index.html
