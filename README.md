# 📉 Subscriber Retention & Predictive Churn Framework

An enterprise-ready predictive analytics framework and machine learning engine optimized for subscription-based business models. This system forecasts customer lifecycle values, pre-emptively flags cancellation risks, and uncovers empirical retention drivers to protect recurring revenue margins.

### 💻 Tech Stack
Python · Pandas · scikit-learn · XGBoost · SHAP · Matplotlib · ReportLab

### 💼 Executive Business Outcomes
* **Proactive Retention Auditing:** Identifies high-risk customer accounts or content assets before churn occurs, enabling growth agencies and account directors to deploy targeted win-back campaigns.
* **Explainable AI Foundations:** Leverages SHAP value equations to isolate exactly which customer behaviors and product variables drive service cancellations, replacing guesswork with statistical certainty.
* **Algorithmic Asset Allocation:** Translates complex model probabilities into clear, non-technical financial playbooks to guide content production budgets and portfolio optimizations.

---

## 🛠️ The Core Deliverable: Content Portfolio Playbook

Standard data science projects deliver standalone, uncontextualized models. **This framework delivers a white-labeled operational playbook.**

By cross-referencing predictive cancellation risks with dual-axis audience engagement signals, the engine maps content assets into five distinct portfolio actions. This allows media agencies to present immediate strategic directives straight to non-technical stakeholders:

*   🏆 **Green-Light:** Top-tier performers with low churn risks and maximum viewer velocity.
*   📈 **Renew Aggressively:** High-risk assets that carry enough engagement scale to justify optimization spend.
*   ⚠️ **Renew Cautiously:** Stable, low-risk properties maintaining a predictable baseline.
*   📉 **Harvest-and-End:** High-risk assets with diminishing engagement—extract remaining residual value.
*   🛑 **Sunset:** Immediate termination candidates failing across risk and volume metrics.

---

## ⚙️ Model Evaluation & Performance Architecture

The predictive modeling layer utilizes an advanced gradient-boosted framework (`XGBoost`), evaluated strictly against a conservative baseline to minimize false positives while capturing systemic retention leaks.

| Model Algorithm | ROC-AUC | Precision | Recall | Classification Role |
| :--- | :---: | :---: | :---: | :--- |
| **Logistic Regression (Baseline)** | 0.847 | 0.37 | 0.81 | Initial feature density benchmarking |
| **XGBoost (Champion Model)** | **0.871** | **0.53** | **0.65** | Production classification engine |

### 🔍 Key Empirical Insights
* **Format Dominates Affinity:** The #1 predictor of early asset cancellation was structural format. Miniseries face exponentially higher churn rates than recurring multi-season structures.
* **The Quality Myth:** Production quality ratings proved statically insignificant, driving an irrelevant **1.8% variance** in overall survival metrics.
* **Volume Assures Survival:** Volume acts as an operational defense signal. Suppressed episode counts and low baseline trend velocity correlate heavily with early cancellation.
* **System Validation Case:** The framework isolated *The Crew* as the highest-risk asset in the testing block with a **96.9% cancellation probability** (accurately forecasting its eventual termination by Netflix).

---

## 📂 Production Directory Topology

```text
├── notebooks/
│   ├── 01_data_exploration.ipynb   # Exploratory Data Analysis & feature variance
│   ├── 02_data_cleaning.ipynb      # Imputation, pipeline parsing, & feature engineering
│   ├── 03_data_analysis.ipynb      # Hypothesis evaluation & visualization generation
│   ├── 04_data_modeling.ipynb      # Logistic Regression baseline vs. XGBoost & SHAP matrices
│   ├── 05_portfolio_analysis.ipynb # Dual-axis segmentations & matrix scoring
│   └── 06_playbook_pdf.ipynb       # ReportLab automated PDF executive compiler
├── data/
│   ├── netflix_shows_complete.csv  # Raw ingestion pulls via custom TMDB API scripts
│   ├── netflix_shows_clean.csv     # Transformed, schema-validated modeling data
│   └── netflix_shows_scored.csv    # Post-inference data containing calculated risk margins
├── visualizations/                 # Standardized, board-ready chart assets
└── content_portfolio_playbook.pdf  # Final white-labeled executive reporting artifact
```

---

## 🚀 Execution & Pipeline Execution

```bash
# Clone and isolate the workspace
git clone https://github.com
cd netflix-cancellation-analysis

# Set up local dependencies
pip install -r requirements.txt
```

### Data Attributions & Case Study
* **Source:** Extracted dynamically via the TMDB API. *This product uses TMDB data but is not endorsed or certified by TMDB.*
* **Full Methodology:** For a comprehensive strategic breakdown of the underlying pipeline architecture and statistical modeling steps, review the formal case study at **[jtambe007.github.io](https://github.io)**.

---

### 🏢 Agency Subcontracting & Custom Deployments
This analytics engine can be retrofitted to run prediction models against your agency's direct subscription datasets (SaaS platforms, e-commerce memberships, digital retainers). To deploy custom churn firewalls or book a data optimization sprint, review our core packages at **[jtambe007.github.io](https://github.io)**.

is allows media agencies to present immediate strategic directives straight to non-technical stakeholders:
