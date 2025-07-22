from bson.decimal128 import Decimal128

def pretty_print_listing(listing):
    price = listing.get('price', 0)
    if isinstance(price, Decimal128):
        price = float(price.to_decimal())
    else:
        price = float(price)
    desc = listing.get('description', '')
    if len(desc) > 200:
        desc = desc[:200] + "..."
    print("="*60)
    print(f"Name:        {listing.get('name')}")
    print(f"Description: {desc}")
    print(f"Price:       ${price:.2f}")
    print(f"Address:     {listing.get('address')}")
    print(f"Link:        {listing.get('link')}")
    print("="*60)
    print()