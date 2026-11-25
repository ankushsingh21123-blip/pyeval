import pyeval
TASK = {"id": "rev", "entrypoint": "rev", "tests": [{"args": ["abc"], "expected": "cba"}, {"args": [""], "expected": ""}]}
def ev(code): return pyeval.evaluate([TASK], [{"task_id": "rev", "code": code}])[0]
def test_correct():
    r = ev('def rev(s):\n    """reverse"""\n    return s[::-1]\n'); assert r["passed"] == 2 and not r["failure_modes"]
def test_wrong_answer():
    assert "wrong_answer" in ev("def rev(s):\n    return s\n")["failure_modes"]
def test_index_error_trace():
    r = ev("def rev(s):\n    return s[0] + s[-1]\n"); assert "IndexError" in r["failure_modes"]; assert "Traceback" in r["cases"][1]["trace"]
def test_timeout():
    assert "timeout" in ev("def rev(s):\n    while True: pass\n")["failure_modes"]
def test_syntax_and_flags():
    r = ev("def rev(s) return s"); assert "SyntaxError" in r["failure_modes"] and "does_not_parse" in r["quality_flags"]
def test_bare_except_flag():
    assert "bare_except" in ev("def rev(s):\n    try:\n        return s[::-1]\n    except:\n        return ''\n")["quality_flags"]
