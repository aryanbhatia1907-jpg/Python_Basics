a="aRYan!!!!!"                     # Strings are immutable
print(a.upper())                   # Print String into Uppercase
print(a.lower())                   # Print String into Lowercase

print(a)                           # Print as defined string
print(a.rstrip("!"))               # Remove defined character 
print(a.replace("aRYan","nayrA"))  # Replace with New String
print(a.split("Y"))                # Create as a List  from defined character and majorily used if space there
print(a.capitalize())              # Capitilize first letter and small others 

str1="Welcome to the Python"
print(str1.center(50,"."))         # align String to the center
# {Total jitna length di hogi usko or string ki length dekh ke usse center me krta h or aage or phiche barabar space deta hai}
print(len(str1))                   # Original String Length
print(len(str1.center(50)))        # String Length after applying Center

print(str1.count("o"))             # Counts that defined character used how many times 
print(str1.endswith("n"))          # Give true if string ends with same as defined else false
print(str1.endswith("e",4,13))     

print(str1.find("x"))              # Helps to find character index *[Gives (-1) is condition is false
print(str1.index("o"))             # Same as find but gives error if condition false

str2="eypy07"
print("\n")
print(str2.isalnum())              # Checks the String is Alpha-Numeric os Not.
print(str2.isalpha())              # Checks only Alphabetical.
print(str2.islower())              # Checks String is Lowercase or Not.
print(str2.isprintable())          # Checks String is Printable or Not.
str3="\n"
print(str3)
print(str3.isprintable())          # False because "\n" Used to Enter only not to print.

print(str1.isspace())              # True if only white spaces present.
print(str1.istitle)                # True only if the first letter of each word of the string is capitalized.
print(str1.startswith("Wel"))      # Checks the string starts with a given value or not.
print(str1.swapcase())             # Changes the character casing of the string.
print(str1.title())                # Capitalizes each letter within the string.