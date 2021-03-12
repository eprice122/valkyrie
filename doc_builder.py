import inspect
import json
import os

import boto3

from valkyrie.nodes.data.data import data_docs
from valkyrie.nodes.indicator.average import average_docs
from valkyrie.nodes.indicator.extrema import extrema_docs
from valkyrie.nodes.indicator.fundamental import fundamental_module
from valkyrie.nodes.indicator.momentum import momentum_docs
from valkyrie.nodes.indicator.statistics import statistics_module
from valkyrie.nodes.order.standard_order import basic_order_docs

libraries = [
    data_docs,
    fundamental_module,
    average_docs,
    basic_order_docs,
    momentum_docs,
    extrema_docs,
    statistics_module,
]
dp = os.path.dirname(os.path.abspath(__file__))

for library in libraries:
    for node in library.nodes:
        path = node.docs_path
        if path and path != "":
            del node.docs_path
            with open(os.path.join(dp, "valkyrie", "docs", path), "r") as g:
                node.docs = g.read()

j = json.dumps(libraries, default=lambda x: x.__dict__)
client = boto3.client("s3")
client.put_object(Body=j, Bucket="sierra.db", Key="docs.json")
