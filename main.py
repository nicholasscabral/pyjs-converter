import re
import json


def convert_python_to_javascript(python_code):
    # Define the dictionary to map Python keywords to JavaScript equivalents
    keyword_dict = {
        'and': '&&',
        'or': '||',
        'not': '!',
        'True': 'true',
        'False': 'false',
        'None': 'null',
        'if': 'if',
        'else': 'else',
        'elif': 'else if',
        'while': 'while',
        'for': 'for',
        'in': 'in',
        'range': 'Array.from({length:',
        'len': '.length',
        'def': 'function',
        'return': 'return',
        'print': 'console.log'
    }

    # Use regular expressions to find and replace Python keywords with their JavaScript equivalents
    for python_keyword, js_keyword in keyword_dict.items():
        python_code = re.sub(r'\b{}\b'.format(
            python_keyword), js_keyword, python_code)

    # Replace Python-style string formatting with JavaScript-style string formatting
    python_code = re.sub(r'(\{.*?\})', '{$1}', python_code)
    python_code = re.sub(r'%\((.*?)\)[sd]', '{$1}', python_code)

    # Add semicolons at the end of statements if they don't already exist
    python_code = re.sub(r'([^;])\n', '\\1;\n', python_code)

    # Convert Python for loop to JavaScript
    python_code = re.sub(
        r'for\s+(\w+)\s+in\s+Array\.from\(\{length:\s+(\d+)\}\)', r'for (var \1 = 0; \1 < \2; \1++)', python_code)

    # Convert Python if statements to JavaScript
    python_code = re.sub(r'if\s+(.*?)\s*:', r'if (\1) {', python_code)
    python_code = re.sub(r'else\s*:', r'} else {', python_code)
    python_code = re.sub(r'elif\s+(.*?)\s*:', r'} else if (\1) {', python_code)

    # Convert Python-style variable declaration to JavaScript-style declaration
    python_code = re.sub(
        r'\bvar\s+(\w+)\b', r'var \1', python_code)

    # Convert indentation to braces
    indent_level = 0
    new_lines = []
    for line in python_code.splitlines():
        if line.startswith(' ' * indent_level):
            line = '{' + line[indent_level:] + '\n'
        elif line.startswith(' ' * (indent_level - 4)):
            indent_level -= 4
            line = '}\n' + ' ' * indent_level + \
                '{' + line[indent_level:] + '\n'
        else:
            raise ValueError('Unexpected indentation level')
        new_lines.append(line)
        indent_level += 4
    javascript_code = ''.join(new_lines)

    return javascript_code


python_code = """
var x = 1
var y = 2
var z = x + y
if z > 2:
    print("z is greater than 2")
else:
    print("z is less than or equal to 2")
"""

javascript_code = convert_python_to_javascript(json.dumps(python_code))

# Remove the quotes around the string
output = javascript_code.strip('"{').rstrip('}"')

# Split the string into lines
lines = output.split('\\n')

# Print each line separately
for line in lines:
    print(line)
