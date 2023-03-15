from base.scarping_sites import *


def new_data():
    newdata = {
        '9to5linux' : nineto5linux(),
        'omglinux' : omg_linux(),
        'itsfoss' : itsfoss(),
        'omgubuntu' : omg_ubuntu()
    }

    return newdata