from checkio_referee import RefereeBase

import settings
import settings_env
from tests import TESTS

cover_unwrap_with_keywords = '''
def cover(f, data):
    return f(data[0], **data[1])
'''


class Referee(RefereeBase):
    TESTS = TESTS
    EXECUTABLE_PATH = settings.EXECUTABLE_PATH
    CURRENT_ENV = settings_env.CURRENT_ENV
    FUNCTION_NAME = "friendly_number"
    ENV_COVERCODE = {
        "python_2": cover_unwrap_with_keywords,
        "python_3": cover_unwrap_with_keywords,
        "javascript": None
    }
