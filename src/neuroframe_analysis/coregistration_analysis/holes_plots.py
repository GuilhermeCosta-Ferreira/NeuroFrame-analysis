# ================================================================
# 0. Section: Imports
# ================================================================
import numpy as np

from ..plots import save_figure_protocol, SaveConfiguration, plot_group_vs_one_metric_bar



# ================================================================
# 1. Section: Plots
# ================================================================
@save_figure_protocol
def plot_group_hole_volume_bar(hole_volumes: np.ndarray | list, mice_list: np.ndarray | list | None = None) -> tuple:
    fig, ax = plot_group_vs_one_metric_bar(
        data=hole_volumes,
        metric_name="Volume of Holes",
        metric_type="mm³",
        group_names=mice_list)

    return fig, ax, _hole_volume_plot_config()


# ──────────────────────────────────────────────────────
# 1.1 Subsection: SaveConfig
# ──────────────────────────────────────────────────────
def _hole_volume_plot_config():
    config = SaveConfiguration(
        file_name="group_hole_volume_plot",
        save_type="none"
    )

    return config
