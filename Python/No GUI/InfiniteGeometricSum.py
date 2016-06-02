start = eval(input("What is the first term of the sequence?\n"))
factor = eval(input("What is the common ratio? (<1)\n"))
print("The infinite geometric sum is",round(start/(1-factor),15))
