import numpy as np

from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

def plot_double_overlay(
    background: np.ndarray,
    foreground: np.ndarray,
    offset: int = 0,
    view: int = 0,
) -> tuple[Figure, Axes]:

    fig, ax = plt.subplots()
    target_slice = generate_slice(view, offset, background.shape)

    ax.imshow(background[target_slice], cmap='gray')
    ax.imshow(foreground[target_slice])

    plt.axis("off")
    plt.tight_layout()
    plt.show(block=False)

    return fig, ax

def generate_slice(view: int, offset: int, shape: np.ndarray) -> tuple[slice, slice, slice]:
    if view == 0: target_slice = (shape[0] // 2 + offset, slice(None), slice(None))
    elif view == 1: target_slice = (slice(None), shape[1] // 2 + offset, slice(None))
    elif view == 2: target_slice = (slice(None), slice(None), shape[2] // 2 + offset)

    return target_slice
