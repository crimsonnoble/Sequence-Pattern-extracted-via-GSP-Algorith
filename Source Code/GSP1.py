#by Jansen Domoguen
import copy



def count_support2(list_set,countries):
	count = 0
	min_sup =.5
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
	min_sup =.5
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

def fir_freq_set(raw_songs,countries):
	raw_songs.sort()
	fir_freq_set = []
	seq = []
	for s in raw_songs:
		seq.append([s])
		if count_support2(seq,countries):
			fir_freq_set.append(s)
			del seq[:]
		else:
			del seq[:]
	return fir_freq_set






def sec_freq_set(prev_set,countries):
	prev_set.sort()
	sec_freq_set=[]
	sec_dumy=[]
	dumy_list=[]
	for s in prev_set:
		dumy_list.append([s])
		for s1 in prev_set:
			dumy_list.append([s1])
			if count_support2(dumy_list,countries):
				container=copy.deepcopy(dumy_list)
				sec_freq_set.append(container)
				del dumy_list[1]
			else:
				del dumy_list[1]
		del dumy_list[:]

	dumy_list2=[]
	i=1
	for s in prev_set:
		dumy_list2.append([s])
		for s2 in prev_set[i:]:
			dumy_list2[0].append(s2)
			if count_support(dumy_list2,countries):
				container = copy.deepcopy(dumy_list2)
				sec_freq_set.append(container)
				dumy_list2[0].remove(s2)
			else:
				dumy_list2[0].remove(s2)
		del dumy_list2[0]
		i=i+1


	for x in sec_freq_set:
		if x not in sec_dumy:
			sec_dumy.append(x)

	sec_freq_set=sec_dumy

	return sec_freq_set




