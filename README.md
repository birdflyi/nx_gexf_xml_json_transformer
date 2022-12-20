# nx_gexf_xml_json_transformer
A case for networkx.write_gexf function with a converter between the xml format and json format of gexf files.

## What is GEXF

GEXF (Graph Exchange XML Format) is a language for describing **complex networks** structures, their associated data and dynamics. Started in 2007 together with the [Gephi](https://gephi.org/) project by different actors, deeply involved in graph exchange issues, the gexf specifications are mature enough to claim being both extensible and [open](http://books.xmlschemata.org/relaxng/relax-CHP-12-SECT-2.html), and suitable for real specific applications. [See details about gexf: http://gexf.net/index.html]

Notes: It has been supported by networkx package. Those are file formats supported by networkx (with function names linke read_xxx or write_xxx) so far : 

- read_xxx and write_xxx: [adjlist, edgelist, gexf, gml, gpickle, graph6, multiline_adjlist, pajek, shp, sparse6, weighted_edgelist]

- only_read_xxx: [graphm, leda]

- only write_xxx: [graphml_lxml, graphml_xml]



## Files

[nx_savegexf_example.py](./nx_savegexf_example.py) creates a case of networkx graph, which is saved as gexf.

[xml_json_transformer.py](./xml_json_transformer.py) implements a function to convert formats between the xml and json for gexf files.

All of gexf files and the derived files is stored in the `./data/` directory.

