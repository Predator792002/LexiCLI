
from functions.run_python_files import run_python_file


result1 = run_python_file("calculator", "main.py")
result2 = run_python_file("calculator", "tests.py")
result3 = run_python_file("calculator", "../main.py")
result4 = run_python_file("calculator", "nonexistent.py")
print(result1)
print('-------------------------------')
print(result2)
print('-------------------------------')
print(result3)
print('-------------------------------')
print(result4)



