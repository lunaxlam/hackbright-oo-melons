"""Classes for melon orders."""

class AbstractMelonOrder:
    """An abstract (base) melon class."""

     # Parameters listed in the __init__ are attributes that we must define; other attributes have a default value
    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        # Following attributes are listed in the __init__() parameters because they must be defined as an argument
        self.species = species
        self.qty = qty
        # Following attributes are not listed in the __init__() parameters because these are default values
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    # Parameters listed in the __init__ are attributes that we must define; other attributes have a default value
    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        # Inherit the __init__() from the AbstractMelonOrder parent class
        super().__init__(species, qty)
        # The following instance-defined attributes override the attribute values set in the parent class
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        # Inherit the __init__() from the AbstractMelonOrder parent class
        super().__init__(species, qty)
        # The following instance-defined attributes override the attribute values set in the parent class
        self.order_type = "international"
        self.tax = 0.17
        # Additional attribute specific to the InternatinalMelonOrder() class
        self.country_code = country_code
        

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
