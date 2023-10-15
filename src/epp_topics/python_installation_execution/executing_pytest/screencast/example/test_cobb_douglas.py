def cobb_douglas(labor, capital, alpha):
    return labor**alpha * capital ** (1 - alpha)


def test_cobb_douglas_identity():
    assert cobb_douglas(1, 1, 0.5) == 1


def test_cobb_douglas_4th_root_labor():
    assert cobb_douglas(16, 1, 0.25) == 2


def test_cobb_douglas_4th_root_capital():
    assert cobb_douglas(1, 16, 0.75) == 2
