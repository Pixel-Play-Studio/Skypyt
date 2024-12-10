Here’s the **README** file for your **SkyPyt** project in English, including a list of commands and other useful information:

---

# SkyPyt Interpreter

**SkyPyt** is a lightweight programming language inspired by Python, Lua, and C#. It allows you to execute `.sky` scripts using a simple, intuitive syntax.

---

## Features
- Easy-to-learn syntax for beginners.
- Inspired by Python, Lua, and C#.
- Supports basic math operations, variables, and logical conditions.
- Extendable and customizable.

---

## Getting Started

### Installation

1. Download the SkyPyt interpreter (`interpreter.exe`) from the [releases](#) section.
2. Place your `.sky` script in the same directory or provide a path to it.

### Running a Script

To run a SkyPyt script:

1. Open the interpreter by double-clicking on `interpreter.exe`.
2. Enter the name of your `.sky` script when prompted, or:
3. Pass the file name directly in the command line:
   ```bash
   interpreter.exe myscript.sky
   ```
The .sky file must be in the same folder what is .sky (look on test.sky on the repository)

---

## SkyPyt Syntax and Commands

### **Variable Management**
- `let <variable> = <value>`  
  Creates or updates a variable.  
  **Example:**  
  ```sky
  let x = 10
  ```

- `print <value>`  
  Prints the value of a variable or expression to the console.  
  **Example:**  
  ```sky
  print x
  ```

---

### **Math Operations**
- `add <x> <y>`  
  Adds two numbers.  
  **Example:**  
  ```sky
  add 5 3  # Result: 8
  ```

- `sub <x> <y>`  
  Subtracts one number from another.  
  **Example:**  
  ```sky
  sub 10 4  # Result: 6
  ```

- `mul <x> <y>`  
  Multiplies two numbers.  
  **Example:**  
  ```sky
  mul 3 3  # Result: 9
  ```

- `div <x> <y>`  
  Divides one number by another. Returns an error if division by zero is attempted.  
  **Example:**  
  ```sky
  div 8 2  # Result: 4
  ```

- `mod <x> <y>`  
  Calculates the remainder of a division.  
  **Example:**  
  ```sky
  mod 10 3  # Result: 1
  ```

- `pow <x> <y>`  
  Raises a number to the power of another.  
  **Example:**  
  ```sky
  pow 2 3  # Result: 8
  ```

---

### **Logical Operations**
- `if <condition>`  
  Evaluates a logical condition. (Future versions will support more complex logic.)  
  **Example:**  
  ```sky
  if x > 5
  ```

---

## Example Script

Here’s a simple `.sky` script:

```sky
let a = 5
let b = 10
let result = add a b
print result
```

Output:
```
Result: 15
```

---

## Customizing the Interpreter

To customize the interpreter, clone the repository and modify `interpreter.py`. You can add new commands or adjust existing behavior.

---

## Errors

Eny errors? contact on our discord (Polish) or email(English/Polish) or Pull requests (slower version)

Discord: https://discord.gg/gCNq5RUBPQ

Email: pixelplay.help@hotmail.com

---

## Contributing

Contributions are welcome! If you have suggestions , feel free to [open an issue](#) or submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Let me know if you need further modifications or additional content! 😊
