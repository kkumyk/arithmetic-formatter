def arithmetic_arranger(problems_list, result=False):

    # Function must only accept a maximum of five problems
    if len(problems_list) > 5:
        return "Error: Too many problems."

    for problem in problems_list:
        problem = problem.replace(" ", "")  # Removing all whitespace from problems_list

        # Checking for '+' and '-' operators
        if "+" in problem:
            problem = problem.replace("+", " ").split()
        elif "-" in problem:
            problem = problem.replace("-", " ").split()
        else:
            return "Error: Operator must be '+' or '-'."

        # Checking for length of both operands
        if len(problem[0]) > 4 or len(problem[1]) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Checking if numbers contain only digits
        if not(problem[0].isdigit() and problem[1].isdigit()):
            return "Error: Numbers must only contain digits."

        line1 = ""  # the line containing the first operand
        line2 = ""  # the line containing the operator and second operand
        line3 = ""  # the line containing dashes
        line4 = ""  # answer to each individual problem

        for i, p in enumerate(problems_list):
            first_operands = [''.join(p.split()[0])]
            operators = [''.join(p.split()[1])]
            second_operands = [''.join(p.split()[2])]

            for first in first_operands:
                for operator in operators:
                    for second in second_operands:
                        # find the longest of the two operands and add two spaces the found length
                        # the two additional spaces are needed to align the second line which will
                        # have the operator and one empty space in-front of the second operand
                        # the result number will be used to calculate the number of empty spaces
                        # and the number of dashes to add for each individual problem
                        longest_digit = max(len(first), len(second)) + 2

                        # add first operands to line1 and right align each of them with rjust method
                        # add four empty spaces at the end of each of them
                        line1 += first.rjust(longest_digit) + "    "

                        # add second operands to line2 and right align each of them with rjust method
                        # the -1 is needed to align this line with the line1 in terms of the length
                        # as this line also contains the operator
                        line2 += operator + second.rjust(longest_digit - 1) + "    "

                        line3 += "-" * longest_digit + "    "

                        # evaluate constructed individual problem string with eval() function
                        # which evaluates the expression if it is a legal Python statement;
                        # if so, it will be executed.
                        operation_res = str(eval(first + operator + second))
                        line4 += operation_res.rjust(longest_digit) + "    "

    # Remove the last four whitespaces from each line
    line1 = line1.rstrip()
    line2 = line2.rstrip()
    line3 = line3.rstrip()
    arranged_string = "\n".join([line1, line2, line3])

    if result:  # Add the fourth line if the result argument is True
        line4 = line4.rstrip()
        arranged_string += "\n" + line4

    return arranged_string

