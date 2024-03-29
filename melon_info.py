"""Print out all the melons in our inventory."""

from melons import melons

def print_melon(melon):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'do not have' if melons[melon]['seedless'] else 'have'
    print(f"{melon}s {have_or_have_not} seeds and are ${melons[melon]['price']:.2f}")


for melon in melons:
    print_melon(melon)