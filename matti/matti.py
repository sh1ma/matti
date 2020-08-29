class Case:
    def __init__(self, pattern, ret_func):
        self.pattern = pattern
        self.callback = ret_func


def case(value, func_or_exception):
    return Case(value, func_or_exception)


def default(func_or_exception):
    return func_or_exception


def do_default(default):
    if isinstance(default, Exception):
        raise default
    else:
        return default()


def match(value):
    def _match(*cases: Case, default=None):
        patterns = {case.pattern: case.callback for case in cases}
        default = default if default is not None else Exception("Default")
        if value in patterns:
            return patterns[value]()
        else:
            return do_default(default)
        # try:
        #     return patterns[value]()
        # except:
        #     return do_default(default)

    return _match
