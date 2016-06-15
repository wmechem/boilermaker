""" Builds a skeleton python program file
w. mechem 6/8/2016
pylint 6/15/2016
flake8

Usage: py_boilermaker.py --name 'module_name.py' --imports --main --tests

Defaults are to NOT INCLUDE import statements, main function, or tests.

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

from datetime import datetime
import argparse

from template import function_definitions, imports, tests

ARGS = None


def add_arguments():
    """ Add arguments from command line to parser. """

    parser = argparse.ArgumentParser()

    parser.add_argument("--user", help="Specify user name",
                        default='wmechem@gmail.com')
    parser.add_argument("--name", help="Specify module name",
                        default='test.py')
    parser.add_argument("--date", help="Optional create or modify date",
                        default=str(datetime.now()))
    parser.add_argument("--desc", help="Description of the module, doc string",
                        default="Test Module Boilerplate")
    parser.add_argument("--tests", help="Generate Unittests",
                        action='store_true')
    parser.add_argument("--imports", help="Include import statements",
                        action='store_true')
    parser.add_argument("--main", help="Generate main()",
                        action='store_true')

    args = parser.parse_args()

    return args


class Boilerplate(object):
    """ Create class instance with template methods. """

    def __init__(self):
        self.function_defs = None
        self.args = add_arguments()
        self._file = None
        self.tests = None
        self.imports = None
        self.line_ret = '\n'

    def gen_comments(self):
        """ Generate the docstring for the first few lines of the program. """
          # line return
        header_comments_section = '"""' + self.line_ret
        header_comments_section += self.args.name + self.line_ret
        header_comments_section += self.args.user + self.line_ret
        header_comments_section += self.args.date + self.line_ret
        header_comments_section += self.args.desc + self.line_ret
        header_comments_section += '"""' + self.line_ret
        print(header_comments_section)

        self.write_to_file(header_comments_section)

        return

    def gen_imports(self):
        """Add imports section. """
        self.imports = imports()
        #[self.write_to_file(name + self.line_ret) for name in imports]
        for name in self.imports:
            self.write_to_file("import " + name + self.line_ret)

    def write_to_file(self, text):
        """ Write contents to module file. """
        _file = self.args.name
        with open(_file, 'a') as out_file:
            out_file.write(text)
        return

    def gen_sections(self):
        """ Generate boilerplate for function definitions. """

        self.function_defs = function_definitions()

        def gen_section_text(name, params):
            """ Generate each line for function definitions. """
            print(name, params)
            section_text = ''
            section_text += self.line_ret * 2
            section_text += 'def '
            section_text += name + '(' + params + '):' + self.line_ret
            section_text += ' ' * 4
            section_text += '""" Doc string for ' + name + '. """'
            section_text += self.line_ret
            section_text += ' ' * 4
            section_text += 'pass'
            section_text += self.line_ret
            section_text += ' ' * 4
            section_text += 'return out_param'
            section_text += self.line_ret

            self.write_to_file(section_text)

            return

        for function_def in self.function_defs:
            function_name = function_def['name']
            params = ", ".join(function_def['params'])
            print(function_name, params)

            gen_section_text(function_name, params)

        return

    def gen_tests(self):
        """ Generate boilerplate for function definitions. """

        self.tests = tests()

        def gen_assert_tests(function_name, test_name):
            """ Generate each line for function definitions. """
            if function_name.find('_') != -1:
            # Convert case to comply with PEP-8 standard for Class names
                class_name = function_name.replace(
                    function_name[function_name.find('_') + 1],
                    function_name[function_name.find('_') + 1].title())

                class_name = class_name.replace('_', '')

                class_name = class_name.replace(class_name[0],
                    class_name[0].title())

            else:
                class_name = function_name.title()

            test_text = ''
            test_text += self.line_ret * 2
            test_text += 'class Test' + class_name
            test_text += 'NotEqual(unittest.TestCase):'
            test_text += self.line_ret
            test_text += ' ' * 4
            test_text += '""" Unittest """' + self.line_ret
            test_text += ' ' * 4
            test_text += '# pylint: disable=R0904' + self.line_ret
            test_text += ' ' * 4
            test_text += 'def setUp(self):' + self.line_ret
            test_text += ' ' * 8
            test_text += 'self.results = (None)' + self.line_ret
            test_text += ' ' * 8
            test_text += 'self.test_data = (123)  # change this!!!!'
            test_text += self.line_ret * 2
            test_text += ' ' * 4
            test_text += 'def test_function(self):' + self.line_ret
            test_text += ' ' * 8
            test_text += '""" Test function Assert Equal """' + self.line_ret
            test_text += ' ' * 8
            test_text += test_name + '(self.results, ' + function_name
            test_text += '(self.test_data))' + self.line_ret
              # 2 lines before next Class

            self.write_to_file(test_text)

            return

        for function_def in self.function_defs:
            function_name = str(function_def['name'])

            for test_name in self.tests:
                gen_assert_tests(function_name, test_name)

        return

    def gen_main(self):
        """Add __main__ with calls to functions. """
        run_text = ""
        run_text += self.line_ret * 2
        run_text += 'def main():'
        run_text += self.line_ret
        run_text += ' ' * 4
        run_text += '""" Execute functions in order. """'
        run_text += self.line_ret

        for function_def in self.function_defs:
            function_name = str(function_def['name'])
            run_text += ' ' * 4
            run_text += function_name + '()'
            run_text += self.line_ret

        run_text += self.line_ret * 2
        run_text += 'if __name__ == "__main__":'
        run_text += self.line_ret
        run_text += ' ' * 4
        run_text += 'unittest.main()'
        run_text += self.line_ret
        run_text += ' ' * 4
        run_text += 'main()'
        run_text += self.line_ret * 2

        self.write_to_file(run_text)

        return


def main():
    """ Execute pipeline functions to build boilerplate file. """
    arguments = add_arguments()
    boilerplate = Boilerplate()

    boilerplate.gen_comments()

    if arguments.imports is not False:
        boilerplate.gen_imports()

    boilerplate.gen_sections()

    if arguments.tests is not False:
        boilerplate.gen_tests()

    if arguments.main is not False:
        boilerplate.gen_main()

if __name__ == '__main__':
    main()
