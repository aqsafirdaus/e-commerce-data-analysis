import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import matplotlib.ticker as ticker

sns.set(style='whitegrid')

# LOAD DATA
all_df = pd.read_csv("dashboard/all_data.csv")
all_df["order_purchase_timestamp"] = pd.to_datetime(all_df["order_purchase_timestamp"])

# SIDEBAR
st.sidebar.title("📊 Dashboard Filter")

min_date = all_df["order_purchase_timestamp"].min()
max_date = all_df["order_purchase_timestamp"].max()

start_date, end_date = st.sidebar.date_input(
    "Pilih Rentang Waktu",
    min_value=min_date,
    max_value=max_date,
    value=[min_date, max_date]
)

main_df = all_df[
    (all_df["order_purchase_timestamp"] >= str(start_date)) &
    (all_df["order_purchase_timestamp"] <= str(end_date))
]

# HEADER
st.title("🛍️ E-Commerce Analytics Dashboard")
st.markdown("Analisis performa penjualan dan perilaku pelanggan")

# KPI SECTION
total_orders = main_df["order_id"].nunique()
total_revenue = round(main_df["total_price"].sum())

col1, col2 = st.columns(2)

col1.metric(
    "🧾 Total Orders", 
    f"{total_orders:,}"
)

col2.metric(
    "💰 Total Revenue", 
    f"{total_revenue:,}"
)

# TREND BULANAN
st.subheader("📈 Monthly Revenue Trend")

main_df['order_purchase_timestamp'] = pd.to_datetime(
    main_df['order_purchase_timestamp'], errors='coerce'
)

monthly_df = main_df.resample(rule='ME', on='order_purchase_timestamp').agg({
    "order_id": "nunique",
    "total_price": "sum"
}).reset_index()

fig, ax = plt.subplots(figsize=(10,5))

ax.plot(
    monthly_df["order_purchase_timestamp"],
    monthly_df["total_price"],
    marker='o'
)

ax.set_title("Revenue per Month")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue")

ax.yaxis.set_major_formatter(
    ticker.FuncFormatter(lambda x, _: f'{int(x):,}')
)

plt.xticks(rotation=45)
st.pyplot(fig)

# TOP PRODUCT CATEGORY
st.subheader("🏆 Top Product Categories")

top_product = main_df.groupby("product_category_name_english")["order_id"] \
    .count().reset_index().sort_values(by="order_id", ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(
    x="order_id",
    y="product_category_name_english",
    data=top_product,
    ax=ax
)

ax.set_title("Top 10 Product Categories")
ax.set_xlabel("Total Orders")

st.pyplot(fig)

# TOP CITY
st.subheader("🌍 Top Customer Cities")

top_city = main_df.groupby("customer_city")["order_id"] \
    .count().reset_index().sort_values(by="order_id", ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(
    x="order_id",
    y="customer_city",
    data=top_city,
    ax=ax
)

ax.set_title("Top Cities by Orders")
st.pyplot(fig)

# RFM ANALYSIS
st.subheader("👥 Customer Behavior (RFM)")

rfm_df = main_df.groupby(by="customer_unique_id", as_index=False).agg({
    "order_purchase_timestamp": "max",
    "order_id": "nunique",
    "total_price": "sum"
})

rfm_df.columns = ["customer_id", "max_date", "frequency", "monetary"]

recent_date = main_df["order_purchase_timestamp"].max()

rfm_df["recency"] = (recent_date - rfm_df["max_date"]).dt.days

# KPI RFM
col1, col2, col3 = st.columns(3)

col1.metric("📅 Avg Recency", round(rfm_df["recency"].mean(), 1))
col2.metric("🔁 Avg Frequency", round(rfm_df["frequency"].mean(), 2))
col3.metric("💸 Avg Monetary", f"{int(rfm_df['monetary'].mean()):,}")

# RFM VISUAL
fig, ax = plt.subplots(1,3, figsize=(15,5))

# Recency
sns.barplot(
    x=rfm_df.sort_values("recency").head(5)["recency"],
    y=["Top 1","Top 2","Top 3","Top 4","Top 5"],
    ax=ax[0]
)
ax[0].set_title("Best Recency")

# Frequency
sns.barplot(
    x=rfm_df.sort_values("frequency", ascending=False).head(5)["frequency"],
    y=["Top 1","Top 2","Top 3","Top 4","Top 5"],
    ax=ax[1]
)
ax[1].set_title("Top Frequency")

# Monetary
sns.barplot(
    x=rfm_df.sort_values("monetary", ascending=False).head(5)["monetary"],
    y=["Top 1","Top 2","Top 3","Top 4","Top 5"],
    ax=ax[2]
)
ax[2].set_title("Top Monetary")

st.pyplot(fig)

# FOOTER
st.markdown("---")
st.caption("🚀 E-Commerce Dashboard | Data Analysis Project")
