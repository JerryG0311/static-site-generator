import unittest
from gencontent import extract_title

class TestGenContent(unittest.TestCase):

    def test_has_header(self):
        text = "# Hello"
        extracted_title = extract_title(text)
        expected = "Hello"
        self.assertEqual(expected, extracted_title)

    def test_no_header(self):
        text = "Hello"
        with self.assertRaises(Exception):
            extract_title(text)




if __name__ == "__main__":
    unittest.main()