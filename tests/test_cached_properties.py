from django.utils.functional import cached_property


class MyClass:
    def __init__(self, value):
        self._value = value

    @cached_property
    def method_as_cached_property(self):
        return self._value

    @property
    def method_as_property(self):
        return self._value

    def just_method(self):
        return self._value


def test001_that_cached_propery_stays_up_to_date():

    my_object = MyClass("original_value")

    assert my_object._value == "original_value"
    assert my_object.just_method() == "original_value"
    assert my_object.method_as_property == "original_value"
    assert my_object.method_as_cached_property == "original_value"

    my_object._value = "NEW_VALUE"

    assert my_object._value == "NEW_VALUE"
    assert my_object.just_method() == "NEW_VALUE"
    assert my_object.method_as_property == "NEW_VALUE"

    # ---- Notice cached_property still has the original value until deleted ---- #
    assert my_object.method_as_cached_property == "original_value"

    del my_object.method_as_cached_property

    assert my_object.method_as_cached_property == "NEW_VALUE"
