import backtrader.indicators as btind

from ...entities import Color, Module
from ._average_true_range import average_true_range, average_true_range_docs
from ._exponential_moving_average import (
    exponential_moving_average,
    exponential_moving_average_docs,
)
from ._simple_moving_average import simple_moving_average, simple_moving_average_docs
from ._simple_moving_average_envelope import sma_env, sma_env_docs
from ._triple_ema import triple_ema, triple_ema_docs
from ._true_range import true_range, true_range_docs
from ._weighted_moving_average import (
    weighted_moving_average,
    weighted_moving_average_docs,
)

average_docs = Module(
    key="average",
    label="Average",
    color=Color(red=197, green=17, blue=98),
    icon="fas fa-snowplow",
    nodes=[
        simple_moving_average_docs,
        exponential_moving_average_docs,
        weighted_moving_average_docs,
        true_range_docs,
        average_true_range_docs,
        sma_env_docs,
        triple_ema_docs,
    ],
)
