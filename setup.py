# -*- coding: utf-8 -*-

import os
import numpy
import numpy.distutils.system_info as sysinfo
from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize

module_dir = os.path.dirname(os.path.abspath(__file__))

mkl_info = sysinfo.get_info("mkl")

include_dirs = ["src/c_lib/include", numpy.get_include()]

if "include_dirs" in mkl_info:
    include_dirs.extend(mkl_info["include_dirs"])

ext_modules = [
    Extension(
        name="mrsimulator.methods",
        sources=[
            "src/c_lib/lib/c_array.c",
            "src/c_lib/lib/MRAngularMomentum.c",
            "src/c_lib/mrmethods/spinning_sidebands.c",
            "src/c_lib/mrmethods/powder_setup.c",
            "src/c_lib/mrmethods/nmr_methods.pyx",
        ],
        include_dirs=include_dirs,
        libraries=["fftw3"],
        language="c",
        extra_compile_args="-O1".split(),
        extra_link_args="-g -lfftw3 -lmkl_intel_lp64 -lmkl_intel_thread \
                        -lmkl_core -ldl -liomp5 -lm -W".split(),
    )
]

setup(
    name="mrsimulator",
    version="0.1.0",
    description="A python toolbox for simulating NMR spectra",
    long_description=open(os.path.join(module_dir, "README.md")).read(),
    author="Deepansh J. Srivastava",
    author_email="srivastava.89@osu.edu",
    python_requires=">=3.0",
    url="https://github.com/DeepanshS/MRsimulator/",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.13.3",
        "astropy>=3.0",
        "pydantic==0.28",
        "requests>=2.21.0",
        "monty==2.0.4",
        "mkl==2019.0",
        "mkl-include==2019.0",
    ],
    extras_require={
        "fancy feature": [
            "matplotlib>=3.0.2",
            "plotly>=3.6",
            "dash>=0.40",
            "dash_daq>=0.1",
        ]
    },
    tests_require=["nose"],
    entry_points={
        "console_scripts": ["nmr_app = mrsimulator.web_interface:main"]
    },
    ext_modules=cythonize(ext_modules),
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
    ],
)
