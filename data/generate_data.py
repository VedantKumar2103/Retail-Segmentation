"""
Generates a synthetic retail dataset modeled after the
UCI 'Online Retail II' dataset (e-commerce transactions, UK retailer).
~25,000 transactions from ~2,500 unique customers across 12 months.
"""
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

np.random.seed(42)
N_CUSTOMERS = 2500
N_TRANSACTIONS = 25000

# Generate customers with different behavior profiles
customer_ids = [f"C{10000+i}" for i in range(N_CUSTOMERS)]
customer_profile = np.random.choice(
    ["VIP", "Regular", "Occasional", "OneTime"], N_CUSTOMERS, p=[0.08, 0.32, 0.40, 0.20]
)
profile_map = dict(zip(customer_ids, customer_profile))

countries = ["United Kingdom", "Germany", "France", "Spain", "Netherlands",
             "Belgium", "Switzerland", "Portugal", "Australia", "Italy"]
country_p = [0.78, 0.06, 0.05, 0.03, 0.025, 0.015, 0.01, 0.01, 0.01, 0.01]

products = [
    ("85123A", "WHITE HANGING HEART T-LIGHT HOLDER", 2.55),
    ("71053", "WHITE METAL LANTERN", 3.39),
    ("84406B", "CREAM CUPID HEARTS COAT HANGER", 2.75),
    ("84029G", "KNITTED UNION FLAG HOT WATER BOTTLE", 3.39),
    ("84029E", "RED WOOLLY HOTTIE WHITE HEART", 3.39),
    ("22752", "SET 7 BABUSHKA NESTING BOXES", 7.65),
    ("21730", "GLASS STAR FROSTED T-LIGHT HOLDER", 4.25),
    ("22633", "HAND WARMER UNION JACK", 1.85),
    ("22632", "HAND WARMER RED POLKA DOT", 1.85),
    ("84879", "ASSORTED COLOUR BIRD ORNAMENT", 1.69),
    ("22745", "POPPY'S PLAYHOUSE BEDROOM", 2.10),
    ("22748", "POPPY'S PLAYHOUSE KITCHEN", 2.10),
    ("22310", "IVORY KNITTED MUG COSY", 1.65),
    ("84969", "BOX OF 6 ASSORTED COLOUR TEASPOONS", 4.25),
    ("22623", "BOX OF VINTAGE JIGSAW BLOCKS", 5.95),
    ("22622", "BOX OF VINTAGE ALPHABET BLOCKS", 9.95),
    ("21791", "VINTAGE HEADS AND TAILS CARD GAME", 1.25),
    ("21035", "SET/2 RED RETROSPOT TEA TOWELS", 2.95),
    ("22720", "SET OF 3 CAKE TINS PANTRY DESIGN", 4.95),
    ("22189", "CREAM HEART CARD HOLDER", 6.95),
]

invoice_dates = pd.date_range("2024-01-01", "2024-12-31", freq="D")

records = []
invoice_counter = 500000

# Assign customers to invoices based on profile
profile_freq = {"VIP": (15, 40), "Regular": (5, 14), "Occasional": (2, 4), "OneTime": (1, 2)}

for cust_id in customer_ids:
    profile = profile_map[cust_id]
    n_invoices = np.random.randint(*profile_freq[profile])
    country = np.random.choice(countries, p=country_p)
    
    for _ in range(n_invoices):
        invoice_no = invoice_counter
        invoice_counter += 1
        invoice_date = np.random.choice(invoice_dates)
        # Each invoice has 1-8 line items
        n_items = np.random.randint(1, 9)
        chosen_products = np.random.choice(len(products), n_items, replace=False)
        for pidx in chosen_products:
            stock_code, desc, price = products[pidx]
            qty = np.random.randint(1, 25) if profile != "VIP" else np.random.randint(2, 50)
            # Add some price variation
            unit_price = round(price * np.random.uniform(0.95, 1.05), 2)
            records.append({
                "InvoiceNo": invoice_no,
                "StockCode": stock_code,
                "Description": desc,
                "Quantity": qty,
                "InvoiceDate": pd.Timestamp(invoice_date) + timedelta(hours=np.random.randint(8, 20),
                                                                       minutes=np.random.randint(0, 60)),
                "UnitPrice": unit_price,
                "CustomerID": cust_id,
                "Country": country
            })

df = pd.DataFrame(records)

# Sprinkle in a few returns (negative quantities) and some missing CustomerIDs
return_idx = df.sample(frac=0.015).index
df.loc[return_idx, "Quantity"] = -df.loc[return_idx, "Quantity"].abs()
missing_idx = df.sample(frac=0.02).index
df.loc[missing_idx, "CustomerID"] = np.nan

df = df.sample(frac=1, random_state=42).reset_index(drop=True)
df.to_csv("/home/claude/analytics_projects/retail_segmentation/data/online_retail.csv", index=False)
print(f"Generated {len(df)} transactions")
print(f"Unique customers: {df['CustomerID'].nunique()}")
print(f"Unique invoices: {df['InvoiceNo'].nunique()}")
print(f"Date range: {df['InvoiceDate'].min()} to {df['InvoiceDate'].max()}")
