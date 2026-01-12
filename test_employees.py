from employee import calculate_bonus

def test_bonus_5000():
    assert calculate_bonus(26) == 5000

def test_bonus_3000():
    assert calculate_bonus(20) == 3000

def test_bonus_1500():
    assert calculate_bonus(15) == 1500

def test_bonus_zero():
    assert calculate_bonus(10) == 0
