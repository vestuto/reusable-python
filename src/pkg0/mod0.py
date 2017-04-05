"""
This is a docstring for the file mod0.py
"""

print("You just imported mod0")

x = 42
message = "Hello from mod0"

def speak(msg=message):
	print(msg)
	return None

if __name__ == "__main__":
	print("The module mod0.py was run as a script")
	exit 0
