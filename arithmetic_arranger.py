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

        elif "-" in problem:
            problem = problem.split("-")
            if len(problem[0]) > 4 or len(problem[1]) > 4:
                return "Error: Numbers cannot be more than four digits."
        else:
            return "Error: Operator must be '+' or '-'."

        line1 = ""  # the line containing the first operand
        line2 = ""  # the line containing the operator and second operand
        line3 = ""  # the line containing dashes
        line4 = ""  # answer to each individual problem

        for i, sub in enumerate(problem_list):
            first_operands = [''.join(sub.split()[0])]
            operators = [''.join(sub.split()[1])]
            second_operands = [''.join(sub.split()[2])]

            for f in first_operands:
                if not (f.isdigit()):
                    return "Error: Numbers must only contain digits."
                for o in operators:
                    for s in second_operands:
                        if not (s.isdigit()):
                            return "Error: Numbers must only contain digits."
                        # each operand not more than 4 digits second line should also have two more chars:
                        # operator and a space b/w operator and sec operand in total 6 spaces should be reserved
                        # after each operand, four spaces need to be added
                        longest_digit = max(len(f), len(s)) + 2
                        line1 += f.rjust(longest_digit) + "    "
                        line2 += o + s.rjust(longest_digit - 1) + "    "
                        line3 += "-" * longest_digit + "    "
                        operation_res = str(eval(f + o + s))
                        line4 += operation_res.rjust(longest_digit) + "    "

    line1 = line1.rstrip()
    line2 = line2.rstrip()  # Removing the last four whitespaces from each line
    line3 = line3.rstrip()
    arranged_string = "\n".join([line1, line2, line3])

    if result:  # Adding the fourth line if the result argument is True
        line4 = line4.rstrip()
        arranged_string += "\n" + line4

    return arranged_string

