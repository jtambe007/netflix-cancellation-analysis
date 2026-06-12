# Subscriber Retention & Churn Optimization Framework

A machine learning engine and survival analysis model optimized for subscription business models to forecast customer lifecycle value, predict cancellation risks, and uncover retention opportunities.


### Business Outcomes Addressed:
* **Proactive Retention Strategy:** Identifies high-risk customer segments before they churn, allowing account managers to run targeted win-back campaigns.
* **Feature Importance Analysis:** Utilizes SHAP values to isolate exactly which user behaviors drive service cancellation.


## Stack

Python · Pandas · scikit-learn · XGBoost · SHAP · Matplotlib · ReportLab


## The Deliverable

Most ML projects ship a model. This one ships a playbook.

The output is a one-page Content Portfolio Playbook based on two independent signals (cancellation risk and engagement) that maps every show to one of five portfolio actions: Green-Light, Renew Aggressively, Renew Cautiously, Harvest-and-End, or Sunset.

## Project Structure

notebooks/
├── 01_data_exploration.ipynb     # EDA and feature analysis
├── 02_data_cleaning.ipynb        # Cleaning and feature engineering
├── 03_data_analysis.ipynb        # Hypothesis testing and visualizations
├── 04_data_modeling.ipynb        # Logistic regression, XGBoost, SHAP
├── 05_portfolio_analysis.ipynb   # Risk/engagement segmentation and matrix
└── 06_playbook_pdf.ipynb         # ReportLab one-pager PDF generator

data/
├── netflix_shows_complete.csv    # Raw data from TMDB API
├── netflix_shows_clean.csv       # Cleaned dataset
└── netflix_shows_scored.csv      # Scored with risk and engagement signals

visualizations/                   # All chart outputs
content_portfolio_playbook.pdf    # Final executive deliverable



## Model Performance

| Model | ROC-AUC | Precision | Recall |
|---|---|---|---|
| Logistic Regression (baseline) | 0.847 | 0.37 | 0.81 |
| XGBoost (champion) | **0.871** | **0.53** | **0.65** |

## Key Findings

- The #1 cancellation predictor was format. Miniseries cancel at a far higher rate than scripted shows.
- Quality rating is nearly irrelevant (1.8% difference).
- Volume signals survival: fewer episodes, fewer seasons, lower popularity all correlate strongly with cancellation
- The highest-risk show in the dataset: The Crew (With a 96.9% probability, it was correctly predicted as it was cancelled May 2021)


## Data Source

TMDB API. This project uses TMDB data but is not endorsed or certified by TMDB.

## Case Study

Full write-up at [jtambe007.github.io](https://jtambe007.github.io)
