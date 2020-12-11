import unittest, datetime
import my_module
from my_module import MyClass, SomeOtherClass
from mock import patch, Mock


class SomeOtherClassTest(unittest.TestCase):

    # To mock a method in a class to return a specific value use @patch.object.
    @patch.object(my_module.MyClass, 'my_method')
    def test_my_method_shouldReturnTrue_whenMyMethodReturnsSomeValue(self, mock_my_method):
        # setup
        mock_my_method.return_value = True
        some_other_class = SomeOtherClass()

        # execute
        result = some_other_class.method_under_test()

        # assert
        self.assertTrue(result)

    # To mock a method in a class with @patch.object but return a different value each time it is called,
    # use side_effect. Side effect allows you to define a custom method and have that method called each time
    # your mock method is called. The value returned from this method will be used as the return value for
    # your mock method.
    @patch('my_module.MyClass')
    def test_my_method_shouldCallMyClassMethodMyMethod_whenSomeOtherClassMethodIsCalled(self, mock_my_class):
        # setup
        some_other_class = SomeOtherClass()

        # execute
        some_other_class.method_under_test()

        # assert
        self.assertTrue(mock_my_class.called)

    # To mock an entire class to test interactions with that class use @patch.
    @patch('my_module.MyClass')
    def test_my_method_shouldReturnTrue_whenSomeOtherClassMethodIsCalledAndAReturnValueIsSet(self, mock_my_class):
        # setup
        mc = mock_my_class.return_value
        mc.my_method.return_value = True
        some_other_class = SomeOtherClass()

        # execute
        result = some_other_class.method_under_test()

        # assert
        self.assertTrue(result)

    # To mock an entire class with @patch and still set the return value of a method in that class,
    # grab the instance of the mock object’s return value and set the method’s return value on the instance.
    # There is a section on the patch page explaining how to do this.
    @patch.object(my_module.MyClass, 'my_method')
    def test_my_method_shouldReturnMultipleValues_whenMyMethodReturnsSomeValue(self, mock_my_method):
        # setup
        list_of_return_values = [True, False, False]

        def side_effect():
            return list_of_return_values.pop()

        mock_my_method.side_effect = side_effect

        # execute
        some_other_class = SomeOtherClass()

        # assert
        self.assertFalse(some_other_class.method_under_test())
        self.assertFalse(some_other_class.method_under_test())
        self.assertTrue(some_other_class.method_under_test())


if __name__ == '__main__':
    unittest.main()
