import streamlit as st
import numpy as np
import joblib

# 1. Page Configuration (Must be first)
st.set_page_config(page_title="CivilTech AI Suite", page_icon="🏗️", layout="wide")

# 2. Crash-Proof UI Renderer
# This safely converts brackets to HTML in the background, preventing chat UI bugs
def render_ui(text):
    clean_text = text.replace("[[", "<").replace("]]", ">")
    st.markdown(clean_text, unsafe_allow_html=True)

# 3. Advanced CSS and Animated Hero Section
render_ui("""
[[style]]
    /* Import Premium High-Tech Font */
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&display=swap');

    /* Animated Moving Gradient Background */
    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    .stApp {
        background: linear-gradient(-45deg, #090a0f, #121420, #0a1128, #001f3f);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        font-family: 'Space Grotesk', sans-serif;
        color: #e0e0e0;
    }

    /* Floating Animation for Custom Hero Section */
    @keyframes float {
        0% { transform: translateY(0px); box-shadow: 0 5px 15px 0px rgba(0,255,136,0.2); }
        50% { transform: translateY(-10px); box-shadow: 0 25px 15px 0px rgba(0,255,136,0.1); }
        100% { transform: translateY(0px); box-shadow: 0 5px 15px 0px rgba(0,255,136,0.2); }
    }
    
    .hero-container {
        text-align: center;
        padding: 3rem 2rem;
        animation: float 4s ease-in-out infinite;
        background: rgba(20, 25, 35, 0.4);
        border-radius: 20px;
        border: 1px solid rgba(0, 255, 136, 0.3);
        backdrop-filter: blur(12px);
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }
    
    /* Glowing Scanner Line Animation inside Hero */
    @keyframes scan {
        0% { top: -10%; opacity: 0; }
        50% { opacity: 1; }
        100% { top: 110%; opacity: 0; }
    }
    .hero-container::before {
        content: "";
        position: absolute;
        width: 100%;
        height: 2px;
        background: #00FF88;
        left: 0;
        animation: scan 3s linear infinite;
        box-shadow: 0 0 15px #00FF88;
    }

    .hero-title {
        background: linear-gradient(90deg, #00FF88, #00C9FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        font-weight: 700;
        letter-spacing: 2px;
        margin-bottom: 0.5rem;
    }
    
    /* Overwrite Default Streamlit Tabs to look like Custom Buttons */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255,255,255,0.05);
        border-radius: 8px;
        padding: 10px 20px;
        border: 1px solid rgba(255,255,255,0.1);
        color: #a0a0a0;
        transition: all 0.3s ease;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: rgba(0, 255, 136, 0.1);
        border-color: #00FF88;
        color: white;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, rgba(0,201,255,0.2) 0%, rgba(146,254,157,0.2) 100%) !important;
        border-color: #00FF88 !important;
        color: #00FF88 !important;
        box-shadow: 0 0 10px rgba(0,255,136,0.2);
    }

    /* Animated Glassmorphism Metric Cards */
    [data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 20px;
        border-radius: 12px;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    [data-testid="stMetric"]:hover {
        transform: translateY(-5px) scale(1.02);
        border-color: #00C9FF;
        box-shadow: 0 8px 25px rgba(0, 201, 255, 0.15);
    }

    /* Custom Input Boxes */
    .stNumberInput input {
        background-color: rgba(0, 0, 0, 0.2) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: #00FF88 !important;
        font-family: monospace;
    }
    
    /* Hide top header bar of Streamlit */
    header {visibility: hidden;}
[[/style]]

[[div class="hero-container"]]
    [[div class="hero-title"]]CIVILTECH AI SUITE[[/div]]
    [[div style="color: #a0a0a0; font-size: 1.1rem; letter-spacing: 3px; font-weight: 300;"]]
        ADVANCED MATERIAL INTELLIGENCE & STRUCTURAL OPTIMIZATION
    [[/div]]
    [[div style="margin-top: 15px; display: inline-block; padding: 5px 15px; border-radius: 20px; background: rgba(0,255,136,0.1); border: 1px solid #00FF88; color: #00FF88; font-size: 0.8rem; font-family: monospace;"]]
        ● SYSTEM ACTIVE // V 2.0
    [[/div]]
[[/div]]
""")

# 4. Safely Load the AI Model
@st.cache_resource
def load_concrete_model():
    try:
        return joblib.load('concrete_model.pkl')
    except Exception as e:
        return None

model = load_concrete_model()

if model is None:
    st.error("Error: 'concrete_model.pkl' not found. Ensure it is saved in this folder.")
    st.stop()

# 5. Core Navigation Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 1. AI Predictor", 
    "🌿 2. Green Optimizer", 
    "🏢 3. STAAD Exporter", 
    "💰 4. Carbon Analytics",
    "🏗️ 5. RCC vs Composite"
])

# ==========================================
# TAB 1: MANUAL PREDICTOR
# ==========================================
with tab1:
    render_ui("[[h3 style='color: #00FF88;']]Neural Network: 28-Day Strength Prediction[[/h3]]")
    
    col1, col2 = st.columns(2)
    with col1:
        c1 = st.number_input("Cement (kg/m³)", 0.0, 600.0, 300.0, key="t1_c")
        s1 = st.number_input("Blast Furnace Slag (kg/m³)", 0.0, 400.0, 20.0, key="t1_s")
        f1 = st.number_input("Fly Ash (kg/m³)", 0.0, 300.0, 15.0, key="t1_f")
        w1 = st.number_input("Water (kg/m³)", 50.0, 300.0, 160.0, key="t1_w")
    with col2:
        sp1 = st.number_input("Superplasticizer (kg/m³)", 0.0, 40.0, 5.0, key="t1_sp")
        ca1 = st.number_input("Coarse Aggregate (kg/m³)", 500.0, 1400.0, 900.0, key="t1_ca")
        fa1 = st.number_input("Fine Aggregate (kg/m³)", 400.0, 1200.0, 750.0, key="t1_fa")
        age1 = st.number_input("Curing Age (Days)", 1, 365, 28, key="t1_age")

    st.write("")
    if st.button("Initialize Neural Prediction", type="primary", use_container_width=True):
        features = np.array([[c1, s1, f1, w1, sp1, ca1, fa1, age1]])
        predicted_strength = model.predict(features)[0]
        st.success(f"Predicted Strength: {predicted_strength:.2f} MPa")
        st.info(f"Design Grade Achieved: M{int(np.floor(predicted_strength))}")

# ==========================================
# TAB 2: GREEN CONCRETE OPTIMIZER
# ==========================================
with tab2:
    render_ui("[[h3 style='color: #00C9FF;']]Monte Carlo: Low-Carbon Mix Generation[[/h3]]")
    target_fck = st.number_input("Target Structural Strength (MPa)", 20.0, 80.0, 45.0, key="t2_target")
    
    if st.button("Simulate 5,000 Mixes & Optimize", type="primary", use_container_width=True):
        with st.spinner("Executing Monte Carlo simulations..."):
            np.random.seed(42)
            n_sims = 5000
            sim_data = np.column_stack((
                np.random.uniform(120, 450, n_sims),
                np.random.uniform(0, 220, n_sims),
                np.random.uniform(0, 180, n_sims),
                np.random.uniform(130, 210, n_sims),
                np.random.uniform(0, 20, n_sims),
                np.random.uniform(800, 1100, n_sims),
                np.random.uniform(600, 950, n_sims),
                np.full(n_sims, 28)
            ))
            
            sim_preds = model.predict(sim_data)
            viable_idx = np.where(sim_preds >= target_fck)[0]
            
            if len(viable_idx) > 0:
                viable_mixes = sim_data[viable_idx]
                viable_preds = sim_preds[viable_idx]
                
                best_idx = np.argmin(viable_mixes[:, 0])
                opt_mix = viable_mixes[best_idx]
                
                st.success(f"Optimal Formulation Isolated: {viable_preds[best_idx]:.2f} MPa")
                
                m1, m2, m3 = st.columns(3)
                m1.metric("Cement Required", f"{opt_mix[0]:.1f} kg")
                m2.metric("Blast Furnace Slag", f"{opt_mix[1]:.1f} kg")
                m3.metric("Fly Ash", f"{opt_mix[2]:.1f} kg")
                
                m4, m5, m6 = st.columns(3)
                m4.metric("Water", f"{opt_mix[3]:.1f} kg")
                m5.metric("Superplasticizer", f"{opt_mix[4]:.1f} kg")
                m6.metric("Total Aggregates", f"{(opt_mix[5] + opt_mix[6]):.1f} kg")
            else:
                st.error("No valid mix met the specified target.")

# ==========================================
# TAB 3: STAAD.PRO EXPORTER
# ==========================================
with tab3:
    render_ui("[[h3 style='color: #00FF88;']]Structural Analysis Interoperability[[/h3]]")
    spec_strength = st.number_input("Target Design Compressive Strength (MPa)", 20.0, 90.0, 45.0, key="t3_fck")
    
    ec_val = 5000 * np.sqrt(spec_strength)
    fcu_val = spec_strength * 1000.0  
    
    # Custom Digital Readout Panels for STAAD Values
    render_ui(f"""
    [[div style="display: flex; gap: 20px; margin-top: 15px; margin-bottom: 25px;"]]
        [[div style="flex: 1; background: rgba(0, 201, 255, 0.05); border-left: 4px solid #00C9FF; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.2);"]]
            [[div style="color: #a0a0a0; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 5px;"]]Characteristic Strength[[/div]]
            [[div style="color: #00C9FF; font-size: 2rem; font-weight: bold; font-family: monospace;"]]{spec_strength:.2f} MPa[[/div]]
        [[/div]]
        [[div style="flex: 1; background: rgba(0, 255, 136, 0.05); border-left: 4px solid #00FF88; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.2);"]]
            [[div style="color: #a0a0a0; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 5px;"]]Modulus of Elasticity (IS 456)[[/div]]
            [[div style="color: #00FF88; font-size: 2rem; font-weight: bold; font-family: monospace;"]]{ec_val:,.2f} N/mm²[[/div]]
        [[/div]]
    [[/div]]
    """)
    
    staad_text = f"""DEFINE MATERIAL START
NAME AI_HPC_{int(spec_strength)}_MPA
E {ec_val:.2f}
POISSON 0.2
DENSITY 24.0
ALPHA 1E-05
DAMP 0.05
TYPE CONCRETE
STRENGTH fcu {fcu_val:.1f}
END DEFINE MATERIAL"""

    st.code(staad_text, language="text")
    st.download_button("Export STAAD.Pro Configuration", data=staad_text, file_name=f"STAAD_Material_M{int(spec_strength)}.txt", type="primary")

# ==========================================
# TAB 4: COST & CARBON ANALYTICS
# ==========================================
with tab4:
    render_ui("[[h3 style='color: #00C9FF;']]Eco-Financial Auditing & SCM Substitution[[/h3]]")
    
    col_in, col_res = st.columns([1, 1])
    
    with col_in:
        c_p = st.number_input("Cement (kg)", value=280.0, key="t4_c")
        s_p = st.number_input("Slag (kg)", value=80.0, key="t4_s")
        f_p = st.number_input("Fly Ash (kg)", value=60.0, key="t4_f")
        w_p = st.number_input("Water (kg)", value=155.0, key="t4_w")
        sp_p = st.number_input("Superplasticizer (kg)", value=4.5, key="t4_sp")
        ca_p = st.number_input("Coarse Aggregate (kg)", value=920.0, key="t4_ca")
        fa_base = st.number_input("Total Fine Aggregate Base (kg)", value=730.0, key="t4_fa")
        
        render_ui("[[br]][[strong]]Sustainable Copper Slag Replacement[[/strong]]")
        cs_percent = st.slider("Substitute River Sand with Copper Slag (%)", 0, 100, 40)
        
        cs_kg = fa_base * (cs_percent / 100.0)
        fa_final = fa_base - cs_kg

    unit_costs = {'c': 8.0, 's': 2.0, 'f': 1.5, 'sp': 50.0, 'ca': 0.8, 'fa': 1.0, 'cs': 0.3} 
    unit_carbon = {'c': 0.90, 's': 0.05, 'f': 0.01, 'sp': 0.20, 'ca': 0.005, 'fa': 0.005, 'cs': 0.001} 
    
    total_cost = (c_p*unit_costs['c']) + (s_p*unit_costs['s']) + (f_p*unit_costs['f']) + (sp_p*unit_costs['sp']) + (ca_p*unit_costs['ca']) + (fa_final*unit_costs['fa']) + (cs_kg*unit_costs['cs'])
    total_co2 = (c_p*unit_carbon['c']) + (s_p*unit_carbon['s']) + (f_p*unit_carbon['f']) + (sp_p*unit_carbon['sp']) + (ca_p*unit_carbon['ca']) + (fa_final*unit_carbon['fa']) + (cs_kg*unit_carbon['cs'])
    
    cost_savings = cs_kg * (unit_costs['fa'] - unit_costs['cs'])
    carbon_savings = cs_kg * (unit_carbon['fa'] - unit_carbon['cs'])
    
    with col_res:
        st.metric(
            label="Calculated Material Cost", 
            value=f"₹ {total_cost:,.2f} / m³", 
            delta=f"-₹ {cost_savings:.2f} (Savings)" if cost_savings > 0 else None,
            delta_color="inverse"
        )
        st.metric(
            label="Embodied Carbon Footprint", 
            value=f"{total_co2:,.2f} kg CO₂ / m³", 
            delta=f"-{carbon_savings:.3f} kg (Reduction)" if carbon_savings > 0 else None,
            delta_color="inverse"
        )
        
        st.divider()
        if total_co2 < 200:
            st.success("Sustainability Rating: EXCELLENT (Ultra-Low Carbon)")
        elif total_co2 < 300:
            st.warning("Sustainability Rating: AVERAGE (Industry Standard)")
        else:
            st.error("Sustainability Rating: POOR (High Carbon Impact)")

# ==========================================
# TAB 5: RCC VS COMPOSITE
# ==========================================
with tab5:
    render_ui("[[h3 style='color: #00FF88;']]Structural Efficiency: Dead Load Differential[[/h3]]")
    
    c_span, c_grade = st.columns(2)
    with c_span:
        # Changed from slider to precise number input
        span = st.number_input("Clear Span of Beam (Meters)", min_value=1.0, max_value=30.0, value=6.0, step=0.1)
    with c_grade:
        fck_comp = st.number_input("Design Concrete Grade (MPa)", value=45.0, min_value=20.0, max_value=80.0, key="t5_fck")

    rcc_depth = (span * 1000) / 12
    rcc_width = rcc_depth / 2
    rcc_vol_per_m = (rcc_width / 1000) * (rcc_depth / 1000)
    rcc_weight_per_m = rcc_vol_per_m * 2500

    comp_steel_depth = (span * 1000) / 20
    comp_deck_thick = 120
    comp_eff_width = (span * 1000) / 4
    comp_conc_vol = (comp_eff_width / 1000) * (comp_deck_thick / 1000)
    comp_conc_weight = comp_conc_vol * 2400
    comp_steel_weight = span * 15
    
    comp_total_weight = comp_conc_weight + comp_steel_weight
    comp_total_depth = comp_steel_depth + comp_deck_thick

    st.markdown("---")
    
    col_rcc, col_comp = st.columns(2)
    
    with col_rcc:
        render_ui("[[div style='text-align: center; color: #ff4b4b; margin-bottom: 10px;']]TRADITIONAL RCC BEAM[[/div]]")
        st.metric("Section Depth", f"{int(rcc_depth)} mm")
        st.metric("Self-Weight (Dead Load)", f"{rcc_weight_per_m:.1f} kg/m")
        
    with col_comp:
        render_ui("[[div style='text-align: center; color: #00FF88; margin-bottom: 10px;']]STEEL-CONCRETE COMPOSITE[[/div]]")
        st.metric("Overall Depth", f"{int(comp_total_depth)} mm", delta=f"-{int(rcc_depth - comp_total_depth)} mm thinner")
        st.metric("Self-Weight (Dead Load)", f"{comp_total_weight:.1f} kg/m", delta=f"-{rcc_weight_per_m - comp_total_weight:.1f} kg/m lighter")