import itertools
import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def binByMean(data,binNo):
    data=np.sort(data)
    total=len(data)
    binWeight=int(total/binNo)
    bin=np.zeros((binNo,binWeight))
    index=0
    for i in range(binNo):
        for j in range(binWeight):
            bin[i,j]=data[index]
            index+=1
    result = np.zeros(binNo)

    for i in range(binNo):
        result[i] = np.mean(bin[i])

    return result






