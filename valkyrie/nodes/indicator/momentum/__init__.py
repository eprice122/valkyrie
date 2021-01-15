from ...entities import Color, Module
from ._bollinger_bands import bollinger_bands, bollinger_bands_docs
from ._cci import cci, cci_docs
from ._derivative import derivative, derivative_docs
from ._macd import macd, macd_docs
from ._rate_of_change import rate_of_change, rate_of_change_docs
from ._rsi import rsi, rsi_docs

momentum_docs = Module(
    key="momentum",
    label="Momentum",
    color=Color(red=0, green=176, blue=255),
    icon="fas fa-hippo",
    nodes=[
        cci_docs,
        rate_of_change_docs,
        rsi_docs,
        derivative_docs,
        bollinger_bands_docs,
    ],
)
