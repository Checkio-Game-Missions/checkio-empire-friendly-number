from checkio_referee import RefereeBase, covercodes, representations, ENV_NAME


import settings_env
from tests import TESTS

cover_unwrap_with_keywords = '''
def cover(f, data):
    return f(data[0], **data[1])
'''

def py_repr(data, f):
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
    FUNCTION_NAMES = {
        ENV_NAME.JS_NODE: "friendlyNumber"
    }

    ENV_COVERCODE = {
        ENV_NAME.PYTHON: cover_unwrap_with_keywords,
        ENV_NAME.JS_NODE: covercodes.js_unwrap_args
    }
    CALLED_REPRESENTATIONS = {
        ENV_NAME.PYTHON: py_repr,
        ENV_NAME.JS_NODE: representations.unwrap_arg_representation
    }
