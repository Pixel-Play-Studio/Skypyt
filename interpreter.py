import sys
import re

# Słownik zmiennych
variables = {}

# Funkcje w języku
def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return x / y if y != 0 else "Division by zero!"
def mod(x, y): return x % y
def pow(x, y): return x ** y

# Funkcje pomocnicze
def parse_value(val):
    try:
        return int(val)
    except ValueError:
        try:
            return float(val)
        except ValueError:
            return variables.get(val.strip(), val.strip('"'))

def calculate_expression(expr):
    """Oblicza wyrażenie matematyczne w formacie `add a b`."""
    parts = expr.split()
    if len(parts) != 3:
        raise ValueError("Invalid expression format. Expected: `operation x y`.")
    op, x, y = parts
    x_val = parse_value(x)
    y_val = parse_value(y)
    if op == "add":
        return add(x_val, y_val)
    elif op == "sub":
        return sub(x_val, y_val)
    elif op == "mul":
        return mul(x_val, y_val)
    elif op == "div":
        return div(x_val, y_val)
    elif op == "mod":
        return mod(x_val, y_val)
    elif op == "pow":
        return pow(x_val, y_val)
    else:
        raise ValueError(f"Unknown operation: {op}")

# Obsługa komend
def execute_line(line):
    if not line.strip():
        return  # Ignoruj puste linie

    if line.startswith("let"):
        try:
            _, var, _, expr = re.split(r'\s+', line, maxsplit=3)
            # Sprawdź, czy wartość to wyrażenie
            if any(op in expr for op in ["add", "sub", "mul", "div", "mod", "pow"]):
                variables[var] = calculate_expression(expr)
            else:
                variables[var] = parse_value(expr)
        except ValueError:
            print(f"Error in `let` command: {line}")
    elif line.startswith("print"):
        try:
            _, expr = line.split(" ", 1)
            if expr.startswith('"') and expr.endswith('"'):
                # Jeśli w cudzysłowach, drukuj tekst
                print(expr.strip('"'))
            else:
                # Inaczej traktuj jako zmienną lub wartość
                result = parse_value(expr)
                print(result)
        except ValueError:
            print(f"Error with `print` command: {line}")
    else:
        print(f"Unknown command: {line}")

# Interpreter
def run_script(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                execute_line(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{filename}' does not exist.")
    except Exception as e:
        print(f"Sorry, something went wrong: {e}")

# Start
if __name__ == "__main__":
    if len(sys.argv) > 1:
        script = sys.argv[1]
    else:
        script = input("Enter file name .sky: ").strip()

    if script:
        run_script(script)
    else:
        print("No file specified. Exiting.")

    input("Press Enter to exit the program...")
