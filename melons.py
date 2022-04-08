"""Classes for melon orders."""

from random import randint
from datetime import datetime


class TooManyMelonsError(ValueError):
    """Raise this error if melon quanity is too high."""

    def __init__(self):
        """Initialize TooManyMelonsError."""

        super().__init__("No more than 100 melons!")


class AbstractMelonOrder:
    """An abstract/base melon class. Not meant to be instantiated."""

    # Clas-level attribute; function as default for all class instances unless overriden at the instance-level
    shipped = False

     # Requirements to instantiate any AbstractMelonOrder class object (which we would not do since this is an abstract class, but subclasses will inherit these requirements)
    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        # Following attributes are listed in the __init__() parameters because they must be defined as an argument
        self.species = species

        # Raise ValueError if the following
        if qty > 100:
            raise TooManyMelonsError

        self.qty = qty
        self.order_type = order_type
        self.tax = tax

    def get_base_price(self):
        """Get a base price."""

        # Get a random integer and store as the "splurge" base price
        base_price = randint(5,9)

        # Get info to adjust the base_price to account for splurge pricing during rush-hour (M-F, 8am-11am local time)
        now = datetime.now()

        splurge_charge = 4

        # Check to see if today's date is M(0)-F(4) and current time is between 8am-11am:
        if now.weekday() in range(0,5) and now.hour() in range(8,12):
            base_price += splurge_charge

        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        # Get a base price
        base_price = self.get_base_price()

        # Flat fee for internatinoal order types with < 10 melons
        international_flat_fee = 3

        # If species type == "christmas" melon
        if self.species == "christmas":
            # Base price is 1.5 times as much as the standard base price
            base_price *= 1.5

        # Calculate the total, including tax
        total = (1 + self.tax) * self.qty * base_price

        # If order_type == "international" and quanity is less than 10, add the international_flat_fee
        if self.order_type == "international" and self.qty < 10:
            total += international_flat_fee

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    # Minimum requirements to instantiate a DomesticMelonOrder() class object:
    def __init__(self, species, qty):
        super().__init__(species, qty, order_type="domestic", tax=0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""


    # Minimum requirements to instantiate an InternationalMelonOrder() class object:
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        # Inherit the __init__() from the AbstractMelonOrder parent class
        super().__init__(species, qty, order_type="international", tax=0.17)
        # Additional attribute specific to the InternatinalMelonOrder() class; will override abstract parent class attributes
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order."""
    # Class-level attribute
    passed_inspection = False

    # Minimum requirements to instantiate a GovernmentcMelonOrder() class object:
    def __init__(self, species, qty):
        super().__init__(species, qty, order_type="government", tax=0)

    def mark_inspection(self, passed):
        """Record whether or not a melon hassed passed inspection as a boolean."""

        self.passed_inspection = passed

