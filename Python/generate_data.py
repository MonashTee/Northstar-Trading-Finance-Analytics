
import pandas as pd
import numpy as np
from pathlib import Path
from itertools import product


# -----------------------------------------
# PROJECT SETUP
# -----------------------------------------

# Set random seed for reproducibility
np.random.seed(42)

# Define project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "Data"

# Create Data folder if it does not exist
DATA_DIR.mkdir(parents=True, exist_ok=True)

print("Project directory:", BASE_DIR)
print("Data directory:", DATA_DIR)


# -----------------------------------------
# 1. GENERATE CUSTOMER MASTER DATA
# -----------------------------------------

# Define customer attributes
customer_types = ["Retailer", "Wholesaler", "Corporate"]

payment_terms = [30, 45, 60]

# Define city and country relationships
customer_locations = [
    ("Berlin", "Germany"),
    ("Hamburg", "Germany"),
    ("Munich", "Germany"),
    ("Cologne", "Germany"),
    ("Frankfurt", "Germany"),
    ("Amsterdam", "Netherlands"),
    ("Rotterdam", "Netherlands"),
    ("Brussels", "Belgium"),
    ("Vienna", "Austria"),
    ("Paris", "France")
]

# Define business descriptions
business_names = [
    "Office Solutions",
    "Industrial Supplies",
    "Commercial Trading",
    "Technology Distribution"
]

# Define legal business suffixes
legal_suffixes = {
    "Germany": "GmbH",
    "Netherlands": "B.V.",
    "Belgium": "BV",
    "Austria": "GmbH",
    "France": "SAS"
}

# Generate all possible customer profiles
customer_profiles = list(
    product(customer_locations, business_names)
)

# Shuffle profiles using the random seed
np.random.shuffle(customer_profiles)

# Generate unique customer names
customer_names = [
    f"{city} {business} {legal_suffixes[country]}"
    for (city, country), business in customer_profiles
]

# Extract customer countries
customer_countries = [
    country
    for (city, country), business in customer_profiles
]

# Generate unique customer IDs
customer_ids = [
    f"CUST{i:03d}" for i in range(1, 41)
]

# Create customer dataset
customers = pd.DataFrame({
    "customer_id": customer_ids,
    "customer_name": customer_names,
    "customer_type": np.random.choice(customer_types, 40),
    "country": customer_countries,
    "payment_terms_days": np.random.choice(payment_terms, 40),
    "customer_status": np.random.choice(
        ["Active", "Inactive"],
        40,
        p=[0.90, 0.10]
    )
})


# -----------------------------------------
# 1.1. VALIDATE CUSTOMER DATA
# -----------------------------------------

print("\nCUSTOMER DATA VALIDATION")

print("Total customers:", len(customers))

print(
    "Unique customer IDs:",
    customers["customer_id"].nunique()
)

print(
    "Unique customer names:",
    customers["customer_name"].nunique()
)

print(
    "Missing values:",
    customers.isnull().sum().sum()
)

# Check for duplicate customer IDs
assert customers["customer_id"].is_unique, "Duplicate customer IDs found!"

# Check for duplicate customer names
assert customers["customer_name"].is_unique, "Duplicate customer names found!"

# Check the expected number of customers
assert len(customers) == 40, "Expected 40 customers!"

# Check payment terms
assert customers["payment_terms_days"].isin(payment_terms).all()

# Check for missing values
assert not customers.isnull().any().any(), "Missing values found!"

print("\nAll customer validation checks passed!")


# -----------------------------------------
# 1.2. EXPORT CUSTOMER DATA
# -----------------------------------------

customers.to_csv(
    DATA_DIR / "customers.csv",
    index=False
)

print("\nCustomer dataset generated successfully!")

print("\nFirst five customers:")
print(customers.head())

print("\nCustomer distribution by country:")
print(customers["country"].value_counts())


# -----------------------------------------
# 2. GENERATE SUPPLIER MASTER DATA
# -----------------------------------------

# Define supplier locations
supplier_locations = [
    ("Berlin", "Germany"),
    ("Hamburg", "Germany"),
    ("Munich", "Germany"),
    ("Frankfurt", "Germany"),
    ("Amsterdam", "Netherlands"),
    ("Rotterdam", "Netherlands"),
    ("Brussels", "Belgium"),
    ("Vienna", "Austria"),
    ("Paris", "France"),
    ("Lyon", "France"),
]

# Define supplier business descriptions
supplier_business_names = [
    "Electronics Wholesale",
    "Office Equipment Supply",
    "Industrial Equipment Trading",
    "Commercial Appliances",
]

# Define country-specific legal suffixes
supplier_legal_suffixes = {
    "Germany": "GmbH",
    "Netherlands": "B.V.",
    "Belgium": "BV",
    "Austria": "GmbH",
    "France": "SAS",
}

# Generate all possible supplier profiles
supplier_profiles = list(
    product(supplier_locations, supplier_business_names)
)

# Shuffle supplier profiles
np.random.shuffle(supplier_profiles)

# Generate unique supplier names
supplier_names = [
    f"{city} {business} {supplier_legal_suffixes[country]}"
    for (city, country), business in supplier_profiles[:20]
]

# Extract supplier countries
supplier_countries = [
    country
    for (city, country), business in supplier_profiles[:20]
]

# Generate unique supplier IDs
supplier_ids = [
    f"SUPP{i:03d}" for i in range(1, 21)
]

# Define supplier payment terms
supplier_payment_terms = [30, 45, 60]

# Create supplier DataFrame
suppliers = pd.DataFrame({
    "supplier_id": supplier_ids,
    "supplier_name": supplier_names,
    "country": supplier_countries,
    "payment_terms_days": np.random.choice(
        supplier_payment_terms, 20
    ),
    "supplier_status": np.random.choice(
        ["Active", "Inactive"],
        20,
        p=[0.90, 0.10]
    )
})


# -----------------------------------------
# 2.1. VALIDATE SUPPLIER DATA
# -----------------------------------------

print("\nSUPPLIER DATA VALIDATION")

print("Total suppliers:", len(suppliers))

print(
    "Unique supplier IDs:",
    suppliers["supplier_id"].nunique()
)

print(
    "Unique supplier names:",
    suppliers["supplier_name"].nunique()
)

print(
    "Missing values:",
    suppliers.isnull().sum().sum()
)

# Validation checks
assert len(suppliers) == 20, "Expected 20 suppliers!"

assert suppliers["supplier_id"].is_unique, (
    "Duplicate supplier IDs found!"
)

assert suppliers["supplier_name"].is_unique, (
    "Duplicate supplier names found!"
)

assert suppliers["payment_terms_days"].isin(
    supplier_payment_terms
).all(), "Invalid supplier payment terms!"

assert not suppliers.isnull().any().any(), (
    "Missing values found!"
)

print("\nAll supplier validation checks passed!")


# -----------------------------------------
# 2.2. EXPORT SUPPLIER DATA
# -----------------------------------------

suppliers.to_csv(
    DATA_DIR / "suppliers.csv",
    index=False
)

print("\nSupplier dataset generated successfully!")

print("\nFirst five suppliers:")
print(suppliers.head())

print("\nSupplier distribution by country:")
print(suppliers["country"].value_counts())


# -----------------------------------------
# 3. GENERATE PRODUCT MASTER DATA
# -----------------------------------------

# Define product categories and their quantities
product_categories = {
    "Electronics & IT": 15,
    "Office Supplies": 15,
    "Industrial Equipment": 10,
    "Commercial Appliances": 10
}

# Define product names by category
product_names_by_category = {
    "Electronics & IT": [
        "Business Laptop",
        "Desktop Computer",
        "Computer Monitor",
        "Wireless Keyboard",
        "Wireless Mouse",
        "Laser Printer",
        "Network Router",
        "External Hard Drive",
        "USB Flash Drive",
        "Laptop Docking Station",
        "Tablet Computer",
        "Webcam",
        "Headset",
        "Network Switch",
        "Server Rack"
    ],

    "Office Supplies": [
        "Office Desk",
        "Ergonomic Office Chair",
        "Filing Cabinet",
        "Conference Table",
        "Bookshelf",
        "Desk Lamp",
        "Whiteboard",
        "Paper Shredder",
        "Storage Cabinet",
        "Meeting Room Chair",
        "Document Scanner",
        "Office Drawer Unit",
        "Reception Desk",
        "Notice Board",
        "Office Partition"
    ],

    "Industrial Equipment": [
        "Electric Drill",
        "Industrial Generator",
        "Air Compressor",
        "Hydraulic Pump",
        "Welding Machine",
        "Industrial Vacuum",
        "Power Saw",
        "Forklift",
        "Pallet Truck",
        "Industrial Pressure Washer"
    ],

    "Commercial Appliances": [
        "Commercial Refrigerator",
        "Industrial Dishwasher",
        "Commercial Microwave",
        "Coffee Machine",
        "Water Dispenser",
        "Commercial Oven",
        "Ice Maker",
        "Display Freezer",
        "Commercial Blender",
        "Food Warmer"
    ]
}

# Define product reference prices by category
# Format: (minimum purchase cost, maximum purchase cost)
purchase_cost_ranges = {
    "Electronics & IT": (80, 1200),
    "Office Supplies": (15, 700),
    "Industrial Equipment": (100, 3500),
    "Commercial Appliances": (100, 2500)
}

# Generate product records
product_records = []

product_number = 1

for category, number_of_products in product_categories.items():

    category_product_names = product_names_by_category[category]

    for product_name in category_product_names:

        # Generate a reference purchase cost
        purchase_cost = round(
            np.random.uniform(
                purchase_cost_ranges[category][0],
                purchase_cost_ranges[category][1]
            ),
            2
        )

        # Set reference selling price using a markup
        markup_rate = np.random.uniform(0.20, 0.45)

        selling_price = round(
            purchase_cost * (1 + markup_rate),
            2
        )

        product_records.append({
            "product_id": f"PROD{product_number:03d}",
            "product_name": product_name,
            "category": category,
            "unit_of_measure": "Unit",
            "standard_selling_price": selling_price,
            "standard_purchase_cost": purchase_cost,
            "inventory_account_code": "1200",
            "revenue_account_code": "4000",
            "cogs_account_code": "5000",
            "product_status": np.random.choice(
                ["Active", "Inactive"],
                p=[0.95, 0.05]
            )
        })

        product_number += 1


# Create product DataFrame
products = pd.DataFrame(product_records)


# -----------------------------------------
# 3.1. VALIDATE PRODUCT DATA
# -----------------------------------------

print("\nPRODUCT DATA VALIDATION")

print("Total products:", len(products))

print(
    "Unique product IDs:",
    products["product_id"].nunique()
)

print(
    "Unique product names:",
    products["product_name"].nunique()
)

print(
    "Missing values:",
    products.isnull().sum().sum()
)

# Validation checks
assert len(products) == 50, "Expected 50 products!"

assert products["product_id"].is_unique, (
    "Duplicate product IDs found!"
)

assert products["product_name"].is_unique, (
    "Duplicate product names found!"
)

assert not products.isnull().any().any(), (
    "Missing values found!"
)

assert (products["standard_purchase_cost"] > 0).all(), (
    "Invalid purchase costs found!"
)

assert (
    products["standard_selling_price"]
    > products["standard_purchase_cost"]
).all(), "Selling price must exceed purchase cost!"

assert products["category"].isin(
    product_categories.keys()
).all(), "Invalid product category found!"

assert products["inventory_account_code"].eq("1200").all()

assert products["revenue_account_code"].eq("4000").all()

assert products["cogs_account_code"].eq("5000").all()

print("\nAll product validation checks passed!")


# -----------------------------------------
# 3.2. EXPORT PRODUCT DATA
# -----------------------------------------

products.to_csv(
    DATA_DIR / "products.csv",
    index=False
)

print("\nProduct dataset generated successfully!")

print("\nFirst five products:")
print(products.head())

print("\nProducts by category:")
print(products["category"].value_counts())



# ==========================================
# 4. DEPARTMENTS DATASET
# ==========================================

departments_data = [
    ("DEPT001", "Sales", "Operating"),
    ("DEPT002", "Procurement", "Operating"),
    ("DEPT003", "Operations", "Operating"),
    ("DEPT004", "Finance", "Support"),
    ("DEPT005", "Administration", "Support")
]

departments = pd.DataFrame(
    departments_data,
    columns=[
        "department_id",
        "department_name",
        "department_type"
    ]
)

# Validation checks
assert len(departments) == 5
assert departments["department_id"].is_unique
assert departments["department_name"].is_unique
assert departments.isnull().sum().sum() == 0

print("\nDepartments dataset:")
print(departments.to_string(index=False))

print("\nAll department validation checks passed!")

# Export to CSV
departments.to_csv(
    DATA_DIR / "departments.csv",
    index=False
)

print("\nDepartments dataset saved successfully!")



# ==========================================
# 5. CHART OF ACCOUNTS DATASET
# ==========================================

accounts_data = [
    # Assets
    ("1000", "Bank", "Asset", "Balance Sheet", "Current Asset", "Debit", "Operating"),
    ("1100", "Accounts Receivable", "Asset", "Balance Sheet", "Current Asset", "Debit", "Operating"),
    ("1200", "Inventory", "Asset", "Balance Sheet", "Current Asset", "Debit", "Operating"),
    ("1300", "Prepaid Expenses", "Asset", "Balance Sheet", "Current Asset", "Debit", "Operating"),
    ("1500", "Property, Plant and Equipment", "Asset", "Balance Sheet", "Non-Current Asset", "Debit", "Investing"),
    ("1590", "Accumulated Depreciation", "Asset", "Balance Sheet", "Non-Current Asset", "Credit", "Non-Cash"),

    # Liabilities
    ("2000", "Accounts Payable", "Liability", "Balance Sheet", "Current Liability", "Credit", "Operating"),
    ("2100", "Accrued Expenses", "Liability", "Balance Sheet", "Current Liability", "Credit", "Operating"),
    ("2200", "VAT Payable", "Liability", "Balance Sheet", "Current Liability", "Credit", "Operating"),

    # Equity
    ("3000", "Share Capital", "Equity", "Balance Sheet", "Equity", "Credit", "Financing"),
    ("3100", "Retained Earnings", "Equity", "Balance Sheet", "Equity", "Credit", "Non-Cash"),

    # Revenue
    ("4000", "Sales Revenue", "Revenue", "Income Statement", "Operating Revenue", "Credit", "Operating"),
    ("4100", "Sales Returns and Allowances", "Revenue", "Income Statement", "Contra Revenue", "Debit", "Operating"),

    # Expenses
    ("5000", "Cost of Goods Sold", "Expense", "Income Statement", "Cost of Sales", "Debit", "Operating"),
    ("5100", "Salaries and Wages", "Expense", "Income Statement", "Operating Expense", "Debit", "Operating"),
    ("5200", "Rent Expense", "Expense", "Income Statement", "Operating Expense", "Debit", "Operating"),
    ("5300", "Utilities Expense", "Expense", "Income Statement", "Operating Expense", "Debit", "Operating"),
    ("5400", "Marketing Expense", "Expense", "Income Statement", "Operating Expense", "Debit", "Operating"),
    ("5500", "Transportation Expense", "Expense", "Income Statement", "Operating Expense", "Debit", "Operating"),
    ("5600", "Office and Administrative Expenses", "Expense", "Income Statement", "Operating Expense", "Debit", "Operating"),
    ("5700", "Depreciation Expense", "Expense", "Income Statement", "Operating Expense", "Debit", "Non-Cash"),
    ("5800", "Other Operating Expenses", "Expense", "Income Statement", "Operating Expense", "Debit", "Operating"),
    ("5900", "Bank Charges", "Expense", "Income Statement", "Operating Expense", "Debit", "Operating")
]

accounts = pd.DataFrame(
    accounts_data,
    columns=[
        "account_code",
        "account_name",
        "account_type",
        "financial_statement",
        "account_subcategory",
        "normal_balance",
        "cash_flow_category"
    ]
)

# Validation checks
assert len(accounts) == 23
assert accounts["account_code"].is_unique
assert accounts["account_name"].is_unique
assert accounts.isnull().sum().sum() == 0

assert set(accounts["account_type"]).issubset({
    "Asset", "Liability", "Equity", "Revenue", "Expense"
})

assert set(accounts["normal_balance"]).issubset({
    "Debit", "Credit"
})

assert set(accounts["financial_statement"]).issubset({
    "Balance Sheet", "Income Statement"
})

assert set(accounts["cash_flow_category"]).issubset({
    "Operating", "Investing", "Financing", "Non-Cash"
})

# Confirm product account references exist
assert {"1200", "4000", "5000"}.issubset(
    set(accounts["account_code"])
)

print("\nChart of Accounts:")
print(accounts.to_string(index=False))

print("\nAll Chart of Accounts validation checks passed!")

# Export to CSV
accounts.to_csv(
    DATA_DIR / "chart_of_accounts.csv",
    index=False
)

print("\nChart of Accounts dataset saved successfully!")
