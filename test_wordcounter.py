import unittest
import wordcounter
from io import StringIO


class TestWordCounter(unittest.TestCase):
    def test_process_line(self):
        line = "these words are my test words"

        counters = {}
        words = wordcounter.process_line(line, counters)

        expected = {
            "words": 2,
            "these": 1,
            "are": 1,
            "my": 1,
            "test": 1
        }

        for word in expected:
            count = expected[word]
            self.assertEqual(counters[word]["count"], count)

        self.assertEqual(len(expected), len(counters))
        self.assertEqual(words, 6)

    def test_process_data(self):
        data_sources = []

        data_sources.append("""
        This is a supposed test file.
        This file has two lines with data.
        """.split("\n"))

        data_sources.append("""
        Another fake file with fake lines.
        """.split("\n"))

        words, counters = wordcounter.process_data(data_sources)

        self.assertEqual(words, 19)
        self.assertEqual(counters["file"]["count"], 3)
        self.assertEqual(counters["This"]["count"], 2)


if __name__ == '__main__':
    unittest.main()