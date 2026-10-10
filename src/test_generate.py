import unittest

from generate import *


class TestGenerate(unittest.TestCase):
    def test_markdown_to_title(self):
        md = """
#  This is the title  
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
- This is a list
- with items
"""
        self.assertEqual(
            extract_title(md),
            'This is the title',
        )

    def test_markdown_to_title_mid(self):
        md = """
## This is the second header  
#  This is the title in the middle 
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
- This is a list
- with items
"""
        self.assertEqual(
            extract_title(md),
            'This is the title in the middle',
        )


if __name__ == "__main__":
    unittest.main()
