import numpy  as np


CHAN = 6
BLACK_CHAN = 0
WHITE_CHAN = 1
TURN_CHAN = 2
VALID_CHAN = 3
RESULT_CHAN = 4
ORIGIN_WHITE_CHAN = 5

surround_struct = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
neighbor_deltas = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])
valid_surround = np.array(
    [
        [False, False, True, False, False],
        [False, True, True, True, False],
        [True, True, True, True, True],
        [False, True, True, True, False],
        [False, False, True, False, False],
    ],
    dtype=bool,
)