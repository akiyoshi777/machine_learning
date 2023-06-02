import pandas as pd
import numpy as np


INPUt_DIR = '../data'

def spam_decision(x):
    '''スパムメールか否かを判定(ルールに基づく手法)'''
    if x.find('search for boy-friend') != -1:    # 文章が無ければ-1を返す。 
        return True
    if x.find('No photo') != -1:
        return True
    return False

def main():
    x = 'I am A. No photo.'
    print(spam_decision(x))

if __name__ == '__main__':
    main()
