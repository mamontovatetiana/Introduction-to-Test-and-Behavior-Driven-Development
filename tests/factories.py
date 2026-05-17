# Task 1
class ProductFactory(factory.Factory):
    """Creates fake products"""

    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n)
    name = factory.Faker("word")
    description = factory.Faker("sentence")
    price = factory.Faker("pydecimal", left_digits=2, right_digits=2, positive=True)
    available = factory.Faker("boolean")
    category = factory.Iterator([Category.CLOTHS, Category.FOOD, Category.HOUSEWARES])

