# Question 1
"""
No, you cannot directly instantiate an abstract class.
Abstract classes serve as blueprints for subclasses and must be inherited to be used.
"""

# Question 2
"""
To ensure that all subclasses follow a defined template.
To prevent direct instantiation and allow only derived classes to be created.
To share common functionality and implement common logic while forcing specific implementations in subclasses.
"""

# Question 3
"""
To force subclasses to implement it when the base class cannot provide a meaningful default implementation.
"""

# Question 4
"""
No, it does not make sense. because if a class is not abstract, it can be instantiated.
If a class contains an abstract method, but the class itself is not abstract, then it breaks Python’s rules.
"""

# Question 5
"""
The parent class has its own __init__ logic, and you want to extend the parent class instead of replacing its behavior.
Also to avoid duplication of code.
"""

# Question 6
"""
To preserve the parent class’s string representation which will enable you to extend the output instead of replacing it.
"""