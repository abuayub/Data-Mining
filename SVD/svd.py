# -*- coding: utf-8 -*-
import os
import math
import string
import PIL
import csv
import numpy as np
import pandas

def main():
    reader=csv.reader(open("att.csv","rt"),delimiter=',')
    x=list(reader)
    result = []
    result = np.array(x).astype('float')
    print(result)
    print(result.shape)
    
    U, S, V = np.linalg.svd(result, full_matrices=True)
    print(U.shape)
    print(S.shape)
    print(V.shape)
    print(S[0])
    print(S[1])
    #print(U)
    #np.reshape(U, (30,2))  
    S1 = np.matrix('0.,0.;0.,0.')
    S1[0,0]= S[0]
    S1[1,1]= S[1]  
    print(S1)
    final = []
    U=np.delete(U, np.s_[2:30], axis= 1)
    print("**********************")
    print (U)
    print(U.shape)
    final = U*S1;
    print("----------------------")
    print(final)
    print(final.shape)

    pd = pandas.DataFrame(final)
    pd.to_csv("attreduced.csv")
main()

