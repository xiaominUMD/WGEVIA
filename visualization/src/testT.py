from scipy.stats import ttest_ind_from_stats
import numpy as np
s = ttest_ind_from_stats(mean1=0.996, std1=0.002, nobs1=10,
                     mean2=0.996, std2=0.001, nobs2=10)
print(s)
