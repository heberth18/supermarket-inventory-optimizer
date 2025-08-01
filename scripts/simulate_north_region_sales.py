import pandas as pd
import numpy as np
from faker import Faker
from random import choice, randint, uniform
from datetime import datetime, timedelta
import os

# Initialize Faker
faker = Faker()
np.random.seed(42)

# Parameters
n_records = 50000
categories = ["Dairy", "Bakery", "Meat", "Beverages", "Cleaning", "Snacks"]
payment_methods = ["Cash", "Card", "Mobile App"]
northern_region_stores = [f"Store_{i}" for i in range(1, 6)]
products = [f"P_{i:04d}" for i in range(100)]

# Data generation 
data = []

for _ in range(n_records):
    product = choice(products)
    category = choice(categories)
    quantity = randint(1, 10)
    price = round(uniform(0.5, 20.0), 2)
    store = choice(northern_region_stores)
    date = faker.date_time_between(start_date="-365d", end_date="now")
    method = choice(payment_methods)

    data.append({
        "sale_id": faker.uuid4(),
        "sale_date": date.strftime("%Y-%m-%d %H:%M:%S"),
        "store_id": store,
        "product_id": product,
        "category": category,
        "quantity": quantity,
        "unit_price": price,
        "total_sale": round(quantity * price, 2),
        "payment_method": method,
        "region": "North"
    })

# Create DataFrame
df = pd.DataFrame(data)

# Create folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# Save as CSV
df.to_csv("data/raw/sales_2024_north_region.csv", index=False)

print("File created: data/raw/sales_2024_north_region.csv")
