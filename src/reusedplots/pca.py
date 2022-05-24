import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Scree plot
# Cumulative PVE vs. Principal Component plot


def scree(explained_variance_ratio, ax=None):
    """ Plot explained_variance_ratio"""
    n_comp = explained_variance_ratio.size
    components = np.arange(n_comp) + 1

    if ax is None:
        ax = plt.gca()

    sns.lineplot(x=components,
                 y=explained_variance_ratio,
                 marker="o",
                 ax=ax)
    sns.lineplot(x=components,
                 y=explained_variance_ratio.cumsum(),
                 marker="o",
                 ax=ax)

    ax.set(title="PVE vs. Principal Component",
           xlabel="Principal Component",
           ylabel="Proportion of Variance Explained",
           ylim=(-0.05, 1.05))
    return ax
# (sns
#  .lineplot(x=np.arange(1, 5),
#            y=pca.explained_variance_ratio_,
#            marker="o")
