"""
Estimate the execution time of a method
"""

import time


__author__ = ["Ekaterina TOMILINA", "Jordan PROCTOR", "Vishwa ELANKUMARAN"]
__copyright__ = "Copyright 2020, La Nage du Requin"
__version__ = "1.0"
__maintainer__ = ["Ekaterina TOMILINA", "Jordan PROCTOR", "Vishwa ELANKUMARAN"]
__email__ = ["ekaterina.tomilina@etu.u-bordeaux.fr",
             "vishwa.elankumaran@etu.u-bordeaux.fr",
             "jordan.proctor@etu.u-bordeaux.fr,"]
__status__ = "finished"


def timeit(method):
    """
            Initialization of the variables

            Parameters
            ----------
                method -> a method

            Returns
            -------
            str
                Execution time of the given method
    """
    def timed(*args, **kw):
        """
                Initialization of the variables

                Parameters
                ----------
                        args -> list
                        kw   -> list

                Returns
                -------
                str
                        Execution time of the given method
        """
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('%r (%r, %r) %2.2f sec' %
              (method.__name__, args, kw, te - ts))
        return result

    return timed
