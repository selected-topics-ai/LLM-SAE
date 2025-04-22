import pandas as pd

from matplotlib import pyplot as plt


def visualize_score_plots(non_normalized: pd.DataFrame, normalized: pd.DataFrame, feature_name: str):

    fig, axs = plt.subplots(figsize=(5, 5), ncols=2, nrows=2)

    ax = axs.flatten()

    ax[0].plot(non_normalized['alpha'], non_normalized['coherence_score'], label="Non-normalized steering")
    ax[0].set_xlabel("alpha")
    ax[0].set_ylabel("Coherence score")
    ax[0].grid(True, alpha=0.2)

    ax[1].plot(non_normalized['alpha'], non_normalized['behavioral_score'])
    ax[1].set_xlabel("alpha")
    ax[1].set_ylabel("Behavioral score")
    ax[1].grid(True, alpha=0.2)

    ax[2].plot(normalized['alpha'], normalized['coherence_score'], color='green', label="Normalized steering")
    ax[2].set_xlabel("alpha")
    ax[2].set_ylabel("Coherence score")
    ax[2].grid(True, alpha=0.2)

    ax[3].plot(normalized['alpha'], normalized['behavioral_score'], color='green')
    ax[3].set_xlabel("alpha")
    ax[3].set_ylabel("Behavioral score")
    ax[3].grid(True, alpha=0.2)

    fig.suptitle(f"Different types of steering applied to SAE \"{feature_name}\" feature")
    fig.legend(bbox_to_anchor=(1.45, 1))
    plt.tight_layout()
    plt.show()