# E-Commerce Sales Analysis

## 📊 Project Overview

This project analyzes an e-commerce retail dataset to understand sales performance, customer behavior, product performance, and country-wise business trends.

The project focuses on using Python-based data analysis and visualization techniques to convert raw transaction data into meaningful business insights.

---

## 🎯 Business Problem

The objective of this project is to answer important business questions such as:

* How much revenue does the business generate?
* Which months have the highest sales?
* Which products generate the most revenue?
* Which products are sold in the highest quantities?
* Which countries contribute the most revenue?
* Who are the highest-value customers?
* How many customers are repeat customers?
* What time of the day generates the most revenue?
* What factors are associated with higher revenue?

---

## 📁 Dataset

The project uses the **Online Retail** transactional dataset.

The dataset contains information about:

* Invoice Number
* Stock Code
* Product Description
* Quantity
* Invoice Date
* Unit Price
* Customer ID
* Country

The original dataset contains approximately **542,000 transactions**.

---

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn

Excel was used only as the source data format.

---

## 🧹 Data Cleaning

The following data-cleaning operations were performed:

* Removed records with missing Customer IDs
* Removed cancelled orders
* Removed transactions with negative quantities
* Removed transactions with invalid/zero prices
* Created a Revenue column
* Converted InvoiceDate into datetime format
* Extracted year, month, month name, day, hour, and day of week

### Revenue Calculation

```text
Revenue = Quantity × UnitPrice
```

---

## 📈 Analysis Performed

### 1. Business KPIs

Calculated:

* Total Revenue
* Total Orders
* Total Units Sold
* Total Customers
* Total Products
* Average Order Value

### 2. Time-Based Analysis

Analyzed:

* Monthly revenue
* Monthly orders
* Monthly quantity sold
* Monthly Average Order Value
* Hourly revenue
* Day-of-week revenue

### 3. Product Analysis

Analyzed:

* Top products by revenue
* Top products by quantity
* Product revenue vs quantity
* Product revenue contribution
* Pareto analysis

### 4. Customer Analysis

Analyzed:

* Top customers by revenue
* Top customers by number of orders
* Customer segmentation
* Customer revenue vs orders
* One-time vs repeat customers
* Repeat customer revenue contribution

### 5. Country Analysis

Analyzed:

* Revenue by country
* Orders by country
* Customers by country
* Top-performing countries

### 6. Statistical Analysis

Created a correlation matrix to examine relationships between:

* Quantity
* Unit Price
* Revenue
* Hour
* Month

---

## 🔑 Key Business Findings

* Total cleaned revenue was approximately **£8.89 million**.
* The dataset contained approximately **18,532 unique orders** after cleaning.
* Approximately **5.15 million units** were sold.
* The business had approximately **4,338 unique customers**.
* The overall Average Order Value was approximately **£479.56**.
* **November 2011** generated the highest monthly revenue at approximately **£1.16 million**.
* **12 PM** was the highest-revenue hour, generating approximately **£1.37 million**.
* Revenue showed strong growth during **September–November 2011**.
* Repeat customers represent an important revenue segment.
* Product and customer concentration can be evaluated using the Pareto analysis.

---

## 💡 Business Recommendations

Based on the analysis:

1. Focus marketing campaigns around high-performing sales periods.

2. Maintain sufficient inventory for high-revenue and high-demand products.

3. Develop loyalty programs to increase repeat purchases.

4. Provide personalized offers to high-value customers.

5. Focus international expansion on high-performing markets.

6. Use historical sales patterns to improve inventory planning.

7. Monitor products that generate high revenue as well as products with high sales volume.

---

## 📊 Visualizations

The project includes visualizations for:

* Monthly Revenue Trend
* Monthly Orders Trend
* Hourly Revenue Trend
* Top Products by Revenue
* Top Products by Quantity
* Top Countries by Revenue
* Top Countries by Orders
* Customer Orders vs Revenue
* Customer Segmentation
* One-Time vs Repeat Customers
* Pareto Revenue Analysis
* Correlation Heatmap
* Final E-Commerce Sales Dashboard

---

## 📂 Project Structure

```text
Ecommerce-Sales-Analysis/
│
├── data/
│   └── OnlineRetail.xlsx
│
├── visualizations/
│
├── ecommerce_analysis.py
│
└── README.md
```

---

## 🚀 Conclusion

This project demonstrates how Python can be used to clean, analyze, visualize, and interpret real-world e-commerce transaction data.

The analysis converts raw transactional data into business-focused insights that can support decisions related to **sales, customers, products, inventory, and marketing**.

---

## 👨‍💻 Skills Demonstrated

**Python | NumPy | Pandas | Matplotlib | Seaborn | Data Cleaning | EDA | Feature Engineering | KPI Analysis | Customer Segmentation | Business Analysis | Data Visualization**
