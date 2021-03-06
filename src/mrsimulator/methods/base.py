# -*- coding: utf-8 -*-
import numpy as np

from .utils import generate_method_from_template
from .utils import METHODS_DATA

__author__ = "Deepansh J. Srivastava"
__email__ = "srivastava.89@osu.edu"

generic_args = r"""

Parameters
----------

name: str (optional).
    The value is the name or id of the method. The default value is None.

label: str (optional).
    The value is a label for the method. The default value is None.

description: str (optional).
    The value is a description of the method. The default value is None.

experiment: CSDM or ndarray (optional).
    An object holding the experimental measurement for the given method, if
    available. The default value is None.

channels: list (optional).
    The value is a list of isotope symbols over which the given method applies.
    An isotope symbol is given as a string with the atomic number followed by its
    atomic symbol, for example, '1H', '13C', and '33S'. The default is an empty
    list.
    The number of isotopes in a `channel` depends on the method. For example, a
    `BlochDecaySpectrum` method is a single channel method, in which case, the
    value of this attribute is a list with a single isotope symbol, ['13C'].

spectral_dimensions: List of :ref:`spectral_dim_api` or dict objects (optional).
    The number of spectral dimensions depends on the given method. For example, a
    `BlochDecaySpectrum` method is a one-dimensional method and thus requires a
    single spectral dimension. The default is a single default
    :ref:`spectral_dim_api` object.

magetic_flux_density: float (optional)
    A global value for the macroscopic magnetic flux density, :math:`H_0`,
    of the applied external magnetic field in units of T. The default is ``9.4``.

rotor_angle: float (optional)
    A global value for the angle between the sample rotation axis and the
    applied external magnetic field, :math:`\theta`, in units of rad. The default
    value is ``0.9553166``, i.e. the magic angle.
"""

args_freq = r"""
rotor_frequency: float (optional)
    A global value for the sample spinning frequency, :math:`\nu_r`, in units of Hz.
    The default value is ``0``.
"""

args_affine = r"""
affine_matrix: np.ndarray or list (optional)
    An affine transformation square matrix,
    :math:`\mathbf{A} \in \mathbb{R}^{n \times n}`, where `n` is the number of
    spectral dimensions. The affine operation follows
    :math:`\mathbf{V}^\prime = \mathbf{A} \cdot \mathbf{V}`,
    where :math:`\mathbf{V}\in\mathbb{R}^n` and :math:`\mathbf{V}^\prime\in\mathbb{R}^n`
    are the initial and transformed frequency coordinates.
"""

# additional_args = args_freq + args_affine

returns = r"""
Return
------
    A :class:`~mrsimulator.Method` instance.
"""

notes = r"""
Note
----

If any parameter is defined outside of the `spectral_dimensions` list, the value
of those parameters is considered global. In a multi-event method, you may also
assign parameter values to individual events.
"""

docstring_generic = "".join([generic_args, args_freq, returns, notes])
docstring_1D = "".join([generic_args, args_freq, returns])

# BlochDecaySpectrum
BlochDecaySpectrum = generate_method_from_template(
    METHODS_DATA["Bloch_decay"], docstring_1D
)

BlochDecayCentralTransitionSpectrum = generate_method_from_template(
    METHODS_DATA["Bloch_decay_central_transition"], docstring_1D
)

# generic 1D method
Method1D = generate_method_from_template(METHODS_DATA["Method1D"], docstring_generic)

# generic 2D method
docstring_2D = "".join([generic_args, args_affine, returns, notes])
Method2D = generate_method_from_template(METHODS_DATA["Method2D"], docstring_2D)


def message(attr, name):
    return f"`{attr}` attribute cannot be modified for {name} method."


def check_for_transition_query(name, spectral_dimensions=[{}, {}]):
    check = [
        "transition_query" in event.keys()
        for item in spectral_dimensions
        if "events" in item.keys()
        for event in item["events"]
    ]

    if np.any(check):
        raise AttributeError(message("transition_query", name))


def check_for_spectral_dimensions(py_dict, n=1):
    """If spectral_dimensions is in py_dict, extract it and then remove from py_dict."""

    if "spectral_dimensions" not in py_dict:
        spectral_dimensions = [{}] * n
    else:
        spectral_dimensions = py_dict["spectral_dimensions"]
        py_dict.pop("spectral_dimensions")
    return spectral_dimensions


def check_for_events(name, spectral_dimensions=[{}, {}]):
    check = ["events" in item.keys() for item in spectral_dimensions]

    if np.any(check):
        raise AttributeError(message("events", name))
