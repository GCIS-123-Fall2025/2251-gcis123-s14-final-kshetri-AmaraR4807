
"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #3 (25 points)
Filename: balance_parenthesis.py

Complete the bracket balancing function below. It checks if (  and  ) brackets are balanced, using a stack.

Function returns 0 if brackets are balanced,
-1 if there are more closing brackets than needed,
and x otherwise, where x is the index of the most recent
unbalanced left bracket.

Examples:
"--(---(------)--"  returns  2 
"()----)" returns -1
"-----() -- ( () )" returns 0

"""
# from node_stack import Stack

def balance_parenthesis(a_string):
    s = a_string
    open_count = 0
    for char in s:
        if char == '(':
            open_count = open_count - 1
        if char == ')':
            open_count = open_count + 1
        return open_count

def main():
    string1 = "--(---(-------)----"
    string2 = "()-----)"
    string3 = "-------() -- (())"
    print(string1, balance_parenthesis(string1))
    print(string2, balance_parenthesis(string2))
    print(string3, balance_parenthesis(string3))
 

if __name__ == "__main__":    main()