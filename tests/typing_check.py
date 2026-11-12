from schemaorg_pydantic import Brand, Graph, ItemAvailability, Offer, Product

offer = Offer(price=79, price_currency="EUR", availability=ItemAvailability.IN_STOCK)
product = Product(id="https://e.com/#p", name="Blue bag", brand=Brand(name="N"), offers=offer)
print(Graph(product).dumps())
