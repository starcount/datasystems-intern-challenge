from __future__ import print_function
from unittest import (
    TestSuite,
    TextTestRunner,
    TestSuite
)
from validation.constants import (
	BANNER,
	TEST_VERBOSITY
)
from validation.run_length_encoding.encoding import (
    TestEncoding as TestRunLengthEncoding
)
from validation.run_length_encoding.serialization import (
        TestSerialization as TestRunLengthEncodingSerialization
)
from validation.sort_merge_join.inner_equality import (
        TestInnerEquality as TestInnerEqualitySortMergeJoin
)

test_runner = TextTestRunner(verbosity=TEST_VERBOSITY)

run_length_encoding_test_suite = TestSuite()
run_length_encoding_test_suite.addTests([
    TestRunLengthEncoding("test_no_symbols"),
    TestRunLengthEncoding("test_one_symbol"),
    TestRunLengthEncoding("test_multiple_runs_per_symbol")])

run_length_encoding_serialization_test_suite = TestSuite()
run_length_encoding_serialization_test_suite.addTests([
    TestRunLengthEncodingSerialization("test_no_symbols"),
    TestRunLengthEncodingSerialization("test_bad_symbol"),
    TestRunLengthEncodingSerialization("test_one_symbol"),
    TestRunLengthEncodingSerialization("test_multiple_runs_per_symbol")])

sort_merge_join_serialization_test_suite = TestSuite()
sort_merge_join_serialization_test_suite.addTests([
    TestInnerEqualitySortMergeJoin("test_empty"),
    TestInnerEqualitySortMergeJoin("test_no_equality"),
    TestInnerEqualitySortMergeJoin("test_unsorted_input"),
    TestInnerEqualitySortMergeJoin("test_cartesian_output")])

print(BANNER)

print("--- Validating Run Length Encoding...\n")

test_runner.run(run_length_encoding_test_suite)

print("--- Validating Run Length Encoding Serialization...\n")

test_runner.run(run_length_encoding_serialization_test_suite)

print("--- Validating Inner Equality Sort Merge Join...\n")

test_runner.run(sort_merge_join_serialization_test_suite)
