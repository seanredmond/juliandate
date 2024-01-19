import math
from juliandate.__version__ import __version__

# Algorithms from:
#
# Urban, Sean E., and P. Kenneth Seidelmann, eds. Explanatory
# Supplement to the Astronomical Almanac. 3. ed. Mill Valley, Calif:
# University Science Books, 2012.


def to_julian(J):
    """Return a Julian calendar date for a Julian Day."""
    # return __jd_to_date(int(J + 0.5) + 1401) + __h_m_s(J)
    return __jd_to_date(J) + __h_m_s(J)


def to_gregorian(J):
    """Return a Gregorian calendar date for a Julian Day."""
    j = 1401
    B = 274277
    C = -38

    return __jd_to_date(J, True) + __h_m_s(J)


def __param_f(J, is_gregorian):
    """Calculate parameter f for conversion algorithm depending on whether the conversion is to Julian or Gregorian calendar."""
    # Urban and Seidelmann, Algorithm 4

    # Values from Table 15.14
    j = 1401
    B = 274277
    C = -38

    if is_gregorian:
        # Formulas 1 & 1a
        return J + j + int((int((4 * J + B) / 146_097) * 3) / 4) + C

    # Formula 1
    return J + j


def from_gregorian(Y, M, D, H=0, m=0, sec=0, ms=0):
    """Return a Julian day for a Gregorian calendar date."""
    return (
        int((1461 * (Y + 4800 + int((M - 14) / 12))) / 4)
        + int((367 * (M - 2 - 12 * int((M - 14) / 12))) / 12)
        - int((3 * int((Y + 4900 + int((M - 14) / 12)) / 100)) / 4)
        + D
        - 32075
    ) + __day_pct(H, m, sec, ms)


def from_julian(Y, M, D, H=0, m=0, sec=0, ms=0):
    """Return a Julian day for a Julian calendar date."""
    return (
        367 * Y
        - int((7 * (Y + 5001 + int((M - 9) / 7))) / 4)
        + int((275 * M) / 9)
        + D
        + 1729777
        + __day_pct(H, m, sec, ms)
    )


def __jd_to_date(jdn, is_gregorian=False):
    """Base calculation for converting from Julian day.

    Urban and Seidelmann, Explanatory Supplement to the Astronomical Almanac. 617–619
    """
    # Round JDN to integer Julian day
    J = int(jdn + 0.5)

    # Values from Table 15.14
    m = 2
    n = 12
    p = 1461
    r = 4
    s = 153
    u = 5
    v = 3
    w = 2
    y = 4716

    f = __param_f(J, is_gregorian)
    e = r * f + v
    g = int((e % p) / r)
    h = u * g + w

    D = int((h % s) / u) + 1
    M = ((int(h / s) + m) % n) + 1
    Y = e / p - y + (n + m - M) / n

    Y = int(e / p) - y + int((n + m - M) / n)

    return (Y, M, D)


def __h_m_s(t):
    """Convert decimal fraction to hours, minutes, (fractional) seconds."""
    pct = t - int(t)
    (hour, r) = __tdiv(pct, 24)
    (minutes, r) = __tdiv(r, 60)
    (seconds, r) = __tdiv(r, 60)
    return ((hour + 12) % 24, minutes, seconds, math.floor(r * 1_000_000 + 0.5))


def __tdiv(t, d):
    return (int(d * t), d * t - int(d * t))


def __day_pct(h, m, sec, ms):
    s = sec + (ms / 1_000_000)
    return ((h * 3600 + m * 60 + s) / 86400) - 0.5


def version():
    return __version__
