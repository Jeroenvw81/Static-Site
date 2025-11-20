import unittest

from gencontent import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_eq(self):
        actual = extract_title("# This is a title")
        self.assertEqual(actual, "This is a title")

    def test_eq_double(self):
        actual = extract_title(
            """
# This is a title

# This is a superfluous title
"""
        )
        self.assertEqual(actual, "This is a title")

    def test_Error(self):
        try:
            extract_title(
            """
This is a faulty title
"""
        )
            self.fail("Should have raised an exception")
        except Exception as e:
            pass
    def test_Error_2(self):
        with self.assertRaises(ValueError):
            extract_title(
                """
## Definitely not an actual title
"""
            )

if __name__ == "__main__":
    unittest.main()

    