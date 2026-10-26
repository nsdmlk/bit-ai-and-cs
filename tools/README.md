# Source Validation

Run `python3 tools/validate_sources.py` from the repository root. Only Python's standard library is required. To check an extracted source copy, pass `--root PATH`. The optional `--json PATH` writes a machine-readable result.

The validator checks local links and heading anchors, missing/remote images, XML validity of SVGs, code-fence balance and accidental public student identifiers/personal-log folders. It does not establish factual correctness, source support, human review or every member's contribution. Inspect the rendered PDF and complete a genuine team review separately.
