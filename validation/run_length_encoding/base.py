from unittest import TestCase
from abc import (
    ABCMeta,
    abstractmethod
)
from validation.util import with_skip_not_implemented

class TestBase(TestCase):

    
    __metaclass__ = ABCMeta


    @abstractmethod
    def _run_test_case(self, unencoded_symbols):
        pass

    @with_skip_not_implemented
    def test_no_symbols(self):
        self._run_test_case("")


    @with_skip_not_implemented
    def test_one_symbol(self):
        self._run_test_case("AAAAAA")


    @with_skip_not_implemented
    def test_multiple_runs_per_symbol(self):
        self._run_test_case("AABBAA")

