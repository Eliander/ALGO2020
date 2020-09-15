from ric_bin_2.grader import confronto_con, answer, ottieni_n
'''
n: limite superiore sul valore da indovinare
'''
def ricerca(n: int):
    min_value = 1
    max_value = n
    while True:
        choose = int((max_value - min_value)/2 + min_value)
        #print('idea: {0}'.format(choose))
        sol = confronto_con(choose)
        # g > x => il numero da trovare è nel lato sopra
        if sol == -1:
            min_value = choose + 1
            #print('maggiore')
        elif sol == 1:
            max_value = choose - 1
            #print('minore')
        elif sol == 0:
            #print(choose)
            break
    answer(choose)

