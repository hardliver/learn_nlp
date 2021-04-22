#coding=utf8
from data import data
import json
import logging


def prints(s):
    pass
    print(s)

def get_startprob():
    """get BMES matrix   
    """
    c = 0
    c_map = {"B":0, "M":0, "E":0, "S":0}

    #caculate the count
    for v in data :
        for key,value in v.items():
            c += 1
            print(f"key {key}, value[0] is {value[0]}")
            c_map[value[0]] += 1
            print(f"c_map[value[0]] is {c_map[value[0]]}")
    return [c_map[i]/float(c) for i in "BMES"]

def get_transmat():
    """get transmat of status
    """
    c = 0
    #record BE:1,BB:2
    c_map = {}
    for v in data :
        for key,value in v.items():
            print(f"key {key}, value[0] is {value[0]}")
            for v_i in range(len(value)-1):
                couple = value[v_i:v_i+2]
                c_couple_source = c_map.get(couple,0)
                c_map[couple] = c_couple_source + 1
                c += 1
            #c_map[value[0]]=c_map[value[0]] +1
            #prints("c_map[value[0]] is "+str(c_map[value[0]]) )
    print(f"get_transmat's c_map is {c_map}")

    res=[]
    for i in "BMES":
        col_count = 0
        for j in "BMES":
            col_count += c_map.get(i+j,0)
        col = [c_map.get(i+j,0)/float(col_count) for j in "BMES"]
        res.append(col)
    return res

def get_words():
    return u"我要吃饭天气不错谢天地"

def get_word_map():
    words=get_words()
    res={}
    for i in range(len(words)):
        res[words[i]]=i
    return res

def get_array_from_phase(phase):
    word_map=get_word_map()
    res=[]
    for key in phase:
        res.append(word_map[key])
    return res

def get_emissionprob():
    #get emmissionprob of status and observers
    c = 0
    #record Bc=0
    #record B我:1,B吃:2
    c_map = {}
    for v in data:
        for key,value in v.items():
            print(f"value[0] is {value[0]}")
            for v_i in range(len(value)):
                couple = value[v_i]+key[v_i]
                print(f"emmition's couple is {couple}")
                c_couple_source = c_map.get(couple,0)
                c_map[couple] = c_couple_source+1
                c += 1
    print(f"emmition's c_map is {c_map}")

    res=[]
    words = get_words()
    for i in "BMES":
        col = [c_map.get(i+j,0)/float(c) for j in words]
        res.append(col)
    return res

if __name__ == "__main__":
    pass
    #print("startprob is ",get_startprob())
    print("transmat is " ,get_transmat())
    #print("emissionprob is " , get_emissionprob())
    #print("word map is ",get_word_map())
