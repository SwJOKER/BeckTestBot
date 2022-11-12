import logging
from string_vars import *


def get_diagnose(points: int) -> str:
    if points not in range(0, 64):
        logging.error(COUNTING_POINTS_ERROR_MSG)
    diagnose = TEST_RESULT_MSG % points
    if points in range(0, 10):
        diagnose += NO_DEPRESS_MSG
    elif points in range(10, 16):
        diagnose += LIGHT_DEPRESS_MSG
    elif points in range(15, 20):
        diagnose += AVERAGE_DEPRESS_MSG
    elif points in range(20, 30):
        diagnose += SEVERE_DEPRESS_MSG
    elif points in range(30, 64):
        diagnose += HARD_DEPRESS_MSG
    return diagnose
