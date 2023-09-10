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
  

  
 
  
  

    
