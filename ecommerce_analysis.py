
import numpy as np 
import pandas as pd  # type: ignore[reportMissingModuleSource]
import matplotlib.pyplot as plt
import seaborn as sns  # type: ignore[reportMissingModuleSource]
df= pd.read_excel("data/OnlineRetail.xlsx")
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())
df= df.drop_duplicates()
print(df.shape)
print("\nQuantity Statistics:")
print(df["Quantity"].describe())
print("\nUnit Price Statistics:")
print(df["UnitPrice"].describe())
print("\nNumber of Countries:")
print(df["Country"].nunique())
print("\nCountries:")
print(df["Country"].unique())
print("\nNumber of Customers:")
print(df["CustomerID"].nunique())
print("\nNumber of Products:")
print(df["StockCode"].nunique())
print("\nCancelled Transactions:")
print(df[df["InvoiceNo"].astype(str).str.startswith("C")].head())
print("\nNegative Quantity Transactions:")
print(df[df["Quantity"] < 0].head())
# create Revenue column 
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
print(
    df[
        ["InvoiceNo", "Description", "Quantity", "UnitPrice", "Revenue"]
    ].head()
)
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month
df["Month_Name"] = df["InvoiceDate"].dt.month_name()
df["Day"] = df["InvoiceDate"].dt.day
df["Hour"] = df["InvoiceDate"].dt.hour



# Remove rows with missing CustomerID
df = df.dropna(subset=["CustomerID"])
print("\nShape after removing missing CustomerID:")
print(df.shape)

# Remove cancelled orders
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]
print("\nShape after removing cancelled orders:")
print(df.shape)

# Remove negative quantities
df = df[df["Quantity"] > 0]
print("\nShape after removing negative quantities:")
print(df.shape)

# Remove invalid prices
df = df[df["UnitPrice"] > 0]
print("\nShape after removing invalid prices:")
print(df.shape)

# Create Revenue column
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
print("\nRevenue:")
print(df[["Quantity", "UnitPrice", "Revenue"]].head())
print(df.shape)
print(df["CustomerID"].isnull().sum())
print(df["Quantity"].min())
print(df["UnitPrice"].min())


# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
# Extract date/time information
df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month
df["Month_Name"] = df["InvoiceDate"].dt.month_name()
df["Day"] = df["InvoiceDate"].dt.day
df["Hour"] = df["InvoiceDate"].dt.hour
print("\nDate and Time Features:")
print(df[
    ["InvoiceDate", "Year", "Month", "Month_Name", "Day", "Hour"]
].head())
print("\nFinal Dataset Shape:")
print(df.shape)
print("\nFinal Columns:")
print(df.columns)
# ==========================================
# STEP 13 - BUSINESS KPIs
# ==========================================
total_revenue = df["Revenue"].sum()
total_orders = df["InvoiceNo"].nunique()
total_units = df["Quantity"].sum()
total_customers = df["CustomerID"].nunique()
total_products = df["StockCode"].nunique()
average_order_value = total_revenue / total_orders

print("\n========== BUSINESS KPIs ==========")
print("Total Revenue:", total_revenue)
print("Total Orders:", total_orders)
print("Total Units Sold:", total_units)
print("Total Customers:", total_customers)
print("Total Products:", total_products)
print("Average Order Value:", average_order_value)
# ==========================================
# STEP 14 - MONTHLY REVENUE ANALYSIS
# ==========================================
# 14.1 Calculate monthly revenue
monthly_revenue = df.groupby(
    ["Year", "Month"]
)["Revenue"].sum().reset_index()
print("\nMonthly Revenue:")
print(monthly_revenue)

# 14.2 Create Year-Month column
monthly_revenue["Year_Month"] = (
    monthly_revenue["Year"].astype(str)
    + "-"
    + monthly_revenue["Month"].astype(str).str.zfill(2)
)
print("\nMonthly Revenue with Year-Month:")
print(monthly_revenue)

# 14.3 Plot Monthly Revenue Trend
plt.figure(figsize=(12, 6))
plt.plot(
    monthly_revenue["Year_Month"],
    monthly_revenue["Revenue"],
    marker="o"
)
plt.title("Monthly Revenue Trend")
plt.xlabel("Year-Month")
plt.ylabel("Revenue (£)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# ==========================================
# STEP 14.4 - HIGHEST & LOWEST REVENUE MONTH
# ==========================================
# Find month with highest revenue
highest_revenue_month = monthly_revenue.loc[
    monthly_revenue["Revenue"].idxmax()
]
# Find month with lowest revenue
lowest_revenue_month = monthly_revenue.loc[
    monthly_revenue["Revenue"].idxmin()
]
print("\n========== REVENUE INSIGHTS ==========")
print(
    "Highest Revenue Month:",
    highest_revenue_month["Year_Month"],
    "£", round(highest_revenue_month["Revenue"], 2)
)
print(
    "Lowest Revenue Month:",
    lowest_revenue_month["Year_Month"],
    "£", round(lowest_revenue_month["Revenue"], 2)
)
# ==========================================
# STEP 15 - MONTHLY ORDERS ANALYSIS
# ==========================================
# 15.1 Calculate monthly orders
monthly_orders = df.groupby(
    ["Year", "Month"]
)["InvoiceNo"].nunique().reset_index()
monthly_orders.rename(
    columns={"InvoiceNo": "Orders"},
    inplace=True
)
print("\nMonthly Orders:")
print(monthly_orders)

# 15.2 Create Year-Month
monthly_orders["Year_Month"] = (
    monthly_orders["Year"].astype(str)
    + "-"
    + monthly_orders["Month"].astype(str).str.zfill(2)
)
print("\nMonthly Orders with Year-Month:")
print(monthly_orders)

# 15.3 Plot Monthly Orders
plt.figure(figsize=(12, 6))
plt.plot(
    monthly_orders["Year_Month"],
    monthly_orders["Orders"],
    marker="o"
)
plt.title("Monthly Orders Trend")
plt.xlabel("Year-Month")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 15.4 Highest & Lowest Order Months
highest_orders_month = monthly_orders.loc[
    monthly_orders["Orders"].idxmax()
]
lowest_orders_month = monthly_orders.loc[
    monthly_orders["Orders"].idxmin()
]
print("\n========== ORDER INSIGHTS ==========")
print(
    "Highest Orders Month:",
    highest_orders_month["Year_Month"],
    int(highest_orders_month["Orders"])
)
print(
    "Lowest Orders Month:",
    lowest_orders_month["Year_Month"],
    int(lowest_orders_month["Orders"])
)
# ==========================================
# STEP 16 - HOURLY SALES ANALYSIS
# ==========================================
# Revenue generated at each hour
hourly_revenue = df.groupby("Hour")["Revenue"].sum().reset_index()
print("\nHourly Revenue:")
print(hourly_revenue)
plt.figure(figsize=(12, 6))
plt.plot(
    hourly_revenue["Hour"],
    hourly_revenue["Revenue"],
    marker="o"
)
plt.title("Hourly Revenue Trend")
plt.xlabel("Hour of the Day")
plt.ylabel("Revenue (£)")
plt.xticks(range(0, 24))
plt.tight_layout()
plt.show()
# Find the hour with highest revenue
best_sales_hour = hourly_revenue.loc[
    hourly_revenue["Revenue"].idxmax()
]
print("\n========== HOURLY SALES INSIGHT ==========")
print(
    "Highest Revenue Hour:",
    int(best_sales_hour["Hour"]),
    ":00",
    "£",
    round(best_sales_hour["Revenue"], 2)
)
# ==========================================
# STEP 17 - TOP PRODUCTS BY REVENUE
# ==========================================
# Calculate revenue generated by each product
product_revenue = df.groupby(
    ["StockCode", "Description"]
)["Revenue"].sum().reset_index()
# Sort products by revenue
product_revenue = product_revenue.sort_values(
    by="Revenue",
    ascending=False
)
print("\nTop 10 Products by Revenue:")
print(product_revenue.head(10))
# ==========================================
# STEP 17.2 - TOP 10 PRODUCTS VISUALIZATION
# ==========================================
top_10_products = product_revenue.head(10)
plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_10_products,
    x="Revenue",
    y="Description"
)
plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue (£)")
plt.ylabel("Product")
plt.tight_layout()
plt.show()
# ==========================================
# STEP 18 - TOP PRODUCTS BY QUANTITY SOLD
# ==========================================
product_quantity = df.groupby(
    ["StockCode", "Description"]
)["Quantity"].sum().reset_index()
product_quantity = product_quantity.sort_values(
    by="Quantity",
    ascending=False
)
print("\nTop 10 Products by Quantity Sold:")
print(product_quantity.head(10))
# ==========================================
# STEP 18.2 - TOP 10 PRODUCTS BY QUANTITY
# ==========================================
top_10_quantity = product_quantity.head(10)
plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_10_quantity,
    x="Quantity",
    y="Description"
)
plt.title("Top 10 Products by Quantity Sold")
plt.xlabel("Quantity Sold")
plt.ylabel("Product")
plt.tight_layout()
plt.show()
# ==========================================
# STEP 19 - TOP COUNTRIES BY REVENUE
# ==========================================
country_revenue = df.groupby("Country")["Revenue"].sum().reset_index()
country_revenue = country_revenue.sort_values(
    by="Revenue",
    ascending=False
)
print("\nTop 10 Countries by Revenue:")
print(country_revenue.head(10))
# ==========================================
# STEP 19.2 - TOP 10 COUNTRIES VISUALIZATION
# ==========================================
top_10_countries = country_revenue.head(10)
plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_10_countries,
    x="Revenue",
    y="Country"
)
plt.title("Top 10 Countries by Revenue")
plt.xlabel("Revenue (£)")
plt.ylabel("Country")
plt.tight_layout()
plt.show()
highest_revenue_country = country_revenue.iloc[0]
print("\n========== COUNTRY REVENUE INSIGHT ==========")
print(
    "Highest Revenue Country:",
    highest_revenue_country["Country"],
    "£",
    round(highest_revenue_country["Revenue"], 2)
)
# ==========================================
# STEP 20 - TOP CUSTOMERS BY REVENUE
# ==========================================
customer_revenue = df.groupby(
    "CustomerID"
)["Revenue"].sum().reset_index()
customer_revenue = customer_revenue.sort_values(
    by="Revenue",
    ascending=False
)
print("\nTop 10 Customers by Revenue:")
print(customer_revenue.head(10))
# ==========================================
# STEP 20.2 - TOP 10 CUSTOMERS VISUALIZATION
# ==========================================
top_10_customers = customer_revenue.head(10)
plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_10_customers,
    x="Revenue",
    y="CustomerID"
)
plt.title("Top 10 Customers by Revenue")
plt.xlabel("Revenue (£)")
plt.ylabel("Customer ID")
plt.tight_layout()
plt.show()
highest_value_customer = customer_revenue.iloc[0]
print("\n========== CUSTOMER REVENUE INSIGHT ==========")
print(
    "Highest Value Customer:",
    int(highest_value_customer["CustomerID"])
)
print(
    "Customer Revenue: £",
    round(highest_value_customer["Revenue"], 2)
)
# ==========================================
# STEP 21 - TOP CUSTOMERS BY NUMBER OF ORDERS
# ==========================================
customer_orders = df.groupby(
    "CustomerID"
)["InvoiceNo"].nunique().reset_index()
customer_orders.rename(
    columns={"InvoiceNo": "Orders"},
    inplace=True
)
customer_orders = customer_orders.sort_values(
    by="Orders",
    ascending=False
)
print("\nTop 10 Customers by Number of Orders:")
print(customer_orders.head(10))
# ==========================================
# STEP 21.2 - TOP 10 CUSTOMERS VISUALIZATION
# ==========================================
top_10_customer_orders = customer_orders.head(10)
plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_10_customer_orders,
    x="Orders",
    y="CustomerID"
)
plt.title("Top 10 Customers by Number of Orders")
plt.xlabel("Number of Orders")
plt.ylabel("Customer ID")
plt.tight_layout()
plt.show()
most_frequent_customer = customer_orders.iloc[0]
print("\n========== CUSTOMER ORDER INSIGHT ==========")
print(
    "Most Frequent Customer:",
    int(most_frequent_customer["CustomerID"])
)
print(
    "Number of Orders:",
    int(most_frequent_customer["Orders"])
)
# ==========================================
# STEP 22 - COUNTRY-WISE ORDERS
# ==========================================
country_orders = df.groupby(
    "Country"
)["InvoiceNo"].nunique().reset_index()
country_orders.rename(
    columns={"InvoiceNo": "Orders"},
    inplace=True
)
country_orders = country_orders.sort_values(
    by="Orders",
    ascending=False
)
print("\nTop 10 Countries by Number of Orders:")
print(country_orders.head(10))
# ==========================================
# STEP 22.2 - COUNTRY ORDERS VISUALIZATION
# ==========================================
top_10_country_orders = country_orders.head(10)
plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_10_country_orders,
    x="Orders",
    y="Country"
)
plt.title("Top 10 Countries by Number of Orders")
plt.xlabel("Number of Orders")
plt.ylabel("Country")
plt.tight_layout()
plt.show()
# ==========================================
# STEP 22.3 - COUNTRY-WISE CUSTOMERS
# ==========================================
country_customers = df.groupby(
    "Country"
)["CustomerID"].nunique().reset_index()
country_customers.rename(
    columns={"CustomerID": "Customers"},
    inplace=True
)
country_customers = country_customers.sort_values(
    by="Customers",
    ascending=False
)
print("\nTop 10 Countries by Number of Customers:")
print(country_customers.head(10))
# ==========================================
# STEP 22.4 - COUNTRY CUSTOMERS VISUALIZATION
# ==========================================
top_10_country_customers = country_customers.head(10)
plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_10_country_customers,
    x="Customers",
    y="Country"
)
plt.title("Top 10 Countries by Number of Customers")
plt.xlabel("Number of Customers")
plt.ylabel("Country")
plt.tight_layout()
plt.show()
# ==========================================
# STEP 23 - PRODUCT PERFORMANCE ANALYSIS
# ==========================================
product_performance = df.groupby(
    ["StockCode", "Description"]
).agg(
    Total_Quantity=("Quantity", "sum"),
    Total_Revenue=("Revenue", "sum")
).reset_index()
product_performance = product_performance.sort_values(
    by="Total_Revenue",
    ascending=False
)
print("\nProduct Performance:")
print(product_performance.head(10))
# ==========================================
# STEP 23.2 - TOP PRODUCTS BY QUANTITY
# ==========================================
top_quantity_products = product_performance.sort_values(
    by="Total_Quantity",
    ascending=False
).head(10)
print("\nTop 10 Products by Quantity:")
print(top_quantity_products)
# ==========================================
# STEP 23.3 - REVENUE VS QUANTITY
# ==========================================
plt.figure(figsize=(12, 6))
sns.scatterplot(
    data=product_performance,
    x="Total_Quantity",
    y="Total_Revenue"
)
plt.title("Product Quantity vs Revenue")
plt.xlabel("Total Quantity Sold")
plt.ylabel("Total Revenue (£)")
plt.tight_layout()
plt.show()
highest_quantity_product = product_performance.loc[
    product_performance["Total_Quantity"].idxmax()
]
print("\n========== PRODUCT PERFORMANCE INSIGHT ==========")
print(
    "Highest Quantity Product:",
    highest_quantity_product["Description"]
)
print(
    "Quantity Sold:",
    int(highest_quantity_product["Total_Quantity"])
)
print(
    "Revenue: £",
    round(highest_quantity_product["Total_Revenue"], 2)
)
# ==========================================
# STEP 24 - DAY OF WEEK SALES ANALYSIS
# ==========================================
df["Day_Name"] = df["InvoiceDate"].dt.day_name()
day_revenue = df.groupby(
    "Day_Name"
)["Revenue"].sum().reset_index()
print("\nRevenue by Day:")
print(day_revenue)
day_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]
day_revenue["Day_Name"] = pd.Categorical(
    day_revenue["Day_Name"],
    categories=day_order,
    ordered=True
)
day_revenue = day_revenue.sort_values("Day_Name")
print("\nRevenue by Day in Correct Order:")
print(day_revenue)
# ==========================================
# STEP 24.3 - DAY-WISE REVENUE VISUALIZATION
# ==========================================
plt.figure(figsize=(10, 6))
sns.barplot(
    data=day_revenue,
    x="Day_Name",
    y="Revenue"
)
plt.title("Revenue by Day of the Week")
plt.xlabel("Day")
plt.ylabel("Revenue (£)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
best_sales_day = day_revenue.loc[
    day_revenue["Revenue"].idxmax()
]
print("\n========== DAY-WISE SALES INSIGHT ==========")
print(
    "Highest Revenue Day:",
    best_sales_day["Day_Name"]
)
print(
    "Revenue: £",
    round(best_sales_day["Revenue"], 2)
)
# ==========================================
# STEP 25 - MONTHLY QUANTITY SOLD
# ==========================================
monthly_quantity = df.groupby(
    ["Year", "Month"]
)["Quantity"].sum().reset_index()
monthly_quantity.rename(
    columns={"Quantity": "Units_Sold"},
    inplace=True
)
monthly_quantity["Year_Month"] = (
    monthly_quantity["Year"].astype(str)
    + "-"
    + monthly_quantity["Month"].astype(str).str.zfill(2)
)
print("\nMonthly Quantity Sold:")
print(monthly_quantity)
# ==========================================
# STEP 25.2 - MONTHLY QUANTITY VISUALIZATION
# ==========================================
plt.figure(figsize=(12, 6))
plt.plot(
    monthly_quantity["Year_Month"],
    monthly_quantity["Units_Sold"],
    marker="o"
)
plt.title("Monthly Quantity Sold Trend")
plt.xlabel("Year-Month")
plt.ylabel("Units Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
highest_quantity_month = monthly_quantity.loc[
    monthly_quantity["Units_Sold"].idxmax()
]
lowest_quantity_month = monthly_quantity.loc[
    monthly_quantity["Units_Sold"].idxmin()
]
print("\n========== QUANTITY INSIGHTS ==========")
print(
    "Highest Quantity Month:",
    highest_quantity_month["Year_Month"],
    int(highest_quantity_month["Units_Sold"])
)
print(
    "Lowest Quantity Month:",
    lowest_quantity_month["Year_Month"],
    int(lowest_quantity_month["Units_Sold"])
)
# ==========================================
# STEP 26 - MONTHLY AVERAGE ORDER VALUE
# ==========================================
monthly_aov = df.groupby(
    ["Year", "Month"]
).agg(
    Revenue=("Revenue", "sum"),
    Orders=("InvoiceNo", "nunique")
).reset_index()
monthly_aov["AOV"] = (
    monthly_aov["Revenue"] / monthly_aov["Orders"]
)
monthly_aov["Year_Month"] = (
    monthly_aov["Year"].astype(str)
    + "-"
    + monthly_aov["Month"].astype(str).str.zfill(2)
)
print("\nMonthly Average Order Value:")
print(monthly_aov)
# ==========================================
# STEP 26.2 - MONTHLY AOV VISUALIZATION
# ==========================================
plt.figure(figsize=(12, 6))
plt.plot(
    monthly_aov["Year_Month"],
    monthly_aov["AOV"],
    marker="o"
)
plt.title("Monthly Average Order Value")
plt.xlabel("Year-Month")
plt.ylabel("Average Order Value (£)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
highest_aov_month = monthly_aov.loc[
    monthly_aov["AOV"].idxmax()
]
lowest_aov_month = monthly_aov.loc[
    monthly_aov["AOV"].idxmin()
]
print("\n========== AOV INSIGHTS ==========")
print(
    "Highest AOV Month:",
    highest_aov_month["Year_Month"],
    "£",
    round(highest_aov_month["AOV"], 2)
)
print(
    "Lowest AOV Month:",
    lowest_aov_month["Year_Month"],
    "£",
    round(lowest_aov_month["AOV"], 2)
)
customer_summary = df.groupby("CustomerID").agg(
    Total_Revenue=("Revenue", "sum"),
    Total_Orders=("InvoiceNo", "nunique"),
    Total_Quantity=("Quantity", "sum")
).reset_index()
print("\nCustomer Summary:")
print(customer_summary.head(10))
customer_summary["Customer_Segment"] = pd.qcut(
    customer_summary["Total_Revenue"].rank(method="first"),
    q=3,
    labels=["Low Value", "Medium Value", "High Value"]
)
print("\nCustomer Segments:")
print(
    customer_summary[
        ["CustomerID", "Total_Revenue", "Total_Orders", "Customer_Segment"]
    ].head(10)
)
segment_counts = customer_summary["Customer_Segment"].value_counts()
print("\nCustomers in Each Segment:")
print(segment_counts)
plt.figure(figsize=(10, 6))
sns.countplot(
    data=customer_summary,
    x="Customer_Segment"
)
plt.title("Customer Segmentation")
plt.xlabel("Customer Segment")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=customer_summary,
    x="Total_Orders",
    y="Total_Revenue"
)
plt.title("Customer Orders vs Revenue")
plt.xlabel("Number of Orders")
plt.ylabel("Total Revenue (£)")
plt.tight_layout()
plt.show()
most_orders_customer = customer_summary.loc[
    customer_summary["Total_Orders"].idxmax()
]
print("\nCustomer with Most Orders:")
print("Customer ID:", int(most_orders_customer["CustomerID"]))
print("Orders:", int(most_orders_customer["Total_Orders"]))
print("Revenue: £", round(most_orders_customer["Total_Revenue"], 2))
highest_revenue_customer = customer_summary.loc[
    customer_summary["Total_Revenue"].idxmax()
]
print("\nHighest Revenue Customer:")
print("Customer ID:", int(highest_revenue_customer["CustomerID"]))
print("Revenue: £", round(highest_revenue_customer["Total_Revenue"], 2))
print("Orders:", int(highest_revenue_customer["Total_Orders"]))
product_analysis = df.groupby(
    ["StockCode", "Description"]
).agg(
    Units_Sold=("Quantity", "sum"),
    Revenue=("Revenue", "sum")
).reset_index()
print("\nProduct Performance:")
print(product_analysis.head(10))
top_revenue_products = product_analysis.sort_values(
    by="Revenue",
    ascending=False
).head(10)
print("\nTop 10 Products by Revenue:")
print(top_revenue_products)
plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_revenue_products,
    x="Revenue",
    y="Description"
)
plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue (£)")
plt.ylabel("Product")
plt.tight_layout()
plt.show()
top_quantity_products = product_analysis.sort_values(
    by="Units_Sold",
    ascending=False
).head(10)
print("\nTop 10 Products by Units Sold:")
print(top_quantity_products)
plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_quantity_products,
    x="Units_Sold",
    y="Description"
)
plt.title("Top 10 Products by Units Sold")
plt.xlabel("Units Sold")
plt.ylabel("Product")
plt.tight_layout()
plt.show()
country_analysis = df.groupby("Country").agg(
    Revenue=("Revenue", "sum"),
    Orders=("InvoiceNo", "nunique"),
    Customers=("CustomerID", "nunique")
).reset_index()
country_analysis = country_analysis.sort_values(
    by="Revenue",
    ascending=False
)
print("\nCountry-wise Performance:")
print(country_analysis.head(10))
top_countries = country_analysis.head(10)
plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_countries,
    x="Revenue",
    y="Country"
)
plt.title("Top 10 Countries by Revenue")
plt.xlabel("Revenue (£)")
plt.ylabel("Country")
plt.tight_layout()
plt.show()
top_order_countries = country_analysis.sort_values(
    by="Orders",
    ascending=False
).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_order_countries,
    x="Orders",
    y="Country"
)
plt.title("Top 10 Countries by Number of Orders")
plt.xlabel("Number of Orders")
plt.ylabel("Country")
plt.tight_layout()
plt.show()
highest_country = country_analysis.iloc[0]
print("\nHighest Revenue Country:")
print("Country:", highest_country["Country"])
print("Revenue: £", round(highest_country["Revenue"], 2))
print("Orders:", int(highest_country["Orders"]))
print("Customers:", int(highest_country["Customers"]))
customer_summary["Customer_Type"] = np.where(
    customer_summary["Total_Orders"] == 1,
    "One-Time Customer",
    "Repeat Customer"
)
print("\nCustomer Type:")
print(
    customer_summary[
        ["CustomerID", "Total_Orders", "Total_Revenue", "Customer_Type"]
    ].head(10)
)
customer_type_count = customer_summary["Customer_Type"].value_counts()
print("\nCustomer Type Count:")
print(customer_type_count)
plt.figure(figsize=(8, 6))
sns.countplot(
    data=customer_summary,
    x="Customer_Type"
)
plt.title("One-Time vs Repeat Customers")
plt.xlabel("Customer Type")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()
customer_type_percentage = (
    customer_type_count / customer_type_count.sum() * 100
)
print("\nCustomer Type Percentage:")
print(customer_type_percentage.round(2))
customer_type_revenue = customer_summary.groupby(
    "Customer_Type"
)["Total_Revenue"].sum().reset_index()
print("\nRevenue by Customer Type:")
print(customer_type_revenue)
customer_type_revenue["Revenue_Percentage"] = (
    customer_type_revenue["Total_Revenue"]
    / customer_type_revenue["Total_Revenue"].sum()
    * 100
)
print("\nRevenue Contribution:")
print(customer_type_revenue)
plt.figure(figsize=(8, 6))
sns.barplot(
    data=customer_type_revenue,
    x="Customer_Type",
    y="Total_Revenue"
)
plt.title("Revenue by Customer Type")
plt.xlabel("Customer Type")
plt.ylabel("Total Revenue (£)")
plt.tight_layout()
plt.show()
for _, row in customer_type_revenue.iterrows():
    print(
        row["Customer_Type"],
        ":",
        round(row["Revenue_Percentage"], 2),
        "% of total revenue"
    )
product_revenue = product_analysis.sort_values(
    by="Revenue",
    ascending=False
).reset_index(drop=True)
print("\nProducts Sorted by Revenue:")
print(product_revenue.head(10))
total_product_revenue = product_revenue["Revenue"].sum()
product_revenue["Revenue_Percentage"] = (
    product_revenue["Revenue"]
    / total_product_revenue
    * 100
)
product_revenue["Cumulative_Revenue_Percentage"] = (
    product_revenue["Revenue_Percentage"].cumsum()
)
print("\nRevenue Contribution:")
print(
    product_revenue[
        [
            "Description",
            "Revenue",
            "Revenue_Percentage",
            "Cumulative_Revenue_Percentage"
        ]
    ].head(10)
)
products_for_80_percent = (
    product_revenue[
        product_revenue["Cumulative_Revenue_Percentage"] <= 80
    ]
)
print(
    "\nNumber of products contributing up to 80% revenue:",
    len(products_for_80_percent)
)
print(
    "Total products:",
    len(product_revenue)
)
plt.figure(figsize=(12, 6))
plt.plot(
    range(1, len(product_revenue) + 1),
    product_revenue["Cumulative_Revenue_Percentage"]
)
plt.axhline(
    y=80,
    linestyle="--"
)
plt.title("Pareto Analysis of Product Revenue")
plt.xlabel("Number of Products")
plt.ylabel("Cumulative Revenue (%)")
plt.tight_layout()
plt.show()
correlation_data = df[
    ["Quantity", "UnitPrice", "Revenue", "Hour", "Month"]
]
correlation_matrix = correlation_data.corr()
print("\nCorrelation Matrix:")
print(correlation_matrix.round(2))
plt.figure(figsize=(10, 6))
sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Matrix of Sales Variables")
plt.tight_layout()
plt.show()
# ==========================================
# STEP 35: KEY BUSINESS INSIGHTS
# ==========================================
print("\n" + "=" * 50)
print("KEY BUSINESS INSIGHTS")
print("=" * 50)
# 1. Overall Business Performance
print("\n1. Overall Business Performance")
print("Total Revenue: £", round(total_revenue, 2))
print("Total Orders:", total_orders)
print("Total Customers:", total_customers)
print("Average Order Value: £", round(average_order_value, 2))

# 2. Best Revenue Month
best_month = monthly_revenue.loc[
    monthly_revenue["Revenue"].idxmax()
]
print("\n2. Best Revenue Month")
print(
    best_month["Year_Month"],
    "generated £",
    round(best_month["Revenue"], 2)
)

# 3. Best Sales Hour
best_hour = hourly_revenue.loc[
    hourly_revenue["Revenue"].idxmax()
]
print("\n3. Best Sales Hour")
print(
    int(best_hour["Hour"]),
    ":00 generated £",
    round(best_hour["Revenue"], 2)
)

# 4. Best Product
best_product = product_analysis.loc[
    product_analysis["Revenue"].idxmax()
]
print("\n4. Best Product by Revenue")
print("Product:", best_product["Description"])
print("Revenue: £", round(best_product["Revenue"], 2))

# 5. Best Country
best_country = country_analysis.iloc[0]
print("\n5. Best Country")
print("Country:", best_country["Country"])
print("Revenue: £", round(best_country["Revenue"], 2))

# 6. Highest Value Customer
best_customer = customer_summary.loc[
    customer_summary["Total_Revenue"].idxmax()
]
print("\n6. Highest Value Customer")
print("Customer ID:", int(best_customer["CustomerID"]))
print("Revenue: £", round(best_customer["Total_Revenue"], 2))

# 7. Repeat Customer Revenue
repeat_revenue = customer_type_revenue[
    customer_type_revenue["Customer_Type"] == "Repeat Customer"
]["Total_Revenue"].iloc[0]
repeat_percentage = (
    repeat_revenue / total_revenue * 100
)
print("\n7. Repeat Customer Contribution")
print(
    "Repeat customers generated",
    round(repeat_percentage, 2),
    "% of total revenue"
)

print("\n" + "=" * 50)
print("BUSINESS RECOMMENDATIONS")
print("=" * 50)
print("""
1. Focus marketing and promotions around high-revenue months.
2. Optimize staffing and marketing campaigns during peak sales hours.
3. Promote high-performing products to increase revenue.
4. Develop loyalty programs to retain repeat customers.
5. Focus international expansion on high-performing countries.
6. Identify high-value customers and provide personalized offers.
7. Use product revenue and quantity analysis to improve inventory planning.
""")

# ==========================================
# STEP 36: FINAL SALES DASHBOARD
# ==========================================

fig = plt.figure(figsize=(16, 12))

# ------------------------------------------
# 1. Monthly Revenue
# ------------------------------------------

ax1 = plt.subplot(2, 2, 1)

sns.lineplot(
    data=monthly_revenue,
    x="Year_Month",
    y="Revenue",
    marker="o",
    ax=ax1
)

ax1.set_title("Monthly Revenue Trend")
ax1.set_xlabel("Month")
ax1.set_ylabel("Revenue (£)")
ax1.tick_params(axis="x", rotation=45)


# ------------------------------------------
# 2. Top 10 Products
# ------------------------------------------

ax2 = plt.subplot(2, 2, 2)

top_products_dashboard = product_analysis.sort_values(
    by="Revenue",
    ascending=False
).head(10)

sns.barplot(
    data=top_products_dashboard,
    x="Revenue",
    y="Description",
    ax=ax2
)

ax2.set_title("Top 10 Products by Revenue")
ax2.set_xlabel("Revenue (£)")
ax2.set_ylabel("Product")


# ------------------------------------------
# 3. Top Countries
# ------------------------------------------

ax3 = plt.subplot(2, 2, 3)

top_countries_dashboard = country_analysis.head(10)

sns.barplot(
    data=top_countries_dashboard,
    x="Revenue",
    y="Country",
    ax=ax3
)

ax3.set_title("Top 10 Countries by Revenue")
ax3.set_xlabel("Revenue (£)")
ax3.set_ylabel("Country")


# ------------------------------------------
# 4. Customer Revenue vs Orders
# ------------------------------------------

ax4 = plt.subplot(2, 2, 4)

sns.scatterplot(
    data=customer_summary,
    x="Total_Orders",
    y="Total_Revenue",
    ax=ax4
)

ax4.set_title("Customer Orders vs Revenue")
ax4.set_xlabel("Number of Orders")
ax4.set_ylabel("Revenue (£)")


# ------------------------------------------
# Dashboard Title
# ------------------------------------------

fig.suptitle(
    "E-Commerce Sales Analysis Dashboard",
    fontsize=16
)

plt.tight_layout()
plt.show()