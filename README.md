# Retail & Marketing Analytics: Customer Segmentation & Growth Strategy

End-to-end customer segmentation project using **RFM (Recency, Frequency, Monetary) analysis** combined with **K-Means clustering** to drive targeted marketing campaigns.

## 📌 Overview

Identify high-value customers, prevent churn, and design segment-specific marketing strategies to maximize Customer Lifetime Value (CLV). The output is a clean customer segmentation that marketing teams can act on immediately.

## 📊 Dataset

- **Source:** Synthetic dataset modeled after the UCI *Online Retail II* dataset (UK-based e-commerce)
- **Size:** ~70,000 transactions across 2,500 unique customers, 12 months
- **Features:** Invoice number, product description, quantity, unit price, customer ID, country, invoice date

## 🛠 Tech Stack

- **Language:** Python 3.10+
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- **Environment:** Jupyter Notebook

## 📁 Folder Structure

```
retail_segmentation/
├── data/
│   ├── generate_data.py        # Reproducible dataset generator
│   └── online_retail.csv       # Generated transaction data
├── notebooks/
│   └── retail_customer_segmentation.ipynb
├── outputs/                     # Charts (PNG) + rfm_segments.csv
├── requirements.txt
└── README.md
```

## 🔬 Pipeline

1. **Data Loading & Cleaning** — Drop missing customer IDs, remove returns, validate prices
2. **EDA** — Monthly revenue trends, top countries, top products by revenue
3. **RFM Feature Engineering** — Calculate Recency, Frequency, Monetary for each customer
4. **K-Means Clustering** — Log-transform skewed features, scale, find optimal k via Elbow + Silhouette
5. **Segment Profiling** — Label segments based on RFM characteristics
6. **Marketing Strategy** — Tactical recommendations per segment

## 📈 Customer Segments Identified

| Segment | Strategy |
|---------|----------|
| 🏆 **Champions** | VIP perks, early access, loyalty rewards, referral asks |
| 💎 **Loyal Customers** | Upsell premium products, personalized recommendations |
| 🌱 **Potential Loyalists** | Welcome series, 2nd-purchase discount, cross-sell |
| ⚠️ **At Risk / Lost** | Win-back campaigns (20–30% off), feedback surveys |

## 🚀 How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# (Optional) Regenerate the dataset
cd data && python generate_data.py && cd ..

# Launch Jupyter
jupyter notebook notebooks/retail_customer_segmentation.ipynb
```

## 💡 Key Insights

- A small group of **Champions** generates a disproportionate share of revenue (Pareto in action).
- **At Risk customers** represent the largest re-engagement opportunity.
- **Q4 shows the strongest seasonal revenue spike** — plan inventory and campaigns accordingly.

## 📝 License

MIT — feel free to use and adapt.
