import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
dbname = os.getenv('DB_NAME')

DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
engine = create_engine(DATABASE_URL)


script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, '..', 'Data', 'Transformed data')
df_orders = pd.read_csv(os.path.join(data_path, "orders.csv"))
df_items = pd.read_csv(os.path.join(data_path, "order_items.csv"))
df_payments = pd.read_csv(os.path.join(data_path, "order_payments.csv"))
df_geolocation = pd.read_csv(os.path.join(data_path, "geolocation.csv"))

df_orders.to_sql("transformed_orders", engine, if_exists="replace", index=False)
df_items.to_sql("transformed_order_items", engine, if_exists="replace", index=False)
df_payments.to_sql("transformed_order_payments", engine, if_exists="replace", index=False)
df_geolocation.to_sql("transformed_geolocation", engine, if_exists="replace", index=False)

print("Se cargaron todas las tablas")
