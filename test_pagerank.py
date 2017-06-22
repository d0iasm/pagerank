import unittest
from pagerank import Pagerank


class TestPagerank(unittest.TestCase):
    def test_init(self):
        pagerank = Pagerank("wikipedia_links/small_links.txt", "wikipedia_links/small_pages.txt")
        self.assertEqual(5, pagerank.edge)
        self.assertEqual(5, pagerank.vertex)
        self.assertEqual(5, len(pagerank.visited))

    def test_read(self):
        pagerank = Pagerank("wikipedia_links/small_links.txt", "wikipedia_links/small_pages.txt")
        pagerank.read()

    def test_rank(self):
        pagerank = Pagerank("wikipedia_links/small_links.txt", "wikipedia_links/small_pages.txt")
        self.assertRaises(Exception, pagerank.rank, -1)
        self.assertRaises(Exception, pagerank.rank, 100)
        self.assertRaises(Exception, pagerank.rank, "hoge")
        # TypeError: expected string or bytes-like object
        # pagerank.rank(0)
        # pagerank.rank(3.5)
        # pagerank.rank(30)
        # pagerank.rank(100)


if __name__ == '__main__':
    unittest.main()
