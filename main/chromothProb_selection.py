" Seaborn - Plot Bar Chart; Author: Samuel Winnall "

################################### Notes #####################################


##############################################################################

import shutil
import errno
import sv_gen
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import csv
import sys


# load data
r_prob_neut_TSV = '../output/sumstats/prob_trends/selection/prob_random.tsv'
probN = pd.read_csv(r_prob_neut_TSV, sep="\t")

r_prob_bias_TSV = '../output/sumstats/prob_trends/selection/prob_biased.tsv'
probB = pd.read_csv(r_prob_bias_TSV, sep="\t")

r_prob_forced_TSV = '../output/sumstats/prob_trends/selection/prob_fixed.tsv'
probF = pd.read_csv(r_prob_forced_TSV, sep="\t")

# create dataframe
prob_df = pd.DataFrame(list(zip(probN, probB, probF)), columns=['Random', 'Biased', 'Fixed'])

# plot figure
sns_plot = sns.barplot(data=prob_df)
plt.savefig("../output/sumstats/prob_trends/selection/chromothProb.png")
