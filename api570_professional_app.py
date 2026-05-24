import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import json

# ============================================================================
# PAGE CONFIGURATION - ENTERPRISE PREMIUM
# ============================================================================

st.set_page_config(
    page_title="Pipeline Integrity System | Enterprise Edition",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# ULTRA-PREMIUM ENTERPRISE STYLING
# ============================================================================

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500;600&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    html, body, [class*="css"] {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0f1425 100%);
        color: #e8eaf6;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0f1425 100%);
    }
    
    /* ===== ENTERPRISE HEADER ===== */
    .enterprise-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 25%, #1a472a 50%, #0f2027 100%);
        padding: 3.5rem 3rem;
        border-radius: 24px;
        margin-bottom: 3rem;
        box-shadow: 
            0 25px 50px -12px rgba(0, 0, 0, 0.5),
            inset 0 1px 0 rgba(255, 255, 255, 0.1),
            0 0 60px rgba(66, 165, 245, 0.15);
        border: 1px solid rgba(66, 165, 245, 0.25);
        backdrop-filter: blur(20px);
        position: relative;
        overflow: hidden;
    }
    
    .enterprise-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: 
            radial-gradient(circle at 20% 50%, rgba(66, 165, 245, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 80%, rgba(34, 197, 94, 0.05) 0%, transparent 50%);
        pointer-events: none;
    }
    
    .enterprise-header h1 {
        color: #ffffff;
        font-size: 3.2rem;
        font-weight: 800;
        margin: 0;
        text-shadow: 0 2px 20px rgba(0, 0, 0, 0.4);
        letter-spacing: -1px;
        position: relative;
        z-index: 1;
        background: linear-gradient(135deg, #ffffff 0%, #a8d8ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .enterprise-header .subtitle {
        color: rgba(255, 255, 255, 0.85);
        font-size: 1.15rem;
        margin: 0.8rem 0 0 0;
        font-weight: 400;
        letter-spacing: 0.3px;
        position: relative;
        z-index: 1;
    }
    
    .enterprise-header .metadata {
        display: flex;
        gap: 3rem;
        margin-top: 2rem;
        position: relative;
        z-index: 1;
        flex-wrap: wrap;
    }
    
    .metadata-item {
        display: flex;
        align-items: center;
        gap: 0.8rem;
    }
    
    .metadata-label {
        color: rgba(255, 255, 255, 0.6);
        font-size: 0.85rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .metadata-value {
        color: #42a5f5;
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.9rem;
        font-weight: 600;
    }
    
    /* ===== CARD COMPONENTS ===== */
    .premium-card {
        background: linear-gradient(135deg, #1a2f4b 0%, #0f1f35 100%);
        border: 1px solid rgba(66, 165, 245, 0.2);
        padding: 2rem;
        border-radius: 16px;
        margin: 1rem 0;
        box-shadow: 
            0 10px 30px rgba(0, 0, 0, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .premium-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(66, 165, 245, 0.05), transparent);
        transition: left 0.5s ease;
    }
    
    .premium-card:hover {
        border-color: rgba(66, 165, 245, 0.4);
        box-shadow: 
            0 20px 50px rgba(66, 165, 245, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
        transform: translateY(-4px);
    }
    
    .premium-card:hover::before {
        left: 100%;
    }
    
    /* ===== METRIC DISPLAY ===== */
    .metric-display {
        background: linear-gradient(135deg, #0f1f35 0%, #1a2f4b 100%);
        padding: 1.8rem;
        border-radius: 12px;
        border: 1px solid rgba(66, 165, 245, 0.15);
        margin: 0.8rem 0;
        transition: all 0.3s ease;
    }
    
    .metric-display:hover {
        background: linear-gradient(135deg, #1a2f4b 0%, #0f1f35 100%);
        border-color: rgba(66, 165, 245, 0.3);
        transform: translateX(4px);
    }
    
    .metric-label {
        color: #7ba3d0;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 0.8rem;
        display: block;
    }
    
    .metric-value {
        color: #42a5f5;
        font-size: 2.5rem;
        font-weight: 800;
        font-family: 'IBM Plex Mono', monospace;
        letter-spacing: -1px;
        line-height: 1;
    }
    
    .metric-unit {
        color: #5a7c99;
        font-size: 1rem;
        margin-left: 0.5rem;
        font-weight: 500;
    }
    
    /* ===== STATUS BADGES ===== */
    .status-badge {
        padding: 2rem;
        border-radius: 14px;
        margin: 1.5rem 0;
        border: 2px solid;
        font-weight: 600;
        backdrop-filter: blur(10px);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
    }
    
    .status-critical {
        background: linear-gradient(135deg, rgba(220, 38, 38, 0.15) 0%, rgba(153, 27, 27, 0.1) 100%);
        border-color: rgba(220, 38, 38, 0.6);
        color: #fca5a5;
    }
    
    .status-warning {
        background: linear-gradient(135deg, rgba(217, 119, 6, 0.15) 0%, rgba(180, 83, 9, 0.1) 100%);
        border-color: rgba(217, 119, 6, 0.6);
        color: #fed7aa;
    }
    
    .status-acceptable {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.15) 0%, rgba(5, 122, 85, 0.1) 100%);
        border-color: rgba(34, 197, 94, 0.6);
        color: #a7f3d0;
    }
    
    /* ===== INPUTS & CONTROLS ===== */
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select,
    .stTextInput > div > div > input,
    .stRadio > div > label,
    input[type="text"],
    input[type="number"],
    select {
        background: linear-gradient(135deg, #1a2f4b 0%, #0f1f35 100%) !important;
        border: 1px solid rgba(66, 165, 245, 0.25) !important;
        color: #e8eaf6 !important;
        border-radius: 10px !important;
        padding: 0.9rem 1.2rem !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.95rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus,
    .stTextInput > div > div > input:focus,
    input[type="text"]:focus,
    input[type="number"]:focus,
    select:focus {
        border-color: #42a5f5 !important;
        box-shadow: 0 0 0 3px rgba(66, 165, 245, 0.2), 
                    0 0 15px rgba(66, 165, 245, 0.3) !important;
        background: linear-gradient(135deg, #0f1f35 0%, #1a2f4b 100%) !important;
    }
    
    /* ===== BUTTONS ===== */
    .stButton > button {
        background: linear-gradient(135deg, #2196F3 0%, #1565C0 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.95rem 2.5rem !important;
        font-weight: 700 !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.95rem !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 8px 25px rgba(33, 150, 243, 0.3) !important;
        letter-spacing: 0.5px !important;
        text-transform: uppercase !important;
    }
    
    .stButton > button:hover {
        box-shadow: 0 15px 40px rgba(33, 150, 243, 0.5) !important;
        transform: translateY(-3px) !important;
        background: linear-gradient(135deg, #1E88E5 0%, #0D47A1 100%) !important;
    }
    
    .stButton > button:active {
        transform: translateY(-1px) !important;
    }
    
    /* ===== SIDEBAR ===== */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0e27 0%, #1a1f3a 50%, #0f1425 100%);
        border-right: 1px solid rgba(66, 165, 245, 0.1);
    }
    
    [data-testid="stSidebar"] > div > div > div {
        background: transparent;
    }
    
    /* ===== DIVIDER ===== */
    .stDivider {
        border-color: rgba(66, 165, 245, 0.2) !important;
    }
    
    /* ===== TABS ===== */
    .stTabs [data-baseweb="tab-list"] {
        border-bottom: 2px solid rgba(66, 165, 245, 0.1);
    }
    
    .stTabs [data-baseweb="tab"] {
        color: #7ba3d0;
        border-radius: 10px 10px 0 0;
        padding: 0.8rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        color: #42a5f5 !important;
        border-color: #42a5f5 !important;
    }
    
    /* ===== DATA EDITOR ===== */
    .stDataFrame {
        background: linear-gradient(135deg, #1a2f4b 0%, #0f1f35 100%);
        border: 1px solid rgba(66, 165, 245, 0.2);
        border-radius: 12px;
        overflow: hidden;
    }
    
    /* ===== SECTION TITLES ===== */
    .section-title {
        color: #42a5f5;
        font-size: 1.5rem;
        font-weight: 800;
        margin: 2.5rem 0 1.5rem 0;
        padding-bottom: 1rem;
        border-bottom: 2px solid rgba(66, 165, 245, 0.2);
        letter-spacing: -0.5px;
    }
    
    /* ===== INFO/ERROR BOXES ===== */
    .stInfo, .stSuccess, .stWarning, .stError {
        border-radius: 12px !important;
        border: 1px solid !important;
        backdrop-filter: blur(10px) !important;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# MATERIAL DATA
# ============================================================================

MATERIAL_DATA = {
    "Carbon Steel A106 Gr B": {"stress_psi": 20000, "temp_rating": 600},
    "Carbon Steel A53 Gr B": {"stress_psi": 20000, "temp_rating": 500},
    "Stainless Steel 304": {"stress_psi": 20000, "temp_rating": 900},
    "Stainless Steel 316": {"stress_psi": 20000, "temp_rating": 950},
    "Stainless Steel 316L": {"stress_psi": 16700, "temp_rating": 950},
    "Alloy Steel P11": {"stress_psi": 22500, "temp_rating": 1100},
    "Alloy Steel P22": {"stress_psi": 22500, "temp_rating": 1200},
    "Nickel Alloy 600": {"stress_psi": 20000, "temp_rating": 1200},
    "Custom Material": {"stress_psi": None, "temp_rating": None},
}

Y_FACTOR_TABLE = {
    -20: 0.4, 0: 0.4, 100: 0.4, 200: 0.4, 300: 0.4, 400: 0.4, 500: 0.4,
    600: 0.4, 700: 0.4, 800: 0.4, 900: 0.4, 950: 0.5, 1000: 0.7, 1050: 0.7,
    1100: 0.7, 1150: 0.7, 1200: 0.7, 1250: 0.7, 1300: 0.7, 1350: 0.7, 1400: 0.7, 1500: 0.7,
}

API_570_CLASS = {
    "Class 1": {"max_interval": 10, "desc": "High pressure, corrosive/flammable, high temp"},
    "Class 2": {"max_interval": 15, "desc": "Medium service conditions"},
    "Class 3": {"max_interval": 20, "desc": "Low pressure, non-corrosive, moderate temp"},
}

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_y_factor(temp_f):
    temps = sorted(Y_FACTOR_TABLE.keys())
    if temp_f <= temps[0]:
        return Y_FACTOR_TABLE[temps[0]]
    if temp_f >= temps[-1]:
        return Y_FACTOR_TABLE[temps[-1]]
    
    for i in range(len(temps) - 1):
        if temps[i] <= temp_f <= temps[i+1]:
            t1, t2 = temps[i], temps[i+1]
            y1, y2 = Y_FACTOR_TABLE[t1], Y_FACTOR_TABLE[t2]
            return y1 + (y2 - y1) * (temp_f - t1) / (t2 - t1)
    return 0.7

def calculate_tmin_asme_b313(od_in, design_pressure_psi, allowable_stress_psi, weld_joint_factor, y_factor, corrosion_allowance_in, mill_undertolerance_frac=0.125):
    if od_in <= 0 or design_pressure_psi <= 0 or allowable_stress_psi <= 0:
        return None, None, None, "Invalid: OD, pressure, stress must be > 0"
    if weld_joint_factor <= 0 or weld_joint_factor > 1:
        return None, None, None, "Weld factor must be between 0 and 1"
    if mill_undertolerance_frac >= 1.0:
        return None, None, None, "Mill undertolerance must be < 1.0"
    
    numerator = design_pressure_psi * od_in
    denominator = 2 * (allowable_stress_psi * weld_joint_factor + design_pressure_psi * y_factor)
    
    if denominator <= 0:
        return None, None, None, "Calculation error"
    
    tp = numerator / denominator
    tm = tp + corrosion_allowance_in
    if tm <= 0:
        return None, None, None, "t_min cannot be negative"
    
    tn = tm / (1 - mill_undertolerance_frac)
    return tp, tm, tn, None

def calculate_corrosion_rate(t_initial, t_final, years):
    if years <= 0:
        return None, "Time period must be positive"
    if t_initial <= t_final:
        return 0, "No corrosion detected"
    cr = (t_initial - t_final) / years
    return cr, None

def calculate_remaining_life(t_actual, t_minimum, corrosion_rate):
    if t_actual <= t_minimum:
        return 0, "CRITICAL"
    if corrosion_rate <= 0:
        return 999, "No corrosion"
    remaining = (t_actual - t_minimum) / corrosion_rate
    return remaining, None

def determine_inspection_interval(remaining_life, api_class="Class 3"):
    max_interval = API_570_CLASS[api_class]["max_interval"]
    interval = min(remaining_life / 2, max_interval)
    return max(0.5, interval)

def get_risk_level(remaining_life):
    if remaining_life <= 0:
        return "CRITICAL", "Immediate action. Depressurize and repair now."
    elif remaining_life <= 2:
        return "CRITICAL", "Critical risk. Schedule immediate turnaround."
    elif remaining_life <= 5:
        return "WARNING", "Elevated risk. Plan repair within 1 year."
    else:
        return "ACCEPTABLE", "Continue normal inspection schedule."

# ============================================================================
# SESSION STATE
# ============================================================================

if 'calculation_history' not in st.session_state:
    st.session_state.calculation_history = []
if 'inspection_data' not in st.session_state:
    st.session_state.inspection_data = pd.DataFrame({
        'Inspection Date': pd.to_datetime(['2020-01-01', '2022-01-01', '2024-01-01']),
        'Thickness (in)': [0.280, 0.260, 0.250],
        'Location': ['TML-01', 'TML-01', 'TML-01'],
    })

# ============================================================================
# ENTERPRISE HEADER
# ============================================================================

st.markdown("""
<div class="enterprise-header">
    <h1>⚙️ Pipeline Integrity Management System</h1>
    <p class="subtitle">Enterprise-Grade Risk Assessment & Inspection Optimization</p>
    <div class="metadata">
        <div class="metadata-item">
            <span class="metadata-label">📋 Standards</span>
            <span class="metadata-value">API 570 | ASME B31.3</span>
        </div>
        <div class="metadata-item">
            <span class="metadata-label">🔐 Grade</span>
            <span class="metadata-value">Enterprise</span>
        </div>
        <div class="metadata-item">
            <span class="metadata-label">⏱️ Session</span>
            <span class="metadata-value">""" + datetime.now().strftime("%Y-%m-%d %H:%M UTC") + """</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# SIDEBAR NAVIGATION
# ============================================================================

with st.sidebar:
    st.markdown('<h2 style="color: #42a5f5; margin-bottom: 1.5rem;">📊 Assessment Modules</h2>', unsafe_allow_html=True)
    
    mode = st.radio(
        "Select Analysis Type",
        [
            "🔬 Full Assessment",
            "📏 Minimum Thickness",
            "⏳ Remaining Life",
            "📈 Corrosion Analysis",
            "📑 Reports & History"
        ],
        label_visibility="collapsed"
    )
    
    st.divider()
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(33, 150, 243, 0.1) 0%, rgba(33, 150, 243, 0.05) 100%); 
                padding: 1.5rem; border-radius: 12px; border: 1px solid rgba(66, 165, 245, 0.2);">
        <p style="font-size: 0.8rem; color: #7ba3d0; margin: 0; line-height: 1.6;">
            <strong>Professional Edition</strong><br>
            Qualified Engineers Only<br>
            PE Verification Required<br>
            Full Code Compliance
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# MODE 1: FULL ASSESSMENT
# ============================================================================

if mode == "🔬 Full Assessment":
    st.markdown('<h2 class="section-title">Full Pipeline Assessment</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1.2, 1.2, 1], gap="large")
    
    with col1:
        st.markdown('<div style="color: #42a5f5; font-size: 1.2rem; font-weight: 700; margin-bottom: 1.5rem;">Pipeline Design</div>', unsafe_allow_html=True)
        
        pipeline_id = st.text_input("Pipeline ID", value="PL-001", placeholder="e.g., PL-RLNG-42")
        service = st.selectbox("Service Type", ["Natural Gas", "Crude Oil", "Condensate", "Water", "Steam"])
        
        st.divider()
        
        od_in = st.number_input("Outside Diameter (OD) [in]", min_value=0.1, value=42.0, step=0.1)
        design_pressure = st.number_input("Design Pressure [psi]", min_value=1.0, value=338.0, step=10.0)
        design_temp_f = st.number_input("Design Temperature [°F]", min_value=-20.0, value=100.0, step=5.0)
        
        st.divider()
        
        material = st.selectbox("Material Grade", list(MATERIAL_DATA.keys()))
        if material == "Custom Material":
            allowable_stress = st.number_input("Allowable Stress [psi]", min_value=1000.0, value=20000.0)
        else:
            allowable_stress = MATERIAL_DATA[material]["stress_psi"]
            st.info(f"✓ {allowable_stress:,} psi")
        
        e_factor = st.number_input("Quality Factor (E)", min_value=0.5, max_value=1.0, value=1.0, step=0.05)
        w_factor = st.number_input("Weld Factor (W)", min_value=0.5, max_value=1.0, value=1.0, step=0.05)
        c_allow = st.number_input("Corrosion Allowance [in]", min_value=0.0, value=0.0625, step=0.001)
    
    with col2:
        st.markdown('<div style="color: #42a5f5; font-size: 1.2rem; font-weight: 700; margin-bottom: 1.5rem;">Thickness & Corrosion</div>', unsafe_allow_html=True)
        
        t_actual = st.number_input("Current Measured Thickness [in]", min_value=0.001, value=0.350, step=0.001)
        
        corr_method = st.radio("Corrosion Rate Input", ["Calculate from History", "Enter Directly"], label_visibility="collapsed")
        
        if corr_method == "Calculate from History":
            t_initial = st.number_input("Initial Thickness [in]", min_value=0.001, value=0.500, step=0.001)
            t_previous = st.number_input("Previous Inspection [in]", min_value=0.001, value=0.370, step=0.001)
            years_total = st.number_input("Years Since Installation", min_value=0.1, value=20.0, step=0.5)
            years_recent = st.number_input("Years Since Last Inspection", min_value=0.1, value=5.0, step=0.5)
            
            cr_lt, _ = calculate_corrosion_rate(t_initial, t_actual, years_total)
            cr_st, _ = calculate_corrosion_rate(t_previous, t_actual, years_recent)
            
            if cr_lt is not None and cr_st is not None:
                cr = max(cr_lt, cr_st)
                st.success(f"✓ {cr:.4f} in/yr")
            else:
                cr = 0.01
        else:
            cr = st.number_input("Corrosion Rate [in/yr]", min_value=0.0, value=0.01, step=0.001)
        
        st.divider()
        
        api_class = st.selectbox("API 570 Class", list(API_570_CLASS.keys()))
    
    with col3:
        st.markdown('<div style="color: #42a5f5; font-size: 1.2rem; font-weight: 700; margin-bottom: 1.5rem;">Results</div>', unsafe_allow_html=True)
        
        y = get_y_factor(design_temp_f)
        tp, tm, tn, calc_error = calculate_tmin_asme_b313(od_in, design_pressure, allowable_stress, e_factor * w_factor, y, c_allow)
        
        if calc_error:
            st.error(f"⚠️ {calc_error}")
        else:
            rl, _ = calculate_remaining_life(t_actual, tm, cr)
            inspection_interval = determine_inspection_interval(rl, api_class)
            risk_level, recommendation = get_risk_level(rl)
            
            calc_record = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "pipeline_id": pipeline_id,
                "remaining_life": rl,
                "risk": risk_level,
            }
            
            if st.button("💾 Save Assessment", use_container_width=True):
                st.session_state.calculation_history.append(calc_record)
                st.success("✓ Saved")
            
            st.divider()
            
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown(f'<div class="metric-display"><span class="metric-label">t_pressure</span><span class="metric-value">{tp:.4f}<span class="metric-unit">in</span></span></div>', unsafe_allow_html=True)
            with col_b:
                st.markdown(f'<div class="metric-display"><span class="metric-label">t_minimum</span><span class="metric-value">{tm:.4f}<span class="metric-unit">in</span></span></div>', unsafe_allow_html=True)
            
            st.markdown(f'<div class="metric-display"><span class="metric-label">t_nominal</span><span class="metric-value">{tn:.4f}<span class="metric-unit">in</span></span></div>', unsafe_allow_html=True)
            
            st.divider()
            
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown(f'<div class="metric-display"><span class="metric-label">Remaining Life</span><span class="metric-value">{rl:.2f}<span class="metric-unit">yrs</span></span></div>', unsafe_allow_html=True)
            with col_b:
                st.markdown(f'<div class="metric-display"><span class="metric-label">Inspection Interval</span><span class="metric-value">{inspection_interval:.2f}<span class="metric-unit">yrs</span></span></div>', unsafe_allow_html=True)
            
            st.divider()
            
            if risk_level == "CRITICAL":
                st.markdown(f'<div class="status-badge status-critical">🔴 CRITICAL<br>{recommendation}</div>', unsafe_allow_html=True)
            elif risk_level == "WARNING":
                st.markdown(f'<div class="status-badge status-warning">🟡 WARNING<br>{recommendation}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="status-badge status-acceptable">🟢 ACCEPTABLE<br>{recommendation}</div>', unsafe_allow_html=True)

# ============================================================================
# MODE 2: MINIMUM THICKNESS
# ============================================================================

elif mode == "📏 Minimum Thickness":
    st.markdown('<h2 class="section-title">ASME B31.3 Minimum Wall Thickness</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown('<div style="color: #42a5f5; font-size: 1.2rem; font-weight: 700; margin-bottom: 1.5rem;">Input Parameters</div>', unsafe_allow_html=True)
        
        od = st.number_input("OD [in]", min_value=0.1, value=6.625, step=0.1)
        p = st.number_input("Design Pressure [psi]", min_value=0.1, value=500.0, step=10.0)
        temp = st.number_input("Design Temperature [°F]", min_value=-20.0, value=400.0, step=10.0)
        
        material = st.selectbox("Material", list(MATERIAL_DATA.keys()), key="tmin_mat")
        if material == "Custom Material":
            stress = st.number_input("Allowable Stress [psi]", min_value=1000.0, value=20000.0)
        else:
            stress = MATERIAL_DATA[material]["stress_psi"]
        
        e = st.number_input("Quality Factor (E)", min_value=0.5, max_value=1.0, value=1.0, step=0.05)
        w = st.number_input("Weld Factor (W)", min_value=0.5, max_value=1.0, value=1.0, step=0.05)
        c = st.number_input("Corrosion Allowance [in]", min_value=0.0, value=0.0625, step=0.001)
    
    with col2:
        st.markdown('<div style="color: #42a5f5; font-size: 1.2rem; font-weight: 700; margin-bottom: 1.5rem;">Calculated Results</div>', unsafe_allow_html=True)
        
        y = get_y_factor(temp)
        tp, tm, tn, error = calculate_tmin_asme_b313(od, p, stress, e * w, y, c)
        
        if error:
            st.error(f"⚠️ {error}")
        else:
            st.markdown(f'<div class="metric-display"><span class="metric-label">Y-Factor @ {int(temp)}°F</span><span class="metric-value">{y:.2f}</span></div>', unsafe_allow_html=True)
            st.divider()
            st.markdown(f'<div class="metric-display"><span class="metric-label">t_pressure (t_p)</span><span class="metric-value">{tp:.4f}<span class="metric-unit">in</span></span></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="metric-display"><span class="metric-label">t_minimum (t_m)</span><span class="metric-value">{tm:.4f}<span class="metric-unit">in</span></span></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="metric-display"><span class="metric-label">t_nominal (t_n)</span><span class="metric-value">{tn:.4f}<span class="metric-unit">in</span></span></div>', unsafe_allow_html=True)

# ============================================================================
# MODE 3: REMAINING LIFE
# ============================================================================

elif mode == "⏳ Remaining Life":
    st.markdown('<h2 class="section-title">API 570 Remaining Life Analysis</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown('<div style="color: #42a5f5; font-size: 1.2rem; font-weight: 700; margin-bottom: 1.5rem;">Thickness Data</div>', unsafe_allow_html=True)
        
        t_act = st.number_input("Current Thickness [in]", min_value=0.001, value=0.350)
        t_min = st.number_input("Minimum Required [in]", min_value=0.001, value=0.250)
        
        corr_method = st.radio("Corrosion Rate", ["Calculate", "Direct Entry"], label_visibility="collapsed")
        
        if corr_method == "Calculate":
            t_init = st.number_input("Initial Thickness [in]", min_value=0.001, value=0.500)
            t_prev = st.number_input("Previous Inspection [in]", min_value=0.001, value=0.370)
            yrs_total = st.number_input("Total Years", min_value=0.1, value=20.0)
            yrs_recent = st.number_input("Recent Years", min_value=0.1, value=5.0)
            
            cr_lt, _ = calculate_corrosion_rate(t_init, t_act, yrs_total)
            cr_st, _ = calculate_corrosion_rate(t_prev, t_act, yrs_recent)
            cr_val = max(cr_lt, cr_st) if cr_lt and cr_st else 0.01
            st.info(f"✓ {cr_val:.4f} in/yr")
        else:
            cr_val = st.number_input("Corrosion Rate [in/yr]", min_value=0.0, value=0.01)
    
    with col2:
        st.markdown('<div style="color: #42a5f5; font-size: 1.2rem; font-weight: 700; margin-bottom: 1.5rem;">Life Assessment</div>', unsafe_allow_html=True)
        
        rl, _ = calculate_remaining_life(t_act, t_min, cr_val)
        risk, rec = get_risk_level(rl)
        insp_int = determine_inspection_interval(rl)
        
        st.markdown(f'<div class="metric-display"><span class="metric-label">Remaining Life</span><span class="metric-value">{rl:.2f}<span class="metric-unit">years</span></span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="metric-display"><span class="metric-label">Thickness Margin</span><span class="metric-value">{t_act - t_min:.4f}<span class="metric-unit">in</span></span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="metric-display"><span class="metric-label">Next Inspection</span><span class="metric-value">{insp_int:.2f}<span class="metric-unit">years</span></span></div>', unsafe_allow_html=True)
        
        st.divider()
        
        if risk == "CRITICAL":
            st.markdown(f'<div class="status-badge status-critical">🔴 CRITICAL<br>{rec}</div>', unsafe_allow_html=True)
        elif risk == "WARNING":
            st.markdown(f'<div class="status-badge status-warning">🟡 WARNING<br>{rec}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="status-badge status-acceptable">🟢 ACCEPTABLE<br>{rec}</div>', unsafe_allow_html=True)

# ============================================================================
# MODE 4: CORROSION ANALYSIS
# ============================================================================

elif mode == "📈 Corrosion Analysis":
    st.markdown('<h2 class="section-title">Corrosion Trend Analysis & Forecasting</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1], gap="large")
    
    with col1:
        st.markdown('<div style="color: #42a5f5; font-size: 1.2rem; font-weight: 700; margin-bottom: 1.5rem;">Inspection History</div>', unsafe_allow_html=True)
        edited_df = st.data_editor(st.session_state.inspection_data, num_rows="dynamic", use_container_width=True)
        st.session_state.inspection_data = edited_df
    
    with col2:
        st.markdown('<div style="color: #42a5f5; font-size: 1.2rem; font-weight: 700; margin-bottom: 1.5rem;">Analysis Settings</div>', unsafe_allow_html=True)
        t_min_trend = st.number_input("Minimum Thickness [in]", min_value=0.001, value=0.150)
        forecast_years = st.number_input("Forecast Years", min_value=1, value=5)
    
    if st.button("📊 Generate Trend Analysis", use_container_width=True):
        try:
            df = st.session_state.inspection_data.copy()
            df['Inspection Date'] = pd.to_datetime(df['Inspection Date'])
            df = df.sort_values('Inspection Date').reset_index(drop=True)
            df['Years'] = (df['Inspection Date'] - df['Inspection Date'].iloc[0]).dt.days / 365.25
            
            z = np.polyfit(df['Years'], df['Thickness (in)'], 1)
            poly = np.poly1d(z)
            cr_trend = -z[0]
            
            max_year = df['Years'].max()
            forecast_x = np.linspace(0, max_year + forecast_years, 100)
            forecast_y = poly(forecast_x)
            
            st.divider()
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=df['Years'], y=df['Thickness (in)'], mode='markers', name='Measured', marker=dict(size=12, color='#42a5f5')))
            fig.add_trace(go.Scatter(x=forecast_x, y=forecast_y, mode='lines', name='Forecast', line=dict(color='#42a5f5', width=4)))
            fig.add_hline(y=t_min_trend, line_dash="dash", line_color="#dc2626", annotation_text="Minimum")
            fig.update_layout(title="Corrosion Trend", xaxis_title="Years", yaxis_title="Thickness (in)", template="plotly_dark", hovermode='x unified')
            st.plotly_chart(fig, use_container_width=True)
            
            st.divider()
            
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.markdown(f'<div class="metric-display"><span class="metric-label">CR</span><span class="metric-value">{cr_trend:.4f}<span class="metric-unit">in/yr</span></span></div>', unsafe_allow_html=True)
            with col_b:
                total_loss = df['Thickness (in)'].iloc[0] - df['Thickness (in)'].iloc[-1]
                st.markdown(f'<div class="metric-display"><span class="metric-label">Total Loss</span><span class="metric-value">{total_loss:.4f}<span class="metric-unit">in</span></span></div>', unsafe_allow_html=True)
            with col_c:
                st.markdown(f'<div class="metric-display"><span class="metric-label">Period</span><span class="metric-value">{max_year:.1f}<span class="metric-unit">yrs</span></span></div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"⚠️ {str(e)}")

# ============================================================================
# MODE 5: REPORTS & HISTORY
# ============================================================================

elif mode == "📑 Reports & History":
    st.markdown('<h2 class="section-title">Assessment History & Reports</h2>', unsafe_allow_html=True)
    
    if not st.session_state.calculation_history:
        st.info("📭 No assessments saved. Run and save an assessment to see history.")
    else:
        hist_df = pd.DataFrame(st.session_state.calculation_history)
        st.dataframe(hist_df, use_container_width=True)
        st.divider()
        csv = hist_df.to_csv(index=False)
        st.download_button("📥 Export CSV", data=csv, file_name=f"assessments_{datetime.now().strftime('%Y%m%d')}.csv", mime="text/csv", use_container_width=True)

# ============================================================================
# FOOTER
# ============================================================================

st.divider()
st.markdown("""
<div style="background: linear-gradient(135deg, rgba(33, 150, 243, 0.08) 0%, rgba(33, 150, 243, 0.04) 100%); 
            padding: 2rem; border-radius: 16px; border: 1px solid rgba(66, 165, 245, 0.15);">
    <p style="color: #7ba3d0; font-size: 0.85rem; margin: 0; line-height: 1.8;">
        <strong>Standards Compliance</strong><br>
        API 570 (4th Ed.) | ASME B31.3 (2022) | API 579 Fitness-for-Service<br><br>
        <strong>Professional Disclaimer</strong><br>
        Enterprise-grade tool for qualified engineers only. Professional Engineer verification required. All results must comply with applicable codes and standards.
    </p>
</div>
""", unsafe_allow_html=True)

