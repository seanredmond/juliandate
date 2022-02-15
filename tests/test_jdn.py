import juliandate as jd

def test_gregorian():
    # A.D. 1969 July 20 20:17:30.0, some precision lacking
    assert jd.to_gregorian(2440423.345486) == (1969, 7, 20, 20, 17, 29, 990416)


def test_julian():
    # 44 March 15 B.C. 15:00:00.0
    print(jd.to_julian(1705426.125000))
    assert jd.to_julian(1705426.125000) == (-43, 3, 15, 15, 0, 0, 0)


def test_from_gregorian():
    assert jd.from_gregorian(1969, 7, 20) == 2440422.5
    assert jd.from_gregorian(1969, 7, 20, 20, 17, 30) == 2440423.345486111
    assert jd.from_gregorian(1969, 7, 20, 8, 17, 30) == 2440422.845486111


def test_from_julian():
    assert jd.from_julian(-43, 3, 15) == 1705425.5
    assert jd.from_julian(-43, 3, 15, 15) == 1705426.125
    assert jd.from_julian(-43, 3, 15, 3) == 1705425.625


def test_rollover():
    # Midnight, 0.5, should be zero
    assert jd.to_julian(1705426.5) == (-43, 3, 16, 0, 0, 0, 0)

    # 0.75 should be 6 AM
    assert jd.to_julian(1705426.75) == (-43, 3, 16, 6, 0, 0, 0)
