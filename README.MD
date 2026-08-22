# RomanPy

[![release](https://img.shields.io/gitea/v/release/parcifal/RomanPy?gitea_url=https%3A%2F%2Fscm.parcifal.dev&label=latest+release)][release]
[![pypi](https://img.shields.io/pypi/v/RomanPy?label=pypi+release)][pypi]
[![develop](https://scm.parcifal.dev/parcifal/RomanPy/badges/workflows/push.yml/badge.svg?label=develop&branch=develop)][develop]
[![master](https://scm.parcifal.dev/parcifal/RomanPy/badges/workflows/push.yml/badge.svg?label=master&branch=master)][master]
[![gitlab](https://img.shields.io/gitlab/last-commit/parcifal%2FRomanPy?label=gitlab+mirror)][gitlab]
[![github](https://img.shields.io/github/last-commit/parcifal%2FRomanPy?label=github+mirror)][github]

![RomanPy Logo](https://scm.parcifal.dev/parcifal/RomanPy/raw/branch/develop/assets/logo.png)

RomanPy is a Python library and CLI for converting decimal numbers to Roman 
numerals. It provides:

 - ASCII or Unicode output (with full support for Unicode numeral symbols)
 - Upper- and lowercase variants
 - Configurable numeral variants (subtractive, extended, apostrophus, medieval,
   zero, or custom mappings)
 - Arithmetic operations (+, -, *, //) between Roman numerals and integers
 - Equality and comparison with ints and strings

> Licensed under the [AGPLv3.0][license].

## Installation

RomanPy is available on PyPI and can be installed using `pip`:

```bash
pip install RomanPy
```

Alternatively, you can pull the repository and install it straight from the 
source:

```bash
git clone git@scm.parcifal.dev:parcifal/RomanPy.git
cd RomanPy
pip install .
```

## Usage (API)

### Basic Conversion

```python
from roman import roman

print(roman(207))  # CCVII
```

### Encoding and Case Variants

```bash
n = roman(1776)

print(n.encode("ascii").upper())   # MDCCLXXVI
print(n.encode("ascii").lower())   # mdcclxxvi
print(n.encode("unicode").upper()) # ⅯⅮⅭⅭⅬⅩⅩⅥ
print(n.encode("unicode").lower()) # ⅿⅾⅽⅽⅼⅹⅹⅵ
```

### Arithmetic with Roman Numerals

Roman numerals can be added, subtracted, multiplied, or divided with  
other Roman numerals or integers:

```python
print(roman(100) + roman(60))   # CLX
print(roman(45) - roman(7))     # XXXVIII
print(roman(533) * 2)           # MLXVI
print(roman(2460) // 10)        # CCXLVI

# mix with ints
print(100 + roman(60))          # CLX
print(roman(1954) == "MCMLIV")  # True
```

### Custom Variants

You can extend or override numeral variants:

```bash
from roman.roman import VARIANT_ZERO

n = roman(0).extend_variant(VARIANT_ZERO)
print(n)  # N
```

Built-in variants include:

 - `VARIANT_BASE` (I, V, X, …)
 - `VARIANT_SUBTRACTIVE` (IV, IX, XL, …)
 - `VARIANT_SUBTRACTIVE_EXTENDED` (IIX, IC, …)
 - `VARIANT_ZERO` (N)
 - `VARIANT_APOSTROPHUS` (large numbers with I) and ((I)))
 - `VARIANT_MEDIEVAL` (A, Z, O, …)

By default, `VARIANT_SUBTRACTIVE` is used.

## Usage (CLI)

Installing RomanPy also provides a roman command-line tool:

```bash
roman 42
# = XLII
```

### Options

```bash
usage: roman [-h] [-a | -A | -u | -U] [-b | -s | -e] [-z] [-p] [-m] [-c DECIMAL NUMERAL] [-v] [-V] value

Convert a decimal number to roman numeral.

positional arguments:
  value                 a decimal number to convert to a roman numeral

optional arguments:
  -h, --help            show this help message and exit
  -a, --ascii           output encoding of roman numerals in lowercase ascii
  -A, --ASCII           output encoding of roman numerals in uppercase ascii (default)
  -u, --unicode         output encoding of roman numerals in lowercase unicode
  -U, --UNICODE         output encoding of roman numerals in uppercase unicode
  -b, --no-base         do not use the base variant
  -s, --subtractive     use the subtractive variant (includes base) (default)
  -e, --subtractive-extended
                        use the extended subtractive variant(includes subtractive)
  -z, --zero            use the zero variant N
  -p, --apostrophus     use the apostrophus method for large numbers
  -m, --medieval        use the medieval variant
  -c DECIMAL NUMERAL, --custom DECIMAL NUMERAL
                        map a decimal number to a roman numeral
  -v, --verbose         increase verbosity
  -V, --version         show program's version number and exit
```

## Contributing

Found a bug? Have a suggestion? Open an issue or submit a merge request at 
[the Forgejo repository](https://scm.parcifal.dev/parcifal/RomanPy). All 
contributions are welcome.

[license]: https://scm.parcifal.dev/parcifal/RomanPy/src/branch/master/LICENSE

[release]: https://scm.parcifal.dev/parcifal/RomanPy/releases/latest
[gitlab]: https://gitlab.com/parcifal/RomanPy
[github]: https://github.com/parcifal/RomanPy
[develop]: https://scm.parcifal.dev/parcifal/RomanPy/src/branch/develop
[master]: https://scm.parcifal.dev/parcifal/RomanPy/src/branch/master

[pypi]: https://pypi.org/project/RomanPy/
