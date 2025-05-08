def who_spent_more(first_candidate, second_candidate):
    first_candidate_total_expenses = 0
    second_candidate_total_expenses = 0
    
    for expense1, expense2 in zip(first_candidate, second_candidate):
        first_candidate_total_expenses += expense1
        second_candidate_total_expenses += expense2
        
    if first_candidate_total_expenses > second_candidate_total_expenses:
        return "O primeiro candidato gastou mais"
    elif second_candidate_total_expenses < first_candidate_total_expenses:
        return "O segundo candidato gastou mais"
    else:
        return "Os dois canditados gastaram a mesma quantidade de dinheiro"


joao_expenses = [300, 500, 200, 800]
pedro_expenses = [200, 400, 500, 700]
print(who_spent_more(joao_expenses, pedro_expenses))