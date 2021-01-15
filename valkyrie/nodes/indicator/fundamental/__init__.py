from ...entities import Color, Module
from ._all_n import all_n, all_n_docs
from ._and_logic import and_logic, and_logic_docs
from ._any_n import any_n, any_n_docs
from ._constant_crossover import constant_crossover, constant_crossover_docs
from ._constant_math import constant_math, constant_math_docs
from ._crossover import crossover, crossover_docs
from ._lookback import lookback, lookback_docs
from ._math import math, math_docs
from ._or_logic import or_logic, or_logic_docs
from ._rank import rank, rank_docs
from ._sum_n import sum_n, sum_n_docs

fundamental_module = Module(
    key="fundamental",
    label="Fundamental",
    color=Color(red=255, green=196, blue=0),
    icon="fas fa-square-root-alt",
    nodes=[
        crossover_docs,
        # constant_crossover_docs,
        math_docs,
        # constant_math_docs,
        or_logic_docs,
        and_logic_docs,
        all_n_docs,
        any_n_docs,
        sum_n_docs,
        lookback_docs,
        rank_docs,
    ],
)
