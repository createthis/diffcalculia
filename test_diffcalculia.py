import unittest
import subprocess

class TestDiffcalculia(unittest.TestCase):
    def run_validator(self, diff):
        result = subprocess.run(
            ['python3', 'diffcalculia.py'],
            input=diff,
            capture_output=True,
            text=True
        )
        return result.returncode, result.stderr

    def test_regex_lookahead_should_pass(self):
        with open('fixtures/regex_lookahead_should_pass.diff', 'r') as f:
            diff = f.read()
        returncode, stderr = self.run_validator(diff)
        self.assertEqual(returncode, 0, f"Expected success, got:\n{stderr}")

    def test_single_hunk_should_pass(self):
        with open('fixtures/single_hunk_should_pass.diff', 'r') as f:
            diff = f.read()
        returncode, stderr = self.run_validator(diff)
        self.assertEqual(returncode, 0, f"Expected success, got:\n{stderr}")

    def test_single_hunk_should_fail(self):
        with open('fixtures/single_hunk_should_fail.diff', 'r') as f:
            diff = f.read()
        returncode, stderr = self.run_validator(diff)
        self.assertNotEqual(returncode, 0, "Expected failure but got success")

    def test_multi_hunk_should_pass(self):
        with open('fixtures/multi_hunk_should_pass.diff', 'r') as f:
            diff = f.read()
        returncode, stderr = self.run_validator(diff)
        self.assertEqual(returncode, 0, f"Expected success, got:\n{stderr}")

    def test_multi_hunk_should_fail(self):
        with open('fixtures/multi_hunk_should_fail.diff', 'r') as f:
            diff = f.read()
        returncode, stderr = self.run_validator(diff)
        self.assertNotEqual(returncode, 0, "Expected failure but got success")

    def test_auto_fix_header_should_correct(self):
        diff_header = '--- a/some/file\n+++ b/some/file\n@@ -266,41 +266,55 @@'
        blank_lines = '\n'.join([''] * 43)
        added_lines = '\n'.join(['+x'] * 13)
        diff = '\n'.join([diff_header, blank_lines, added_lines, ''])
        result = subprocess.run(
            ['python3', 'diffcalculia.py', '--fix'],
            input=diff,
            capture_output=True,
            text=True
        )
        self.assertEqual(result.returncode, 0, f"Expected success, got:\n{result.stderr}")
        self.assertIn('Let me fix that for you', result.stderr)
        self.assertIn('@@ -266,43 +266,56 @@', result.stdout)

if __name__ == '__main__':
    unittest.main()

