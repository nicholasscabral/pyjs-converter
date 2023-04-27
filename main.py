import re


def convert_python_to_javascript(python_code):
    # Define the dictionary to map Python keywords to JavaScript equivalents
    keyword_dict = {
        "and": "&&",
        "or": "||",
        "not": "!",
        "True": "true",
        "False": "false",
        "None": "null",
        "if": "if",
        "else": "else",
        "elif": "else if",
        "while": "while",
        "for": "for",
        "in": "in",
        "range": "Array.from({length: ",
        "len": ".length",
        "def": "function",
        "return": "return",
        "print": "console.log",
    }

    # Use regular expressions to find and replace Python keywords with their JavaScript equivalents
    for python_keyword, js_keyword in keyword_dict.items():
        python_code = re.sub(r"\b{}\b".format(python_keyword), js_keyword, python_code)

    # Replace '=' with 'var'
    python_code = re.sub(r"(\b\w+\b)\s*=\s*", "var \\1 = ", python_code)

    # Replace Python-style string formatting with JavaScript-style string formatting
    python_code = re.sub(r"(\{.*?\})", "{$1}", python_code)
    python_code = re.sub(r"%\((.*?)\)[sd]", "{$1}", python_code)

    # Add semicolons at the end of statements if they don't already exist
    python_code = re.sub(r"([^;])\n", "\\1\n", python_code)

    return python_code


python_code = """
x = 1
y = 2
z = x + y
if z > 2:
    print("z is greater than 2")
else:
    print("z is less than or equal to 2")
"""

javascript_code = convert_python_to_javascript(python_code)
print(javascript_code)
