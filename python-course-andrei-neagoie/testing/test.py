import unittest
import main


# now functionality of TestCase is availabe in our class TestMain
class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        # this will before every tets
        print('about to test a function')
        return super().setUp()

    def tearDown(self) -> None:
        # this will run after every function (test)
        print("Cleaning up")
        return super().tearDown()

    def test_do_stuff(self) -> None:
        '''
        Do Stuff function gives the correct result
        '''
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, test_param + 5)

    def test_do_stuff2(self) -> None:
        '''
        Do Stuff function gives the ValueError if param is string instead of integer
        '''
        test_param = 'umerkang'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self) -> None:
        '''
        Do Stuff function returns string "please return a number", when None is passed as parameter
        '''
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please return a number')

    def test_do_stuff4(self) -> None:
        '''
        Do Stuff function returns string "please return a number", when empty string is passed as parameter
        '''
        test_param = ""
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please return a number')


# if we only run this file using python test.py, then only these tests will run
if __name__ == "__main__":
    # this will run all the tests in class TestMain
    unittest.main()

# command to run all test files
# python -m unittest
