"""A rule-based prediction example used in Module 00.

This is not machine learning: the formula is written by the programmer.
Run with: python tiny_prediction.py
"""

def estimate_price(area):
    """Return a simple illustrative estimate from floor area."""
    if area < 0:
        raise ValueError("Area cannot be negative.")
    return 2.0 * area + 20


def main():
    areas = [50, 70]
    for area in areas:
        print(f"Area {area}: estimate {estimate_price(area):.1f}")


if __name__ == "__main__":
    main()
