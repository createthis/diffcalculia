#!/usr/bin/env python3
import sys
import re

fix_mode = False
if '--fix' in sys.argv:
    fix_mode = True
    sys.argv.remove('--fix')

def validate_patch(patch_text):
    print("\n=== DEBUG: Input Validation ===", file=sys.stderr)
    lines = patch_text.splitlines()
    if len(lines) < 4:
        print(f"❌ Need minimum 4 lines, got {len(lines)}", file=sys.stderr)
        sys.exit(1)

    print(f"Lines[0] (---): {repr(lines[0])}", file=sys.stderr)
    print(f"Lines[1] (+++): {repr(lines[1])}", file=sys.stderr)

    hunk_indices = [i for i, l in enumerate(lines) if l.startswith('@@ ')]
    if not hunk_indices:
        print("❌ No unified diff hunks found", file=sys.stderr)
        sys.exit(1)

    fixes = []
    for hunk_num, start in enumerate(hunk_indices, 1):
        header = lines[start]
        print(f"\nHunk {hunk_num} header: {repr(header)}", file=sys.stderr)
        m = re.match(r'^@@ -(\d+),(\d+) \+(\d+),(\d+) @@', header)
        if not m:
            print("❌ Malformed unified diff header", file=sys.stderr)
            sys.exit(1)
        old_start, old_len, new_start, new_len = map(int, m.groups())
        print(f"Header claims: old_len={old_len}, new_len={new_len}", file=sys.stderr)

        end = hunk_indices[hunk_num] if hunk_num < len(hunk_indices) else len(lines)
        hunk_body = lines[start+1:end]

        actual_old = sum(1 for ln in hunk_body if ln == '' or ln[0] in ' -')
        actual_new = sum(1 for ln in hunk_body if ln == '' or ln[0] in ' +')
        print(f"Actually found: old_lines={actual_old}, new_lines={actual_new}", file=sys.stderr)

        if old_len != actual_old or new_len != actual_new:
            if fix_mode:
                fixes.append((start, old_start, new_start, actual_old, actual_new))
            else:
                print(f"❌ Line count mismatch in hunk {hunk_num}!\n"
                      f"  - Old lines: claimed {old_len} ≠ actual {actual_old}\n"
                      f"  - New lines: claimed {new_len} ≠ actual {actual_new}",
                      file=sys.stderr)
                sys.exit(1)

    if fix_mode and fixes:
        print("Let me fix that for you", file=sys.stderr)
        for idx, old_start, new_start, a_old, a_new in fixes:
            lines[idx] = f"@@ -{old_start},{a_old} +{new_start},{a_new} @@"
        fixed = "\n".join(lines) + "\n"
        print(fixed, end='')
        print(fixed, end='', file=sys.stderr)
        sys.exit(0)

    print("\n✅ Patch validation passed", file=sys.stderr)
    print(patch_text, end='')
    sys.exit(0)

def main():
    validate_patch(sys.stdin.read())

if __name__ == "__main__":
    main()

