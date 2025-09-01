import io
import math
import unittest

from contextlib import redirect_stdout

from src.base_convert import base_convert
from src.compress import compress
from src.deg_to_rad import deg_to_rad
from src.sort import sort
from src.str_to_hex import str_to_hex

def str_to_text_output(s: str) -> str:
    """Run str_to_hex on the given string and return its output

    Args:
        s (str): String to convert to hex

    Returns:
        str: Hex string
    """
    buf = io.StringIO()
    with redirect_stdout(buf):
        try:
            str_to_hex(s)
        except Exception as e:
            # Return a sentinel so tests can assert no accidental output on exceptions
            output = buf.getvalue()
            return f"__EXC__:{type(e).__name__}:{str(e)}|OUT:{output!r}"
    return buf.getvalue().strip()

def base_convert_output(value: int, new_base: int) -> str:
    """Run base_convert while capturing stdout; return printed text without trailing newline.

    Args:
        value (int): Value to convert to hex
        new_base (int): New base to convert to
    Returns:
        str: Hex string
    """
    buf = io.StringIO()
    with redirect_stdout(buf):
        try:
            base_convert(value, new_base)
        except Exception as e:
            # Return a sentinel so tests can assert no accidental output on exceptions
            output = buf.getvalue()
            return f"__EXC__:{type(e).__name__}:{str(e)}|OUT:{output!r}"
    return buf.getvalue().strip()

class TestDegToRad(unittest.TestCase):

    def test_zero_degrees(self):
        self.assertAlmostEqual(0.0, deg_to_rad(0))

    def test_ninety_degrees(self):
        self.assertAlmostEqual(math.pi / 2, deg_to_rad(90))

    def test_one_eighty_degrees(self):
        self.assertAlmostEqual(math.pi, deg_to_rad(180))

    def test_two_seventy_degrees(self):
        self.assertAlmostEqual(3 * math.pi / 2, deg_to_rad(270))

    def test_three_sixty_degrees(self):
        self.assertAlmostEqual(2 * math.pi, deg_to_rad(360))

    def test_negative_angle(self):
        self.assertAlmostEqual(-math.pi / 2, deg_to_rad(-90))

    def test_large_angle(self):
        self.assertAlmostEqual(4 * math.pi, deg_to_rad(720))

    def test_compare_with_math_radians(self):
        for deg in [0, 15, 30, 45, 60, 90, 123, 180, -45, -180, 360]:
            with self.subTest(deg=deg):
                self.assertAlmostEqual(math.radians(deg), deg_to_rad(deg))

class TestSort(unittest.TestCase):
    def test_sort_ascending_numbers(self):
        self.assertEqual([1, 2, 3], sort([3, 1, 2], 'asc'))

    def test_sort_descending_numbers(self):
        self.assertEqual([3, 2, 1], sort([3, 1, 2], 'desc'))

    def test_sort_none_returns_original(self):
        data = [5, 2, 9]
        self.assertEqual(data, sort(data, 'none'))

    def test_empty_list(self):
        self.assertEqual([], sort([], 'asc'))
        self.assertEqual([], sort([], 'desc'))
        self.assertEqual([], sort([], 'none'))

    def test_duplicates_in_list(self):
        self.assertEqual([1, 2, 4, 4], sort([4, 2, 4, 1], 'asc'))
        self.assertEqual([4, 4, 2, 1], sort([4, 2, 4, 1], 'desc'))

    def test_strings_sorting(self):
        self.assertEqual(['a', 'b', 'c'], sort(['b', 'a', 'c'], 'asc'))
        self.assertEqual(['c', 'b', 'a'], sort(['b', 'a', 'c'], 'desc'))

    def test_invalid_direction_raises(self):
        with self.assertRaises(ValueError):
            sort([1, 2, 3], 'up')

    def test_list_with_mixed_types(self):
        # Sorting of mixed types (str, int) is invalid in Python 3
        with self.assertRaises(TypeError):
            sort([1, "a", 3], 'asc')

class TestCompress(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(compress(""), "")

    def test_single_character(self):
        self.assertEqual("1a", compress("a"))

    def test_no_repeats(self):
        self.assertEqual("1a1b1c", compress("abc"))

    def test_simple_repeats(self):
        self.assertEqual("3a2b", compress("aaabb"))

    def test_multiple_runs(self):
        self.assertEqual("1a3b5c3d", compress("abbbcccccddd"))

    def test_all_same_character(self):
        self.assertEqual("4a", compress("aaaa"))

    def test_numbers_and_symbols(self):
        self.assertEqual("312!", compress("111!!"))

    def test_case_sensitivity(self):
        # 'a' vs 'A' should be distinct
        self.assertEqual("2a2A", compress("aaAA"))

class TestBaseConvert(unittest.TestCase):
    # --- Error handling ---
    def test_raises_when_base_less_than_2(self):
        out = base_convert_output(10, 1)
        self.assertTrue(out.startswith("__EXC__:ValueError:Base must be >= 2"),
                        f"Expected ValueError for base < 2; got {out}")

    def test_raises_when_base_negative(self):
        out = base_convert_output(10, -2)
        self.assertTrue(out.startswith("__EXC__:ValueError:Base must be >= 2"),
                        f"Expected ValueError for base < 2; got {out}")

    # --- Zero ---
    def test_zero_prints_single_zero(self):
        self.assertEqual("0", base_convert_output(0, 2))

    # --- Positive values ---
    def test_binary_conversion(self):
        self.assertEqual("1010", base_convert_output(10, 2))

    def test_hex_conversion_uppercase_letters(self):
        # 31 -> 1F in base 16
        self.assertEqual("1F", base_convert_output(31, 16))

    def test_base_36_uses_letters(self):
        # 35 -> Z, 36 -> 10
        self.assertEqual("Z", base_convert_output(35, 36))
        self.assertEqual("10", base_convert_output(36, 36))

    def test_small_numbers(self):
        self.assertEqual("1", base_convert_output(1, 2))
        self.assertEqual("10", base_convert_output(2, 2))
        self.assertEqual("10", base_convert_output(7, 7))

    # --- Negative values ---
    def test_negative_values_have_leading_minus(self):
        # 42 in base 5 = 132 -> expect "-132"
        self.assertEqual("-132", base_convert_output(-42, 5), )

    # --- Formatting guarantees ---
    def test_no_extra_whitespace_or_blank_output(self):
        out = base_convert_output(255, 8)  # 255 -> 377
        self.assertEqual(out, "377")
        # Ensure no internal spaces for this case
        self.assertNotIn(" ", out)


class TestStrToHex(unittest.TestCase):
    def test_empty(self):
        self.assertEqual("", str_to_text_output(""))

    def test_basic(self):
        self.assertEqual("41 42 43", str_to_text_output("ABC"))

    def test_lowercase(self):
        self.assertEqual("68 65 6C 6C 6F", str_to_text_output("hello"))

    def test_padding(self):
        self.assertEqual("00 07", str_to_text_output("\x00\x07"))

    def test_non_ascii(self):
        self.assertEqual("C5", str_to_text_output("Å"))


if __name__ == '__main__':
    unittest.main()