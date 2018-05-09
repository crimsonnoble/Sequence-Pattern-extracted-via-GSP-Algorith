#by Jansen Domoguen
import copy

def measure_prediction_support(freq_set,countries):
    measure=0
    for seq in freq_set:
        if count_support3(seq,countries):
            measure+=1

    return measure



def count_support3(list_set,countries):
    count = 0
    min_sup =0.3
    length=len(list_set)
    max_count = len(countries)
    for country in countries:
        wk=0
        for i in range((len(country)//4),len(country)//2):
            set1=country[i]
            dumy_set=set(list_set[wk])
            if set1.issuperset(dumy_set):
                wk=wk+1
                if wk==length:
                    count=count+1
                    break
        if float(count / max_count) >= min_sup:
            return True

    return False