A basic function in Python consists of several parts that work together to define what the function does and how it behaves. Here’s a breakdown of each part:

### 1. **Function Definition**
   - A function in Python is defined using the `def` keyword followed by the function name and parentheses. The body of the function is indented under the definition.
   
   ```python
   def my_function():
       pass  # Function body goes here
   ```

### 2. **Function Name**
   - The **function name** is used to identify the function and call it later. It follows the same naming conventions as variables (must start with a letter or an underscore and can include letters, numbers, and underscores).
   
   Example:
   ```python
   def greet():
       print("Hello, world!")
   ```

### 3. **Parameters (Optional)**
   - **Parameters** are variables that act as placeholders for values you pass into the function when calling it. Parameters are defined inside the parentheses after the function name.
   - They allow the function to accept input and perform operations on it.
   
   Example:
   ```python
   def add(a, b):   # 'a' and 'b' are parameters
       return a + b
   ```

   - **Note**: Parameters are optional. A function can have no parameters, one parameter, or multiple parameters.

### 4. **Docstring (Optional, but recommended)**
   - A **docstring** is a string that is placed inside the function, right after the function definition, and is used to describe what the function does. It is optional, but highly recommended for clarity and documentation purposes.
   - The docstring is enclosed in triple quotes (`""" ... """`).
   
   Example:
   ```python
   def greet(name):
       """This function greets the person passed as an argument."""
       print(f"Hello, {name}!")
   ```

   - You can access the docstring of a function using the `help()` function or the `.__doc__` attribute.

### 5. **Function Body**
   - The **body** of the function contains the statements that define what the function does when it is called. The body is indented (usually by 4 spaces).
   
   Example:
   ```python
   def multiply(a, b):
       result = a * b  # Function body: calculates product
       return result    # Returns the result of multiplication
   ```

### 6. **Return Statement (Optional)**
   - The `return` statement specifies the value that the function will output when called. If no `return` statement is provided, the function returns `None` by default.
   - You can return multiple values as a tuple by separating them with commas.
   
   Example:
   ```python
   def add(a, b):
       return a + b   # Returns the sum of 'a' and 'b'
   
   def get_coords():
       return 10, 20  # Returns a tuple (10, 20)
   ```

### 7. **Function Call**
   - After defining a function, you can call it by using its name followed by parentheses. If the function takes parameters, you pass the appropriate values inside the parentheses.
   
   Example:
   ```python
   result = add(3, 4)  # Calling the 'add' function with 3 and 4
   print(result)        # Outputs 7
   ```

### 8. **Scope (Local vs Global)**
   - Variables defined inside a function are **local variables**, meaning they only exist within that function.
   - Variables defined outside the function are **global variables** and can be accessed anywhere in the program, including inside the function, unless shadowed by a local variable.
   
   Example of **local variable**:
   ```python
   def greet():
       message = "Hello!"   # 'message' is a local variable
       print(message)
   ```

   Example of **global variable**:
   ```python
   greeting = "Hello!"  # Global variable

   def greet():
       print(greeting)  # Accesses the global variable
   ```

### 9. **Arguments (Function Call)**
   - **Arguments** are the actual values or expressions you provide when calling a function. These values are assigned to the parameters in the function definition.
   
   Example:
   ```python
   def greet(name):  # 'name' is the parameter
       print(f"Hello, {name}!")
   
   greet("Alice")    # "Alice" is the argument
   ```

### Full Example of a Basic Function

```python
def multiply(a, b):
    """
    Multiplies two numbers and returns the result.
    
    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.
    
    Returns:
    int, float: The product of the two numbers.
    """
    result = a * b  # Function body: performs multiplication
    return result   # Return the result

# Function call with arguments
product = multiply(3, 4)
print(product)  # Output: 12
```

### Summary of Function Parts:
- **`def` keyword**: Used to define the function.
- **Function name**: Identifies the function.
- **Parameters (optional)**: Variables that accept values when the function is called.
- **Docstring (optional)**: Describes what the function does.
- **Body**: Contains the statements that define the function's behavior.
- **`return` (optional)**: Specifies the output of the function.
- **Function call**: Used to execute the function with arguments.

This structure allows you to write reusable and modular code, making it easier to organize and maintain your programs.