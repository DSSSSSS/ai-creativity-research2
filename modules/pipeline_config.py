"""
Pipeline configuration - central path management for scoring methods.

Toggle SCORING_METHOD between "wps" and "top" to switch the entire pipeline.
All notebooks should import paths from this module instead of hardcoding.

Usage:
    from pipeline_config import *
    df = pd.read_csv(ORIGINALITY_FILE)
"""

import os
from pathlib import Path

# ============================================================
# Toggle here: "wps" (Word Probability Scoring) or "top" (Top-1)
# ============================================================
SCORING_METHOD = "wps"

# ============================================================
# API settings for originality scoring
# ============================================================
API_URL = "https://openscoring.du.edu/llm"
HEADERS = {
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded",
}
MODEL = "ocsai2"
LANGUAGE = "chi"
TASK = "uses"
ELAB_METHOD = "none"

# LOGPROB_SCORING differs by method
if SCORING_METHOD == "wps":
    LOGPROB_SCORING = "true"
else:
    LOGPROB_SCORING = "false"

# ============================================================
# Repo root (resolved from this file's location)
# ============================================================
REPO_ROOT = Path(__file__).resolve().parent.parent

# ============================================================
# Data directories (method-specific)
# ============================================================
DATA_DIR = REPO_ROOT / "data"

if SCORING_METHOD == "wps":
    SCORING_DIR = DATA_DIR / "analysis" / "scoring"
    PERFORMANCE_DIR = DATA_DIR / "analysis" / "performance"
    POST_CALL_DIR = DATA_DIR / "analysis" / "post_call"
else:
    SCORING_DIR = DATA_DIR / "analysis" / "scoring_top"
    PERFORMANCE_DIR = DATA_DIR / "analysis" / "performance_top"
    POST_CALL_DIR = DATA_DIR / "analysis" / "post_call_top"

# Preprocessed & pickle (shared, not method-specific)
PREPROCESSED_DIR = DATA_DIR / "preprocessed"
PICKLE_DIR = DATA_DIR / "pickle"
AI_FREQ_DIR = DATA_DIR / "analysis" / "ai_freq"
PRE_CALL_DIR = DATA_DIR / "analysis" / "pre_call"

# ============================================================
# Key file paths
# ============================================================
RESPONSES_FILE = PREPROCESSED_DIR / "responses.csv"
ORIGINALITY_FILE = SCORING_DIR / "originality.csv"
PERFORMANCE_FILE = PERFORMANCE_DIR / "performance.csv"
POST_CALL_METRICS_FILE = POST_CALL_DIR / "post_call_metrics.csv"

# Pickle files (shared)
USER_MSGS_FILE = PICKLE_DIR / "user_msgs.pkl"
AI_EVENTS_FILE = PICKLE_DIR / "ai_events.pkl"
TIMELINE_FILE = PICKLE_DIR / "timeline.pkl"

# AI freq & pre-call (not method-specific)
AI_FREQ_FILE = AI_FREQ_DIR / "ai_freq_metrics.csv"
PRE_CALL_FILE = PRE_CALL_DIR / "pre_call_metrics.csv"
PARTICIPANTS_FILE = PICKLE_DIR / "participants.pkl"

# ============================================================
# Reporting output directories (method-specific)
# ============================================================
REPORTING_BASE = REPO_ROOT / "analysis" / "reporting"

if SCORING_METHOD == "wps":
    BY_TRIAL_OUTPUT = REPORTING_BASE / "by_trial" / "output"
    BY_RAW_OUTPUT = REPORTING_BASE / "by_raw" / "output"
else:
    BY_TRIAL_OUTPUT = REPORTING_BASE / "by_trial" / "output_top"
    BY_RAW_OUTPUT = REPORTING_BASE / "by_raw" / "output_top"

# Intermediate CSVs
AI_CALL_FEATURES_FILE = BY_TRIAL_OUTPUT / "ai_call_features_by_trial.csv"
TRIAL_WITH_CLUSTER_FILE = BY_TRIAL_OUTPUT / "trial_with_cluster.csv"
SEMANTIC_STEPS_FILE = BY_TRIAL_OUTPUT / "semantic_steps_by_trial.csv"
CUMULATIVE_SEMANTIC_FILE = BY_TRIAL_OUTPUT / "cumulative_semantic_distance.csv"

# ============================================================
# Print current config on import
# ============================================================
print(f"[pipeline_config] SCORING_METHOD={SCORING_METHOD}, LOGPROB_SCORING={LOGPROB_SCORING}")
print(f"[pipeline_config] SCORING_DIR={SCORING_DIR}")
print(f"[pipeline_config] PERFORMANCE_DIR={PERFORMANCE_DIR}")
print(f"[pipeline_config] BY_TRIAL_OUTPUT={BY_TRIAL_OUTPUT}")
