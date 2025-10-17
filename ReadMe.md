# AeroFit Treadmill Customer Profiling Project

## Overview

This project analyzes AeroFit treadmill sales data to uncover how customer characteristics — such as age, income, fitness level, and usage — influence product preferences.  
The goal is to build a customer profile for each treadmill model to help the marketing team make data-driven decisions on sales and targeting.

---

## Dataset

The dataset was obtained from:  
[https://github.com/J-Data-Guy/Aerofit_Project/tree/main](https://github.com/J-Data-Guy/Aerofit_Project/tree/main)

**Column Descriptions:**

| Column | Description |
|--------|--------------|
| **Product** | Product purchased: KP281, KP481, or KP781 |
| **Age** | Customer age in years |
| **Gender** | Male / Female |
| **Education** | Years of education |
| **MaritalStatus** | Single or Partnered |
| **Usage** | Average number of times per week the customer plans to use the treadmill |
| **Fitness** | Self-rated fitness on a 1–5 scale (1 = poor, 5 = excellent) |
| **Income** | Annual income in USD |
| **Miles** | Average number of miles the customer expects to walk/run per week |

**Product Information:**
- **KP281** — Entry-level model, \$1,500  
- **KP481** — Mid-level model, \$1,750  
- **KP781** — Advanced model, \$2,500  

---

## Tech Stack

- **SQL (SQLite)** — Exploratory queries and aggregation  
- **Python (Pandas, Matplotlib, Seaborn)** — Descriptive analytics & visualization  
- **Spyder IDE** — Development environment  

---

## Analysis Steps

### SQL Analysis
- Calculated average **age**, **fitness**, and **income** per product  
- Explored **gender** and **marital status** distribution  

### Python Descriptive Analytics
- Computed averages and visualized distributions (bar, box, and histogram plots)  
- Created **two-way contingency tables** to compute marginal and conditional probabilities  

---

## Insights

- **KP281 (Entry-Level):** Attracts new or casual users with lower income and fitness levels.  
- **KP481 (Mid-Tier):** Appeals to average users, showing balanced demographics.  
- **KP781 (Premium):** Favored by higher-income, more experienced, and primarily male customers.  
- **Income**, **fitness**, and **intended frequency of usage** are the strongest predictors of product preference.  
- **Age** and **marital status** do not significantly influence purchasing behavior.  

---

## Medium Article

A detailed walkthrough of this project — including SQL logic, Python visuals, and business insights — is available on Medium:  
[Customer Profiling with SQL and Python: Understanding Treadmill Buyers](https://medium.com/@bitoskostas1/customer-profiling-with-sql-and-python-understanding-treadmill-buyers-44fd4db1bbc9)

---

## Connect

**Author:** Konstantinos Bitos  
Email: [bitoskostas1@gmail.com](mailto:bitoskostas1@gmail.com)  
Medium: [@bitoskostas1](https://medium.com/@bitoskostas1)
