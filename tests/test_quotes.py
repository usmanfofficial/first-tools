from quote_generator import get_random_quote

def test_quote_nonempty():
    q = get_random_quote()
    assert isinstance(q, str) and len(q) > 0
