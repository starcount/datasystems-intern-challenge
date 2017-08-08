from unittest import TestCase
from validation.util import with_skip_not_implemented
from sort_merge_join.inner_equality import join


class TestInnerEquality(TestCase):

    @with_skip_not_implemented
    def test_empty(self):
        self.assertEqual(join([], [], 'a', 'a'), [])
        self.assertEqual(join(
            [{'a': 1, 'b': 1}],
            [], 'a', 'a'),
            [])
        self.assertEqual(join(
            [],
            [{'a': 1, 'b': 1}], 'a', 'a'),
            [])

    @with_skip_not_implemented
    def test_no_equality(self):
        self.assertEqual(join(
            [{'a': 1}],
            [{'a': 2}], 'a', 'a'),
            [])

    @with_skip_not_implemented
    def test_unsorted_input(self):
        self.assertEqual(join(
            [{'a': 3}, {'a': 1}, {'a': 2}],
            [{'a': 2}], 'a', 'a'),
            [({'a': 2}, {'a': 2})])
        self.assertEqual(join(
            [{'a': 2}],
            [{'a': 3}, {'a': 1}, {'a': 2}], 'a', 'a'),
            [({'a': 2}, {'a': 2})])
        self.assertEqual(join(
            [{'a': 4}, {'a': 1}, {'a': 3}, {'a': 2}],
            [{'a': 2}, {'a': 4}], 'a', 'a'),
            [({'a': 2}, {'a': 2}), ({'a': 4}, {'a': 4})])

    @with_skip_not_implemented
    def test_cartesian_output(self):
        self.assertEqual(join(
            [{'a': 1} for _ in range(3)],
            [{'a': 1} for _ in range(4)], 'a', 'a'),
            [({'a': 1}, {'a': 1}) for _ in range(3 * 4)])

