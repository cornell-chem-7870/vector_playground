import numpy as np
import matplotlib.pyplot as plt
from vector_playground.vector_math import plot_transformation
from matplotlib.widgets import TextBox


def _place_axes_for_textboxes(fig):
    axes = [
        [
            fig.add_axes([0.10, 0.20, 0.15, 0.03]),
            fig.add_axes([0.1, 0.15, 0.15, 0.03]),
            fig.add_axes([0.1, 0.10, 0.15, 0.03]),
        ],
        [
            fig.add_axes([0.45, 0.20, 0.15, 0.03]),
            fig.add_axes([0.45, 0.15, 0.15, 0.03]),
            fig.add_axes([0.45, 0.1, 0.15, 0.03]),
        ],
        [
            fig.add_axes([0.8, 0.20, 0.15, 0.03]),
            fig.add_axes([0.8, 0.15, 0.15, 0.03]),
            fig.add_axes([0.8, 0.10, 0.15, 0.03]),
        ],
    ]
    return axes


def _build_textboxes(fig):
    axes = _place_axes_for_textboxes(fig)

    # Start with the identity matrix as the default values.
    # Flatten so 1D for easy looping.
    default_values = np.eye(3)

    # Add textboxes to each axis
    amp_textboxes = []
    for i in range(3):
        for j in range(3):
            ax = axes[i][j]
            amp_textboxes.append(
                TextBox(ax, r"$a_{%d%d}=$" % (i, j), initial=default_values[i, j])
            )

    return amp_textboxes


def _update_axes(ax):
    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([-3, 3])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")


def main():
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection="3d")
    fig.subplots_adjust(bottom=0.4)

    __, quiver = plot_transformation(np.eye(3), ax)
    _update_axes(ax)

    textboxes = _build_textboxes(fig)

    def update_plot(val):
        transformation_matrix = np.array(
            [
                [float(textbox.text) for textbox in textboxes[:3]],
                [float(textbox.text) for textbox in textboxes[3:6]],
                [float(textbox.text) for textbox in textboxes[6:]],
            ]
        )
        ax.clear()
        __, quiver = plot_transformation(transformation_matrix, ax)
        _update_axes(ax)
        plt.draw()

    for textbox in textboxes:
        textbox.on_submit(update_plot)

    plt.show()


if __name__ == "__main__":
    main()
