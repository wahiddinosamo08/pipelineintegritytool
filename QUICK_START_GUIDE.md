# API 570 / ASME B31.3 Pipeline Remaining Life Calculator
## Quick Start Guide v2.0

---

## 🚀 INSTALLATION

### Local Development
```bash
# 1. Install Python 3.9+
python --version

# 2. Clone/download the app
cd api570-calculator

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run
streamlit run api570_professional_app.py

# App will open at: http://localhost:8501
```

### Docker Deployment (Enterprise)
```bash
# Build image
docker build -t api570-calculator:2.0 .

# Run container
docker run -p 8501:8501 \
  -v /data/calculations:/app/data \
  api570-calculator:2.0

# Access at: http://server-ip:8501
```

### Streamlit Cloud (Free Hosting)
```bash
# 1. Push to GitHub
git push origin main

# 2. Go to share.streamlit.io
# 3. Connect GitHub repo
# 4. Deploy in 2 clicks

# Public URL: https://api570-calculator.streamlit.app
```

---

## 📖 USER WORKFLOWS

### Workflow 1: Quick Remaining Life Calculation (5 minutes)

1. **Select Mode:** "⏳ Remaining Life"
2. **Input Known Thicknesses:**
   - Current Measured: 0.350 in
   - Minimum Required: 0.250 in
3. **Corrosion Rate:**
   - Option A: Calculate from history (if you have old inspections)
   - Option B: Enter directly (if you know the rate)
4. **Read Results:** Remaining life, next inspection date, risk level

**Use Case:** Field inspector with latest thickness reading

---

### Workflow 2: Full Pipeline Assessment (15 minutes)

1. **Select Mode:** "🔬 Full Assessment"
2. **Fill Pipeline Info:**
   - Pipeline ID: PL-RLNG-42
   - Location: Karachi-Sawan
   - Service: Natural Gas
3. **Pipe Specifications:**
   - OD: 42 in
   - Design Pressure: 338 psi
   - Material: Carbon Steel A106 Gr B
4. **Current Thickness Data:**
   - Measured: 0.500 in
   - Corrosion rate: 0.01 in/yr
5. **Click "Save to History"**
6. **Download CSV for your records**

**Use Case:** Annual inspection report, engineering decision-making

---

### Workflow 3: Trend Analysis with Forecasting (20 minutes)

1. **Select Mode:** "📊 Trend Analysis"
2. **Edit Table** (or paste from Excel):
   | Inspection Date | Thickness (in) | Location |
   |---|---|---|
   | 2020-01-01 | 0.280 | TML-01 |
   | 2022-01-01 | 0.260 | TML-01 |
   | 2024-01-01 | 0.250 | TML-01 |
3. **Set Parameters:**
   - Minimum Thickness: 0.150 in
   - Forecast Period: 5 years ahead
4. **Click "Analyze"**
5. **Review:**
   - Corrosion rate trend
   - Years remaining to minimum thickness
   - Forecasted thickness in future

**Use Case:** Multi-year RBI (risk-based inspection) planning

---

## 🎯 INPUT GUIDELINES

### Thickness Measurements
- **Always measure at thinnest point** (TML = Thickness Measurement Location)
- **Multiple points per location** (min 3 per section)
- **Unit:** Inches (in) or millimeters (mm)
  - 0.5 in = 12.7 mm
  - Record to 0.001 in precision (±0.025 mm)

### Design Parameters
- **Nominal OD:** Check nameplate or design drawing
- **Design Pressure:** From ASME code plate (PSI or bar)
- **Design Temperature:** Max operating temperature in °F
- **Material Grade:** From mill cert or design spec
  - Carbon Steel: A106, A53, A333
  - Stainless: 304, 316, 316L
  - Alloy: P11, P22 (chromium-molybdenum)

### Corrosion Allowance
- **Carbon Steel (normal water/gas):** 0.0625 in (1.59 mm) typical
- **Carbon Steel (sour service):** 0.125 in (3.18 mm)
- **Stainless (most conditions):** 0.0 in
- **Check engineering drawings** for specific allowance

### Corrosion Rate Selection
- **Use MAX of:**
  - Long-term CR = (t_initial - t_current) / (total years)
  - Short-term CR = (t_previous - t_current) / (years since last inspection)
- **Conservative approach:** Always pick the higher rate
- **Example:**
  - LT: (0.562 - 0.250) / 20 years = 0.0156 in/yr
  - ST: (0.370 - 0.250) / 5 years = 0.0240 in/yr
  - **Use: 0.0240 in/yr** (the maximum)

---

## 📊 INTERPRETING RESULTS

### Status Indicators

**🔴 CRITICAL (RL ≤ 2 years)**
- Action Required: IMMEDIATE
- Recommendation: Depressurize if unsafe. Schedule emergency repair.
- Inspection Interval: 6 months (minimum)
- Next Step: Notify management. Issue work order.

**🟡 WARNING (2 < RL ≤ 5 years)**
- Action Required: NEAR-TERM
- Recommendation: Include in next scheduled turnaround (within 1 year)
- Inspection Interval: Calculated (usually 1-2 years)
- Next Step: Plan repair scope. Budget allocation.

**🟢 ACCEPTABLE (RL > 5 years)**
- Action Required: ROUTINE
- Recommendation: Continue normal inspection per API 570
- Inspection Interval: Calculated (often 3-5 years)
- Next Step: Schedule next inspection per interval.

---

### Understanding the Metrics

**Remaining Life = (t_actual - t_minimum) / Corrosion Rate**
- In **years** until pipe reaches minimum thickness
- Example: (0.350 - 0.250) / 0.01 = 10 years
- **Action:** Schedule next inspection in 5 years (½ remaining life)

**Thickness Margin = t_actual - t_minimum**
- In **inches** of safety buffer above minimum
- Example: 0.350 - 0.250 = 0.100 in margin
- If margin < 0.050 in → elevated risk (corrosion accelerating)

**Next Inspection Interval**
- In **years** until next required inspection
- Per API 570 SEC 6.3: MIN(remaining_life/2, max_class_interval)
- Class 1: Max 10 years
- Class 2: Max 15 years
- Class 3: Max 20 years

---

## ❌ COMMON ERRORS & FIXES

### Error: "Invalid parameters: OD, pressure, stress must be > 0"
**Problem:** You entered 0 or negative for diameter/pressure/stress  
**Fix:** Check input values. Diameter, pressure, and allowable stress must all be positive

### Error: "Weld factor must be between 0 and 1"
**Problem:** Weld joint factor > 1.0 entered  
**Fix:** For seamless pipe: 1.0. For welded: 0.85-0.95. Check ASME B31.3 for your code category.

### Error: "Mill undertolerance must be < 1.0"
**Problem:** Mill tolerance set to 100% or higher  
**Fix:** Typical values: 0.0 (perfect), 0.125 (12.5%, standard), 0.20 (20% old spec)

### Result: Remaining Life = "999 years"
**Problem:** Corrosion rate = 0 (no thickness loss detected)  
**Fix:** Verify measurements. Is this new pipe with no prior data? Use conservative estimate.

### Result: "No corrosion detected (thickness increased)"
**Problem:** Recent measurement is thicker than previous  
**Fix:** Check for:**
  - Measurement errors (different location on pipe)
  - Unit mismatch (inches vs. mm)
  - Fouling/deposits added to OD (not true thickness increase)

### CSV Won't Open in Excel
**Problem:** Encoding or delimiter issue  
**Fix:** Open in Excel as CSV with UTF-8 encoding. Or open in Google Sheets (auto-converts)

---

## 🔐 DATA PRIVACY & SECURITY

- **This tool runs locally** (Streamlit Cloud) or on your server (Docker)
- **No data is sent to cloud** (except if you export to email/cloud storage)
- **Session data cleared** when browser closed (except saved calculations)
- **Audit trail:** All calculations can be exported to CSV for compliance records
- **User logins:** Set up via corporate SSO if deployed on enterprise server

---

## 🛠️ TROUBLESHOOTING

### App Won't Load
```
Problem: "Connection refused" or blank page
Steps:
1. Check Python version: python --version (need 3.9+)
2. Check port 8501 is available: lsof -i :8501
3. Reinstall dependencies: pip install --upgrade -r requirements.txt
4. Clear cache: rm -rf ~/.streamlit ~/.cache
5. Run with verbose: streamlit run --logger.level=debug api570_professional_app.py
```

### Calculations Are Slow
```
Problem: Table editor or charts take > 5 seconds
Causes: Large inspection history (100+ rows)
Fix:
1. Clear history: Use "Clear History" button
2. Export old data: Use "Export History" before clearing
3. Upgrade hardware: If on weak server, add CPU/RAM
```

### Can't Save Calculations
```
Problem: "Save to History" button does nothing
Causes: Browser cache, session expired
Fix:
1. Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
2. Clear cookies: Settings > Privacy > Clear browsing data
3. Switch browser temporarily
4. Check browser console: F12 > Console tab for errors
```

---

## 📞 SUPPORT

### Quick Questions
- Check this guide first (Ctrl+F to search)
- Review API 570 / ASME B31.3 standards

### Bug Reports
Include:
1. Steps to reproduce
2. Input values you entered
3. Expected vs. actual result
4. Screenshot
5. Browser & OS info

### Feature Requests
- Suggest new materials? Email material specs + allowable stress data
- Need PDF reports? Request planned for v2.1
- Multi-user logins? Planned for v2.2

---

## 📚 RECOMMENDED READING

Before using this tool, engineers should review:

**API 570 (4th Edition)**
- Section 5: Inspection Types (visual, UT, radiography)
- Section 6: Inspection Intervals (class-based)
- Section 7: Corrosion Rate Calculations
- Section 10: Pressure Test Procedures

**ASME B31.3 (2022)**
- Section 300: Pressure Design
- Section 304.1.2: Design Thickness Formula
- Table A-1: Allowable Stresses by Material
- Table 304.1.1: Y-Factor (temperature coefficient)

**API 580 (Risk-Based Inspection Framework)**
- If this becomes part of your RBI program

---

## 🎓 WORKED EXAMPLE

**Scenario:** 10-year-old 6" carbon steel gas transmission line

**Given Data:**
- OD: 6.625 in
- Design Pressure: 600 psi
- Design Temp: 100°F
- Material: A106 Gr B (S = 20,000 psi)
- Nominal Thickness: 0.280 in
- Current Measured: 0.250 in
- Previous Inspection (5 yrs ago): 0.260 in
- Initial Thickness (10 yrs ago): 0.280 in
- Corrosion Allowance: 0.0625 in
- API 570 Class: Class 2

**Step 1: Calculate t_min (ASME B31.3)**
```
Y-factor @ 100°F = 0.4
E = 1.0 (seamless), W = 1.0

t_p = (600 × 6.625) / (2 × (20,000 × 1.0 + 600 × 0.4))
    = 3,975 / (2 × 20,240)
    = 3,975 / 40,480
    = 0.0982 in

t_m = 0.0982 + 0.0625 = 0.1607 in
```

**Step 2: Calculate Corrosion Rate**
```
LT: (0.280 - 0.250) / 10 = 0.003 in/yr
ST: (0.260 - 0.250) / 5 = 0.002 in/yr
Selected: MAX(0.003, 0.002) = 0.003 in/yr
```

**Step 3: Calculate Remaining Life**
```
RL = (0.250 - 0.1607) / 0.003
   = 0.0893 / 0.003
   = 29.8 years ≈ 30 years
```

**Step 4: Determine Inspection Interval**
```
Interval = MIN(30/2, 15) = MIN(15, 15) = 15 years
(Class 2 max = 15 years)
```

**Result:** ✅ ACCEPTABLE
- Remaining Life: 30 years
- Next Inspection: 15 years (per Class 2 API 570)
- Recommendation: Continue normal monitoring

---

## 📄 VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024 Q1 | Initial release (student version) |
| 2.0 | 2024 Q2 | Professional hardening, validation, enterprise UI |
| 2.1 | 2024 Q4 | PDF reports, multi-language (planned) |
| 3.0 | 2025 | API integrations, authentication (planned) |

---

**Last Updated:** 2024  
**Standards Edition:** API 570 (4th), ASME B31.3 (2022)  
**For questions or feedback:** engineering-support@company.com
