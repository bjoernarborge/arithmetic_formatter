# Creating a function that receives a list of strings that are arithmetic problems
# and returns the problems arranged vertically and side-by-side.
# The function optionally takes a second argument. When the second argument is set to True, the answers are displayed.
def arithmetic_arranger(problems, show_answers=False):
    # Error: Too many problems. More than 5 problems.
    if len(problems) > 5:
        return "Error: Too many problems."
    # Error: Operator must be '+' or '-'. Operator is not '+' or '-'.
    for problem in problems:
        if problem.split()[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
    # Error: Numbers must only contain digits. Number contains a letter.
    for problem in problems:
        if not problem.split()[0].isdigit() or not problem.split()[2].isdigit():
            return "Error: Numbers must only contain digits."
    # Error: Numbers cannot be more than four digits. Number is more than 4 digits.
    for problem in problems:
        if len(problem.split()[0]) > 4 or len(problem.split()[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

    # If no errors, then arrange the problems vertically and side-by-side.
    # There should be single space between the operator and the longest number.
    # Numbers should be right aligned.
    # There should be four spaces between each problem.
    # There should be dashes at the bottom of each problem.
    first_operand = []
    second_operand = []
    operator = []
    for problem in problems:
        first_operand.append(problem.split()[0])
        second_operand.append(problem.split()[2])
        operator.append(problem.split()[1])
        
   






