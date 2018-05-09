#by Jansen Domoguen
import copy



def seq_pattern(freq_set,countries):
    candi_patt=candi_generator(freq_set)
    seq_patt = []
    for x in candi_patt:
        if count_support2(x,countries):
            seq_patt.append(x)

    return seq_patt

def candi_generator(freq_set):

    freq_set.sort()
    seq_patt = []
    dict1 = Srem_seq(freq_set)
    dict2 = Lrem_seq(freq_set)
    length = len(freq_set)
    match=[]
    for k in range(length):
        avail_set = list(range(length))
        match.extend(equal_to(dict1[k], dict2, avail_set))
        if len(match)>0:
            dumy_seq_patt = join_opp(match, freq_set, k)
            seq_patt.extend(prune(dumy_seq_patt, freq_set))
            del dumy_seq_patt[:]
            del match[:]

    seq_patt=remove_dup(seq_patt)
    return seq_patt

def Srem_seq(freq_set):
    start_dict = {}
    k = 0
    for seq in freq_set:
        dumy_list=copy.deepcopy(seq)
        del dumy_list[0][0]
        if dumy_list[0]==[]:
            del dumy_list[0]
        start_dict[k]=dumy_list
        k = k + 1
    return start_dict


def Lrem_seq(freq_set):
    last_dict = {}
    k = 0
    for seq in freq_set:
        dumy_list=copy.deepcopy(seq)
        del dumy_list[-1][-1]
        if dumy_list[-1]==[]:
            del dumy_list[-1]
        last_dict[k]=dumy_list
        k = k + 1

    return last_dict

def equal_to(seq, dict2, avail_set):
    num = []
    for k in avail_set:
        if seq==dict2[k]:
            num.append(k)
    return num


def join_opp(list1, freq_set, k):
    seq_patt = []
    ref_set = freq_set[k]
    length = len(ref_set)
    for num in list1:
        dumy_list = copy.deepcopy(ref_set)
        dumy_list2 = freq_set[num]

        if length < len(dumy_list2):
            dumy_list.append(dumy_list2[-1])


        elif length == len(dumy_list2):
            if len(dumy_list2[-1]) > 1:
                for x in dumy_list2[-1]:
                    if x not in dumy_list[-1]:
                        dumy_list[-1].append(x)

            else:
                dumy_list.append(dumy_list2[-1])
        else:
            del dumy_list[-1]
            dumy_list.append(dumy_list2[-1])

        seq_patt.append(dumy_list)

    return seq_patt


def prune(unprune_set, prev_set):
    dumy_list = []
    count = 0
    max_count = len(prev_set)
    for unprune in unprune_set:
        for prev in prev_set:
            if is_contiguous_subseq(unprune,prev):
                count=count+1
                if float(count/max_count)>=.01:
                    dumy_list.append(unprune)

    return dumy_list


def is_contiguous_subseq(unprune, prev):
    k = 0
    counter=0
    signal = False
    leng=len(prev)
    dumy2 =set(unprune[k])
    for seq in prev:
        dumy1=set(seq)
        if dumy2.issuperset(dumy1):
            signal = True
            k += 1
            if k==leng:
                return True
            counter+=1
            if counter==len(unprune):
                return False
            dumy2=set(unprune[k])
        else:
            if signal:
                return False
    return False

def remove_dup(seq_patt):
    seq_dumy = []
    for x in seq_patt:
        if x not in seq_dumy:
            seq_dumy.append(x)
    return seq_dumy




def count_support2(list_set,countries):
    count = 0
    min_sup =0.6
    length=len(list_set)
    max_count = len(countries)
    for country in countries:
        wk=0
        for i in range(len(country)//4):
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


def count_support(list_set,countries):
    count = 0
    min_sup =0.6
    length=len(list_set)
    max_count = len(countries)
    for country in countries:
        wk=0
        for set1 in country:
            dumy_set=set(list_set[wk])
            if set1.issuperset(dumy_set):
                wk=wk+1
                if wk==length:
                    count=count+1
                    break
        if float(count / max_count) >= min_sup:
            return True

    return False

