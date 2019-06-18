from mrsimulator.parseable import Parseable

__author__ = "Deepansh J. Srivastava"
__email__ = ["srivastava.89@osu.edu", "deepansh2012@gmail.com"]


class Site(Parseable):

    nucleus: str = "1H"
    isotropic_chemical_shift: float = 0
    shift_anisotropy: float = 0
    shift_asymmetry: float = 0
    alpha: float = 0
    beta: float = 0
    gamma: float = 0

    __property_unit_types = {
        "isotropic_chemical_shift": "dimensionless",
        "shift_anisotropy": "dimensionless",
        "alpha": "angle",
        "beta": "angle",
        "gamma": "angle"
    }

    __property_default_units = {
        "isotropic_chemical_shift": "ppm",
        "shift_anisotropy": "ppm",
        "alpha": "rad",
        "beta": "rad",
        "gamma": "rad"
    }
