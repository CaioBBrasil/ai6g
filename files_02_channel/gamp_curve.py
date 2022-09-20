import numpy as np
import numpy.typing as npt

snrdb = np.arange(-30, 33, 3)
nmse_em_bg_gamp = np.array(
    [
        1.077390595246807e01,
        7.842803259905770e00,
        5.057300291644731e00,
        1.730706438170362e00,
        -2.985668043447252e00,
        -8.655906498126079e00,
        -1.359642191095016e01,
        -1.699861565324826e01,
        -1.960330426437051e01,
        -2.100083973751815e01,
        -2.167033506724910e01,
        -2.204707105030500e01,
        -2.223144574404241e01,
        -2.227563898922593e01,
        -2.208913329459328e01,
        -2.172430523044925e01,
        -2.135104260104325e01,
        -2.091503169591856e01,
        -2.031060101633953e01,
        -1.974666080748985e01,
        -1.888577896461370e01,
    ]
)


def nmse_data() -> tuple[npt.ArrayLike, npt.ArrayLike]:
    return (snrdb, nmse_em_bg_gamp)
