import numpy as np
import matplotlib.pyplot as plt


def build_3d_point_grid(num_vectors_per_dim: int = 3) -> np.ndarray:
    """
    Builds as box of vectors in 3D space.
    """
    x = np.linspace(-1, 1, num_vectors_per_dim)
    y = np.linspace(-1, 1, num_vectors_per_dim)
    z = np.linspace(-1, 1, num_vectors_per_dim)

    X, Y, Z = np.meshgrid(x, y, z)
    point_grid = np.array([X.flatten(), Y.flatten(), Z.flatten()]).T

    return point_grid


def plot_transformation(
    transformation_matrix: np.ndarray,
    ax: plt.Axes,
) -> plt.Axes:
    """
    Plots the transformation of a 3D point grid using a transformation matrix.

    Args:
        transformation_matrix (np.ndarray): The transformation matrix.
        ax (plt.Axes): The matplotlib axes to plot on.

    Returns:
        plt.Axes: The matplotlib axes with the plot.
    """
    point_grid = build_3d_point_grid()
    transformed_points = np.dot(point_grid, transformation_matrix)

    origin = np.zeros(transformed_points.shape[0])

    # Plot the vectors to the transformed points as a quiver plot.
    quiver_plot = ax.quiver(
        origin,
        origin,
        origin,
        transformed_points[:, 0],
        transformed_points[:, 1],
        transformed_points[:, 2],
        color="r",
    )

    return ax, quiver_plot
