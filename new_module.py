"""
new_module.py
someuser@somedomain.com
2016-06-16 13:01:02.543783
Test Module Boilerplate
"""
import io
import unittest


def open_file(file_name, mode, encoding):
    """ Doc string for functionopen_file. """
    return


def read_file(file_name, mode, encoding):
    """ Doc string for functionread_file. """
    return


def parse_text(text):
    """ Doc string for functionparse_text. """
    return


def write_to_db(db_name, table_name):
    """ Doc string for functionwrite_to_db. """
    return


class Dbadapter(object):
    """ Doc string for class Dbadapter. """
    def __init__(self, host, database, port):
        self.host = host
        self.database = database
        self.port = port

    def __str__(self, cls):
        return str(cls.__class__.__name__)

class Person(object):
    """ Doc string for class Person. """
    def __init__(self, last_name, first_name, street, city, state, zipcode):
        self.last_name = last_name
        self.first_name = first_name
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self, cls):
        return str(cls.__class__.__name__)

class Organization(object):
    """ Doc string for class Organization. """
    def __init__(self, name, industry, revenues, employees, ticker):
        self.name = name
        self.industry = industry
        self.revenues = revenues
        self.employees = employees
        self.ticker = ticker

    def __str__(self, cls):
        return str(cls.__class__.__name__)

class TestOpenFileassertNotEqual(unittest.TestCase):
    """ Unittest """
    # pylint: disable=R0904
    def setUp(self):
        self.results = (None)
        self.test_data = (123)  # change this!!!!

    def test_function(self):
        """ Test function Assert Equal """
        assertNotEqual(self.results, open_file(self.test_data))


class TestOpenFileassertEqual(unittest.TestCase):
    """ Unittest """
    # pylint: disable=R0904
    def setUp(self):
        self.results = (None)
        self.test_data = (123)  # change this!!!!

    def test_function(self):
        """ Test function Assert Equal """
        assertEqual(self.results, open_file(self.test_data))


class TestReadFileassertNotEqual(unittest.TestCase):
    """ Unittest """
    # pylint: disable=R0904
    def setUp(self):
        self.results = (None)
        self.test_data = (123)  # change this!!!!

    def test_function(self):
        """ Test function Assert Equal """
        assertNotEqual(self.results, read_file(self.test_data))


class TestReadFileassertEqual(unittest.TestCase):
    """ Unittest """
    # pylint: disable=R0904
    def setUp(self):
        self.results = (None)
        self.test_data = (123)  # change this!!!!

    def test_function(self):
        """ Test function Assert Equal """
        assertEqual(self.results, read_file(self.test_data))


class TestParseTexTassertNotEqual(unittest.TestCase):
    """ Unittest """
    # pylint: disable=R0904
    def setUp(self):
        self.results = (None)
        self.test_data = (123)  # change this!!!!

    def test_function(self):
        """ Test function Assert Equal """
        assertNotEqual(self.results, parse_text(self.test_data))


class TestParseTexTassertEqual(unittest.TestCase):
    """ Unittest """
    # pylint: disable=R0904
    def setUp(self):
        self.results = (None)
        self.test_data = (123)  # change this!!!!

    def test_function(self):
        """ Test function Assert Equal """
        assertEqual(self.results, parse_text(self.test_data))


class TestWriTeTodbassertNotEqual(unittest.TestCase):
    """ Unittest """
    # pylint: disable=R0904
    def setUp(self):
        self.results = (None)
        self.test_data = (123)  # change this!!!!

    def test_function(self):
        """ Test function Assert Equal """
        assertNotEqual(self.results, write_to_db(self.test_data))


class TestWriTeTodbassertEqual(unittest.TestCase):
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

