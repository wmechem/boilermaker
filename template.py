"""
w.mechem
6/10/2016
Config module to define function names, imports, and tests
that are imported by boilermaker.py
pylint 10/10 6/10/2016
flake8 6/10/2016

Copyright 2016 Willard H. Mechem, III

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

"""


def function_definitions():
    """ Make function definitions for these function names and paramters
    i.e., [dict(name='name', params=('a','b')),]
    """

    function_defs = [
        dict(name='open_file',
             params=('file_name', 'mode', 'encoding')),
        dict(name='read_file',
             params=('file_name', 'mode', 'encoding')),
        dict(name='parse_text',
             params=('text',)),
        dict(name='write_to_db',
             params=('db_name', 'table_name')),
        ]

    return function_defs


def imports():
    """ Make import statements for these modules. """
    imports_list = [
        'io',
        'unittest'
        ]
    return imports_list


def tests():
    """ Make these Unittests for each function. """
    tests_list = [
        'assertNotEqual',
        'assertEqual'
        ]
    return tests_list
