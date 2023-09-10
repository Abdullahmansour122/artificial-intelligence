    from logic import Expression


class Action:
    def __init__(self, name, precond_pos, precond_neg, effect_add, effect_rem):
        self.name = name
        self.precond_pos = precond_pos
        self.precond_neg = precond_neg
        self.effect_add = effect_add
        self.effect_rem = effect_rem

class PDDL:
    def __init__(self, init, actions, goal_test):
        self.init = init
        self.actions = actions
        self.goal_test = goal_test

def have_cake_and_eat_cake_too():
    init = [expr('Have(Cake)')]

    def goal_test(kb):
        required = [expr('Have(Cake)'), expr('Eaten(Cake)')]
        return all(kb.ask(q) is not False for q in required)

    precond_pos = [expr('Have(Cake)')]
    precond_neg = []
    effect_add = [expr('Eaten(Cake)')]
    effect_rem = [expr('Have(Cake)')]
    eat_cake = Action(expr('Eat(Cake)'), precond_pos, precond_neg, effect_add, effect_rem)

    precond_pos = []
    precond_neg = [expr('Have(Cake)')]
    effect_add = [expr('Have(Cake)')]
    effect_rem = []
    bake_cake = Action(expr('Bake(Cake)'), precond_pos, precond_neg, effect_add, effect_rem)

    return PDDL(init, [eat_cake, bake_cake], goal_test)

def expr(s):
    return Expression.from_string(s, symbols)

def main():
    print(have_cake_and_eat_cake_too())

if __name__ == '__main__':
    main()
  

  
 
  
  

    

import os
from udacity_pa import udacity

nanodegree = 'nd898'
projects = ['classical_planning']
filenames_all = ['my_planning_graph.py', 'report.pdf']

def submit(args):
    filenames = []
    for filename in filenames_all:
        if os.path.isfile(filename):
            filenames.append(filename)

    if 'my_planning_graph.py' not in filenames:
        raise RuntimeError(
            "The file 'my_planning_graph.py' was not found in your current directory. This " +
            "file MUST be included in every PA submission.")
    if 'report.pdf' not in filenames:
        print(
            "WARNING: Make sure your submission includes a file named 'report.pdf' if you " +
            "expect this to be your final submission in the classroom for review.")

    udacity.submit(nanodegree, projects[0], filenames, 
                   environment = args.environment,
                   jwt_path = args.jwt_path)
