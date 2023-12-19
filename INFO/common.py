from random import choice
tables = [
    "users",
    "customers",
    "products",
    "orders",
    "invoices",
]

columns = [
    "id",
    "name",
    "email",
    "phone",
    "create_at",
    "updated_at"
]

table_common = choice(tables)
columns_common = choice(columns)


