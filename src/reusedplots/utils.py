import seaborn as sns
import matplotlib.pyplot as plt

stim_grid_all = {
    "kiwi_ea_eb_only":
        [
            [
                "pfo @ 0.0",
                "eb @ -5.5",
                "eb @ -4.5",
                "eb @ -3.5"
            ],
            [
                "ea @ -6.2",
                "ea @ -6.2, eb @ -5.5",
                "ea @ -6.2, eb @ -4.5",
                "ea @ -6.2, eb @ -3.5"
            ],
            [
                "ea @ -5.2",
                "ea @ -5.2, eb @ -5.5",
                "ea @ -5.2, eb @ -4.5",
                "ea @ -5.2, eb @ -3.5"
            ],
            [
                "ea @ -4.2",
                "ea @ -4.2, eb @ -5.5",
                "ea @ -4.2, eb @ -4.5",
                "ea @ -4.2, eb @ -3.5"
            ]
        ],

    "control1_top2_ramps":
        [
            [
                "pfo @ 0.0",
                "2h @ -7.0",
                "2h @ -6.0",
                "2h @ -5.0"
            ],
            [
                "1o3ol @ -5.0",
                "1o3ol @ -5.0, 2h @ -7.0",
                "1o3ol @ -5.0, 2h @ -6.0",
                "1o3ol @ -5.0, 2h @ -5.0"
            ],
            [
                "1o3ol @ -4.0",
                "1o3ol @ -4.0, 2h @ -7.0",
                "1o3ol @ -4.0, 2h @ -6.0",
                "1o3ol @ -4.0, 2h @ -5.0"
            ],
            [
                "1o3ol @ -3.0",
                "1o3ol @ -3.0, 2h @ -7.0",
                "1o3ol @ -3.0, 2h @ -6.0",
                "1o3ol @ -3.0, 2h @ -5.0"
            ]
        ],

    "control1":
        [
            ["pfo @ 0.0", "ms @ -3.0", "va @ -3.0"],
            ["fur @ -4.0", "1o3ol @ -3.0", "2h @ -5.0"],
            ["cmix @ -2.0", "cmix @ -1.0", "cmix @ 0.0"]

        ],
    "kiwi": [
        ["pfo @ 0.0", "EtOH @ -2.0", "IaOH @ -3.6"],
        ["IaA @ -3.7", "ea @ -4.2", "eb @ -3.5"],
        ["kiwi @ -2.0", "kiwi @ -1.0", "kiwi @ 0.0"]
    ]

}


def get_stim_grid_subplots(movie_type):
    fig_mosaic = stim_grid_all[movie_type]

    if movie_type in ['kiwi_ea_eb_only', 'control1_top2_ramps']:
        hspace = 0.5
    else:
        hspace = 0.4
    fig, ax_dict = plt.subplot_mosaic(fig_mosaic,
                                      #sharex='all', sharey='all',
                                      # subplot_kw=dict(sharex='all',
                                      #                 sharey='all',
                                      #                 ),
                                      gridspec_kw=dict(
                                          top=0.9,
                                          # height_ratios=hratio,
                                          wspace=0.2,
                                          hspace=0.2
                                      ),
                                      figsize=(11, 8.5),
                                      )
    return fig, ax_dict


def draw_stim_lines(ax, stim_labels, stim_ict, lut=None,
                    text_kwargs=None,
                    line_kwargs=None,
                    fraction_yrange=1):
    """
    Draw vertical lines on axes, with stimulus str labels.
    To draw lines on bottom, set line_kwargs['zorder'] = 0.

    """
    xmin, xmax = ax.get_xlim()

    ymin, ymax = ax.get_ylim()
    yrange = ymax - ymin

    if fraction_yrange != 1:
        ymax = ymin + fraction_yrange * yrange

    line_kwargs0 = dict(linestyle='-', linewidth=2, alpha=0.5)
    text_kwargs0 = dict(fontsize=8, rotation='vertical', va='top', ha='right')

    if text_kwargs is not None:
        text_kwargs0.update(text_kwargs)

    if line_kwargs is not None:
        line_kwargs0.update(line_kwargs)

    for ict, stim in zip(stim_ict, stim_labels):
        if (lut is not None) and (stim in lut.keys()):
            ax.axvline(ict, color=lut[stim], **line_kwargs0)
        else:
            ax.axvline(ict, **line_kwargs0)
        ax.text(ict, ymax, stim, **text_kwargs0)

    ax.set_xlim([xmin, xmax])
    ax.set_ylim([ymin, ymax])
    return ax
