def analyze_code(file_name, code):

    issues = []

    lines = code.split("\n")

    # Large file detection
    if len(lines) > 500:
        issues.append(f"{file_name}: Large file (>500 lines)")

    # Long function detection
    function_length = 0

    for line in lines:

        if "def " in line or "function " in line:
            function_length = 0

        function_length += 1

        if function_length > 50:
            issues.append(f"{file_name}: Long function detected")
            break

    # Deep nesting detection
    for line in lines:

        indent = len(line) - len(line.lstrip())

        if indent > 12:
            issues.append(f"{file_name}: Deep nesting detected")
            break

    return issues