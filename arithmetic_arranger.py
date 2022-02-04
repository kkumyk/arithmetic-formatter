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
            elif not(problem[0].isdigit() or problem[1].isdigit()):
                return "Error: Numbers must only contain digits."

        elif "-" in problem:
            problem = problem.split("-")
            if len(problem[0]) > 4 or len(problem[1]) > 4:
                return "Error: Numbers cannot be more than four digits."
            elif not(problem[0].isdigit() or problem[1].isdigit()):
                return "Error: Numbers must only contain digits."

        else:
            return "Error: Operator must be '+' or '-'."

        if not result:
            res = ''
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
                            # each operand not more than 4 digits second line should also have two more chars:
                            # operator and a space b/w operator and sec operand in total 6 spaces should be reserved
                            # after each operand, four spaces need to be added
                            longest_digit = max(len(f), len(s)) + 2
                            line1 += f.rjust(longest_digit) + "    "
                            line2 += o + s.rjust(longest_digit-1) + "    "
                            line3 += "-" * longest_digit + "    "
            line1 = line1.rstrip()
            line2 = line2.rstrip()  # Removing the last four whitespaces from each line
            line3 = line3.rstrip()
            res += "\n".join([line1, line2, line3])

        return res.rjust(longest_digit) + "    "

# print(arithmetic_arranger(['3801 - 2', '123 + 49']))
#
# print(arithmetic_arranger(['3801 - 2', '123 + 49']))



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
