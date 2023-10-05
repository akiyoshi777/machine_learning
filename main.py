import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

INPUt_DIR = '../data'

def spam_decision(x):
    '''スパムメールか否かを判定(ルールに基づく手法)'''
    if x.find('search for boy-friend') != -1:    # 文章が無ければ-1を返す。 
        return True
    if x.find('No photo') != -1:
        return True
    return False

def sigmoid_function_form():
    fig, ax = plt.subplots()
    x = np.linspace(-10, 10, 1000)
    ax.plot(x, 1/(1+np.exp(-x)))
    plt.show()

def main():
    x = 'I am A. No photo.'
    #sigmoid_function_form()
    #print(spam_decision(x))
    x = [1,2,3,4]
    y = [2,3,4,5]
    
    # グラフを描画
    plt.plot(x, y)
    plt.show()

if __name__ == '__main__':
    main()
