import pandas as pd
import streamlit as st
from PIL import Image
import os

st.title("Pizza Sales Analysis")
data = pd.read_csv("mega 2 web/pizza_sales_summary.csv")

st.subheader("Data preview")
st.write(data.head(10))

insights = """

**📊 1. Overall Business Performance**
Total Sales Revenue: ₹195.92K

Total Number of Orders: Not shown directly, but visible through charts and bar heights.

**🧭 2. Sales by Category**
Top-Selling Category (Revenue):

Supreme – ₹202.2K (25.46%) (Highest)

Other Categories & Their Contributions:

Classic – ₹193K

Chicken – ₹220K

Veggie – ₹19K (Lowest)

**🍕 3. Pizza-wise Insights**
🛒 Orders Count:
Top Ordered Pizzas:

The Classic Deluxe Pizza – ~2300 orders

The Barbecue Chicken Pizza – ~2250 orders

The Hawaiian Pizza – ~2200 orders

The Pepperoni Pizza – ~2200 orders

The Thai Chicken Pizza – ~2150 orders

All pizzas have similar order counts, indicating balanced popularity.

💵 Sales Revenue:
Top Grossing Pizzas:

The Thai Chicken Pizza – ₹42K+

The Barbecue Chicken Pizza – ₹40K+

The California Chicken Pizza – ₹39K+

Least Grossing Pizza:

The Spicy Italian Pizza – Below ₹35K

**🕒 4. Time of Day Analysis**
Peak Sales Time:

Between 1 PM and 3 PM (13:00–15:00)

Low Activity Times:

After 9 PM (21:00 onward) sees a sharp drop in orders.

Order Flow:

Starts increasing around 11 AM, peaks in early afternoon, drops slightly by 5 PM.

**🌄 5. Orders by Day Timing**
Afternoon:

Most active time of day for orders (>25K orders)

Evening:

Second highest (~18K+ orders)

Night and Morning:

Very low engagement (<5K orders combined)

**📅 6. Day of Week Analysis**
Top Performing Days (Order Volume):

Friday – Highest

Saturday – Second highest

Moderate Days:

Thursday, Wednesday, Tuesday, Monday

Lowest Orders:

Sunday

**📌 7. Behavioral Patterns**
Customers prefer ordering in the Afternoon on Fridays and Saturdays.

Lunch hours (1–3 PM) and weekends are critical for marketing.

Thai Chicken and Barbecue Chicken Pizzas are both revenue and order winners—great candidates for upselling or combos.

Veggie category and Spicy Italian Pizza need promotion or reconsideration.

"""

st.subheader("📜Insights")
st.write(insights)

st.subheader("📊 Power BI Dashboard")

try:
    img = Image.open("mega 2 web/p1 page 1.png")
    st.image(img)
except FileNotFoundError:
    st.warning(" ")
