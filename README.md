# Swiggy-Data-Analysis-using-Python-SQL-and-Power-BI

---

## 📖 Project Summary & Strategic Purpose

In hyper-local food delivery ecosystems like Swiggy, sustained market leadership relies on balancing three main forces: **customer satisfaction (ratings)**, **operational velocity (delivery speed)**, and **vendor pricing strategy (affordability vs. luxury margins)**. Imbalances across these segments—such as logistics delays or hyper-local drops in food quality—directly degrade user trust, increase customer churn, and harm corporate revenue. 

The purpose of this project is to build an end-to-end data intelligence product that transforms raw, unorganized restaurant marketplace data into structured, strategic insights. By looking closely at spatial supply density, pricing structures, menu architectures, and logistics turnaround times, this analysis diagnoses hidden friction points. The final platform enables regional city managers, operations leads, and category heads to make data-driven decisions that minimize delivery SLA breaches, address vendor underperformance, and optimize high-margin premium portfolios to maximize platform Gross Merchandise Value (GMV).

---

## 🛠️ Technologies & Tools Used

*   **Data Ingestion & Engineering:** Python (Pandas, NumPy)
*   **Statistical Analysis & EDA:** Python (Matplotlib, Seaborn)
*   **Relational Database Engine:** SQL (PostgreSQL)
*   **Semantic Data Modeling & BI:** Power BI Desktop (DAX, Power Query)
*   **Stakeholder Delivery:** Microsoft PowerPoint, Report in PDF

---

## ⚙️ Phase-Wise Implementation Flow

### Phase 1: Data Engineering & Exploratory Pipeline (Python)
The initial phase focused on transforming raw, unstructured marketplace listings into a clean, analytically reliable data asset using Python. Automated cleaning scripts were built to handle text normalization, remove duplicate restaurant records, handle missing coordinates, and filter out corrupted data points—such as null fields or ratings falling below a logical 1.0 baseline. This established a trustworthy data foundation, preventing downstream calculation errors in the database and reporting layers.

Once data integrity was ensured, custom feature engineering was applied to embed core business rules into the rows. Continuous delivery time values were bucketed into discrete speed categories (`<=45m: Fast`, `46-60m: Normal`, `>60m: Slow`), ratings were grouped into categorical quality tiers (`rating_band`), and menu workloads were quantified by calculating string-delimited `cuisine_count` attributes. Finally, a multi-conditional logical flag was scripted to automatically isolate high-performing, reasonably priced vendors (`high_value_flag`), turning raw data into functional indicators for business segmentation.

### Phase 2: Relational Database Modeling & Analytical Deep-Dives (SQL)
With the engineered dataset prepared, Phase 2 migrated the data into a production-grade relational database environment. A strict destination schema was defined using explicit structural datatypes and constraints via a standalone initialization script. Centralizing the records into structured tables allowed for persistent, optimized query execution, moving away from local memory limitations and setting up an enterprise-style data warehousing format.

An array of fifteen advanced business intelligence queries was then constructed to stress-test hypotheses regarding platform operations. These scripts utilized complex window functions (`DENSE_RANK()`), conditional case aggregations, and advanced textual data transformations like `UNNEST(STRING_TO_ARRAY)` to split multi-valued cuisine strings into granular categorical arrays. These queries exposed high-risk marketplace nodes—such as the operational cohort suffering from simultaneously slow delivery speeds and dropping rating averages—providing clear vendor target lists for intervention.

### Phase 3: Semantic Data Modeling & Interactive Reporting (Power BI)
Phase 3 involved importing the database schemas into Power BI Desktop to craft an immersive, dashboard-driven business intelligence solution. Relationships were configured to support clean cross-filtering, and a suite of explicit DAX measures was engineered to calculate core platform KPIs (such as overall rating health, distribution percentages, and fast delivery shares). The visual canvas was built using a custom dark layout designed for executive presentation, prioritizing readability and immediate cognitive tracking.

The final visual product spans a 4-page analytical story:
1.  **Executive Overview:** Provides a high-level health check of platform footprint, rating health, and city presence.
2.  **Customer & Quality Analysis:** Deep-dives into how price influences ratings and isolates underperforming vendor regions.
3.  **Pricing & Value Strategy:** Evaluates menu pricing dynamics, identifies high-value outliers, and surfaces top luxury anchors.
4.  **Delivery & Cuisine Insights:** Models the exact threshold where menu complexity begins to delay food preparation and logistics speeds.

---

## 🎯 Conclusion & Strategic Roadmap

This comprehensive analysis successfully bridges technical data engineering with executive business execution. The empirical insights generated from this platform provide clear, high-impact strategies for corporate stakeholders:

*   **Fulfillment Optimization:** Address slow-delivery clusters in **Kolkata and Chennai** by implementing predictive dispatch adjustments and encouraging kitchens with high menu complexity to streamline their delivery-focused menus.
*   **Quality Governance:** Launch localized quality-uplift initiatives in **Mumbai, Pune, and Kolkata** to address their high numbers of low-rated restaurants, protecting the platform's core user trust.
*   **Category Expansion:** Leverage city-wide supply profiles to capture new markets—such as introducing premium dining brands into budget-dense regions like **Surat**.
*   **High-Value Retention:** Promote identified top-tier, affordable local favorites through curated in-app collections to boost repeat order behaviors and increase user engagement.

---
