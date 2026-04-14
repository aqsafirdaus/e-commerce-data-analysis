# 🛍️ E-Commerce Data Analysis Dashboard

Dashboard interaktif ini dibuat menggunakan **Streamlit** untuk menganalisis performa penjualan dan perilaku pelanggan berdasarkan dataset e-commerce.

Dashboard ini menampilkan:

* 📊 Total Orders & Revenue
* 📈 Trend penjualan bulanan
* 🏆 Kategori produk terlaris
* 🌍 Kota dengan jumlah transaksi terbanyak
* 👥 Analisis perilaku pelanggan (RFM)

---

## ⚙️ Setup Environment - Anaconda

```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

---

## ⚙️ Setup Environment - Python (Virtual Environment)

Jika menggunakan Python biasa:

```
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
pip install -r requirements.txt
```

---


## ▶️ Menjalankan Dashboard

```
streamlit run dashboard.py
```

---

## 📌 Fitur Utama Dashboard

* **Filter Rentang Waktu** untuk analisis data
* **KPI (Key Performance Indicator)**:

  * Total Orders
  * Total Revenue
* **Visualisasi Interaktif**:

  * Trend revenue bulanan
  * Top product categories
  * Top customer cities
* **RFM Analysis**:

  * Recency (terakhir transaksi)
  * Frequency (jumlah transaksi)
  * Monetary (total pengeluaran)

---

## 📊 Insight yang Dihasilkan

Dashboard ini membantu:

* Memahami performa bisnis dari waktu ke waktu
* Mengidentifikasi produk unggulan
* Mengetahui wilayah dengan pelanggan terbanyak
* Menganalisis perilaku pelanggan berdasarkan transaksi

---

## 🚀 Teknologi yang Digunakan

* Python
* Pandas
* Matplotlib
* Seaborn
* Streamlit


