from django.test import TestCase

_test_case = TestCase()

assert_contains = _test_case.assertContains
assert_not_contains = _test_case.assertNotContains
assert_template_use = _test_case.assertTemplateUsed
