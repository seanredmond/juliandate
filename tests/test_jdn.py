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
    # Noon, 0.0 should be hour 12
    assert jd.to_julian(1705426) == (-43, 3, 15, 12, 0, 0, 0)

    # 0.25 should be hour 18
    assert jd.to_julian(1705426.25) == (-43, 3, 15, 18, 0, 0, 0)
    
    # Midnight, 0.5, should be zero
    assert jd.to_julian(1705426.5) == (-43, 3, 16, 0, 0, 0, 0)

    # 0.75 should be 6 AM
    assert jd.to_julian(1705426.75) == (-43, 3, 16, 6, 0, 0, 0)


def test_gregorian_rollover():
    assert jd.to_gregorian(2440646.0)[:6] == (1970, 2, 28, 12, 0, 0)
    assert jd.to_gregorian(2440646.1)[:6] == (1970, 2, 28, 14, 24, 0)
    assert jd.to_gregorian(2440646.2)[:6] == (1970, 2, 28, 16, 48, 0)
    assert jd.to_gregorian(2440646.3)[:6] == (1970, 2, 28, 19, 11, 59)
    assert jd.to_gregorian(2440646.4)[:6] == (1970, 2, 28, 21, 35, 59)
    assert jd.to_gregorian(2440646.5)[:6] == (1970, 3, 1, 0, 0, 0)
    assert jd.to_gregorian(2440646.6)[:6] == (1970, 3, 1, 2, 24, 0)
    assert jd.to_gregorian(2440646.7)[:6] == (1970, 3, 1, 4, 48, 0)
    assert jd.to_gregorian(2440646.8)[:6] == (1970, 3, 1, 7, 11, 59)
    assert jd.to_gregorian(2440646.9)[:6] == (1970, 3, 1, 9, 35, 59)
    assert jd.to_gregorian(2440647.0)[:6] == (1970, 3, 1, 12, 0, 0)    


def test_rounding():
    assert jd.to_julian(1566223.56309468) == (-424, 2, 2, 1, 30, 51, 380349)


def test_version():
    assert jd.version() == "1.0.4"


def test_julian_day0():
    assert jd.to_julian(0) == (-4712, 1, 1, 12, 0, 0, 0)
    assert jd.from_julian(-4712, 1, 1, 12, 0, 0, 0) == 0


def test_gregorian_day0():
    assert jd.to_gregorian(0) == (-4713, 11, 24, 12, 0, 0, 0)
    assert jd.from_gregorian(-4713, 11, 24, 12, 0, 0, 0) == 0


def test_for_rounding_error():
    # Some values that were subject to from_gregorian rounding error
    # (Issue #2)
    assert jd.from_gregorian(*jd.to_gregorian(187100)) == 187100
    assert jd.from_gregorian(*jd.to_gregorian(150576)) == 150576
    assert jd.from_gregorian(*jd.to_gregorian(41003)) == 41003
    assert jd.from_gregorian(*jd.to_gregorian(28951)) == 28951
    assert jd.from_gregorian(*jd.to_gregorian(4479)) == 4479
    assert jd.from_gregorian(*jd.to_gregorian(0)) == 0


def test_fliegel_van_flandern():
    # Fliegel, Henry F., and Thomas C. Van Flandern. “A Machine
    # Algorithm for Processing Calendar Dates.” Communcations of the
    # ACM 11, no. 10 (1968): 657.
    assert jd.from_gregorian(1970, 1, 1, 12) == 2440588
