.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/HW-3.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/HW-3
    .. image:: https://readthedocs.org/projects/HW-3/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://HW-3.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/HW-3/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/HW-3
    .. image:: https://img.shields.io/pypi/v/HW-3.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/HW-3/
    .. image:: https://img.shields.io/conda/vn/conda-forge/HW-3.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/HW-3
    .. image:: https://pepy.tech/badge/HW-3/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/HW-3
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/HW-3

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

====
HW-3 - Vortex Shedding Wake Analysis
====


This project analyzing time-series data from a numerically simulated turbulent wake behind an oscillating cylinder, using various static and interactive visualizations to explore vortex shedding characteristics.


This project explores the turbulent wake created by an oscillating cylinder, specifically analyzing the effects of vortex shedding across different distances from the cylinder. Using time-series data collected every 0.25 seconds over a 100-second interval, we visualize and analyze patterns in velocity and vorticity measurements along sampling lines at distances of 2D, 4D, 6D, 8D, 10D, and 12D (where D is the cylinder diameter).

The data provides insights into the behavior of turbulent wakes, characterized by variables such as Reynolds number, normalized amplitude A_star and velocity ratio U_star. 
This project includes both static and interactive visualizations to examine spatial and temporal variations in wake patterns.

Key visualizations include:

Static Plots: A time-series line plot of velocity components and a heatmap of vorticity distribution, highlighting how wake characteristics change over space and time.
Interactive Plot: A dynamic visualization that allows users to explore specific distances and time intervals, facilitating deeper insight into the wake structure.


.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.6. For details and usage
information on PyScaffold see https://pyscaffold.org/.
