# Starcount Datasystems Internship Challenge

## Getting Started

* Install Python >= 2.7
* In the project root directory, run `python validate_solutions.py`, you should see something like this:

```
--- Validating Run Length Encoding...

test_no_symbols (validation.run_length_encoding.encoding.TestEncoding) ... skipped 'Not implemented yet'
test_one_symbol (validation.run_length_encoding.encoding.TestEncoding) ... skipped 'Not implemented yet'
test_multiple_runs_per_symbol (validation.run_length_encoding.encoding.TestEncoding) ... skipped 'Not implemented yet'

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK (skipped=3)
--- Validating Run Length Encoding Serialization...

test_no_symbols (validation.run_length_encoding.serialization.TestSerialization) ... skipped 'Not implemented yet'
test_bad_symbol (validation.run_length_encoding.serialization.TestSerialization) ... skipped 'Not implemented yet'
test_one_symbol (validation.run_length_encoding.serialization.TestSerialization) ... skipped 'Not implemented yet'
test_multiple_runs_per_symbol (validation.run_length_encoding.serialization.TestSerialization) ... skipped 'Not implemented yet'

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK (skipped=4)
--- Validating Inner Equality Sort Merge Join...

test_empty (validation.sort_merge_join.inner_equality.TestInnerEquality) ... skipped 'Not implemented yet'
test_no_equality (validation.sort_merge_join.inner_equality.TestInnerEquality) ... skipped 'Not implemented yet'
test_unsorted_input (validation.sort_merge_join.inner_equality.TestInnerEquality) ... skipped 'Not implemented yet'
test_cartesian_output (validation.sort_merge_join.inner_equality.TestInnerEquality) ... skipped 'Not implemented yet'

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK (skipped=4)
```

* Complete the solutions to the problems below and rerun this script, if your solutions are correct the tests will run and pass.


## Problems

### Run Length Encoding
Under `run_length_encoding` there is a partially implemented [run length encoding](https://en.wikipedia.org/wiki/Run-length_encoding) algorithm. Complete the encoder so that it returns a list of 2-tuples containing run length and symbol. For example:

```
encode("AAAABBAAAA") returns [(4, "A"), (2, "B"), (4, "A")]

```

You can validate your solution by running `python validate_solutions.py`.

### Run Length Encoding Serialization

Complete the serializer so that it takes a list of 2-tuples containing run length and symbol and returns a valid string or raises an error. For example:

```
serialize([(4, "A"), (2, "B"), (4, "A")]) returns "4A2B4A"

and 

serialize([(5, "5")]) raises SerializationError
```

You can validate your solution by running `python validate_solutions.py`.

### Sort Merge Join
Under `sort_merge_join` there is a partially implemented [sort merge join](https://en.wikipedia.org/wiki/Sort-merge_join) algorithm, complete the solution so that it is able to perform an [inner join](https://en.wikipedia.org/wiki/Join_(SQL)#Inner_join) on an equality condition. For a description of the algorithm and pseudo code see [Wikipedia](https://en.wikipedia.org/wiki/Sort-merge_join).


You can validate your solution by running `python validate_solutions.py`.
