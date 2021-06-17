from __future__ import division

def average(array):
    N =len(set(array))
    avg = (sum(set(array)) / N)
    return avg

array = [161,182,161,154,176,170,167,171,170,174]

average(array)
