import importlib

def test(name):
    paralib = ['a','b','c','d','e','f','g','h','i']

    ali_solution = 'problem.'+name+'.'+name
    solution = 'solution.'+name+'.'+name
    case_from = 'solution.'+name+'.test_cases'

    case_module = importlib.import_module(case_from)
    cases = case_module.get()

    ali_module = importlib.import_module(ali_solution)
    my_module = importlib.import_module(solution)

    for case in cases:
        paras = {}
        expr = 'solve('
        nn = 0
        for pa in case:
            paras[paralib[nn]] = pa
            if nn > 0:
                expr += ','
            expr+=paralib[nn]
            nn +=1
        expr +=')'

        paras['solve']= ali_module.solve
        ali_answer = eval(expr,{}, paras)
        paras['solve']= my_module.solve
        cor_answer = eval(expr, {}, paras)
        if ali_answer != cor_answer:
            print "Wrong at case: "+str(case)
            exit()

    print "Accept!"


if __name__ == "__main__":
    # problem_name = raw_input("Enter the name of problem you want to test: ")
    problem_name = 'is_prime_number'
    test(problem_name)