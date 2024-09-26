import numpy as np
import matplotlib.pyplot as plt


def compute_and_draw_mandelbrot_set(
    *,
    itercount: int = 60,
    bound: int = 10,
    x_axis=np.linspace(-2, stop=2, num=1_000),
    y_axis=np.linspace(-2, stop=2, num=1_000),
    colormap: str = "jet",
    x_y_pairs=list(),
) -> None:
    def helper_function_for_convergence(
        c: complex,
        *,
        seed: int | float | complex = 0,
        returnvalue_when_convergent: int | float | complex = 0,
    ) -> int | float | complex:
        for current_step in range(itercount):
            if abs(seed) >= bound:
                _ = "sequence is divergent"
                return current_step
            seed = seed**2 + c
        _ = "sequence is convergent"
        return returnvalue_when_convergent

    x_y_pairs = [
        [helper_function_for_convergence(complex(x, y)) for x in x_axis] for y in y_axis
    ]

    def setup_plot() -> None:
        figure = plt.axes().pcolormesh(x_axis, y_axis, x_y_pairs, cmap=colormap)
        plt.colorbar(figure)
        plt.xlabel("Re(z)")
        plt.ylabel("Im(z)")
        plt.title("Mandelbrot set")

    setup_plot()
    plt.show()


def main(*args, **kwargs) -> None:
    """
    https://en.wikipedia.org/wiki/Mandelbrot_set
    """
    compute_and_draw_mandelbrot_set()


if __name__ == "__main__":
    main()
