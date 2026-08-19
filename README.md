# Enterprise Analytics & Agentic AI Pipeline

## Architecture Overview
This project replaces manual spreadsheet reporting with an automated, predictive, and LLM-powered data pipeline. It ingests messy transactional data, validates financials, executes statistical A/B tests, trains a machine learning model to predict revenue, and wraps the output in an autonomous natural language data agent.

### Core Tech Stack
* **Data Engineering:** Python, Pandas, NumPy
* **Statistical Analysis:** SciPy (Welch's T-Test)
* **Machine Learning:** Scikit-Learn (Random Forest Regressor)
* **Agentic AI:** LangChain, Google Gemini 1.5/2.5 API
* **Visualization:** Matplotlib, Seaborn

---

## Phase Execution & Business Outcomes

### 1. Automated Data Engineering & Integrity Audit
* **The Problem:** Manual spreadsheet cleaning does not scale and hides silent financial errors.
* **The System:** Engineered a vectorized Pandas pipeline to parse mixed date formats, calculate operational latency, and mathematically reconstruct unit economics (Revenue, Cost, Margin).
* **The Impact:** Automatically processed 4,200+ rows and deployed a programmatic audit flag, instantly quarantining 62 calculation anomalies before they could corrupt the downstream models.

### 2. Statistical Rigor (A/B Testing)
* **The Problem:** Judging marketing campaigns by surface-level averages leads to capital misallocation.
* **The System:** Executed a Welch's T-Test to evaluate the efficacy of a recent marketing campaign on 30-day user revenue.
* **The Impact:** Calculated a P-value of 0.916, proving the revenue difference was statistical noise. Recommended immediately halting the campaign, preventing further wasted spend.

### 3. Predictive ML Engine (Random Forest)
* **The Problem:** Dashboards only report the past; businesses need to predict the future.
* **The System:** Trained a Random Forest Regressor to predict continuous monthly sales based on operational variables (Footfall, Staffing, Spend, Discounts). 
* **The Impact:** Achieved a high predictive accuracy ($R^2 = 0.753$). Extracted Gini feature importance to prove that Physical Footfall drives 74.67% of revenue, rendering the current discount strategy mathematically irrelevant.

### 4. Agentic AI Intelligence Layer
* **The Problem:** Static dashboards require manual slicing and bottleneck decision-making.
* **The System:** Deployed a self-correcting LangChain Pandas DataFrame Agent powered by Google Gemini. 
* **The Impact:** Stakeholders can query the final operational dataset in natural language. The agent dynamically generates Python code, executes it against the local environment, and returns synthesized statistical answers instantly.
