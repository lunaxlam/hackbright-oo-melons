"""Classes for melon orders."""

class AbstractMelonOrder:
    """An abstract/base melon class. Not meant to be instantiated."""

    # Clas-level attribute; function as default for all class instances unless overriden at the instance-level
    tax = 0.8
    shipped = False

     # Requirements to instantiate any AbstractMelonOrder class object (which we would not do since this is an abstract class, but subclasses will inherit these requirements)
    def __init__(self, species, qty, order_type):
        """Initialize melon order attributes."""

        # Following attributes are listed in the __init__() parameters because they must be defined as an argument
        self.species = species
        self.qty = qty
        self.order_type = order_type

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
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

    # Requirements to instantiate an InternationalMelonOrder() class object:
    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        # Inherit the __init__() from the AbstractMelonOrder parent class
        super().__init__(species, qty, order_type="domestic")


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    # Class-level attribute
    tax = 0.17

    # Requirements to instantiate an InternationalMelonOrder() class object:
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        # Inherit the __init__() from the AbstractMelonOrder parent class
        super().__init__(species, qty, order_type="international")
        # Additional attribute specific to the InternatinalMelonOrder() class; will override abstract parent class attributes
        self.country_code = country_code
        

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order."""

    # Class-level attribute
    passed_inspection = False

    # Requirements to instantiate an InternationalMelonOrder() class object:
    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        # Inherit the __init__() from the AbstractMelonOrder parent class
        super().__init__(species, qty, order_type="domestic")

    def mark_inspection(self, passed):
        """Record whether or not a melon hassed passed inspection as a boolean."""

        self.passed_inspection = passed