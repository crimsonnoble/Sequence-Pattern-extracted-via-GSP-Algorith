#by Jansen Domoguen
from GSP_1st_2nd import fir_freq_set,sec_freq_set
from GSP_main_2nd import candi_generator, seq_pattern
from GSP_Prediction import measure_prediction_support
import copy
from multiprocessing  import Pool
import glob
import os
import time
import pandas as pd





def country_seq(filename):
    raw_data = pd.read_csv(filename, na_values=[" ", "0", "#REF!"],
                           dtype={"Track Name": str, "Position": object, "Week": float})
    raw_data.dropna(thresh=3, inplace=True)
    raw_data.Week = raw_data.Week.shift(1)
    raw_data.at[0, 'Week'] = 1
    proc_data = raw_data.groupby('Week').head(10).reset_index(drop=True)
    proc_data.rename(index=str, columns={"Track Name": "Songs"}, inplace=True)
    dumy_list = list(proc_data["Songs"])

    i = 0
    country_seq = []
    for x in dumy_list:
        if i % 10 == 0:
            country_seq.append({x})
        else:
            country_seq[i // 10].add(x)
        i = i + 1

    return country_seq






def main():
    start_time = time.time()
    os.chdir("C:\\Users\\Jansen Domoguen\\Desktop\\database\\spotify\\For_project")
    path = r'C:\Users\Jansen Domoguen\Desktop\database\spotify\For_project'
    filenames = glob.glob(path + "/*.csv")

    p = Pool()
    countries = p.map(country_seq, filenames)
    raw_songs = list(set([song for country in countries for sub_songs in country for song in sub_songs]))
    #print(len(raw_songs))

    p.close()
    p.join

    first_seq=fir_freq_set(raw_songs,countries)
    second_seq=sec_freq_set(first_seq,countries)
    print(len(first_seq))
    print(len(second_seq))

    dumy_seq=second_seq
    size=len(second_seq)

    i=3
    
    while size>0:

        Sequence=seq_pattern(dumy_seq,countries)
        size=len(Sequence)
        measure=measure_prediction_support(Sequence,countries)
        #print("Sequential Pattern ",i,"-",Sequence)
        print("The number of ",str(i),"-sequence patterns is ",len(Sequence))
        if len(Sequence)>0:
            print("The of sequence pattern that passes for ", i, "-sequence patern is ", measure)
            print("The ratio is ", measure / len(Sequence))
        i+=1
        dumy_seq=Sequence

    print("My program took", time.time() - start_time, "to run")


if __name__=="__main__":
    main()