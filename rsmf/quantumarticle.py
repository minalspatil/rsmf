"""
Support for the quantumarticle documentclass of Quantum journal.
"""

import matplotlib.pyplot as plt

from .revtexlike import RevtexLikeFormatter, RevtexLikeParser


class QuantumarticleFormatter(RevtexLikeFormatter):
    """Sets up the plot with the fitting arguments so that the font sizes of the plot
    and the font sizes of the document are well aligned.

    Args:
        columns (str, optional):  the columns you used to set up your quantumarticle,
            either "onecolumn" or "twocolumn". Defaults to "twocolumn".
        paper (str, optional): the paper size you used to set up your quantumarticle,
            either "a4paper" or "letterpaper". Defaults to "a4paper".
        fontsize (int, optional): the fontsize you used to set up your quantumarticle,
            either 10, 11 or 12. Defaults to 10.
    """

    _widths = {
        "onecolumn": {"a4paper": 5.93, "letterpaper": 6.16},
        "twocolumn": {"a4paper": 3.22, "letterpaper": 3.34},
    }

    _wide_widths = {
        "onecolumn": {"a4paper": 5.93, "letterpaper": 6.16},
        "twocolumn": {"a4paper": 6.72, "letterpaper": 6.95},
    }

    _colors = {"quantumviolet": "#53257F", "quantumgray": "#555555"}

    def __init__(self, columns="twocolumn", paper="a4paper", fontsize=10, **kwargs):
        super().__init__(columns, paper, fontsize)

    def set_rcParams(self):
        """Adjust the rcParams to the default values for Quantumarticle."""
        super().set_rcParams()

        plt.rcParams["font.family"] = "sans-serif"

        plt.rcParams[
            "pgf.preamble"
        ] = r"\usepackage{lmodern} \usepackage[utf8x]{inputenc} \usepackage[T1]{fontenc}"

        plt.rcParams["axes.edgecolor"] = self._colors["quantumgray"]


"""Parser for the quantumarticle document class."""
quantumarticle_parser = RevtexLikeParser(["{quantumarticle}"], QuantumarticleFormatter)
