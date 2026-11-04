# Week 3: Python-Based Machine Learning Model Development and Evaluation Plan

## TelePulse AI — ML Pipeline Engineering, Bayesian Optimization & Cost-Sensitive Evaluation

### Project Overview
This deliverable provides a detailed, end-to-end plan for developing, tuning, validating, and deploying a supervised machine learning model using Python. The project addresses customer churn prediction formulated as an imbalanced binary classification problem, covering every phase from data preprocessing through production serving.

### Deliverable Contents
- **Problem Formulation** — Mathematical binary classification setup with business justification
- **Preprocessing Pipeline** — Scikit-Learn ColumnTransformer with RobustScaler, Yeo-Johnson, OneHotEncoder, TargetEncoder
- **Feature Engineering** — Price velocity, support ticket acceleration, product stickiness index, engagement drop ratio
- **Class Imbalance Handling** — SMOTE-NC resampling inside CV folds + cost-weighted loss functions (scale_pos_weight = 2.77)
- **Model Benchmarking** — Tournament across Logistic Regression, Random Forest, XGBoost, LightGBM (Champion), CatBoost
- **Bayesian Hyperparameter Optimization** — 50-trial Optuna TPE search with MedianPruner early stopping
- **Evaluation Metrics** — PR-AUC (primary), ROC-AUC, Recall, Brier Score, calibration via CalibratedClassifierCV
- **Cost-Benefit Threshold Tuning** — Optimal τ* = 0.38 from financial payoff matrix (TP: +$650, FP: −$35, FN: −$1,200)
- **SHAP Explainability** — TreeSHAP global feature importance and local waterfall attributions
- **Production Deployment Plan** — FastAPI microservice, Docker, MLflow registry, Redis cache, Evidently AI drift monitoring

### Strategic Diagrams (Embedded in Report)
| Figure | Description |
|--------|-------------|
| `figures/w3_fig1_ml_pipeline.png` | End-to-End ML Training Pipeline Architecture |
| `figures/w3_fig2_model_eval.png` | ROC Curves, PR-AUC Curves & Confusion Matrix |
| `figures/w3_fig3_shap_importance.png` | SHAP Global Feature Importance Rankings |
| `figures/w3_fig4_deployment.png` | Production Deployment & Drift Monitoring Pipeline |

### Tools & Technologies
Python 3.13 · Scikit-Learn · LightGBM · XGBoost · CatBoost · Optuna · SHAP · Imbalanced-Learn · MLflow · FastAPI · Docker · Evidently AI
