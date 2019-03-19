#!/usr/bin/env python3

import random
import itertools
import sys, getopt
import argparse
import numpy as np
from sklearn import preprocessing

def get_args():
  parser = argparse.ArgumentParser(description='generates vectors for community simulation')
  parser.add_argument('-f', '--profile', help='profile file path',
    type=str, metavar='PROFILE', required=True)
  parser.add_argument('-g', '--groups', help='nb of groups',
    type=int, metavar='GROUPS', required=True)
  parser.add_argument('-m', '--meta', help='nb of metagenomes by groups',
    type=int, metavar='META', required=True)
  parser.add_argument('-o', '--output', help='output directory',
    type=str, metavar='OUTPUT', required=True)

  return parser.parse_args()

def get_meta(vec, nb):

    for x in range(nb):
        list2=list()
        for i in np.nditer(vec):
            #print(i, end=' ')
            temp=abs(float(random.gauss(0, i)))
            list2.append(float(temp))

        vec2 = np.array(list2)
        vec_temp = np.add(vec, vec2)
        vecsum=np.sum(vec_temp)
        norm_vec=vec_temp/vecsum

        if x==0:
            vec_total=norm_vec
            #print(vec_total.shape)
        else :
            vec_total=np.vstack((vec_total, norm_vec)) 
            #print(vec_total.shape)
        
#    vec3_normalized_l1 = preprocessing.normalize(vec_total, norm='l1')

    return vec_total

def get_group(vec):
    list2=list()
    for i in np.nditer(vec):
        #print(i, end=' ')
        temp=abs(float(random.gauss(1, i)))
        list2.append(float(temp))

    vec2 = np.array(list2)
    group = np.add(vec, vec2)
    groupsum=np.sum(group)
    print(groupsum)
    norm_group=group/groupsum
    print(np.sum(norm_group))
    return norm_group

def main():
    args = get_args()
    outfile= args.output
    myprofile= args.profile
    mymeta= args.meta
    mygroup= args.groups
    my_vec = list()

    fout = open(outfile, 'w')

    fin = open(myprofile, "r")
    for x in fin:
        name, abundance = x.split("\t")
        my_vec.append(float(abundance.strip()))

    vec = np.array(my_vec)
    #print(np.sum(vec))

    if mygroup==1:
        new_vec = get_meta(vec, mymeta)
        print(new_vec)
        print(new_vec.shape)
        #print(np.sum(new_vec))
    else :
        for x in range(mygroup):
            new_group=get_group(vec)
            new_vec=get_meta(new_group, mymeta)
            print(new_vec)


if __name__ == "__main__":main()