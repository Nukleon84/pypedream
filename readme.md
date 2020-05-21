# PypeDREAM - Python Process Engineering : Design - Rating - Evaluation - Analysis & Modeling

## Overview
PypeDREAM is a port of my original process engineering library MiniSim (https://github.com/Nukleon84/MiniSim). This project is intended to be a test to learn how to program a Python package.

With a direct port, MiniSim will no longer rely on pythonnet and .net datatypes and can be run on any platform that supports Python.

The PypeDREAM package is a collection of Python modules that can be used to simulate stationary chemical processes using mass- and energy balances. The library includes a basic implementation of the IKCAPE Thermodynamics and a handful of simple unit operations. The resulting equation system is solved simulatenously using a Newton-type solver.

This program was build for fun and the enjoyment of exploring process simulation tools. It was heavily inspired by the PhD thesis of K.-H. Lau and G. Varma. These two doctoral thesises were written in the early 90ies and explore the possibility of an object-oriented flowsheet simulator. Now, nearly 25 years later modern software development tools make it possible for even a single person to write such an application.

Development of a process simulator using object oriented programming: Information modeling and program structure Gadiraju V. Varma https://lib.dr.iastate.edu/cgi/viewcontent.cgi?article=11354&context=rtd

Development of a process simulator using object oriented programming: Numerical procedures and convergence studies Kheng Hock Lau https://lib.dr.iastate.edu/cgi/viewcontent.cgi?article=11324&context=rtd

The thermodynamics methods implemented in this libary are part of the IKCAPE thermodynamics. I reimplemented the equations in my own modeling framework. I also use the neutral input format described in their user guide as an input format. http://dechema.de/en/IK_CAPE+THERMO-p-40.html


## Migration Progress
* Expression Trees
    * Arithmetic Expressions [x]
    * Trigonometric Expressions [x]
    * Special Functions  [x]
    * Min/Max Expressions [x]
    * Forward-Mode Automatic Differentiation [x]
* Unit Of Measures [x]
* Numerics
    * Scalar Newton-Raphson [x]
    * Scalar Bisection [x]
    * Newton-Raphson Solver [x]
    * Dulmage Mendelsohn Decomposition [ ]

* Thermodynamics: 
    * Substances [x]
    * PropertyPackages [x]
    * Flash Routines [ ]
    * IKCAPE Neutral File Importer [ ]
    * ChemSep Database Adapter [ ]

* Flowsheeting
    * MaterialStream [ ]
    * Basic Unit Operations [ ]
    * Distillation Column [ ]
    * Reactor [ ]
    * Rate-based Distillation [ ]
 
 * Dynamic Simulation ? (under consideration)
    * Backwards Euler Integrator [ ]
    * BDF2 Integrator with Adaptive Stepsize [ ]    

## Getting Started

This library is currently under development and no package is published yet.

## Dependencies
It is my goal to use as few dependencies as possible to make installation of the package as easy as possible. As this library is intended for learning/teaching, some numeric features are implemented from scratch.

 * NumPy 
 * SciPy
