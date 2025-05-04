# Diffcalculia

Dyscalculia is a learning disability that impacts a person's ability to understand numbers and perform mathematical calculations.

One would think the venerable UNIX `diff` and `patch` tools would be the perfect for AIs to edit code.

Unfortunately, AIs have trouble outputting valid unified diffs, mostly due to their dyscalculia.

This tool is meant to be used by AIs as a crutch in generating valid unified diffs, at least until they learn to overcome their dyscalculia.


## Running Tests

This directory contains tests for the `diffcalculia.py` tool which validates and corrects unified diff formats.

To run the test suite:

```bash
python3 test_diffcalculia.py
```

## Test Cases

The test suite includes:
1. `test_should_pass`: Validates a correctly formatted unified diff
2. `test_should_fail`: Verifies the validator catches malformed diffs

## Expected Output

Successful tests will show:
```
..
----------------------------------------------------------------------
Ran 2 tests in X.XXs

OK
```

Failed tests will show detailed error output.

## Debugging

For debugging validation failures:
1. Check the stderr output showing the validation steps
2. Verify the diff format matches unified diff specifications
3. Check line counts match between headers and actual changes
