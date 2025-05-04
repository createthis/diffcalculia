# Diffcalculia

Dyscalculia is a learning disability that impacts a person's ability to understand numbers and perform mathematical calculations.

One would think the venerable UNIX `diff` and `patch` tools would be perfect for AIs to edit code.

Unfortunately, AIs have trouble outputting valid unified diffs, mostly due to their dyscalculia.

This tool is meant to be used by AIs as a crutch in generating valid unified diffs, at least until they learn to overcome their dyscalculia.


## Usage

### Open Hands AI

Open Hands AI mounts the project at `/workspace`.

If you want your agentic coder to utilize `diff` and `patch` to edit files, simply copy and paste this snippet into your prompt:

````
# File Editing

1. Run this once via bash:

   ```bash
   python3 -m venv my_venv
   source my_venv/bin/activate
   python3 -m pip install --force-reinstall git+https://github.com/createthis/diffcalculia.git
   ```

2. You can edit a file with the `patch` CLI command, via the execute_bash tool.
   Call `patch` like this, replacing YOUR_DIFF_HERE with your diff:

   ```bash
   cat << 'EOF' | diffcalculia --fix | \
     patch -p0 --ignore-whitespace --verbose -r - -V never /workspace/file_to_edit
   YOUR_DIFF_HERE
   EOF
   ```
   
   `patch` notoriously has very unhelpful error messages. The `diffcalculia --fix` command will give you helpful error 
   messages in case your patch is malformed. It will even fix minor line count discrepancies for you automatically!
````

## Running Tests

This directory contains tests for the `diffcalculia.py` tool which validates and corrects unified diff formats.

To run the test suite:

```bash
python3 test_diffcalculia.py
```
