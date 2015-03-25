from checkio_referee import RefereeBase

import settings
import settings_env
from tests import TESTS

cover_unwrap_with_keywords = '''
def cover(f, data):
    return f(data[0], **data[1])
'''

def py_repr(f, data):
    number = data["input"][0]
    keywords = data["input"][1]
    res = "{}({}".format(f, number)
    for k, v in keywords.items():
        res += ', {}={}'.format(k, v if not isinstance(v, str) else '"' + v + '"')
    return res + ")"


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "friendly_number"
    ENV_COVERCODE = {
        "python_2": cover_unwrap_with_keywords,
        "python_3": cover_unwrap_with_keywords,
        "javascript": None
    }
    CALLED_REPRESENTATIONS = {
        "python_2": py_repr,
        "python_3": py_repr,
        "javascript": None
    }
