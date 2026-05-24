# Pipeline Integrity Management System
## Enterprise Edition | Professional Assessment & RBI Planning

![Version](https://img.shields.io/badge/version-2.0.0--enterprise-blue.svg)
![Standards](https://img.shields.io/badge/standards-API%20570%20%7C%20ASME%20B31.3-green.svg)
![License](https://img.shields.io/badge/license-Professional%20Use-red.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)

---

## 📋 Overview

**Pipeline Integrity Management System** is an enterprise-grade web application for professional engineers specializing in **risk-based inspection (RBI) planning**, **remaining life calculation**, and **pipeline asset management**.

Built on **API 570 (Piping Inspection Code)** and **ASME B31.3 (Process Piping)**, this tool provides:
- Real-time wall thickness calculations
- Remaining service life prediction
- Corrosion rate trend analysis
- Inspection interval optimization
- Fitness-for-service assessment

---

## 🎯 Key Features

### 🔬 **Five Analysis Modules**

| Module | Purpose | Output |
|--------|---------|--------|
| **🔬 Full Assessment** | Complete pipeline evaluation | t_min, Remaining Life, Risk Level, Next Inspection |
| **📏 Minimum Thickness** | ASME B31.3 design calculations | t_pressure, t_minimum, t_nominal |
| **⏳ Remaining Life** | API 570 service life analysis | Years remaining, Thickness margin, Inspection date |
| **📈 Corrosion Analysis** | Historical trend forecasting | Corrosion rate, Total loss, Future thickness projection |
| **📑 Reports & History** | Assessment management | CSV export, Calculation history, Audit trail |

---

## 🏗️ Technical Architecture

### **Technology Stack**
```
Frontend:    Streamlit 1.28.0+ (Web Framework)
Plotting:    Plotly (Interactive Charts)
Analysis:    NumPy, Pandas, SciPy
Database:    In-memory session state
Standards:   API 570, ASME B31.3, NACE SP0169
```

### **System Requirements**
- **Python**: 3.9 or higher
- **Memory**: 512MB minimum (1GB recommended)
- **Browser**: Chrome, Firefox, Safari, Edge (modern versions)
- **OS**: Windows, macOS, Linux

---

## 📦 Installation

### **Step 1: Create Virtual Environment**
```bash
uv venv --python 3.11
```

### **Step 2: Activate Environment**

**macOS/Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### **Step 3: Install Dependencies**
```bash
uv pip install streamlit pandas numpy scipy matplotlib seaborn plotly
```

Or use requirements file:
```bash
uv pip install -r requirements.txt
```

### **Step 4: Run Application**
```bash
streamlit run api570_enterprise.py
```

### **Step 5: Access Web Interface**
Open browser to: **http://localhost:8501**

---

## 🔧 Quick Start Guide

### **Scenario 1: Calculate Remaining Life**

1. **Select Mode**: "⏳ Remaining Life (API 570)"
2. **Enter Data**:
   - Current Thickness: 0.350 in
   - Minimum Required: 0.250 in
   - Corrosion Rate: 0.01 in/yr
3. **View Results**: Remaining life, thickness margin, next inspection interval
4. **Save**: Click "💾 Save Assessment" for history

### **Scenario 2: Design Check (ASME B31.3)**

1. **Select Mode**: "📏 Minimum Thickness (ASME B31.3)"
2. **Input Design Parameters**:
   - OD: 6.625 in
   - Design Pressure: 500 psi
   - Material: Carbon Steel A106 Gr B
   - Corrosion Allowance: 0.0625 in
3. **Review Results**: t_p, t_m, t_n thicknesses
4. **Compare**: Against measured wall thickness from UT inspection

### **Scenario 3: Trend Analysis**

1. **Select Mode**: "📈 Corrosion Analysis"
2. **Enter Inspection History**:
   - Date 1: 2020-01-01 → 0.280 in
   - Date 2: 2022-01-01 → 0.260 in
   - Date 3: 2024-01-01 → 0.250 in
3. **Set Parameters**:
   - Minimum Thickness: 0.150 in
   - Forecast Years: 5
4. **Generate Trend**: View graph + corrosion rate calculation
5. **Export**: Download CSV for report

---

## 📊 Module Details

### **Module 1: Full Assessment (🔬)**

**Inputs:**
- Pipeline geometry (OD, design pressure, temperature)
- Material properties (grade, allowable stress)
- Design factors (E, W factors; corrosion allowance)
- Current condition (measured thickness)
- Corrosion data (history or direct rate)
- API 570 class

**Calculations:**
```
ASME B31.3:
  Y-factor = f(temperature)
  t_p = (P × D) / [2(S×E×W + P×Y)]
  t_m = t_p + c
  t_n = t_m / (1 - mill_tolerance)

API 570:
  Remaining Life = (t_actual - t_min) / CR
  Inspection Interval = min(RL/2, class_max)
  
Risk Assessment:
  RL ≤ 0:   CRITICAL (repair now)
  RL ≤ 2:   CRITICAL (turnaround scheduled)
  RL ≤ 5:   WARNING (plan within 1 year)
  RL > 5:   ACCEPTABLE (continue schedule)
```

**Outputs:**
- Thickness calculations (t_p, t_m, t_n)
- Remaining service life (years)
- Next inspection date
- Risk classification with recommendations
- Save to history for audit trail

---

### **Module 2: Minimum Thickness (📏)**

**ASME B31.3 Section 304.1.2 Calculations**

**Formula:**
```
t_p = (P × D) / [2(S × E × W + P × Y)]

Where:
  P  = Design pressure (psi)
  D  = Outside diameter (in)
  S  = Allowable stress (psi)
  E  = Quality factor (weld)
  W  = Weld factor
  Y  = Temperature derating factor
  t_p = Pressure design thickness
  
Then:
  t_m = t_p + c  (add corrosion allowance)
  t_n = t_m / (1 - mill_tolerance)
```

**Material Database Included:**
- Carbon Steel A106 Gr B (20,000 psi)
- Stainless Steel 304/316 (20,000 psi)
- Alloy Steel P11/P22 (22,500 psi)
- Custom material input supported

**Temperature Factor (Y):**
Automatically interpolates from ASME B31.3 Table 304.1.1 for temperature range -20°F to 1500°F

---

### **Module 3: Remaining Life (⏳)**

**API 570 Assessment**

**Methods:**
1. **Calculate from History**: Uses two corrosion rates (long-term and short-term), selects maximum
2. **Direct Entry**: Input known corrosion rate

**Calculation:**
```
Remaining Life = (t_actual - t_minimum) / corrosion_rate

Inspection Interval = min(RL/2, API_570_Class_Max)
  Class 1: max 10 years
  Class 2: max 15 years
  Class 3: max 20 years
  
Minimum interval: 6 months
```

**Safety Guards:**
- If t_actual ≤ t_minimum: RL = 0 (immediate repair)
- If CR = 0: RL = 999 years (no corrosion)
- If CR < 0: Error (thickness increasing?)

---

### **Module 4: Corrosion Analysis (📈)**

**Trend Analysis & Forecasting**

**Features:**
- Load inspection history (date, thickness, location)
- Edit data in-app (add/remove rows)
- Fit polynomial trend line
- Calculate corrosion rate
- Forecast future thickness
- Interactive Plotly chart

**Metrics Calculated:**
- Corrosion Rate (in/year)
- Total thickness loss
- Inspection period (years)
- Projected time to minimum thickness

**Example Output:**
```
Inspection History:
  2020-01-01: 0.280 in
  2022-01-01: 0.260 in
  2024-01-01: 0.250 in

Results:
  Corrosion Rate: 0.0150 in/yr
  Total Loss: 0.0300 in over 4 years
  Period: 4.0 years
```

---

### **Module 5: Reports & History (📑)**

**Assessment Management**

- View all saved calculations
- Timestamp for each assessment
- Pipeline ID, service type, risk level
- Export to CSV for Excel/reports
- Audit trail for compliance

**Export Format:**
```csv
timestamp,pipeline_id,service,remaining_life,t_min,risk
2024-01-15 14:30,PL-RLNG-42,Natural Gas,12.5,0.2505,ACCEPTABLE
2024-01-15 14:45,PL-OIL-16,Crude Oil,2.3,0.1850,CRITICAL
```

---

## 🎨 Interface Design

### **Design Philosophy**
- **Dark Enterprise Theme**: Professional, focus-friendly dark mode
- **Glassmorphism**: Modern floating cards with blur effects
- **Micro-interactions**: Smooth transitions and hover effects
- **Premium Typography**: Inter font family + IBM Plex Mono for metrics
- **Color Psychology**: Electric blue for trust, subtle gradients for depth

### **Components**
- **Premium Header**: Enterprise branding with metadata
- **Metric Cards**: Interactive displays with hover effects
- **Status Badges**: Color-coded risk levels (Critical/Warning/Acceptable)
- **Interactive Charts**: Plotly visualizations with dark theme
- **Professional Inputs**: Styled form fields with focus states

---

## 📐 Standards & Formulas

### **API 570 (Piping Inspection Code) - 4th Edition**

**Key Sections Implemented:**
- **Section 6.1**: Inspection planning and scheduling
- **Section 6.3**: Risk-based inspection intervals
- **Section 9**: Corrosion rate determination
- **Appendix E**: Remaining life calculation

**Corrosion Rate Determination (API 570, Section 9):**
```
Long-term CR:  (t_initial - t_current) / years_since_install
Short-term CR: (t_prev_inspection - t_current) / years_since_last

Selected CR = MAX(CR_long-term, CR_short-term)
```

### **ASME B31.3 (Process Piping Code) - 2022 Edition**

**Section 304 (Design Thickness):**
```
Straight Pipe (t_p):
  t_p = (P × D) / [2(S × E × W + P × Y)]

With Corrosion Allowance:
  t_m = t_p + c
  
Nominal Thickness (accounting for mill tolerance):
  t_n = t_m / (1 - mill_tolerance)
```

**Material Allowable Stresses (typical examples):**
| Material | Temperature | Allowable Stress |
|----------|-------------|-----------------|
| A106 Gr B | 0-100°F | 20,000 psi |
| P22 | 0-100°F | 22,500 psi |
| 316SS | 0-100°F | 20,000 psi |

**Y-Factor (Table 304.1.1):**
```
Temperature < 950°F:  Y = 0.4
950°F ≤ T ≤ 1000°F:   Y = 0.5
Temperature > 1000°F: Y = 0.7
(Interpolated for intermediate temperatures)
```

---

## 🔐 Professional Use Guidelines

### **Qualified Users**
✅ Licensed Professional Engineers (PE)  
✅ API 570 Certified Inspectors  
✅ Pipeline engineers with ASME B31.3 experience  
✅ Inspection supervisors and planners  

### **Verification Requirements**
- All results must be reviewed by a Professional Engineer
- Must comply with applicable codes and standards
- Site-specific conditions must be considered
- Results are engineering recommendations, not final decisions

### **Documentation**
- Save all assessments (built-in history)
- Export CSV for report generation
- Timestamp all calculations for audit trail
- Keep records per API 570 Section 6.6

---

## 📝 Input Data Guide

### **Required Inputs (Full Assessment)**

```
PIPELINE DESIGN:
  - Outside Diameter (OD) [inches]
  - Design Pressure [psi]
  - Design Temperature [°F]
  
MATERIAL PROPERTIES:
  - Material Grade (dropdown or custom)
  - Quality Factor E (0.5-1.0)
  - Weld Factor W (0.5-1.0)
  - Corrosion Allowance [inches]
  
CONDITION DATA:
  - Current Measured Thickness [inches]
  - Corrosion Rate [in/year] OR historical data
  
SERVICE CLASSIFICATION:
  - API 570 Class (1, 2, or 3)
```

### **Units & Conventions**
| Parameter | Unit | Range | Notes |
|-----------|------|-------|-------|
| Diameter | inches | 0.1 - 999 | Imperial units |
| Pressure | psi | 1 - 10,000 | Gauge pressure |
| Temperature | °F | -20 to 1500 | Design condition |
| Thickness | inches | 0.001 - 1.0 | Decimal format |
| Corrosion Rate | in/year | 0 - 0.1 | Long-term average |
| Time | years | 0.1 - 100 | Inspection intervals |

---

## 🚀 Advanced Features

### **Corrosion Rate Calculation**
```python
# Long-term (from installation)
CR_LT = (thickness_new - thickness_now) / years_operating

# Short-term (recent)
CR_ST = (thickness_last_inspection - thickness_now) / years_since_last

# Selected (more conservative)
CR = MAX(CR_LT, CR_ST)
```

### **Risk-Based Inspection Intervals**
```
Remaining Life (years) → Inspection Interval
  0-2:   CRITICAL (6 months or immediate)
  2-5:   WARNING (next interval = RL/2, max 1 year)
  5-10:  ELEVATED (next interval = RL/2, max 3 years)
  10+:   ACCEPTABLE (next interval = RL/2, max class_limit)
```

### **Safety Guards Built-In**
✅ Division by zero protection  
✅ Negative thickness detection  
✅ Invalid factor validation  
✅ Data range checking  
✅ Material property verification  

---

## 📊 Example Calculations

### **Example 1: 42" Natural Gas Line (RLNG)**

**Input Data:**
```
Pipeline: PL-RLNG-42 (Natural Gas)
OD: 42.0 in
Design Pressure: 338 psi
Design Temperature: 100°F
Material: Carbon Steel A106 Gr B
E Factor: 1.0 (seamless)
W Factor: 1.0 (no weld)
Corrosion Allowance: 1/16 in (0.0625 in)

Current Thickness: 0.350 in
Initial Thickness: 0.500 in
Years Operating: 20 years
Corrosion Rate: 0.0075 in/yr
API 570 Class: Class 1
```

**Calculations:**

ASME B31.3:
```
Y(100°F) = 0.4
t_p = (338 × 42) / [2(20000 × 1.0 × 1.0 + 338 × 0.4)]
    = 14196 / [40000 + 135.2]
    = 0.3547 in

t_m = 0.3547 + 0.0625 = 0.4172 in
t_n = 0.4172 / (1 - 0.125) = 0.4768 in
```

API 570:
```
Remaining Life = (0.350 - 0.4172) / 0.0075
              = -0.0672 / 0.0075
              = CRITICAL (t_actual < t_min)

Risk Level: CRITICAL
Action: Immediate repair required
```

---

### **Example 2: Minimum Thickness Design Check**

**Input:**
```
OD: 6.625 in
Pressure: 500 psi
Temperature: 400°F
Material: Stainless Steel 316
E = 1.0, W = 1.0
Corrosion Allowance: 0.0625 in
```

**Result:**
```
Y(400°F) = 0.4
t_p = 0.0831 in
t_m = 0.1456 in
t_n = 0.1664 in

Design specification: Use t_n = 0.1664 in nominal (schedule 40 typical)
```

---

## 🔄 Workflow Example

**Step-by-Step: Complete Assessment**

1. **Open Application**
   ```bash
   streamlit run api570_enterprise.py
   ```

2. **Select "🔬 Full Assessment"**

3. **Enter Pipeline Design** (Left column)
   - Pipeline ID: PL-001
   - Service: Natural Gas
   - OD: 42 in, Pressure: 338 psi, Temp: 100°F
   - Material: A106, E=1.0, W=1.0, C=0.0625

4. **Enter Thickness & Corrosion** (Middle column)
   - Measured: 0.350 in
   - Calculate from history:
     - Initial: 0.500 in
     - Previous: 0.370 in
     - Years: 20, Recent: 5

5. **View Results** (Right column)
   - t_p = 0.3547 in
   - t_m = 0.4172 in
   - t_n = 0.4768 in
   - Remaining Life = CRITICAL
   - Risk Level: CRITICAL

6. **Save Assessment**
   - Click "💾 Save Assessment"
   - Records to history with timestamp

7. **Export for Report**
   - Go to "📑 Reports & History"
   - Click "📥 Export CSV"
   - Use in Excel/Word for formal documentation

---

## 🐛 Troubleshooting

### **Issue: "Invalid denominator" error**

**Cause:** Combination of input parameters creates negative or zero denominator in ASME B31.3 formula

**Solution:**
- Increase allowable stress
- Decrease Y-factor (lower design temperature)
- Check material selection
- Verify weld/quality factors are between 0.5-1.0

### **Issue: Remaining Life = 999 years**

**Cause:** Corrosion rate = 0 (no corrosion detected)

**Solution:**
- Enter measured corrosion rate directly if history incomplete
- Verify inspection data shows thickness loss
- Check units (must be in/year)

### **Issue: "Current thickness < minimum required"**

**Cause:** Measured wall thickness is below minimum required per ASME B31.3

**Solution:**
- **CRITICAL**: Repair immediately
- Consider immediate depressurization
- Plan emergency turnaround
- Consult engineering team

### **Issue: Browser won't connect to localhost:8501**

**Cause:** Streamlit server not running or port in use

**Solution:**
```bash
# Check if server is running
lsof -i :8501

# Kill existing process if needed
kill -9 <PID>

# Restart
streamlit run api570_enterprise.py --server.port 8502
```

---

## 📚 References & Standards

### **Primary Standards**
- **API 570** (4th Edition, 2020): Piping Inspection Code
- **ASME B31.3** (2022 Edition): Process Piping Code  
- **API 579** (2016): Fitness-For-Service Evaluation
- **NACE SP0169** (2013): Cathodic Protection

### **Related Documents**
- API 580: Risk-Based Inspection
- ASME B31.8: Gas Transmission Piping Systems
- API 583: Corrosion and Its Prevention in Oil and Gas Production and Processing

---

## 🔐 Data Security & Compliance

### **Data Handling**
- All calculations performed locally (no cloud transmission)
- Session data stored in browser memory (cleared on exit)
- Optional CSV export for local storage
- No personally identifiable information (PII) collected

### **Compliance**
- Follows API 570 documentation requirements
- Audit trail via history export
- Professional use only (PE verification required)
- Suitable for formal engineering reports

---

## 💡 Best Practices

### **For Inspectors**
1. Always verify measured thickness with multiple UT readings
2. Use maximum corrosion rate (long-term vs short-term)
3. Include corrosion allowance appropriate for service
4. Document all assumptions in report
5. Save assessments for future comparison

### **For Engineers**
1. Review inspector data before calculations
2. Consider site-specific conditions not in calculator
3. Use professional judgment for safety margin
4. Verify Y-factors for actual operating temperature
5. Document all baseline data (pipe mill cert, original thickness)

### **For Management**
1. Use risk-based intervals to optimize inspection budget
2. Export history for regulatory audits
3. Track pipelines approaching critical remaining life
4. Plan maintenance around inspection findings
5. Maintain audit trail per API 570

---

## 📞 Support & Contact

### **For Technical Issues**
- Check this README troubleshooting section
- Verify Python version (3.9+)
- Confirm all dependencies installed
- Check browser compatibility (modern Chrome/Firefox recommended)

### **For Standards Questions**
- Consult API 570, ASME B31.3 directly
- Contact Professional Engineer on staff
- Review API technical publications

### **Version Information**
```
Application: Pipeline Integrity Management System
Version: 2.0.0 Enterprise Edition
Release Date: 2024
Python Version: 3.9+
Streamlit Version: 1.28.0+
Status: Production Ready
```

---

## 📄 License & Disclaimer

**PROFESSIONAL USE ONLY**

This tool is intended for:
- Licensed Professional Engineers
- API 570 Certified Inspectors  
- Qualified Pipeline Engineers

**Disclaimer:**
Results generated by this tool are engineering calculations based on input parameters and applicable standards (API 570, ASME B31.3). All results must be verified and approved by a Professional Engineer before use. This tool does not replace professional engineering judgment, on-site inspection, or regulatory compliance requirements. Users accept full responsibility for accuracy of input data and appropriateness of conclusions.

---

## 🎓 Learning Resources

### **Getting Started**
1. Read this README completely
2. Run Module 2 (Minimum Thickness) with example values
3. Try Module 3 (Remaining Life) with sample data
4. Save and export an assessment

### **Deepening Knowledge**
- Review formulas in "Standards & Formulas" section above
- Study example calculations
- Refer to API 570 Section 6 for inspection philosophy
- Review ASME B31.3 Section 304 for design equations

### **Professional Development**
- Pursue API 570 certification (40-hour course)
- Take ASME B31.3 design courses
- Attend pipeline integrity management seminars
- Join professional organizations (ASME, API)

---

**END OF README**

---

**Questions?** Review the module descriptions and example calculations above. For standards clarifications, consult the primary references (API 570, ASME B31.3) or a Professional Engineer.

