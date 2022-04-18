import unittest
from get_first_link import _get_first_link_helper


class TestSuite(unittest.TestCase):
    def test_valid_page(self):
        with open("downloaded/epistemology.txt", "r") as f:
            html = f.read()
        self.assertEqual(
            _get_first_link_helper(html, []),
            "https://en.wikipedia.org/wiki/Ancient_Greek_language",
        )

    def test_valid_page_revisit(self):
        with open("downloaded/epistemology.txt", "r") as f:
            html = f.read()
        self.assertEqual(
            _get_first_link_helper(
                html, ["https://en.wikipedia.org/wiki/Ancient_Greek_language"]
            ),
            "https://en.wikipedia.org/wiki/-logy",
        )

    def test_invalid_page(self):
        with open("downloaded/invalid_article.txt", "r") as f:
            html = f.read()
        self.assertEqual(
            _get_first_link_helper(html, []),
            None,
        )


if __name__ == "__main__":
    unittest.main()
