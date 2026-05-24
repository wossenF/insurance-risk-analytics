# src/hypothesis_tests.py

from scipy import stats
import numpy as np
import pandas as pd

def t_test(group_a, group_b):
    stat, p_value = stats.ttest_ind(group_a, group_b, equal_var=False)
    return stat, p_value

def chi_square_test(contingency_table):
    stat, p_value, dof, expected = stats.chi2_contingency(contingency_table)
    return stat, p_value

def z_test(p1, p2, n1, n2):
    p = (p1*n1 + p2*n2) / (n1 + n2)

    se = np.sqrt(p * (1 - p) * (1/n1 + 1/n2))
    z = (p1 - p2) / se

    p_value = 2 * (1 - stats.norm.cdf(abs(z)))
    return z, p_value