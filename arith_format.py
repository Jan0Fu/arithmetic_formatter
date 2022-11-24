def arithmetic_arranger(x, solve=False) :
    mathlist = list()
    numlist = list()
    onlynumbers = list()
    mathlist.append(x)
    first = ''
    second = ''
    third = ''
    fourth = ''
    
    for problems in mathlist :
        numproblems = len(problems)

        if numproblems > 5 : 
            return ('Error: Too many problems.')
        
        for problem in problems :
            if problem.find('*') > -1 or problem.find('/') > -1: 
                return ("Error: Operator must be '+' or '-'.")

            numlist.append(problem[:problem.find(' ')])
            numlist.append(problem[problem.find(' ') + 1:problem.find(' ') + 2])
            numlist.append(problem[problem.find(' ') + 3:])
            onlynumbers.append(problem[:problem.find(' ')])
            onlynumbers.append(problem[problem.find(' ') + 3:])
        
        for item in onlynumbers:
            if len(item) > 4 :
                return ('Error: Numbers cannot be more than four digits.')
    
        for item in onlynumbers :
            if item.isdigit() is False :
                return ('Error: Numbers must only contain digits.')

        for problem in x :

            first_operand = problem.split(' ')[0]
            operator = problem.split(' ')[1]
            second_operand = problem.split(' ')[2]
            solution = eval(first_operand + operator + second_operand)

            length = max(len(first_operand), len(second_operand)) + 2
            toprow = str(first_operand).rjust(length)
            midrow = operator + str(second_operand).rjust(length -1)
            line = '' 
            bottomrow = str(solution).rjust(length)

            for z in range(length) :
                line += '-'

            first += toprow + '    '
            second += midrow + '    '
            third += line + '    '
            fourth += bottomrow + '    '
            
        first = first[:len(first) -4]
        second = second[:len(second) -4]
        third = third[:len(third) -4]
        fourth = fourth[:len(fourth) -4]
                
        if solve is True :
            string = '\n'.join((first, second, third, fourth))
        else :
            string = '\n'.join((first, second, third))

    return print(string)

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)