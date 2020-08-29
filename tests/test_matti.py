from matti.matti import match, case, default


def test_match1():
    x = 1
    num = match(x)(
        case(1, lambda: "one"),
        case(2, lambda: "two"),
        default=default(lambda: "anything"),
    )
    assert num == "one"


def test_match2():
    def _test_match2(greeting):
        return match(greeting)(
            case("hello", lambda: "こんにちは"),
            case("goodbye", lambda: "さよなら"),
            default=default(lambda: "?"),
        )

    assert _test_match2("hello") == "こんにちは"
    assert _test_match2("goodbye") == "さよなら"
    assert _test_match2("see you") == "?"
