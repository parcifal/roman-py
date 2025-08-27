"""
Definition of the RomanPy module.
"""
from typing import Union

_ENCODING_ASCII = "ascii"
_ENCODING_UNICODE = "unicode"

VARIANT_BASE = {
    0: "N",
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}

VARIANT_SUBTRACTIVE = {
    4: "IV",
    9: "IX",
    40: "XL",
    400: "CD",
    900: "CM"
}

VARIANT_SUBTRACTIVE_EXTENDED = {
    8: "IIX",
    17: "IIIXX",
    18: "IIXX",
    97: "IIIC",
    98: "IIC",
    99: "IC"
}

VARIANT_APOSTROPHUS = {
    500: "I)",
    1000: "(I)",
    5000: "I))",
    10000: "((I))",
    50000: "I)))",
    100000: "(((I)))"
}

VARIANT_MEDIEVAL = {
    5: "A",
    7: "Z",
    11: "O",
    40: "F",
    70: "S",
    80: "R",
    90: "N",
    150: "Y",
    151: "K",
    160: "T",
    200: "H",
    250: "E",
    300: "B",
    400: "P",
    500: "Q"
}

_MAPPING_UNICODE_UPPER = {
    "(((I)))": "ↈ",
    "I)))": "ↇ",
    "((I))": "ↂ",
    "I))": "ↁ",
    "(I)": "ↀ",
    "I)": "Ⅾ",
    "IX": "Ⅸ",
    "IV": "Ⅳ",
    "XII": "Ⅻ",
    "XI": "Ⅺ",
    "VIII": "Ⅷ",
    "VII": "Ⅶ",
    "VI": "Ⅵ",
    "III": "Ⅲ",
    "II": "Ⅱ",
    "M": "Ⅿ",
    "D": "Ⅾ",
    "C": "Ⅽ",
    "L": "Ⅼ",
    "X": "Ⅹ",
    "V": "Ⅴ",
    "I": "Ⅰ",
}

_MAPPING_UNICODE_LOWER = {
    ")": "ↄ",
    "(": "ⅽ",
    "IX": "ⅸ",
    "IV": "ⅳ",
    "XII": "ⅻ",
    "XI": "ⅺ",
    "VIII": "ⅷ",
    "VII": "ⅶ",
    "VI": "ⅵ",
    "III": "ⅲ",
    "II": "ⅱ",
    "M": "ⅿ",
    "D": "ⅾ",
    "C": "ⅽ",
    "L": "ⅼ",
    "X": "ⅹ",
    "V": "ⅴ",
    "I": "ⅰ"
}

_ENCODINGS = [
    _ENCODING_ASCII,
    _ENCODING_UNICODE,
]

_DEFAULT_ENCODING = _ENCODING_ASCII
_DEFAULT_VARIANT = VARIANT_BASE | VARIANT_SUBTRACTIVE


class _RomanNumeral:
    """
    The roman numeral class.
    """

    def __init__(self,
                 value: int,
                 encoding: str = _DEFAULT_ENCODING,
                 uppercase: bool = True,
                 variant: Union[dict[int, str], list[str]] = None):

        assert value >= 0, "a roman numeral cannot be negative"
        assert encoding in _ENCODINGS, \
            f"specified encoding \"{encoding}\" unknown"

        if variant is None:
            variant = _DEFAULT_VARIANT

        self._value = value
        self._encoding = encoding
        self._uppercase = uppercase
        self._variant = variant

    def encode(self, encoding: str):
        """
        Return a roman numeral of the same value and case as the current
        roman numeral, with the specified encoding.
        """
        return _RomanNumeral(self._value,
                             encoding,
                             self._uppercase,
                             self._variant)

    def upper(self):
        """
        Return a roman numeral of the same value and encoding as the current
        roman numeral, in uppercase.
        """
        return _RomanNumeral(self._value,
                             self._encoding,
                             True,
                             self._variant)

    def lower(self):
        """
        Return a roman numeral of the same value and encoding as the current
        roman numeral, in lowercase.
        """
        return _RomanNumeral(self._value,
                             self._encoding,
                             False,
                             self._variant)

    def extend_variant(self, variant: dict[int, str]):
        """
        Return a roman numeral, identical to the current one, with current
        variant extended as specified.
        """
        return _RomanNumeral(self._value,
                             self._encoding,
                             self._uppercase,
                             self._variant | variant)

    def set_variant(self, variant: dict[int, str]):
        """
        Return a roman numeral, identical to the current one, with the
        variant as specified.
        """
        return _RomanNumeral(self._value,
                             self._encoding,
                             self._uppercase,
                             variant)

    def __str__(self):
        if self._value == 0:
            return self._variant.get(0, "")

        carry = self._value
        numeral = ""

        for value, digit in sorted(self._variant.items(), reverse=True):
            if value == 0:
                continue
            while value <= carry:
                carry = carry - value
                numeral = numeral + digit

        if self._encoding is _ENCODING_ASCII:
            return numeral if self._uppercase else numeral.lower()

        mapping = _MAPPING_UNICODE_UPPER if self._uppercase else \
            _MAPPING_UNICODE_LOWER

        for old, new in mapping.items():
            numeral = numeral.replace(old, new)

        return numeral

    __repr__ = __str__

    def __eq__(self, other):
        if isinstance(other, _RomanNumeral):
            return self._value == other._value
        if isinstance(other, int):
            return self._value == other
        if isinstance(other, str):
            return str(self) == other
        return NotImplemented

    def __ne__(self, other):
        return not other == self

    def __gt__(self, other):
        if isinstance(other, _RomanNumeral):
            return self._value > other._value
        if isinstance(other, int):
            return self._value > other
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, _RomanNumeral):
            return self._value < other._value
        if isinstance(other, int):
            return self._value < other
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, _RomanNumeral):
            return self._value >= other._value
        if isinstance(other, int):
            return self._value >= other
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, _RomanNumeral):
            return self._value <= other._value
        if isinstance(other, int):
            return self._value <= other
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, _RomanNumeral):
            return _RomanNumeral(self._value + other._value)
        if isinstance(other, int):
            return _RomanNumeral(self._value + other)
        return NotImplemented

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, _RomanNumeral):
            return _RomanNumeral(self._value - other._value)
        if isinstance(other, int):
            return _RomanNumeral(self._value - other)
        return NotImplemented

    __rsub__ = __sub__

    def __mul__(self, other):
        if isinstance(other, _RomanNumeral):
            return _RomanNumeral(self._value * other._value)
        if isinstance(other, int):
            return _RomanNumeral(self._value * other)
        return NotImplemented

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, _RomanNumeral):
            return _RomanNumeral(int(self._value / other._value))
        if isinstance(other, int):
            return _RomanNumeral(int(self._value / other))
        return NotImplemented

    __rtruediv__ = __truediv__

    def __floordiv__(self, other):
        if isinstance(other, _RomanNumeral):
            return _RomanNumeral(self._value // other._value)
        if isinstance(other, int):
            return _RomanNumeral(self._value // other)
        return NotImplemented

    __rfloordiv__ = __floordiv__
