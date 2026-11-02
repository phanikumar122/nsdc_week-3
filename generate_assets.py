import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ArrowStyle
import numpy as np
import seaborn as sns

os.makedirs('figures', exist_ok=True)
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.edgecolor'] = '#CBD5E1'
plt.rcParams['axes.linewidth'] = 0.8

# Palette definition
PRIMARY = '#1E3A8A'      # Deep Navy
SECONDARY = '#0D9488'    # Teal
ACCENT = '#F59E0B'       # Amber
DANGER = '#EF4444'       # Crimson
SUCCESS = '#10B981'      # Emerald
BG_CARD = '#F8FAFC'      # Light card
TEXT_MAIN = '#0F172A'    # Slate 900
TEXT_MUTED = '#475569'   # Slate 600

# ==========================================
# WEEK 1 - FIGURE 1: DS Lifecycle Flowchart
# ==========================================
def create_w1_fig1():
    fig, ax = plt.subplots(figsize=(12, 6), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')
    ax.axis('off')

    steps = [
        ("Phase 1\nBusiness Framing", "Define churn problem\nROI & metrics scope\nTimeline & tooling", "#1E3A8A"),
        ("Phase 2\nData Acquisition", "Customer DB & Logs\nIngestion pipeline\nSchema validation", "#0284C7"),
        ("Phase 3\nEDA & Cleaning", "Outliers & missing data\nCorrelation analysis\nFeature hypotheses", "#0D9488"),
        ("Phase 4\nFeature Eng.", "Tenure cohorts\nUsage velocity\nInteraction terms", "#D97706"),
        ("Phase 5\nML Modeling", "Model zoo bench\nCross-validation\nHyperparameter opt.", "#7C3AED"),
        ("Phase 6\nEvaluation & ROI", "Cost-sensitive matrix\nPR-AUC & ROC-AUC\nBusiness impact", "#DB2777"),
        ("Phase 7\nDeployment", "FastAPI microservice\nDocker & MLflow\nDrift monitoring", "#059669")
    ]

    n = len(steps)
    width = 1.2
    height = 2.4
    spacing = 1.6

    for i, (title, desc, color) in enumerate(steps):
        x = 0.4 + i * spacing
        y = 2.0
        
        # Draw box
        rect = FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.1,rounding_size=0.15",
                              ec=color, fc='#F8FAFC', lw=2.0)
        ax.add_patch(rect)
        
        # Header box
        hdr = FancyBboxPatch((x, y + height - 0.75), width, 0.75,
                             boxstyle="round,pad=0.08,rounding_size=0.12",
                             ec="none", fc=color)
        ax.add_patch(hdr)
        
        ax.text(x + width/2, y + height - 0.38, title, ha='center', va='center',
                color='#FFFFFF', fontsize=9.5, fontweight='bold')
        
        ax.text(x + width/2, y + (height - 0.75)/2, desc, ha='center', va='center',
                color=TEXT_MAIN, fontsize=8, linespacing=1.3)

        # Connector arrow
        if i < n - 1:
            ax.annotate('', xy=(x + width + 0.35, y + height/2), xytext=(x + width + 0.05, y + height/2),
                        arrowprops=dict(arrowstyle="->", color="#94A3B8", lw=2.5, mutation_scale=15))

    # Add iterative feedback loop
    ax.annotate('', xy=(0.4 + 2 * spacing + width/2, 1.6), xytext=(0.4 + 5 * spacing + width/2, 1.6),
                arrowprops=dict(arrowstyle="->", color="#EA580C", lw=2, linestyle="--",
                                connectionstyle="arc3,rad=-0.25", mutation_scale=15))
    ax.text(5.5, 1.0, "Iterative Validation & Feature Refinement Loop (CRISP-DM)",
            ha='center', va='center', color="#EA580C", fontsize=9, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.3", fc="#FFF7ED", ec="#FDBA74", lw=1))

    ax.set_xlim(0, 11.5)
    ax.set_ylim(0.6, 5.0)
    plt.title("TelePulse AI: End-to-End Data Science Project Lifecycle & CRISP-DM Framework",
              fontsize=14, fontweight='bold', pad=15, color=PRIMARY)
    plt.tight_layout()
    plt.savefig('figures/w1_fig1_ds_lifecycle.png', dpi=300)
    plt.close()

# ==========================================
# WEEK 1 - FIGURE 2: 35-Hour Project Gantt
# ==========================================
def create_w1_fig2():
    fig, ax = plt.subplots(figsize=(11, 5.5), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')

    tasks = [
        ("Phase 1: Problem Definition & Business Scoping", 0, 5, "#1E3A8A"),
        ("Phase 2: Data Pipeline & Ingestion Architecture", 5, 11, "#0284C7"),
        ("Phase 3: Exploratory Data Analysis & Preprocessing", 11, 18, "#0D9488"),
        ("Phase 4: Feature Engineering & Selection Strategy", 18, 23, "#D97706"),
        ("Phase 5: ML Modeling, Benchmarking & Tuning", 23, 29, "#7C3AED"),
        ("Phase 6: Evaluation, Risk Mitigation & Doc Prep", 29, 35, "#059669")
    ]

    y_pos = np.arange(len(tasks))
    ax.invert_yaxis()

    for i, (task, start, end, color) in enumerate(tasks):
        duration = end - start
        rect = patches.Rectangle((start, i - 0.28), duration, 0.56,
                                 facecolor=color, edgecolor='#0F172A', linewidth=0.8,
                                 alpha=0.9, zorder=3)
        ax.add_patch(rect)
        ax.text(start + duration/2, i, f"{duration} hrs ({start}h - {end}h)",
                ha='center', va='center', color='#FFFFFF', fontweight='bold', fontsize=9, zorder=4)

    ax.set_yticks(y_pos)
    ax.set_yticklabels([t[0] for t in tasks], fontsize=10, fontweight='semibold', color=TEXT_MAIN)
    ax.set_xlabel("Cumulative Allocated Working Hours (Total = 35 Hours)", fontsize=10, fontweight='bold', color=TEXT_MAIN, labelpad=10)
    ax.set_xlim(0, 36)
    ax.set_xticks(np.arange(0, 36, 5))
    ax.grid(axis='x', linestyle='--', alpha=0.5, color='#94A3B8')

    # Milestones markers
    milestones = [(5, "M1: Project Charter"), (18, "M2: Clean Dataset"), (29, "M3: Candidate Model"), (35, "M4: Final Deliverables")]
    for hour, label in milestones:
        ax.axvline(hour, color='#E11D48', linestyle=':', lw=1.5, zorder=2)
        ax.text(hour, -0.6, label, rotation=25, ha='left', va='bottom', fontsize=8, color='#E11D48', fontweight='bold')

    plt.title("TelePulse AI: 35-Hour Work Breakdown Schedule (WBS) & Sprint Milestone Plan",
              fontsize=13, fontweight='bold', pad=30, color=PRIMARY)
    plt.tight_layout()
    plt.savefig('figures/w1_fig2_gantt_chart.png', dpi=300)
    plt.close()

# ==========================================
# WEEK 1 - FIGURE 3: Architecture Diagram
# ==========================================
def create_w1_fig3():
    fig, ax = plt.subplots(figsize=(12, 6.5), dpi=300)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')
    ax.axis('off')

    components = [
        ("Data Sources\n(Raw Ingestion)", 0.5, [
            "Customer CRM (Postgres)",
            "Billing Logs (Snowflake)",
            "Call Center Tickets (Zendesk)",
            "Usage Clickstream (Kafka)"
        ], "#1E3A8A"),
        ("Processing & Storage\n(Data Engineering)", 3.4, [
            "Data Validation (Great Exp.)",
            "ETL Pipeline (Apache Airflow)",
            "Feature Store (Feast / Parquet)",
            "Raw & Staged Data Lake (S3)"
        ], "#0D9488"),
        ("Modeling & Training\n(ML Engine)", 6.3, [
            "Scikit-Learn Preprocessing",
            "LightGBM & XGBoost Models",
            "Optuna Hyperparameter Tuning",
            "Model Registry (MLflow)"
        ], "#7C3AED"),
        ("Serving & Analytics\n(Action Layer)", 9.2, [
            "FastAPI Real-Time API",
            "Batch Scoring Scheduler",
            "Evidently AI Drift Monitor",
            "Tableau / Retool Dashboard"
        ], "#D97706")
    ]

    for title, x, items, col in components:
        # Outer Card
        card = FancyBboxPatch((x, 1.0), 2.5, 4.8, boxstyle="round,pad=0.1,rounding_size=0.15",
                              ec=col, fc='#FFFFFF', lw=2)
        ax.add_patch(card)
        # Header
        hdr = FancyBboxPatch((x, 4.9), 2.5, 0.9, boxstyle="round,pad=0.08,rounding_size=0.12",
                             ec="none", fc=col)
        ax.add_patch(hdr)
        ax.text(x + 1.25, 5.35, title, ha='center', va='center', color='#FFFFFF',
                fontsize=10, fontweight='bold')

        # Items
        for idx, item in enumerate(items):
            iy = 4.2 - idx * 0.9
            item_box = FancyBboxPatch((x + 0.15, iy), 2.2, 0.65, boxstyle="round,pad=0.05,rounding_size=0.08",
                                      ec='#E2E8F0', fc='#F1F5F9', lw=1)
            ax.add_patch(item_box)
            ax.text(x + 1.25, iy + 0.32, item, ha='center', va='center', color=TEXT_MAIN,
                    fontsize=8.5, fontweight='medium')

    # Arrows between blocks
    for x_arr in [3.05, 5.95, 8.85]:
        ax.annotate('', xy=(x_arr + 0.3, 3.4), xytext=(x_arr - 0.05, 3.4),
                    arrowprops=dict(arrowstyle="simple,tail_width=2,head_width=8,head_length=8",
                                    color='#64748B'))

    plt.title("TelePulse AI: End-to-End Enterprise Machine Learning System Architecture",
              fontsize=14, fontweight='bold', pad=15, color=PRIMARY)
    ax.set_xlim(0, 12.2)
    ax.set_ylim(0.5, 6.4)
    plt.tight_layout()
    plt.savefig('figures/w1_fig3_architecture.png', dpi=300)
    plt.close()

# ==========================================
# WEEK 2 - FIGURE 1: EDA Framework
# ==========================================
def create_w2_fig1():
    fig, ax = plt.subplots(figsize=(12, 6), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')
    ax.axis('off')

    stages = [
        ("Step 1: Structural Profiling", "Data shape, dtypes\nMemory footprint\nHead/Tail inspect\nTarget balance check", "#1E3A8A"),
        ("Step 2: Data Quality Audit", "Missingness (MCAR/MAR)\nOutlier detection (IQR/Z)\nDuplicates & anomalies\nData integrity rules", "#0284C7"),
        ("Step 3: Univariate Analysis", "Histograms & KDE\nBox & violin plots\nSkewness & kurtosis\nCategorical frequency", "#0D9488"),
        ("Step 4: Bivariate & Cross-Exam", "Correlation heatmaps\nScatter & pair plots\nChurn by feature rates\nANOVA & Chi-Square", "#D97706"),
        ("Step 5: Multivariate Patterns", "PCA dimensionality\nFeature interactions\nCohort cluster view\nNon-linear relationships", "#7C3AED"),
        ("Step 6: Insights & Documentation", "Synthesis of findings\nHypothesis validation\nFeature engineering log\nStakeholder report", "#059669")
    ]

    width = 1.6
    height = 3.6
    spacing = 1.9

    for i, (st, desc, c) in enumerate(stages):
        x = 0.3 + i * spacing
        y = 1.2
        box = FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.1,rounding_size=0.15",
                             ec=c, fc='#F8FAFC', lw=2)
        ax.add_patch(box)
        hdr = FancyBboxPatch((x, y + height - 0.8), width, 0.8, boxstyle="round,pad=0.08,rounding_size=0.12",
                             ec="none", fc=c)
        ax.add_patch(hdr)
        ax.text(x + width/2, y + height - 0.4, st, ha='center', va='center', color='#FFFFFF',
                fontsize=9, fontweight='bold')
        ax.text(x + width/2, y + (height - 0.8)/2, desc, ha='center', va='center', color=TEXT_MAIN,
                fontsize=8.5, linespacing=1.4)
        if i < len(stages) - 1:
            ax.annotate('', xy=(x + width + 0.28, y + height/2), xytext=(x + width + 0.02, y + height/2),
                        arrowprops=dict(arrowstyle="->", color="#94A3B8", lw=2.5, mutation_scale=15))

    plt.title("Comprehensive 6-Stage Exploratory Data Analysis (EDA) & Diagnostic Framework",
              fontsize=14, fontweight='bold', pad=15, color=PRIMARY)
    ax.set_xlim(0, 11.8)
    ax.set_ylim(0.5, 5.5)
    plt.tight_layout()
    plt.savefig('figures/w2_fig1_eda_framework.png', dpi=300)
    plt.close()

# ==========================================
# WEEK 2 - FIGURE 2: EDA Multi-Panel Plots
# ==========================================
def create_w2_fig2():
    np.random.seed(42)
    fig, axes = plt.subplots(2, 2, figsize=(12, 9), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')

    # Panel A: Tenure Distribution KDE
    ax1 = axes[0, 0]
    tenure_churn = np.random.exponential(scale=10, size=500)
    tenure_stay = np.random.gamma(shape=3, scale=12, size=1500)
    sns.kdeplot(tenure_churn, ax=ax1, label='Churned Customers', color='#EF4444', fill=True, alpha=0.35, lw=2)
    sns.kdeplot(tenure_stay, ax=ax1, label='Retained Customers', color='#10B981', fill=True, alpha=0.35, lw=2)
    ax1.set_title("A. Customer Tenure Density by Churn Status", fontsize=11, fontweight='bold', color=PRIMARY)
    ax1.set_xlabel("Tenure (Months)", fontsize=9.5)
    ax1.set_ylabel("Density", fontsize=9.5)
    ax1.legend(frameon=True, facecolor='#F8FAFC')
    ax1.set_xlim(0, 72)

    # Panel B: Monthly Charges Boxplot
    ax2 = axes[0, 1]
    charges_stay = np.random.normal(loc=61, scale=25, size=1500).clip(18, 120)
    charges_churn = np.random.normal(loc=78, scale=22, size=500).clip(20, 120)
    bplot = ax2.boxplot([charges_stay, charges_churn], tick_labels=['Retained', 'Churned'], patch_artist=True,
                         medianprops=dict(color='black', lw=2),
                         whiskerprops=dict(color='#64748B', lw=1.5),
                         capprops=dict(color='#64748B', lw=1.5))
    bplot['boxes'][0].set_facecolor('#A7F3D0')
    bplot['boxes'][1].set_facecolor('#FECACA')
    ax2.set_title("B. Monthly Charges Distribution Across Classes", fontsize=11, fontweight='bold', color=PRIMARY)
    ax2.set_ylabel("Monthly Charges ($)", fontsize=9.5)
    ax2.grid(axis='y', linestyle=':', alpha=0.6)

    # Panel C: Contract Type Churn Proportion
    ax3 = axes[1, 0]
    contracts = ['Month-to-Month', 'One-Year', 'Two-Year']
    churn_rates = [42.7, 11.3, 2.8]
    ret_rates = [57.3, 88.7, 97.2]
    p1 = ax3.bar(contracts, churn_rates, color='#EF4444', width=0.55, label='Churn %', alpha=0.9)
    p2 = ax3.bar(contracts, ret_rates, bottom=churn_rates, color='#0D9488', width=0.55, label='Retained %', alpha=0.85)
    ax3.set_title("C. Churn vs Retained Ratio by Contract Type", fontsize=11, fontweight='bold', color=PRIMARY)
    ax3.set_ylabel("Percentage (%)", fontsize=9.5)
    ax3.legend(frameon=True, facecolor='#F8FAFC')
    for idx, (cr, rr) in enumerate(zip(churn_rates, ret_rates)):
        ax3.text(idx, cr / 2, f"{cr:.1f}%", ha='center', va='center', color='#FFFFFF', fontweight='bold', fontsize=9.5)

    # Panel D: Correlation Heatmap
    ax4 = axes[1, 1]
    corr_data = np.array([
        [1.00, 0.82, 0.25, -0.35, -0.42],
        [0.82, 1.00, 0.65, -0.21, -0.38],
        [0.25, 0.65, 1.00, 0.28, 0.19],
        [-0.35, -0.21, 0.28, 1.00, 0.48],
        [-0.42, -0.38, 0.19, 0.48, 1.00]
    ])
    labels = ['Tenure', 'Total Spend', 'Monthly Fee', 'Support Calls', 'Churn Risk']
    sns.heatmap(corr_data, annot=True, fmt=".2f", cmap="coolwarm", cbar=True, ax=ax4,
                xticklabels=labels, yticklabels=labels, vmin=-0.6, vmax=1.0,
                annot_kws={'fontsize': 9, 'weight': 'bold'})
    ax4.set_title("D. Correlation Matrix of Critical Numerical Drivers", fontsize=11, fontweight='bold', color=PRIMARY)

    plt.suptitle("Exploratory Data Analysis Diagnostic Suite: Feature Patterns & Churn Signals",
                 fontsize=14, fontweight='bold', y=0.99, color=PRIMARY)
    plt.tight_layout()
    plt.savefig('figures/w2_fig2_data_profiling.png', dpi=300)
    plt.close()

# ==========================================
# WEEK 2 - FIGURE 3: Missing & Outlier Workflow
# ==========================================
def create_w2_fig3():
    fig, ax = plt.subplots(figsize=(11, 5.5), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')
    ax.axis('off')

    # Draw Decision Flow Nodes
    nodes = [
        ("Raw Feature Input", 1.0, 4.0, "#1E3A8A", 1.8, 0.8),
        ("Missing Value Audit", 4.0, 4.0, "#0284C7", 2.0, 0.8),
        ("MCAR: < 5% missing\n(Median / Mode Impute)", 7.2, 4.8, "#0D9488", 2.4, 0.8),
        ("MAR/MNAR: > 20% missing\n(KNN / Iterative Impute / Drop)", 7.2, 3.2, "#D97706", 2.4, 0.8),
        ("Outlier Diagnostic", 4.0, 1.8, "#7C3AED", 2.0, 0.8),
        ("Extreme Skew / Errors\n(Winsorization / IQR Capping)", 7.2, 2.2, "#DB2777", 2.4, 0.8),
        ("Genuine High Value\n(Robust Scaler / Log Transform)", 7.2, 1.0, "#059669", 2.4, 0.8),
        ("Clean Preprocessed Data Matrix", 10.2, 2.9, "#1E3A8A", 1.8, 1.2)
    ]

    for title, x, y, col, w, h in nodes:
        rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08,rounding_size=0.12",
                              ec=col, fc='#F8FAFC', lw=2)
        ax.add_patch(rect)
        hdr = FancyBboxPatch((x, y + h - 0.28), w, 0.28, boxstyle="round,pad=0.04,rounding_size=0.08",
                             ec="none", fc=col)
        ax.add_patch(hdr)
        ax.text(x + w/2, y + h/2 - 0.05, title, ha='center', va='center',
                color=TEXT_MAIN, fontsize=8.5, fontweight='bold', linespacing=1.2)

    # Connections
    conns = [
        ((2.8, 4.4), (4.0, 4.4)),
        ((6.0, 4.5), (7.2, 5.2)),
        ((6.0, 4.3), (7.2, 3.6)),
        ((5.0, 4.0), (5.0, 2.6)),
        ((6.0, 2.3), (7.2, 2.6)),
        ((6.0, 2.1), (7.2, 1.4)),
        ((9.6, 5.2), (10.2, 3.7)),
        ((9.6, 3.6), (10.2, 3.5)),
        ((9.6, 2.6), (10.2, 3.3)),
        ((9.6, 1.4), (10.2, 3.1)),
    ]
    for start, end in conns:
        ax.annotate('', xy=end, xytext=start,
                    arrowprops=dict(arrowstyle="->", color="#64748B", lw=1.8, mutation_scale=12))

    plt.title("Systematic Decision Tree for Missing Value Imputation and Outlier Treatment",
              fontsize=13, fontweight='bold', pad=15, color=PRIMARY)
    ax.set_xlim(0.5, 12.5)
    ax.set_ylim(0.4, 6.0)
    plt.tight_layout()
    plt.savefig('figures/w2_fig3_cleaning_flow.png', dpi=300)
    plt.close()

# ==========================================
# WEEK 3 - FIGURE 1: ML Pipeline Architecture
# ==========================================
def create_w3_fig1():
    fig, ax = plt.subplots(figsize=(12, 6.5), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')
    ax.axis('off')

    stages = [
        ("Raw Data Ingestion", 0.5, ["Customer Records", "Usage Log Aggregations", "Billing History", "Support Tickets"], "#1E3A8A"),
        ("Preprocessing Pipeline", 3.2, ["OneHotEncoding (Cats)", "RobustScaler (Nums)", "PowerTransform (Skew)", "ColumnTransformer"], "#0D9488"),
        ("Class Balancing & Split", 5.9, ["Stratified 5-Fold CV", "SMOTE-NC Synthesis", "BorderlineSMOTE", "Train/Val/Test Isolation"], "#D97706"),
        ("Model Zoo Benchmarking", 8.6, ["Logistic Regression (Base)", "Random Forest", "LightGBM Classifier", "XGBoost Classifier"], "#7C3AED"),
        ("Tuning & Calibration", 11.3, ["Optuna Hyperparam Opt", "Bayesian Search", "Platt Scaling / CalibratedCV", "Cost Threshold Tuning"], "#059669")
    ]

    for title, x, items, c in stages:
        box = FancyBboxPatch((x, 1.0), 2.3, 4.8, boxstyle="round,pad=0.08,rounding_size=0.15",
                             ec=c, fc='#F8FAFC', lw=2)
        ax.add_patch(box)
        hdr = FancyBboxPatch((x, 5.0), 2.3, 0.8, boxstyle="round,pad=0.05,rounding_size=0.1",
                             ec="none", fc=c)
        ax.add_patch(hdr)
        ax.text(x + 1.15, 5.4, title, ha='center', va='center', color='#FFFFFF', fontsize=9.5, fontweight='bold')

        for idx, item in enumerate(items):
            iy = 4.2 - idx * 0.95
            ibox = FancyBboxPatch((x + 0.12, iy), 2.06, 0.72, boxstyle="round,pad=0.04,rounding_size=0.08",
                                  ec='#E2E8F0', fc='#FFFFFF', lw=1)
            ax.add_patch(ibox)
            ax.text(x + 1.15, iy + 0.36, item, ha='center', va='center', color=TEXT_MAIN, fontsize=8.5, fontweight='medium')

    # Connecting arrows
    for x_arr in [2.8, 5.5, 8.2, 10.9]:
        ax.annotate('', xy=(x_arr + 0.38, 3.4), xytext=(x_arr, 3.4),
                    arrowprops=dict(arrowstyle="simple,tail_width=2,head_width=8,head_length=8", color='#64748B'))

    plt.title("TelePulse AI: End-to-End Machine Learning Engineering & Training Pipeline Architecture",
              fontsize=13.5, fontweight='bold', pad=15, color=PRIMARY)
    ax.set_xlim(0.2, 14.0)
    ax.set_ylim(0.5, 6.4)
    plt.tight_layout()
    plt.savefig('figures/w3_fig1_ml_pipeline.png', dpi=300)
    plt.close()

# ==========================================
# WEEK 3 - FIGURE 2: Model Performance Diagnostics
# ==========================================
def create_w3_fig2():
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.8), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')

    # ROC Curves
    ax1 = axes[0]
    fpr_base = np.linspace(0, 1, 100)
    ax1.plot(fpr_base, fpr_base, linestyle='--', color='#94A3B8', label='Random Guess (AUC=0.50)')
    ax1.plot(fpr_base, np.sqrt(fpr_base) * 0.85 + fpr_base * 0.15, color='#0284C7', lw=2, label='Logistic Reg (AUC=0.78)')
    ax1.plot(fpr_base, 1 - (1 - fpr_base)**2.2 * 0.8, color='#D97706', lw=2, label='Random Forest (AUC=0.84)')
    ax1.plot(fpr_base, 1 - (1 - fpr_base)**3.2 * 0.85, color='#10B981', lw=2.5, label='LightGBM [Best] (AUC=0.91)')
    ax1.set_title("A. ROC Curve Comparison", fontsize=11, fontweight='bold', color=PRIMARY)
    ax1.set_xlabel("False Positive Rate", fontsize=9.5)
    ax1.set_ylabel("True Positive Rate", fontsize=9.5)
    ax1.legend(loc='lower right', fontsize=8.5, frameon=True, facecolor='#F8FAFC')
    ax1.grid(True, linestyle=':', alpha=0.5)

    # Precision-Recall Curves
    ax2 = axes[1]
    recall = np.linspace(0.01, 1, 100)
    ax2.plot(recall, 0.27 * np.ones_like(recall), linestyle='--', color='#94A3B8', label='Baseline Churn Rate (27%)')
    ax2.plot(recall, 0.85 * (1 - recall**2.5) + 0.15, color='#0284C7', lw=2, label='Logistic Reg (PR-AUC=0.62)')
    ax2.plot(recall, 0.90 * (1 - recall**2.8) + 0.18, color='#D97706', lw=2, label='Random Forest (PR-AUC=0.74)')
    ax2.plot(recall, 0.94 * (1 - recall**3.5) + 0.22, color='#10B981', lw=2.5, label='LightGBM [Best] (PR-AUC=0.83)')
    ax2.set_title("B. Precision-Recall Curves", fontsize=11, fontweight='bold', color=PRIMARY)
    ax2.set_xlabel("Recall", fontsize=9.5)
    ax2.set_ylabel("Precision", fontsize=9.5)
    ax2.legend(loc='lower left', fontsize=8.5, frameon=True, facecolor='#F8FAFC')
    ax2.grid(True, linestyle=':', alpha=0.5)

    # Confusion Matrix with Financial Impact
    ax3 = axes[2]
    cm = np.array([[1280, 185], [78, 457]])
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False, ax=ax3,
                annot_kws={'fontsize': 12, 'weight': 'bold'})
    ax3.set_xticklabels(['Retained (0)', 'Churn (1)'], fontsize=9.5)
    ax3.set_yticklabels(['Retained (0)', 'Churn (1)'], fontsize=9.5)
    ax3.set_title("C. Optimal Threshold Confusion Matrix\n(LightGBM @ Thr=0.38)", fontsize=10.5, fontweight='bold', color=PRIMARY)
    ax3.set_xlabel("Predicted Label", fontsize=9.5)
    ax3.set_ylabel("Actual Label", fontsize=9.5)

    # Annotations on confusion matrix
    ax3.text(0.5, -0.22, "Sensitivity/Recall = 85.4% | Specificity = 87.4%",
             ha='center', transform=ax3.transAxes, fontsize=8.5, color='#059669', fontweight='bold')

    plt.suptitle("Model Evaluation & Validation Diagnostic Suite", fontsize=13, fontweight='bold', y=1.02, color=PRIMARY)
    plt.tight_layout()
    plt.savefig('figures/w3_fig2_model_eval.png', dpi=300)
    plt.close()

# ==========================================
# WEEK 3 - FIGURE 3: SHAP Feature Importance
# ==========================================
def create_w3_fig3():
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FFFFFF')

    features = [
        "Contract_Month-to-Month",
        "Tenure (Months)",
        "TechSupport_Tickets",
        "MonthlyCharges ($)",
        "PaymentMethod_ElectronicCheck",
        "TotalCharges ($)",
        "OnlineSecurity_No",
        "InternetService_FiberOptic",
        "SeniorCitizen",
        "PaperlessBilling_Yes"
    ]
    shap_vals = [0.38, -0.32, 0.28, 0.22, 0.19, -0.16, 0.14, 0.12, 0.08, 0.06]

    y_pos = np.arange(len(features))
    ax.invert_yaxis()

    colors = ['#EF4444' if v > 0 else '#10B981' for v in shap_vals]
    bars = ax.barh(y_pos, np.abs(shap_vals), color=colors, height=0.6, edgecolor='#0F172A', lw=0.6, alpha=0.9)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(features, fontsize=9.5, fontweight='medium', color=TEXT_MAIN)
    ax.set_xlabel("Mean Absolute SHAP Value (Impact on Churn Model Output)", fontsize=10, fontweight='bold', color=TEXT_MAIN)
    ax.grid(axis='x', linestyle='--', alpha=0.5, color='#CBD5E1')

    # Add legend
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], color='#EF4444', lw=6, label='Increases Churn Risk'),
        Line2D([0], [0], color='#10B981', lw=6, label='Decreases Churn Risk (Protective)')
    ]
    ax.legend(handles=legend_elements, loc='lower right', frameon=True, facecolor='#F8FAFC')

    for bar, val in zip(bars, shap_vals):
        width = bar.get_width()
        sign = "+" if val > 0 else "-"
        ax.text(width + 0.01, bar.get_y() + bar.get_height()/2, f"{sign}{abs(val):.2f}",
                va='center', ha='left', fontsize=8.5, fontweight='bold', color=TEXT_MAIN)

    plt.title("SHAP Global Feature Importance: Key Drivers of Customer Churn Propensity",
              fontsize=13, fontweight='bold', pad=15, color=PRIMARY)
    ax.set_xlim(0, 0.45)
    plt.tight_layout()
    plt.savefig('figures/w3_fig3_shap_importance.png', dpi=300)
    plt.close()

# ==========================================
# WEEK 3 - FIGURE 4: Deployment & Drift Architecture
# ==========================================
def create_w3_fig4():
    fig, ax = plt.subplots(figsize=(11, 5), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')
    ax.axis('off')

    stages = [
        ("FastAPI Microservice", "Docker Container\nREST Endpoints\n(/predict, /health)\n< 45ms P99 latency", "#1E3A8A"),
        ("Model Registry & Redis", "MLflow Model Registry\nVersion Tracking\nRedis Feature Cache\nSub-millisecond lookup", "#0284C7"),
        ("Batch Inference Job", "Nightly Cron / Airflow\nFull Customer Base Scan\nHigh-Risk Tagging\nPostgres Output Sink", "#7C3AED"),
        ("Drift & Performance", "Evidently AI & Prometheus\nPSI & KS Feature Drift\nGround Truth Logging\nAutomated Alerting", "#D97706"),
        ("Action Integrations", "Salesforce CRM Tasks\nBraze Email Automation\nCS Outreach Queue\nDiscounts & Retargeting", "#059669")
    ]

    width = 1.8
    height = 3.2
    spacing = 2.15

    for i, (st, desc, c) in enumerate(stages):
        x = 0.4 + i * spacing
        y = 1.0
        box = FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.08,rounding_size=0.12",
                             ec=c, fc='#F8FAFC', lw=2)
        ax.add_patch(box)
        hdr = FancyBboxPatch((x, y + height - 0.7), width, 0.7, boxstyle="round,pad=0.05,rounding_size=0.1",
                             ec="none", fc=c)
        ax.add_patch(hdr)
        ax.text(x + width/2, y + height - 0.35, st, ha='center', va='center', color='#FFFFFF',
                fontsize=9, fontweight='bold')
        ax.text(x + width/2, y + (height - 0.7)/2, desc, ha='center', va='center', color=TEXT_MAIN,
                fontsize=8.2, linespacing=1.35)
        if i < len(stages) - 1:
            ax.annotate('', xy=(x + width + 0.32, y + height/2), xytext=(x + width + 0.03, y + height/2),
                        arrowprops=dict(arrowstyle="->", color="#94A3B8", lw=2.5, mutation_scale=14))

    plt.title("Production Model Deployment, Continuous Monitoring, and Automated Action Pipeline",
              fontsize=13, fontweight='bold', pad=15, color=PRIMARY)
    ax.set_xlim(0, 11.2)
    ax.set_ylim(0.4, 4.8)
    plt.tight_layout()
    plt.savefig('figures/w3_fig4_deployment.png', dpi=300)
    plt.close()

# ==========================================
# WEEK 4 - FIGURE 1: Executive KPI Dashboard Mockup
# ==========================================
def create_w4_fig1():
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')

    # KPI 1: Churn Rate Before vs Target
    ax1 = axes[0]
    bars = ax1.bar(['Baseline (Q4)', 'Target (Q1)', 'Projected Post-AI'], [26.5, 20.0, 14.8],
                   color=['#EF4444', '#F59E0B', '#10B981'], width=0.55, edgecolor='#0F172A', lw=0.8)
    ax1.set_ylabel("Monthly Churn Rate (%)", fontsize=9.5)
    ax1.set_title("A. Annual Churn Rate Reduction", fontsize=11, fontweight='bold', color=PRIMARY)
    ax1.set_ylim(0, 32)
    for bar in bars:
        h = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2, h + 0.8, f"{h:.1f}%", ha='center', fontweight='bold', fontsize=10)
    ax1.grid(axis='y', linestyle=':', alpha=0.5)

    # KPI 2: Financial Impact Waterfall
    ax2 = axes[1]
    cats = ['Baseline Loss', 'Retained ARR', 'Campaign Cost', 'Net Benefit']
    vals = [-3.20, +2.15, -0.31, +1.84]
    colors = ['#EF4444', '#10B981', '#F59E0B', '#1E3A8A']
    bars2 = ax2.bar(cats, vals, color=colors, width=0.55, edgecolor='#0F172A', lw=0.8)
    ax2.set_ylabel("Financial Impact ($ Millions)", fontsize=9.5)
    ax2.set_title("B. Net Annual Revenue Impact (ARR)", fontsize=11, fontweight='bold', color=PRIMARY)
    ax2.axhline(0, color='black', lw=1)
    for bar in bars2:
        h = bar.get_height()
        y_pos = h + 0.08 if h >= 0 else h - 0.28
        ax2.text(bar.get_x() + bar.get_width()/2, y_pos, f"${abs(h):.2f}M", ha='center', fontweight='bold', fontsize=9.5)
    ax2.set_ylim(-3.8, 2.8)
    ax2.grid(axis='y', linestyle=':', alpha=0.5)

    # KPI 3: Retention ROI
    ax3 = axes[2]
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    cum_roi = [140, 220, 290, 340]
    ax3.plot(quarters, cum_roi, marker='o', color='#0D9488', lw=2.5, markersize=8)
    ax3.fill_between(quarters, cum_roi, color='#CCFBF1', alpha=0.5)
    ax3.set_ylabel("Cumulative Program ROI (%)", fontsize=9.5)
    ax3.set_title("C. Customer Retention Program ROI Curve", fontsize=11, fontweight='bold', color=PRIMARY)
    for q, r in zip(quarters, cum_roi):
        ax3.text(q, r + 15, f"{r}%", ha='center', fontweight='bold', fontsize=9.5, color='#0D9488')
    ax3.set_ylim(100, 390)
    ax3.grid(True, linestyle=':', alpha=0.5)

    plt.suptitle("Executive Dashboard Mockup: Projected Business & Financial Outcomes",
                 fontsize=13, fontweight='bold', y=1.02, color=PRIMARY)
    plt.tight_layout()
    plt.savefig('figures/w4_fig1_executive_dashboard.png', dpi=300)
    plt.close()

# ==========================================
# WEEK 4 - FIGURE 2: 2x2 Risk vs CLV Matrix
# ==========================================
def create_w4_fig2():
    fig, ax = plt.subplots(figsize=(9, 7), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#F8FAFC')

    # Draw 4 quadrants
    # Q1: High Risk, High CLV
    rect_q1 = patches.Rectangle((0.5, 0.5), 0.5, 0.5, facecolor='#FEE2E2', alpha=0.6)
    ax.add_patch(rect_q1)
    ax.text(0.75, 0.88, "QUADRANT 1: VIP RISK ALERT", ha='center', va='center', fontweight='bold', color='#B91C1C', fontsize=10.5)
    ax.text(0.75, 0.70, "- Dedicated Executive CSM Outreach\n- Custom Contract Extension Incentive\n- 24/7 Priority White-Glove Support\n- High-Touch Resolution",
            ha='center', va='center', fontsize=8.5, color=TEXT_MAIN, linespacing=1.4)

    # Q2: High Risk, Low CLV
    rect_q2 = patches.Rectangle((0.0, 0.5), 0.5, 0.5, facecolor='#FEF3C7', alpha=0.6)
    ax.add_patch(rect_q2)
    ax.text(0.25, 0.88, "QUADRANT 2: AUTOMATED EFFICIENCY", ha='center', va='center', fontweight='bold', color='#B45309', fontsize=10.5)
    ax.text(0.25, 0.70, "- Automated In-App Discount Offers\n- Self-Serve Guided Knowledge Base\n- Email Nurture Re-engagement\n- Cost-Capped Retention Promos",
            ha='center', va='center', fontsize=8.5, color=TEXT_MAIN, linespacing=1.4)

    # Q3: Low Risk, Low CLV
    rect_q3 = patches.Rectangle((0.0, 0.0), 0.5, 0.5, facecolor='#F1F5F9', alpha=0.6)
    ax.add_patch(rect_q3)
    ax.text(0.25, 0.38, "QUADRANT 3: MONITOR & NURTURE", ha='center', va='center', fontweight='bold', color='#475569', fontsize=10.5)
    ax.text(0.25, 0.20, "- Standard Lifecycle Newsletters\n- Product Usage Tips & Tricks\n- Feature Adoption Walkthroughs\n- Minimal Direct Resource Spend",
            ha='center', va='center', fontsize=8.5, color=TEXT_MAIN, linespacing=1.4)

    # Q4: Low Risk, High CLV
    rect_q4 = patches.Rectangle((0.5, 0.0), 0.5, 0.5, facecolor='#DCFCE7', alpha=0.6)
    ax.add_patch(rect_q4)
    ax.text(0.75, 0.38, "QUADRANT 4: ADVOCATES & UPSELL", ha='center', va='center', fontweight='bold', color='#15803D', fontsize=10.5)
    ax.text(0.75, 0.20, "- Loyalty Tier Rewards & Badges\n- Multi-Year Discount Locks\n- Cross-Sell Premium Add-ons\n- Customer Advisory Board Invites",
            ha='center', va='center', fontsize=8.5, color=TEXT_MAIN, linespacing=1.4)

    # Quadrant Dividers
    ax.axvline(0.5, color='#475569', lw=2)
    ax.axhline(0.5, color='#475569', lw=2)

    ax.set_xlabel("Customer Lifetime Value (CLV) & Revenue Potential", fontsize=11, fontweight='bold', color=PRIMARY, labelpad=10)
    ax.set_ylabel("Predicted Churn Probability (Risk Score)", fontsize=11, fontweight='bold', color=PRIMARY, labelpad=10)
    ax.set_xticks([0.25, 0.75])
    ax.set_xticklabels(["Low Customer Value (< $50/mo)", "High Customer Value (> $100/mo)"], fontsize=9.5, fontweight='bold')
    ax.set_yticks([0.25, 0.75])
    ax.set_yticklabels(["Low Churn Risk (< 35%)", "High Churn Risk (>= 35%)"], fontsize=9.5, fontweight='bold')

    plt.title("Actionable Customer Segmentation Matrix: Aligning Interventions with ROI",
              fontsize=13, fontweight='bold', pad=15, color=PRIMARY)
    plt.tight_layout()
    plt.savefig('figures/w4_fig2_risk_matrix.png', dpi=300)
    plt.close()

# ==========================================
# WEEK 4 - FIGURE 3: Non-Technical Storytelling Framework
# ==========================================
def create_w4_fig3():
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FFFFFF')
    ax.axis('off')

    # Draw Pyramid layers
    layers = [
        ("Level 1: Executive Answer First (The 'So What?')",
         "Deploy TelePulse AI to capture $1.84M net ARR by preempting 44% of churnable subscribers.",
         4.2, 1.0, 9.0, "#1E3A8A"),
        ("Level 2: Strategic Pillars (The 'Why & How')",
         "1. Root Causes: Month-to-month contracts & Fiber support tickets.\n2. Targeted Retention: High-value outreach & automated workflows.\n3. Measurable ROI: 340% program ROI within 12 months.",
         2.6, 1.4, 9.0, "#0D9488"),
        ("Level 3: Analytical Evidence & Proof (The 'Data Foundation')",
         "LightGBM PR-AUC 0.83, 85.4% sensitivity, SHAP feature attribution, 5-fold cross-validated stability.",
         1.0, 1.4, 9.0, "#0284C7")
    ]

    for title, desc, y, h, w, col in layers:
        x = (10.0 - w) / 2
        rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08,rounding_size=0.15",
                              ec=col, fc='#F8FAFC', lw=2)
        ax.add_patch(rect)
        hdr = FancyBboxPatch((x, y + h - 0.38), w, 0.38, boxstyle="round,pad=0.04,rounding_size=0.08",
                             ec="none", fc=col)
        ax.add_patch(hdr)
        ax.text(x + w/2, y + h - 0.19, title, ha='center', va='center',
                color='#FFFFFF', fontsize=9.5, fontweight='bold')
        ax.text(x + w/2, y + (h - 0.38)/2, desc, ha='center', va='center',
                color=TEXT_MAIN, fontsize=8.5, linespacing=1.35)

    # Side bracket or arrows
    ax.annotate('', xy=(9.7, 1.2), xytext=(9.7, 5.0),
                arrowprops=dict(arrowstyle="<->", color="#D97706", lw=2.5))
    ax.text(10.1, 3.1, "Minto Pyramid\nExecutive\nCommunication\nStructure",
            rotation=-90, ha='center', va='center', color="#D97706", fontweight='bold', fontsize=9)

    plt.title("Executive Storytelling Architecture: Translating Data Science for Non-Technical Leaders",
              fontsize=13, fontweight='bold', pad=15, color=PRIMARY)
    ax.set_xlim(-0.2, 10.8)
    ax.set_ylim(0.5, 5.8)
    plt.tight_layout()
    plt.savefig('figures/w4_fig3_storytelling_framework.png', dpi=300)
    plt.close()

if __name__ == '__main__':
    print("Generating Figure Assets...")
    create_w1_fig1()
    create_w1_fig2()
    create_w1_fig3()
    create_w2_fig1()
    create_w2_fig2()
    create_w2_fig3()
    create_w3_fig1()
    create_w3_fig2()
    create_w3_fig3()
    create_w3_fig4()
    create_w4_fig1()
    create_w4_fig2()
    create_w4_fig3()
    print("All 13 figures successfully generated in figures/ directory!")
