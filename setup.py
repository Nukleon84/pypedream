from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Compiled Jacobian Evaluation',
    ext_modules=cythonize("pypedream/numerics/fill_jacobian.pyx"),
    zip_safe=False,
)