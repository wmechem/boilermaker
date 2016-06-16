"""
new_module.py
someuser@somedomain.com
2016-06-16 10:43:44.611795
Test Module Boilerplate
"""
import io
import unittest


def open_file(file_name, mode, encoding):
    """ Doc string for open_file. """
    pass
    return out_param


def read_file(file_name, mode, encoding):
    """ Doc string for read_file. """
    pass
    return out_param


def parse_text(text):
    """ Doc string for parse_text. """
    pass
    return out_param


def write_to_db(db_name, table_name):
    """ Doc string for write_to_db. """
    pass
    return out_param


class TestOpenFileNotEqual(unittest.TestCase):
    """ Unittest """
    # pylint: disable=R0904
    def setUp(self):
        self.results = (None)
        self.test_data = (123)  # change this!!!!

    def test_function(self):
        """ Test function Assert Equal """
        assertNotEqual(self.results, open_file(self.test_data))


class TestOpenFileNotEqual(unittest.TestCase):
    """ Unittest """
    # pylint: disable=R0904
    def setUp(self):
        self.results = (None)
        self.test_data = (123)  # change this!!!!

    def test_function(self):
        """ Test function Assert Equal """
        assertEqual(self.results, open_file(self.test_data))


class TestReadFileNotEqual(unittest.TestCase):
    """ Unittest """
    # pylint: disable=R0904
    def setUp(self):
        self.results = (None)
        self.test_data = (123)  # change this!!!!

    def test_function(self):
        """ Test function Assert Equal """
        assertNotEqual(self.results, read_file(self.test_data))


class TestReadFileNotEqual(unittest.TestCase):
    """ Unittest """
    # pylint: disable=R0904
    def setUp(self):
        self.results = (None)
        self.test_data = (123)  # change this!!!!

    def test_function(self):
        """ Test function Assert Equal """
        assertEqual(self.results, read_file(self.test_data))


class TestParseTexTNotEqual(unittest.TestCase):
    """ Unittest """
    # pylint: disable=R0904
    def setUp(self):
        self.results = (None)
        self.test_data = (123)  # change this!!!!

    def test_function(self):
        """ Test function Assert Equal """
        assertNotEqual(self.results, parse_text(self.test_data))


class TestParseTexTNotEqual(unittest.TestCase):
    """ Unittest """
    # pylint: disable=R0904
    def setUp(self):
        self.results = (None)
        self.test_data = (123)  # change this!!!!

    def test_function(self):
        """ Test function Assert Equal """
        assertEqual(self.results, parse_text(self.test_data))


class TestWriTeTodbNotEqual(unittest.TestCase):
    """ Unittest """
    # pylint: disable=R0904
    def setUp(self):
        self.results = (None)
        self.test_data = (123)  # change this!!!!

    def test_function(self):
        """ Test function Assert Equal """
        assertNotEqual(self.results, write_to_db(self.test_data))


class TestWriTeTodbNotEqual(unittest.TestCase):
    """ Unittest """
    # pylint: disable=R0904
    def setUp(self):
        self.results = (None)
        self.test_data = (123)  # change this!!!!

    def test_function(self):
        """ Test function Assert Equal """
        assertEqual(self.results, write_to_db(self.test_data))


def main():
    """ Execute functions in order. """
    open_file()
    read_file()
    parse_text()
    write_to_db()


if __name__ == "__main__":
    unittest.main()
    main()

