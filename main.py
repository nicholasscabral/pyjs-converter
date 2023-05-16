import re
import json
from tkinter import filedialog

def is_python_code_valid(python_code):
    try:
        compile(python_code, "<string>", "exec")
        return True
    except SyntaxError:
        return False


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
        'in': 'of',
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

    # Replace '=' with 'var'
    python_code = re.sub(r'(\b\w+\b)\s*=\s*', 'var \\1 = ', python_code)

    # Replace Python-style string formatting with JavaScript-style string formatting
    python_code = re.sub(r'(\{.*?\})', '{$1}', python_code)
    python_code = re.sub(r'%\((.*?)\)[sd]', '{$1}', python_code)

    # Add semicolons at the end of statements if they don't already exist
    python_code = re.sub(r'([^;])\n', '\\1;', python_code)

    # Convert Python for loop to JavaScript
    python_code = re.sub(
        r'for\s+(\w+)\s+in\s+Array\.from\(\{length:\s+(\d+)\}\)', r'for (var \1 = 0; \1 < \2; \1++)', python_code)

    # Convert Python if statements to JavaScript
    python_code = re.sub(r'if\s+(.*?)\s*:', r'if (\1) {', python_code)
    python_code = re.sub(r'else\s*:', r'} else {', python_code)
    python_code = re.sub(r'elif\s+(.*?)\s*:', r'} else if (\1) {', python_code)

    # Convert indentation to braces
    indent_level = 0
    new_lines = []
    for line in python_code.splitlines():
        if line.startswith(' ' * indent_level):
            line = '{' + line[indent_level:] + ';'
        elif line.startswith(' ' * (indent_level - 4)):
            indent_level -= 4
            line = '};' + ' ' * indent_level + \
                '{' + line[indent_level:] + ';'
        else:
            raise ValueError('Unexpected indentation level')
        new_lines.append(line)
        indent_level += 4
    javascript_code = ''.join(new_lines)

    return javascript_code


# input_path = input('Enter input path: ')
input_path = filedialog.askopenfile(title="SELECIONE O ARQUIVO DE ENTRADA")
input_path = input_path.name

# output_file_path = input("Enter output path: ")
output_file_path = "output.js"

with open(input_path, 'r') as f:
    python_code = f.read()

if not is_python_code_valid(python_code):
    print('PYTHON CODE NOT COMPILABLE, EXITING...')
    exit(1)

# Convert the Python code to JavaScript
javascript_code = convert_python_to_javascript(python_code)


# Print the formatted JavaScript code
formatted_code = re.sub(r';{2,}', ';', javascript_code)
formatted_code = formatted_code[1:] + ';}'
lines = formatted_code.split(';')
for line in lines:
    if line:
        print('    ' + line.strip())
        with open(output_file_path, 'a') as f:
            f.write('    ' + line.strip() + '\n')


# analisar o tipo da expressao e fazer um pre processamento das variaveis no escopo
# nomes de variaveis devem ser unicos! nao podem se repetir (primeiro a gente assume que o codigo do usuario vai satisfazer essa condicoes, depois a gente pensa em casos de teste e erro)
# declarar todas as variaveis no escopo global
# testar se o codigo de entrada e compilavel ou nao
