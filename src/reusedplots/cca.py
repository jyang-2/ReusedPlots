import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from .pca import scree


def plot_inputs(df_X, df_Y, evr_x, evr_y, annot=False):
    mosaic = [
        ['X', 'Y'],
        ['X_scree', 'Y_scree']
              ]
    fig_inputs = plt.figure(constrained_layout=True, figsize=(11, 11))

    n_odors, n_comp = df_X.shape

    axd = fig_inputs.subplot_mosaic(
        mosaic,
        gridspec_kw={"height_ratios": [3, 1],
                     "width_ratios": [1, 1]},
    )

    cmap = 'Spectral_r'
    is_square = False

    sns.heatmap(df_X,
                square=is_square,
                xticklabels=True,
                yticklabels=True,
                cbar_kws=dict(shrink=0.5),
                ax=axd['X'],
                cmap=cmap,
                annot=annot,
                ).set(title='X')

    sns.heatmap(df_Y,
                square=is_square,
                xticklabels=True,
                yticklabels=True,
                cbar_kws=dict(shrink=0.5),
                ax=axd['Y'],
                cmap=cmap,
                annot=True
                ).set(title='Y')

    scree(evr_x, axd['X_scree'])
    scree(evr_y, axd['Y_scree'])

    return fig_inputs, axd
