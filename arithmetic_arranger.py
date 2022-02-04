def arithmetic_arranger(problem_list, result=False):
    # First Error Handling: Function must only accept a maximum of seven problems
    if len(problem_list) > 5:
        return "Error: Too many problems."

    for problem in problem_list:
        problem = problem.replace(" ", "")  # Removing all whitespace from problem_list
        # Checking for the supported Operators ('+' and '-' only)
        if "+" in problem:
            problem = problem.split("+")
            if len(problem[0]) > 4 or len(problem[1]) > 4:
                return "Error: Numbers cannot be more than four digits."
            if type(problem[0]) != int or type(problem[1]) != int:
                return "Error: Numbers must only contain digits."

        elif "-" in problem:
            problem = problem.split("-")
            if len(problem[0]) > 4 or len(problem[1]) > 4:
                return "Error: Numbers cannot be more than four digits."
            if type(problem[0]) != int or type(problem[1]) != int:
                return "Error: Numbers must only contain digits."

        else:
            return "Error: Operator must be '+' or '-'."

        if not result:
            line1 = ''
            line2 = ''
            line3 = ''
            for i, sub in enumerate(problem_list):
                first_operands = [''.join(sub.split()[0])]
                operators = [''.join(sub.split()[1])]
                second_operands = [''.join(sub.split()[2])]

                for f in first_operands:
                    for o in operators:
                        for s in second_operands:
                            # each operand not more than 4 digits
                            # second line should also have two more chars: operator and a space b/w operator and sec operand
                            # in total 6 spaces should be reserved
                            # after each operand, four spaces need to be added
                            line1 += " " * (6 - len(f)) + f + " " * 4
                            # two spaces for operator and an empty space b/w operator and operand, plus four digit num
                            line2 += o + " " * (5 - len(s)) + s + " " * 4
                            line3 += "-" * 6 + " " * 4
            print(line1 + '\n' + line2 + '\n' + line3 + '\n')
            return line1 + '\n' + line2 + '\n' + line3 + '\n'

# print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))



#     # Output description:
#     # If result argument is True, there will be four output line, else - three lines.
#     line1 = ""  # the line containing the first operand
#     line2 = ""  # the line containing the operator and second operand
#     line3 = ""  # the line containing dashes
#     line4 = ""  # answer to each individual problem
#
#     arranged_string = ""
#
#     return arranged_string  # Return the arranged string.
