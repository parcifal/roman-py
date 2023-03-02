"""
Tests for the Roman class.
"""
from unittest import TestCase

from roman import roman

TEST_ROMAN_NUMERALS_ASCII_UPPER = {
    39: "XXXIX",
    246: "CCXLVI",
    789: "DCCLXXXIX",
    2421: "MMCDXXI",
    160: "CLX",
    207: "CCVII",
    1009: "MIX",
    1066: "MLXVI",
    1776: "MDCCLXXVI",
    1918: "MCMXVIII",
    1954: "MCMLIV",
    2014: "MMXIV"
}

TEST_ROMAN_NUMERALS_ASCII_LOWER = {
    v: c.lower() for v, c in TEST_ROMAN_NUMERALS_ASCII_UPPER.items()
}

TEST_ROMAN_NUMERALS_UNICODE_UPPER = {
    39: "ⅩⅩⅩⅨ",
    246: "ⅭⅭⅩⅬⅥ",
    789: "ⅮⅭⅭⅬⅩⅩⅩⅨ",
    2421: "ⅯⅯⅭⅮⅩⅪ",
    160: "ⅭⅬⅩ",
    207: "ⅭⅭⅦ",
    1009: "ⅯⅨ",
    1066: "ⅯⅬⅩⅥ",
    1776: "ⅯⅮⅭⅭⅬⅩⅩⅥ",
    1918: "ⅯⅭⅯⅩⅧ",
    1954: "ⅯⅭⅯⅬⅣ",
    2014: "ⅯⅯⅩⅣ"
}

TEST_ROMAN_NUMERALS_UNICODE_LOWER = {
    39: "ⅹⅹⅹⅸ",
    246: "ⅽⅽⅹⅼⅵ",
    789: "ⅾⅽⅽⅼⅹⅹⅹⅸ",
    2421: "ⅿⅿⅽⅾⅹⅺ",
    160: "ⅽⅼⅹ",
    207: "ⅽⅽⅶ",
    1009: "ⅿⅸ",
    1066: "ⅿⅼⅹⅵ",
    1776: "ⅿⅾⅽⅽⅼⅹⅹⅵ",
    1918: "ⅿⅽⅿⅹⅷ",
    1954: "ⅿⅽⅿⅼⅳ",
    2014: "ⅿⅿⅹⅳ"
}


class TestRoman(TestCase):
    """
    A test case for the Roman class.
    """

    def test_roman_int_to_ascii_upper(self):
        """
        Assert that a decimal number can be converted to
        an ASCII upper-case roman numeral.
        """
        for value, numeral in TEST_ROMAN_NUMERALS_ASCII_UPPER.items():
            with self.subTest(value=value):
                self.assertEqual(numeral, str(roman(value)))

    def test_roman_int_to_ascii_lower(self):
        """
        Assert that a decimal number can be converted to
        an ASCII lower-case roman numeral.
        """
        for value, numeral in TEST_ROMAN_NUMERALS_ASCII_LOWER.items():
            with self.subTest(value=value):
                self.assertEqual(numeral, str(roman(value).lower()))

    def test_roman_int_to_unicode(self):
        """
        Assert that a decimal number can be converted to
        a unicode roman numeral.
        """
        for value, numeral in TEST_ROMAN_NUMERALS_UNICODE_UPPER.items():
            with self.subTest(value=value):
                self.assertEqual(numeral, str(roman(value).encode("unicode")))

    def test_roman_int_to_unicode_lower(self):
        """
        Assert that a decimal number can be converted to
        a unicode lower-case roman numeral.
        """
        for value, numeral in TEST_ROMAN_NUMERALS_UNICODE_LOWER.items():
            with self.subTest(value=value):
                self.assertEqual(
                    numeral, str(roman(value).encode("unicode").lower()))

    def test_roman_eq_roman(self):
        """
        Assert that two roman numerals of equal value are equal.
        """
        self.assertEqual(roman(1), roman(1))

    def test_roman_ne_roman(self):
        """
        Assert that two roman numerals of differt value are not equal.
        """
        self.assertNotEqual(roman(1), roman(2))

    def test_roman_eq_int(self):
        """
        Assert that a roman numeral and decimal number
        of equal value are equal.
        """
        self.assertEqual(1, roman(1))

    def test_roman_ne_int(self):
        """
        Assert that a roman numeral and decimal number
        of different value are not equal.
        """
        self.assertNotEqual(2, roman(1))

    def test_roman_eq_str(self):
        """
        Assert that a roman numeral and a string representing
        a roman numeral of equal value are equal.
        """
        self.assertEqual("I", roman(1))

    def test_roman_ne_str(self):
        """
        Assert that a roman numeral and a string not representing
        a roman numeral of equal value are not equal.
        """
        self.assertNotEqual("II", roman(1))

    def test_roman_gt_roman(self):
        """
        Assert that a roman numeral is greater than
        another roman numeral of lesser value.
        """
        self.assertGreater(roman(2), roman(1))

    def test_roman_gt_int(self):
        """
        Assert that a roman numeral is greater than
        an integer of lesser value.
        """
        self.assertLess(roman(1), 2)

    def test_roman_lt_roman(self):
        """
        Assert that a roman numeral is lesser than
        another roman numeral of greater value.
        """
        self.assertLess(roman(1), roman(2))

    def test_roman_lt_int(self):
        """
        Assert that a roman numeral is lesser than
        an integer of greater value.
        """
        self.assertLess(roman(1), 2)

    def test_roman_ge_roman(self):
        """
        Assert that a roman numeral is greater than or equal to
        another roman numeral of lesser or equal value.
        """
        with self.subTest():
            self.assertGreaterEqual(roman(2), roman(1))
        with self.subTest():
            self.assertGreaterEqual(roman(1), roman(1))

    def test_roman_ge_int(self):
        """
        Assert that a roman numeral is greater than or equal to
        an integer of lesser or equal value.
        """
        with self.subTest():
            self.assertGreaterEqual(2, roman(1))
        with self.subTest():
            self.assertGreaterEqual(roman(1), roman(1))

    def test_roman_le_roman(self):
        """
        Assert that a roman numeral is less than or equal to
        another roman numeral of greater or equal value.
        """
        with self.subTest():
            self.assertLessEqual(1, roman(2))
        with self.subTest():
            self.assertLessEqual(roman(1), 1)

    def test_roman_add_roman(self):
        """
        Assert that a roman numeral can be added to another roman numeral.
        """
        self.assertEqual(2, roman(1) + roman(1))

    def test_roman_add_int(self):
        """
        Assert that a decimal can be added to a roman numeral.
        """
        self.assertEqual(2, roman(1) + 1)

    def test_roman_sub_roman(self):
        """
        Assert that a roman numeral can be subtracted
        from another roman numeral.
        """
        self.assertEqual(1, roman(2) - roman(1))

    def test_roman_sub_int(self):
        """
        Assert that a decimal can be subtracted from a roman numeral.
        """
        self.assertEqual(1, roman(2) - 1)

    def test_roman_mul_roman(self):
        """
        Assert that a roman numeral can be multiplied with another
        roman numeral.
        """
        self.assertEqual(2, roman(1) * roman(2))

    def test_roman_mul_int(self):
        """
        Assert that a roman numeral can be multiplied with decimal.
        """
        self.assertEqual(2, roman(1) * 2)

    def test_roman_truediv_roman(self):
        """
        Assert that a roman numeral can be true divided
        by another roman numeral.
        """
        self.assertEqual(1, roman(2) / roman(2))

    def test_roman_truediv_int(self):
        """
        Assert that a roman numeral can be true divided by a decimal.
        """
        self.assertEqual(1, roman(2) / 2)

    def test_roman_floordiv_roman(self):
        """
        Assert that a roman numeral can be floor divided
        by another roman numeral.
        """
        self.assertEqual(1, roman(2) // roman(2))

    def test_roman_floordiv_int(self):
        """
        Assert that a roman numeral can be floor divided by a decimal.
        """
        self.assertEqual(1, roman(2) // 2)
