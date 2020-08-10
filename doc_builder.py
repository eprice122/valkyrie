import inspect
import json
import os

from valkyrie.nodes.data.data import data_docs
from valkyrie.nodes.indicator.average import average_docs
from valkyrie.nodes.indicator.fundamental import fundamental_docs
from valkyrie.nodes.order.standard_order import basic_order_docs


def build(fp):
    libraries = [data_docs, fundamental_docs, average_docs, basic_order_docs]
    dp = os.path.dirname(os.path.abspath(__file__))

    """
    for library in libraries:
        for node in library.nodes:
            path = node.docs_path
            del node.docs_path
            with open(os.path.join(dp, path), "r") as g:
                node.docs = g.read()
    """

    with open(fp, "w") as f:
        json.dump(libraries, f, default=lambda x: x.__dict__)


build("docs-v2.json")
