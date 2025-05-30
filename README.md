# Diffcalculia

Dyscalculia is a learning disability that impacts a person's ability to understand numbers and perform mathematical calculations.

One would think the venerable UNIX `diff` and `patch` tools would be perfect for AIs to edit code.

Unfortunately, AIs have trouble outputting valid unified diffs, mostly due to their dyscalculia.

This tool is meant to be used by AIs as a crutch in generating valid unified diffs, at least until they learn to overcome their dyscalculia.


## Usage

### Typescript Port
FYI, the Typescript port is here: https://github.com/createthis/diffcalculia-ts

### Open Hands AI

Open Hands AI mounts the project at `/workspace`.

If you want your agentic coder to utilize `diff` and `patch` to edit files, simply copy and paste this snippet into your prompt:

````
# File Reading and Editing

1. Run this once via bash:

   ```bash
   python3 -m venv my_venv && \
   source my_venv/bin/activate && \
   python3 -m pip install --force-reinstall git+https://github.com/createthis/diffcalculia.git
   ```

   DO NOT FORGET THIS STEP! IF YOU DO, `diffcalculia` WILL NOT BE INSTALLED!

2. You can edit a file with the `patch` CLI command, via the execute_bash tool.
   Call `patch` like this, replacing YOUR_DIFF_HERE with your diff:

   ```bash
   cat << 'EOF' | diffcalculia --fix | \
     patch -p0 --ignore-whitespace --verbose -r- --no-backup-if-mismatch /workspace/file_to_edit
   YOUR_DIFF_HERE
   EOF
   ```
   
   The `diffcalculia --fix` command will fix minor line count discrepancies for 
   you automatically!

   NOTE: You **MUST** use unified diff format. Do **NOT** use context-diff format.

3. Use `patch` to edit files and add tests. DO NOT USE str_replace_editor. It has
   trouble with large files.

4. Use `cat -n /path | sed -E 's/^([[:space:]]*[0-9]+)\t/\1|/'` to read files. DO 
   NOT USE str_replace_editor. It will truncate large files.
````

### Open Hands AI - no str_replace_editor

[This PR](https://github.com/All-Hands-AI/OpenHands/pull/8310) allows Open Hands AI to be used with `str_replace_editor`
disabled.

In your `docker run` command, add:
```bash
-e AGENT_ENABLE_EDITOR=false \
```

With `str_replace_editor` disabled, our prompt becomes less complex:
````
# File Reading and Editing

1. Run this once via bash:

   ```bash
   python3 -m venv my_venv && \
   source my_venv/bin/activate && \
   python3 -m pip install --force-reinstall git+https://github.com/createthis/diffcalculia.git
   ```

   DO NOT FORGET THIS STEP! IF YOU DO, `diffcalculia` WILL NOT BE INSTALLED!

2. You can edit a file with the `patch` CLI command, via the execute_bash tool.
   Call `patch` like this, replacing YOUR_DIFF_HERE with your diff:

   ```bash
   cat << 'EOF' | diffcalculia --fix | \
     patch -p0 --ignore-whitespace --verbose -r- --no-backup-if-mismatch /workspace/file_to_edit
   YOUR_DIFF_HERE
   EOF
   ```
   
   The `diffcalculia --fix` command will fix minor line count discrepancies for 
   you automatically!

   NOTE: You **MUST** use unified diff format. Do **NOT** use context-diff format.

3. Use `patch` to edit files and add tests.

4. Use `cat -n /path | sed -E 's/^([[:space:]]*[0-9]+)\t/\1|/'` to read files.
````

## Running Tests

This directory contains tests for the `diffcalculia.py` tool which validates and corrects unified diff formats.

To run the test suite:

```bash
python3 test_diffcalculia.py
```
