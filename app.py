"""
Dashboard Financiero Integral - Distribuciones Andina Comercial S.A.S. (2021 - 2025)
Desarrollado en Streamlit con visualizaciones interactivas Plotly
Analista Financiero Senior: Diagnóstico Estratégico y Creación de Valor
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import io

from data_engine import load_financial_data, calculate_kpis

# ---------------------------------------------------------
# CONFIGURACIÓN GENERAL DE LA PÁGINA
# ---------------------------------------------------------
st.set_page_config(
    page_title="Dashboard Financiero | Andina Comercial S.A.S.",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# ESTILOS CSS PERSONALIZADOS
# ---------------------------------------------------------
st.markdown("""
<style>
    /* Estilos globales y paleta ejecutiva */
    .main {
        background-color: #f8fafc;
    }
    .metric-card {
        background: white;
        border-radius: 10px;
        padding: 16px 20px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
        border: 1px solid #e2e8f0;
        margin-bottom: 12px;
    }
    .metric-title {
        font-size: 0.85rem;
        font-weight: 600;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 4px;
    }
    .metric-value {
        font-size: 1.7rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 4px;
    }
    .metric-delta-pos {
        color: #10b981;
        font-size: 0.85rem;
        font-weight: 600;
    }
    .metric-delta-neg {
        color: #ef4444;
        font-size: 0.85rem;
        font-weight: 600;
    }
    .metric-sub {
        font-size: 0.8rem;
        color: #94a3b8;
    }
    .badge-pill {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    .badge-success { background-color: #d1fae5; color: #065f46; }
    .badge-warning { background-color: #fef3c7; color: #92400e; }
    .badge-info { background-color: #e0f2fe; color: #0369a1; }
    .badge-danger { background-color: #fee2e2; color: #991b1b; }
    
    .section-header {
        font-size: 1.25rem;
        font-weight: 700;
        color: #1e293b;
        margin-top: 15px;
        margin-bottom: 10px;
        border-bottom: 2px solid #3b82f6;
        padding-bottom: 6px;
    }
    .narrative-box {
        background-color: #eff6ff;
        border-left: 4px solid #3b82f6;
        padding: 14px 18px;
        border-radius: 0 8px 8px 0;
        margin: 10px 0 20px 0;
        font-size: 0.95rem;
        color: #1e3a8a;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# CARGA DE DATOS
# ---------------------------------------------------------
@st.cache_data
def get_data():
    return calculate_kpis()

df_kpis, df_balance, df_er, df_cff = get_data()
years = [2021, 2022, 2023, 2024, 2025]

# ---------------------------------------------------------
# BARRA LATERAL (SIDEBAR)
# ---------------------------------------------------------
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/combo-chart.png", width=64)
    st.title("Andina Comercial")
    st.caption("Distribuciones Andina Comercial S.A.S. | NIT 900.842.115-3")
    st.caption("Sector: Distribución B2B Tecnologías y Equipos")
    
    st.divider()
    st.subheader("⚙️ Configuración del Análisis")
    
    selected_year = st.selectbox(
        "Año Focal de Evaluación:",
        options=years,
        index=4,  # Por defecto 2025
        help="Seleccione el año sobre el cual calcular métricas puntuales e índices de variación."
    )
    
    compare_mode = st.radio(
        "Modo de Visualización Temporal:",
        ["Trayectoria Histórica Completa (2021-2025)", f"Foco en Año Focal ({selected_year})"],
        index=0
    )
    
    st.divider()
    st.markdown("### 📥 Descarga de Estados")
    
    # Generador de Excel con todos los estados
    def to_excel():
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df_balance.to_excel(writer, sheet_name='Balance General', index=False)
            df_er.to_excel(writer, sheet_name='Estado Resultados', index=False)
            df_cff.to_excel(writer, sheet_name='Flujo de Efectivo', index=False)
            df_kpis.to_excel(writer, sheet_name='Indicadores Financieros', index=False)
        return output.getvalue()

    excel_data = to_excel()
    st.download_button(
        label="📄 Descargar Estados en Excel",
        data=excel_data,
        file_name="Andina_Comercial_Financiero_2021_2025.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        use_container_width=True
    )
    
    st.divider()
    st.info("💡 **Cifras expresadas en:** Millones de Pesos Colombianos (COP) salvo indicación porcentual o días.")

# ---------------------------------------------------------
# ENCABEZADO PRINCIPAL
# ---------------------------------------------------------
col_head1, col_head2 = st.columns([3, 1])
with col_head1:
    st.title("📊 Tablero de Control Financiero y Creación de Valor")
    st.markdown("""
    **Distribuciones Andina Comercial S.A.S.** | Diagnóstico Estratégico–Financiero Multianual (2021–2025)
    *De la tensión de liquidez por capital de trabajo hacia la escala rentable, eficiencia en caja y desapalancamiento.*
    """)
with col_head2:
    st.markdown(f"""
    <div style="text-align: right; background: #e2e8f0; padding: 10px; border-radius: 8px;">
        <span style="font-size: 0.8rem; color: #475569;">AÑO FOCAL ACTIVO</span><br>
        <span style="font-size: 1.8rem; font-weight: 800; color: #1e293b;">{selected_year}</span><br>
        <span class="badge-pill badge-success">Auditoría Aprobada</span>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# DEFINICIÓN DE PESTAÑAS (TABS)
# ---------------------------------------------------------
tab_resumen, tab_rentabilidad, tab_ktno, tab_solvencia, tab_flujo, tab_simulador, tab_estados, tab_dictamen = st.tabs([
    "🎯 Resumen Ejecutivo",
    "📈 Rentabilidad & DuPont",
    "🔄 Capital de Trabajo & CCE",
    "🛡️ Solvencia & Deuda",
    "💵 Flujo de Caja & FCF",
    "🎛️ Simulador What-If",
    "📑 Estados Financieros",
    "🧠 Dictamen del Analista"
])

# Obtener datos del año focal y del año previo (para deltas)
kpi_focus = df_kpis[df_kpis['Año'] == selected_year].iloc[0]
prev_year = selected_year - 1 if selected_year > 2021 else None
kpi_prev = df_kpis[df_kpis['Año'] == prev_year].iloc[0] if prev_year else None

def get_delta_str(val_now, val_prev, is_pct=False, is_inverted=False, suffix=""):
    if val_prev is None:
        return "Año base", ""
    diff = val_now - val_prev
    diff_pct = (diff / abs(val_prev)) * 100 if val_prev != 0 else 0
    
    # Decidir si la subida es positiva o negativa (e.g. CCE o deuda bajando es bueno)
    is_good = (diff < 0) if is_inverted else (diff > 0)
    css_class = "metric-delta-pos" if is_good else "metric-delta-neg"
    sign = "+" if diff > 0 else ""
    
    if is_pct:
        delta_str = f"{sign}{diff:.2f} p.p. vs {prev_year}"
    else:
        delta_str = f"{sign}{diff:,.1f}{suffix} ({sign}{diff_pct:.1f}%)"
    return delta_str, css_class

# =========================================================================
# TAB 1: RESUMEN EJECUTIVO
# =========================================================================
with tab_resumen:
    st.markdown('<div class="section-header">Puntos de Control Clave (Scorecard Gerencial)</div>', unsafe_allow_html=True)
    
    col_kpi1, col_kpi2, col_kpi3, col_kpi4, col_kpi5, col_kpi6 = st.columns(6)
    
    # 1. Ventas
    d_v, c_v = get_delta_str(kpi_focus['Ventas'], kpi_prev['Ventas'] if kpi_prev is not None else None, suffix="M")
    with col_kpi1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Ventas Netas</div>
            <div class="metric-value">${kpi_focus['Ventas']:,.0f}M</div>
            <div class="{c_v}">{d_v}</div>
            <div class="metric-sub">Ingresos Operacionales</div>
        </div>
        """, unsafe_allow_html=True)
        
    # 2. Margen EBITDA
    d_eb, c_eb = get_delta_str(kpi_focus['Margen EBITDA (%)'], kpi_prev['Margen EBITDA (%)'] if kpi_prev is not None else None, is_pct=True)
    with col_kpi2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Margen EBITDA</div>
            <div class="metric-value">{kpi_focus['Margen EBITDA (%)']:.1f}%</div>
            <div class="{c_eb}">{d_eb}</div>
            <div class="metric-sub">EBITDA: ${kpi_focus['EBITDA']:,.0f}M</div>
        </div>
        """, unsafe_allow_html=True)
        
    # 3. ROE
    d_roe, c_roe = get_delta_str(kpi_focus['ROE (%)'], kpi_prev['ROE (%)'] if kpi_prev is not None else None, is_pct=True)
    with col_kpi3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">ROE (Patrimonio)</div>
            <div class="metric-value">{kpi_focus['ROE (%)']:.1f}%</div>
            <div class="{c_roe}">{d_roe}</div>
            <div class="metric-sub">ROA: {kpi_focus['ROA (%)']:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)
        
    # 4. Ciclo Conversión Efectivo (CCE)
    d_cce, c_cce = get_delta_str(kpi_focus['CCE (Días)'], kpi_prev['CCE (Días)'] if kpi_prev is not None else None, is_inverted=True, suffix="d")
    with col_kpi4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Ciclo Efectivo (CCE)</div>
            <div class="metric-value">{kpi_focus['CCE (Días)']:.0f} días</div>
            <div class="{c_cce}">{d_cce}</div>
            <div class="metric-sub">PKT: {kpi_focus['PKT (%)']:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)
        
    # 5. Flujo de Caja Libre
    d_fcf, c_fcf = get_delta_str(kpi_focus['FCF'], kpi_prev['FCF'] if kpi_prev is not None else None, suffix="M")
    with col_kpi5:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Flujo Libre (FCF)</div>
            <div class="metric-value">${kpi_focus['FCF']:,.0f}M</div>
            <div class="{c_fcf}">{d_fcf}</div>
            <div class="metric-sub">CFO: ${kpi_focus['CFO']:,.0f}M</div>
        </div>
        """, unsafe_allow_html=True)
        
    # 6. Deuda Neta / EBITDA
    d_de, c_de = get_delta_str(kpi_focus['Deuda Neta / EBITDA'], kpi_prev['Deuda Neta / EBITDA'] if kpi_prev is not None else None, is_inverted=True, suffix="x")
    with col_kpi6:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Deuda Neta / EBITDA</div>
            <div class="metric-value">{kpi_focus['Deuda Neta / EBITDA']:.2f}x</div>
            <div class="{c_de}">{d_de}</div>
            <div class="metric-sub">Cobertura: {kpi_focus['Cobertura Intereses']:.1f}x</div>
        </div>
        """, unsafe_allow_html=True)
        
    # Narrativa Ejecutiva de Transformación
    st.markdown("""
    <div class="narrative-box">
        <strong>📌 SÍNTESIS DEL DIAGNÓSTICO FINANCIERO ESTRATÉGICO:</strong><br>
        En 2021, Distribuciones Andina Comercial S.A.S. experimentó la clásica trampa del crecimiento B2B: <em>"vendía sin generar caja"</em> (FCF negativo de -$288M, CCE de 75 días y consumo severo de liquidez en cartera e inventarios).<br>
        Entre 2022 y 2025, la compañía ejecutó un exitoso plan integral de saneamiento:
        <strong>(1)</strong> Optimización del ciclo de efectivo (reducción de 19 días de caja),
        <strong>(2)</strong> Apalancamiento operativo mediante la adopción de canales digitales B2B (dilución de gastos SG&A de 16.3% a 14.5%),
        <strong>(3)</strong> Expansión del margen EBITDA del 8.7% al 10.5% y del ROE del 16.6% al 21.1%, y
        <strong>(4)</strong> Fuerte desapalancamiento neto (Deuda Neta/EBITDA disminuyó de 1.69x a 0.51x con caja final récord de $12,450M).
    </div>
    """, unsafe_allow_html=True)
    
    # Gráficos de Resumen
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.subheader("Evolución de Ingresos y Rentabilidad Operativa")
        fig_rev = make_subplots(specs=[[{"secondary_y": True}]])
        fig_rev.add_trace(
            go.Bar(
                x=df_kpis['Año'],
                y=df_kpis['Ventas'],
                name="Ventas Netas ($M)",
                marker_color="#2563eb",
                opacity=0.85
            ),
            secondary_y=False
        )
        fig_rev.add_trace(
            go.Scatter(
                x=df_kpis['Año'],
                y=df_kpis['Margen EBITDA (%)'],
                name="Margen EBITDA (%)",
                line=dict(color="#10b981", width=3.5),
                mode='lines+markers+text',
                text=[f"{v:.1f}%" for v in df_kpis['Margen EBITDA (%)']],
                textposition="top center"
            ),
            secondary_y=True
        )
        fig_rev.update_layout(
            height=380,
            margin=dict(l=20, r=20, t=30, b=20),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            hovermode="x unified"
        )
        fig_rev.update_yaxes(title_text="Ventas ($ COP)", secondary_y=False, tickformat="$,.0f")
        fig_rev.update_yaxes(title_text="Margen EBITDA (%)", secondary_y=True, ticksuffix="%")
        st.plotly_chart(fig_rev, use_container_width=True)
        
    with col_chart2:
        st.subheader("Transformación de Liquidez: Ciclo CCE vs Flujo de Caja Libre")
        fig_cce_fcf = make_subplots(specs=[[{"secondary_y": True}]])
        fig_cce_fcf.add_trace(
            go.Scatter(
                x=df_kpis['Año'],
                y=df_kpis['CCE (Días)'],
                name="Ciclo Conversión Efectivo (Días)",
                line=dict(color="#f59e0b", width=3, dash='dash'),
                mode='lines+markers+text',
                text=[f"{v:.0f}d" for v in df_kpis['CCE (Días)']],
                textposition="bottom center"
            ),
            secondary_y=False
        )
        fig_cce_fcf.add_trace(
            go.Bar(
                x=df_kpis['Año'],
                y=df_kpis['FCF'],
                name="Flujo Caja Libre ($M)",
                marker_color=np.where(df_kpis['FCF'] >= 0, '#059669', '#dc2626'),
                opacity=0.85
            ),
            secondary_y=True
        )
        fig_cce_fcf.update_layout(
            height=380,
            margin=dict(l=20, r=20, t=30, b=20),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            hovermode="x unified"
        )
        fig_cce_fcf.update_yaxes(title_text="Días de CCE", secondary_y=False)
        fig_cce_fcf.update_yaxes(title_text="FCF ($ COP)", secondary_y=True, tickformat="$,.0f")
        st.plotly_chart(fig_cce_fcf, use_container_width=True)

    # Semáforo de Gestión Financiera Integral
    st.subheader(f"🚦 Matriz de Diagnóstico y Salud Financiera ({selected_year})")
    
    def get_status_badge(condition, good_text, bad_text):
        if condition:
            return f'<span class="badge-pill badge-success">🟢 {good_text}</span>'
        else:
            return f'<span class="badge-pill badge-danger">🔴 {bad_text}</span>'
            
    col_s1, col_s2, col_s3, col_s4, col_s5 = st.columns(5)
    with col_s1:
        st.markdown(f"""
        **1. Liquidez Inmediata**<br>
        Razón Cte: **{kpi_focus['Razón Corriente']:.2f}x**<br>
        {get_status_badge(kpi_focus['Razón Corriente'] >= 1.5, "Óptima (>1.5x)", "Riesgo (<1.5x)")}
        """, unsafe_allow_html=True)
    with col_s2:
        st.markdown(f"""
        **2. Eficiencia KTNO**<br>
        PKT: **{kpi_focus['PKT (%)']:.1f}%**<br>
        {get_status_badge(kpi_focus['PKT (%)'] <= 16.0, "Excelente (<16%)", "Presión KTNO")}
        """, unsafe_allow_html=True)
    with col_s3:
        st.markdown(f"""
        **3. Solvencia / Cobertura**<br>
        Cobertura Int: **{kpi_focus['Cobertura Intereses']:.1f}x**<br>
        {get_status_badge(kpi_focus['Cobertura Intereses'] >= 4.0, "Sólida (>4.0x)", "Vulnerable")}
        """, unsafe_allow_html=True)
    with col_s4:
        st.markdown(f"""
        **4. Rentabilidad (ROE)**<br>
        ROE: **{kpi_focus['ROE (%)']:.1f}%**<br>
        {get_status_badge(kpi_focus['ROE (%)'] >= 18.0, "Alto Valor (>18%)", "Moderado")}
        """, unsafe_allow_html=True)
    with col_s5:
        st.markdown(f"""
        **5. Apalancamiento Neto**<br>
        Deuda Neta/EBITDA: **{kpi_focus['Deuda Neta / EBITDA']:.2f}x**<br>
        {get_status_badge(kpi_focus['Deuda Neta / EBITDA'] <= 1.2, "Desapalancada", "Apalancada")}
        """, unsafe_allow_html=True)

# =========================================================================
# TAB 2: RENTABILIDAD & DUPONT
# =========================================================================
with tab_rentabilidad:
    st.markdown('<div class="section-header">Estructura de Rentabilidad y Descomposición DuPont</div>', unsafe_allow_html=True)
    
    col_pnl1, col_pnl2 = st.columns([3, 2])
    
    with col_pnl1:
        st.subheader(f"Cascada de Resultados (P&L Waterfall - {selected_year})")
        wf_vals = [
            kpi_focus['Ventas'],
            -kpi_focus['Costo de Ventas'],
            kpi_focus['Utilidad Bruta'],
            -df_er.set_index('Cuenta').loc['Gastos de administración', selected_year],
            -df_er.set_index('Cuenta').loc['Gastos de ventas', selected_year],
            -df_er.set_index('Cuenta').loc['Depreciaciones y amortizaciones', selected_year],
            kpi_focus['EBIT'],
            -kpi_focus['Intereses'],
            kpi_focus['EBT'],
            -df_er.set_index('Cuenta').loc['Impuesto de renta', selected_year],
            kpi_focus['Utilidad Neta']
        ]
        wf_text = [
            "Ventas", "(-) Costo Ventas", "Utilidad Bruta", 
            "(-) Gastos Adm", "(-) Gastos Vtas", "(-) Depreciación",
            "EBIT (Operacional)", "(-) Gastos Financieros", "EBT",
            "(-) Impuesto Renta", "Utilidad Neta"
        ]
        wf_measures = [
            "absolute", "relative", "total",
            "relative", "relative", "relative",
            "total", "relative", "total",
            "relative", "total"
        ]
        
        fig_wf = go.Figure(go.Waterfall(
            name="P&L",
            orientation="v",
            measure=wf_measures,
            x=wf_text,
            textposition="outside",
            text=[f"${abs(v):,.0f}" for v in wf_vals],
            y=wf_vals,
            connector={"line": {"color": "#94a3b8"}},
            decreasing={"marker": {"color": "#ef4444"}},
            increasing={"marker": {"color": "#10b981"}},
            totals={"marker": {"color": "#1e3a8a"}}
        ))
        fig_wf.update_layout(
            height=430,
            margin=dict(l=20, r=20, t=30, b=20),
            yaxis=dict(title="Millones COP", tickformat="$,.0f"),
            showlegend=False
        )
        st.plotly_chart(fig_wf, use_container_width=True)
        
    with col_pnl2:
        st.subheader("Dinámica Multianual de Márgenes (%)")
        fig_marg = go.Figure()
        fig_marg.add_trace(go.Scatter(x=df_kpis['Año'], y=df_kpis['Margen Bruto (%)'], name="Margen Bruto", line=dict(color="#3b82f6", width=3), mode='lines+markers'))
        fig_marg.add_trace(go.Scatter(x=df_kpis['Año'], y=df_kpis['Margen EBITDA (%)'], name="Margen EBITDA", line=dict(color="#10b981", width=3), mode='lines+markers'))
        fig_marg.add_trace(go.Scatter(x=df_kpis['Año'], y=df_kpis['Margen Operacional (%)'], name="Margen EBIT", line=dict(color="#f59e0b", width=3), mode='lines+markers'))
        fig_marg.add_trace(go.Scatter(x=df_kpis['Año'], y=df_kpis['Margen Neto (%)'], name="Margen Neto", line=dict(color="#8b5cf6", width=3), mode='lines+markers'))
        
        fig_marg.update_layout(
            height=430,
            margin=dict(l=20, r=20, t=30, b=20),
            yaxis=dict(title="Porcentaje (%)", ticksuffix="%"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_marg, use_container_width=True)

    st.markdown('<div class="section-header">Descomposición del Retorno Sobre el Patrimonio (Modelo DuPont)</div>', unsafe_allow_html=True)
    
    st.markdown("""
    El análisis DuPont divide el **ROE** en sus tres componentes fundamentales:
    $$\\text{ROE} = \\text{Margen Neto} \\times \\text{Rotación de Activos} \\times \\text{Multiplicador de Capital}$$
    """)
    
    col_dup1, col_dup2, col_dup3, col_dup4 = st.columns(4)
    with col_dup1:
        st.markdown(f"""
        <div class="metric-card" style="border-left: 5px solid #8b5cf6;">
            <div class="metric-title">1. Margen Neto (Rentabilidad)</div>
            <div class="metric-value">{kpi_focus['Margen Neto (%)']:.2f}%</div>
            <div class="metric-sub">2021: 3.73% ➔ 2025: 5.57% (+1.84 p.p.)</div>
            <div style="font-size:0.75rem; color:#64748b; margin-top:4px;">Mayor poder de captura por dilución de costos operativos y menores cargas financieras.</div>
        </div>
        """, unsafe_allow_html=True)
    with col_dup2:
        st.markdown(f"""
        <div class="metric-card" style="border-left: 5px solid #3b82f6;">
            <div class="metric-title">2. Rotación Activos (Eficiencia)</div>
            <div class="metric-value">{kpi_focus['Rotación Activos']:.2f}x</div>
            <div class="metric-sub">2021: 2.08x ➔ 2025: 1.89x</div>
            <div style="font-size:0.75rem; color:#64748b; margin-top:4px;">Inversiones en CAPEX logístico y gran acumulación de efectivo aumentan el denominador.</div>
        </div>
        """, unsafe_allow_html=True)
    with col_dup3:
        st.markdown(f"""
        <div class="metric-card" style="border-left: 5px solid #f59e0b;">
            <div class="metric-title">3. Apalancamiento (Estructura)</div>
            <div class="metric-value">{kpi_focus['Multiplicador Capital']:.2f}x</div>
            <div class="metric-sub">2021: 2.13x ➔ 2025: 2.01x</div>
            <div style="font-size:0.75rem; color:#64748b; margin-top:4px;">Desapalancamiento saludable por capitalización interna de resultados acumulados.</div>
        </div>
        """, unsafe_allow_html=True)
    with col_dup4:
        st.markdown(f"""
        <div class="metric-card" style="border-left: 5px solid #10b981;">
            <div class="metric-title">= Retorno Patrimonio (ROE)</div>
            <div class="metric-value">{kpi_focus['ROE (%)']:.2f}%</div>
            <div class="metric-sub">2021: 16.58% ➔ 2025: 21.14% (+4.56 p.p.)</div>
            <div style="font-size:0.75rem; color:#64748b; margin-top:4px;"><strong>Conclusión DuPont:</strong> El incremento del ROE está fundamentado en eficiencia real y margen, NO en sobreendeudamiento.</div>
        </div>
        """, unsafe_allow_html=True)

    # Gráfico Comparativo ROE, ROA y ROIC
    st.subheader("Comparativo de Retornos: ROE vs ROA vs ROIC")
    col_ret1, col_ret2 = st.columns([3, 2])
    with col_ret1:
        fig_ret = go.Figure()
        fig_ret.add_trace(go.Bar(x=df_kpis['Año'], y=df_kpis['ROE (%)'], name="ROE (Patrimonio)", marker_color="#8b5cf6"))
        fig_ret.add_trace(go.Bar(x=df_kpis['Año'], y=df_kpis['ROIC (%)'], name="ROIC (Capital Invertido)", marker_color="#06b6d4"))
        fig_ret.add_trace(go.Bar(x=df_kpis['Año'], y=df_kpis['ROA (%)'], name="ROA (Activos Totales)", marker_color="#3b82f6"))
        fig_ret.update_layout(
            barmode='group',
            height=340,
            margin=dict(l=20, r=20, t=30, b=20),
            yaxis=dict(title="Retorno Porcentual (%)", ticksuffix="%"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_ret, use_container_width=True)
    with col_ret2:
        st.markdown(f"""
        <div style="background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px;">
            <h4 style="margin-top:0; color: #1e293b;">Dilución de Gastos Operacionales (SG&A)</h4>
            <p style="font-size: 0.85rem; color: #64748b;">
                Gracias al canal digital B2B introducido en 2024 y mejoras en logística, los gastos crecieron a menor ritmo que los ingresos:
            </p>
            <ul>
                <li><strong>Gastos Administración:</strong> pasaron de 7.50% (2021) a <strong>6.50%</strong> (2025).</li>
                <li><strong>Gastos Ventas:</strong> pasaron de 8.80% (2021) a <strong>8.00%</strong> (2025).</li>
                <li><strong>Total SG&A sobre Ventas:</strong> optimización total de <strong>16.30% ➔ 14.50%</strong> (180 p.b. liberados).</li>
            </ul>
            <div style="background: #ecfdf5; border-radius: 6px; padding: 10px; font-size: 0.85rem; color: #065f46;">
                ✅ <strong>Efecto Palanca Operativa:</strong> Cada punto porcentual de crecimiento comercial aporta mayor utilidad incremental a la operación.
            </div>
        </div>
        """, unsafe_allow_html=True)

# =========================================================================
# TAB 3: CAPITAL DE TRABAJO & CCE
# =========================================================================
with tab_ktno:
    st.markdown('<div class="section-header">Gestión del Capital de Trabajo Neto Operativo (KTNO) y Ciclo de Efectivo</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="narrative-box">
        <strong>⚡ EL NÚCLEO ESTRATÉGICO DE ANDINA:</strong><br>
        Al ser un distribuidor mayorista con entrega inmediata y crédito a 30-60 días, el capital de trabajo inmoviliza sumas críticas. 
        En 2021, la rotación de cartera e inventario demandó un <strong>CCE de 75 días</strong>. Mediante estrictas políticas de crédito, mejor planeación de compras y renegociación de plazos con proveedores (de 40 a 45 días), el ciclo se contrajo a <strong>56 días</strong> en 2025.
    </div>
    """, unsafe_allow_html=True)
    
    col_dias1, col_dias2 = st.columns(2)
    
    with col_dias1:
        st.subheader("Desglose del Ciclo de Conversión de Efectivo (Días)")
        fig_dias = go.Figure()
        fig_dias.add_trace(go.Bar(x=df_kpis['Año'], y=df_kpis['DIO (Días Inventario)'], name="(+) Días Inventario (DIO)", marker_color="#f59e0b"))
        fig_dias.add_trace(go.Bar(x=df_kpis['Año'], y=df_kpis['DSO (Días Cartera)'], name="(+) Días Cartera (DSO)", marker_color="#3b82f6"))
        fig_dias.add_trace(go.Bar(x=df_kpis['Año'], y=-df_kpis['DPO (Días Proveedores)'], name="(-) Días Proveedores (DPO)", marker_color="#10b981"))
        fig_dias.add_trace(go.Scatter(x=df_kpis['Año'], y=df_kpis['CCE (Días)'], name="= CCE Neto (Días)", line=dict(color="#1e1b4b", width=3.5), mode='lines+markers+text', text=[f"{v:.0f}d" for v in df_kpis['CCE (Días)']], textposition="top center"))
        
        fig_dias.update_layout(
            barmode='relative',
            height=400,
            margin=dict(l=20, r=20, t=30, b=20),
            yaxis=dict(title="Días de Operación"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_dias, use_container_width=True)
        
    with col_dias2:
        st.subheader("Productividad del Capital de Trabajo (PKT) y KTNO")
        fig_pkt = make_subplots(specs=[[{"secondary_y": True}]])
        fig_pkt.add_trace(
            go.Bar(x=df_kpis['Año'], y=df_kpis['KTNO'], name="KTNO ($M COP)", marker_color="#6366f1", opacity=0.85),
            secondary_y=False
        )
        fig_pkt.add_trace(
            go.Scatter(x=df_kpis['Año'], y=df_kpis['PKT (%)'], name="PKT (% sobre Ventas)", line=dict(color="#ec4899", width=3), mode='lines+markers+text', text=[f"{v:.1f}%" for v in df_kpis['PKT (%)']], textposition="bottom center"),
            secondary_y=True
        )
        fig_pkt.update_layout(
            height=400,
            margin=dict(l=20, r=20, t=30, b=20),
            yaxis=dict(title="KTNO ($M)", tickformat="$,.0f"),
            yaxis2=dict(title="PKT (%)", ticksuffix="%"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_pkt, use_container_width=True)

    # Métricas de Palanca de Crecimiento (PDC) y Caja Liberada
    st.subheader("Palanca de Crecimiento (PDC) y Efecto de Caja Liberada")
    col_pdc1, col_pdc2 = st.columns([1, 1])
    
    with col_pdc1:
        st.markdown(f"""
        <div class="metric-card">
            <h4>Palanca de Crecimiento (PDC = Margen EBITDA / PKT)</h4>
            <p style="font-size: 0.9rem; color: #475569;">
                Métrica conceptual del modelo de <em>Óscar León García</em>:
            </p>
            <table style="width: 100%; border-collapse: collapse; font-size: 0.85rem;">
                <tr style="border-bottom: 1px solid #cbd5e1; background: #f1f5f9;">
                    <th style="padding: 6px;">Año</th><th>Margen EBITDA</th><th>PKT</th><th>PDC</th><th>Interpretación</th>
                </tr>
        """, unsafe_allow_html=True)
        for _, row in df_kpis.iterrows():
            pdc_badge = '<span class="badge-pill badge-warning">Caja Condicionada (<1.0)</span>' if row['PDC (Palanca Crecimiento)'] < 1.0 else '<span class="badge-pill badge-success">Generadora (>1.0)</span>'
            st.markdown(f"""
                <tr style="border-bottom: 1px solid #e2e8f0;">
                    <td style="padding: 6px; font-weight:600;">{int(row['Año'])}</td>
                    <td>{row['Margen EBITDA (%)']:.1f}%</td>
                    <td>{row['PKT (%)']:.1f}%</td>
                    <td style="font-weight:700; color:#1e293b;">{row['PDC (Palanca Crecimiento)']:.2f}</td>
                    <td>{pdc_badge}</td>
                </tr>
            """, unsafe_allow_html=True)
        st.markdown("""
            </table>
            <p style="font-size: 0.8rem; color: #64748b; margin-top: 8px;">
                *En 2021, con PDC de 0.46, cada nuevo peso vendido exigía 18.8 centavos en KTNO y solo aportaba 8.7 en EBITDA (destrucción de liquidez). En 2025, el PDC avanzó a 0.73, cerrando sustancialmente la brecha de liquidez estructural.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_pdc2:
        # Cálculo de Caja Liberada Acumulada
        # Si Andina hubiese mantenido la PKT de 2021 (18.84%) sobre las ventas de 2025 ($120,000M):
        ktno_teorico_2025 = 120000 * (df_kpis.loc[0, 'PKT (%)'] / 100.0)
        ktno_real_2025 = df_kpis.loc[4, 'KTNO']
        caja_liberada_total = ktno_teorico_2025 - ktno_real_2025
        
        st.markdown(f"""
        <div class="metric-card" style="border-left: 5px solid #10b981;">
            <h4>Caja Liberada por Eficiencia en KTNO (2021 vs 2025)</h4>
            <div style="font-size: 2.2rem; font-weight: 800; color: #059669;">
                +${caja_liberada_total:,.1f}M COP
            </div>
            <p style="font-size: 0.9rem; color: #334155;">
                <strong>¿Qué significa este valor?</strong><br>
                Si Andina hubiese operado en 2025 con la ineficiencia de capital de trabajo de 2021 (PKT de 18.84%), habría requerido <strong>${ktno_teorico_2025:,.0f}M</strong> en KTNO. 
                Al haber optimizado procesos y reducido la PKT al 14.45% (KTNO real de <strong>${ktno_real_2025:,.0f}M</strong>), la gerencia <strong>liberó exactamente ${caja_liberada_total:,.0f} millones de pesos en efectivo directo</strong>.
            </p>
            <div style="background: #e0f2fe; padding: 10px; border-radius: 6px; font-size: 0.85rem; color: #0369a1;">
                💡 <em>Esta caja liberada financió de manera orgánica el 100% del CAPEX tecnológico e industrial ($3,500M) de 2025 sin necesidad de nuevo endeudamiento.</em>
            </div>
        </div>
        """, unsafe_allow_html=True)

# =========================================================================
# TAB 4: SOLVENCIA & ESTRUCTURA DE DEUDA
# =========================================================================
with tab_solvencia:
    st.markdown('<div class="section-header">Estructura de Capital, Solvencia y Apalancamiento Financiero</div>', unsafe_allow_html=True)
    
    col_liq1, col_liq2 = st.columns(2)
    
    with col_liq1:
        st.subheader("Indicadores de Liquidez Corriente y Cobertura")
        fig_liq = go.Figure()
        fig_liq.add_trace(go.Scatter(x=df_kpis['Año'], y=df_kpis['Razón Corriente'], name="Razón Corriente (AC/PC)", line=dict(color="#2563eb", width=3), mode='lines+markers+text', text=[f"{v:.2f}x" for v in df_kpis['Razón Corriente']], textposition="top center"))
        fig_liq.add_trace(go.Scatter(x=df_kpis['Año'], y=df_kpis['Prueba Ácida'], name="Prueba Ácida ((AC-Inv)/PC)", line=dict(color="#10b981", width=3), mode='lines+markers+text', text=[f"{v:.2f}x" for v in df_kpis['Prueba Ácida']], textposition="bottom center"))
        fig_liq.add_trace(go.Scatter(x=df_kpis['Año'], y=df_kpis['Razón Efectivo'], name="Razón Súper Ácida (Caja/PC)", line=dict(color="#f59e0b", width=3), mode='lines+markers'))
        fig_liq.add_hline(y=1.0, line_dash="dash", line_color="red", annotation_text="Límite Cobertura 1.0x")
        
        fig_liq.update_layout(
            height=380,
            margin=dict(l=20, r=20, t=30, b=20),
            yaxis=dict(title="Veces (x)"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_liq, use_container_width=True)
        
    with col_liq2:
        st.subheader("Desapalancamiento Neto: Deuda Financiera Neta / EBITDA")
        fig_lev = make_subplots(specs=[[{"secondary_y": True}]])
        fig_lev.add_trace(
            go.Bar(x=df_kpis['Año'], y=df_kpis['Deuda Neta'], name="Deuda Neta ($M)", marker_color="#64748b", opacity=0.85),
            secondary_y=False
        )
        fig_lev.add_trace(
            go.Scatter(x=df_kpis['Año'], y=df_kpis['Deuda Neta / EBITDA'], name="Deuda Neta / EBITDA (x)", line=dict(color="#dc2626", width=3.5), mode='lines+markers+text', text=[f"{v:.2f}x" for v in df_kpis['Deuda Neta / EBITDA']], textposition="top center"),
            secondary_y=True
        )
        fig_lev.update_layout(
            height=380,
            margin=dict(l=20, r=20, t=30, b=20),
            yaxis=dict(title="Deuda Neta ($M)", tickformat="$,.0f"),
            yaxis2=dict(title="Múltiplo (x)", ticksuffix="x"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_lev, use_container_width=True)

    # Estructura del Pasivo y Cobertura de Intereses
    col_str1, col_str2 = st.columns(2)
    with col_str1:
        st.subheader(f"Composición de la Deuda Financiera ({selected_year})")
        df_bal_idx = df_balance.set_index('Cuenta')
        deuda_cp_val = df_bal_idx.loc['Obligaciones financieras CP', selected_year]
        deuda_lp_val = df_bal_idx.loc['Obligaciones financieras LP', selected_year]
        prov_val = df_bal_idx.loc['Proveedores', selected_year]
        otros_p_val = df_bal_idx.loc['Cuentas por pagar y otros pasivos', selected_year] + df_bal_idx.loc['Impuestos por pagar', selected_year]
        
        fig_pie_pas = px.pie(
            values=[deuda_cp_val, deuda_lp_val, prov_val, otros_p_val],
            names=['Deuda Bancaria Corto Plazo', 'Deuda Bancaria Largo Plazo', 'Proveedores Comerciales', 'Otros Pasivos Operativos'],
            color_discrete_sequence=['#ef4444', '#f59e0b', '#3b82f6', '#94a3b8'],
            hole=0.45
        )
        fig_pie_pas.update_layout(height=340, margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(fig_pie_pas, use_container_width=True)
        
    with col_str2:
        st.subheader("Cobertura de Gastos Financieros (Intereses)")
        fig_cob = go.Figure()
        fig_cob.add_trace(go.Bar(x=df_kpis['Año'], y=df_kpis['Cobertura Intereses'], name="Cobertura EBITDA / Intereses", marker_color="#10b981"))
        fig_cob.add_trace(go.Scatter(x=df_kpis['Año'], y=df_kpis['Cobertura EBIT'], name="Cobertura EBIT / Intereses", line=dict(color="#1e3a8a", width=3), mode='lines+markers'))
        fig_cob.add_hline(y=3.0, line_dash="dot", line_color="orange", annotation_text="Umbral Mínimo Seguro 3.0x")
        
        fig_cob.update_layout(
            height=340,
            margin=dict(l=20, r=20, t=20, b=20),
            yaxis=dict(title="Veces Cobertura (x)"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_cob, use_container_width=True)

# =========================================================================
# TAB 5: FLUJO DE CAJA & FCF
# =========================================================================
with tab_flujo:
    st.markdown('<div class="section-header">Análisis de Flujo de Efectivo y Calidad del Beneficio</div>', unsafe_allow_html=True)
    
    col_cff1, col_cff2 = st.columns([3, 2])
    
    with col_cff1:
        st.subheader("Evolución de los Tres Flujos: Operación, Inversión y Financiación")
        df_cff_idx = df_cff.set_index('Concepto')
        cf_op = [df_cff_idx.loc['Flujo neto operación (CFO)', y] for y in years]
        cf_inv = [df_cff_idx.loc['Flujo neto inversión (CFI)', y] for y in years]
        cf_fin = [df_cff_idx.loc['Flujo neto financiación (CFF)', y] for y in years]
        
        fig_cfs = go.Figure()
        fig_cfs.add_trace(go.Bar(x=years, y=cf_op, name="CFO: Operación", marker_color="#10b981"))
        fig_cfs.add_trace(go.Bar(x=years, y=cf_inv, name="CFI: Inversión (CAPEX)", marker_color="#ef4444"))
        fig_cfs.add_trace(go.Bar(x=years, y=cf_fin, name="CFF: Financiación", marker_color="#3b82f6"))
        fig_cfs.add_trace(go.Scatter(x=years, y=df_kpis['FCF'], name="Flujo Libre (FCF)", line=dict(color="#1e1b4b", width=3.5), mode='lines+markers'))
        
        fig_cfs.update_layout(
            barmode='group',
            height=380,
            margin=dict(l=20, r=20, t=30, b=20),
            yaxis=dict(title="Millones COP", tickformat="$,.0f"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_cfs, use_container_width=True)
        
    with col_cff2:
        st.subheader("Trayectoria del Saldo de Efectivo Final")
        fig_cash = go.Figure()
        fig_cash.add_trace(go.Scatter(
            x=df_kpis['Año'],
            y=df_kpis['Efectivo'],
            fill='tozeroy',
            fillcolor='rgba(59, 130, 246, 0.15)',
            line=dict(color='#2563eb', width=3),
            mode='lines+markers+text',
            text=[f"${v:,.0f}M" for v in df_kpis['Efectivo']],
            textposition="top center"
        ))
        fig_cash.update_layout(
            height=380,
            margin=dict(l=20, r=20, t=30, b=20),
            yaxis=dict(title="Saldo de Caja ($M COP)", tickformat="$,.0f")
        )
        st.plotly_chart(fig_cash, use_container_width=True)

    # Calidad de la Utilidad y Conciliación
    st.subheader(f"Calidad de la Utilidad y Conversión a Efectivo ({selected_year})")
    col_cq1, col_cq2, col_cq3 = st.columns(3)
    
    with col_cq1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Ratio Calidad de Utilidad (CFO / Neta)</div>
            <div class="metric-value">{kpi_focus['CFO / Utilidad Neta']:.2f}x</div>
            <div class="metric-sub">Meta saludable: > 1.0x</div>
            <p style="font-size:0.8rem; color:#475569; margin-top:6px;">
                En 2021 este ratio era de solo <strong>0.74x</strong> (las utilidades contables no estaban respaldadas por efectivo). En {selected_year} es <strong>{kpi_focus['CFO / Utilidad Neta']:.2f}x</strong>, confirmando máxima solidez y calidad contable.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_cq2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Inversión de Capital (CAPEX)</div>
            <div class="metric-value">${kpi_focus['CAPEX']:,.0f}M</div>
            <div class="metric-sub">Compras de PPE y Sistemas</div>
            <p style="font-size:0.8rem; color:#475569; margin-top:6px;">
                Financiado totalmente por la caja operativa sin incrementar estrés financiero. Acumulado en el quinquenio: <strong>$15,000M</strong> en activos productivos.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_cq3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Retorno al Accionista (Dividendos)</div>
            <div class="metric-value">${kpi_focus['Dividendos']:,.0f}M</div>
            <div class="metric-sub">Payout Ratio: {(kpi_focus['Dividendos']/kpi_focus['Utilidad Neta'])*100:.1f}%</div>
            <p style="font-size:0.8rem; color:#475569; margin-top:6px;">
                La empresa pagó <strong>$0M</strong> en 2021 para salvaguardar liquidez. A partir de 2022 implementó un reparto sostenible del <strong>35%</strong> de las utilidades.
            </p>
        </div>
        """, unsafe_allow_html=True)

# =========================================================================
# TAB 6: SIMULADOR DE ESCENARIOS WHAT-IF
# =========================================================================
with tab_simulador:
    st.markdown('<div class="section-header">Simulador Estratégico Interactivo (Sensibilidad & Proyecciones)</div>', unsafe_allow_html=True)
    
    st.markdown("""
    Explore el impacto en la liquidez y generación de valor modificando los inductores operativos clave a partir de la base de **2025**.
    """)
    
    col_sim_ctl, col_sim_res = st.columns([1, 2])
    
    with col_sim_ctl:
        st.subheader("🎛️ Inductores de Decisión")
        sim_growth = st.slider("Crecimiento Proyectado en Ventas (%)", min_value=-15.0, max_value=30.0, value=10.0, step=1.0)
        sim_gm = st.slider("Margen Bruto (%)", min_value=20.0, max_value=32.0, value=25.0, step=0.5)
        sim_dso = st.slider("Días de Cartera (DSO)", min_value=30, max_value=65, value=43, step=1)
        sim_dio = st.slider("Días de Inventario (DIO)", min_value=40, max_value=75, value=58, step=1)
        sim_dpo = st.slider("Días de Proveedores (DPO)", min_value=30, max_value=60, value=45, step=1)
        sim_sga_dilution = st.slider("Ahorro / Costo Adicional SG&A (% Ventas)", min_value=-2.0, max_value=2.0, value=0.0, step=0.25)
        
    with col_sim_res:
        st.subheader("📊 Resultados Proyectados del Escenario Simulado")
        
        # Base 2025
        base_sales = 120000.0
        proj_sales = base_sales * (1.0 + sim_growth / 100.0)
        proj_cogs = proj_sales * (1.0 - sim_gm / 100.0)
        proj_gp = proj_sales * (sim_gm / 100.0)
        
        # Gastos SG&A base 14.5% + ajuste
        proj_sga_pct = 14.5 + sim_sga_dilution
        proj_sga = proj_sales * (proj_sga_pct / 100.0)
        proj_deprec = 1700.0
        proj_ebit = proj_gp - proj_sga - proj_deprec
        proj_ebitda = proj_ebit + proj_deprec
        proj_int = 1400.0
        proj_ebt = proj_ebit - proj_int
        proj_tax = proj_ebt * 0.30 if proj_ebt > 0 else 0
        proj_net = proj_ebt - proj_tax
        
        # Capital de Trabajo Simulado
        proj_cartera = (proj_sales * sim_dso) / 365.0
        proj_inventario = (proj_cogs * sim_dio) / 365.0
        proj_proveedores = (proj_cogs * sim_dpo) / 365.0
        proj_ktno = (proj_cartera + proj_inventario) - proj_proveedores
        proj_cce = sim_dio + sim_dso - sim_dpo
        proj_pkt = (proj_ktno / proj_sales) * 100.0
        
        # Variación de KTNO vs 2025 base
        base_ktno = kpi_focus['KTNO']
        delta_ktno = proj_ktno - base_ktno  # Si es positivo, absorbe caja; si es negativo, libera caja
        caja_impacto = -delta_ktno
        
        # Métricas proyectadas en tarjetas
        col_r1, col_r2, col_r3 = st.columns(3)
        with col_r1:
            st.metric("Ventas Proyectadas", f"${proj_sales:,.0f}M", f"{sim_growth:+.1f}%")
            st.metric("Nuevo KTNO Requerido", f"${proj_ktno:,.0f}M", f"{delta_ktno:+,.0f}M")
        with col_r2:
            st.metric("EBITDA Proyectado", f"${proj_ebitda:,.0f}M", f"{(proj_ebitda/proj_sales)*100:.1f}% Margen")
            st.metric("Nuevo Ciclo Efectivo (CCE)", f"{proj_cce:.0f} días", f"{proj_cce - 56:+.0f} días vs 2025")
        with col_r3:
            st.metric("Utilidad Neta Proyectada", f"${proj_net:,.0f}M", f"{(proj_net/proj_sales)*100:.1f}% Margen")
            caja_txt = "Liberación Neta de Caja" if caja_impacto >= 0 else "Absorción Neta de Caja"
            st.metric(caja_txt, f"${abs(caja_impacto):,.0f}M", f"{'+' if caja_impacto>=0 else '-'}")

        # Gráfico comparativo de impacto
        fig_sim = go.Figure()
        fig_sim.add_trace(go.Bar(
            x=["Cartera (DSO)", "Inventario (DIO)", "Proveedores (DPO)", "KTNO Neto"],
            y=[kpi_focus['Cartera'], kpi_focus['Inventario'], -kpi_focus['Proveedores'], kpi_focus['KTNO']],
            name="Línea Base Real 2025",
            marker_color="#94a3b8"
        ))
        fig_sim.add_trace(go.Bar(
            x=["Cartera (DSO)", "Inventario (DIO)", "Proveedores (DPO)", "KTNO Neto"],
            y=[proj_cartera, proj_inventario, -proj_proveedores, proj_ktno],
            name="Escenario Proyectado",
            marker_color="#2563eb"
        ))
        fig_sim.update_layout(
            barmode='group',
            height=300,
            margin=dict(l=20, r=20, t=20, b=20),
            yaxis=dict(title="Millones COP", tickformat="$,.0f"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_sim, use_container_width=True)

# =========================================================================
# TAB 7: ESTADOS FINANCIEROS AUDITADOS
# =========================================================================
with tab_estados:
    st.markdown('<div class="section-header">Estados Financieros Completos con Análisis Vertical y Horizontal</div>', unsafe_allow_html=True)
    
    st_selector = st.radio(
        "Seleccionar Estado Financiero para Visualización y Auditoría:",
        ["Balance General", "Estado de Resultados", "Estado de Flujo de Efectivo", "Tabla Maestra de Ratios"],
        horizontal=True
    )
    
    if st_selector == "Balance General":
        st.subheader("Balance General (2021 - 2025)")
        # Preparar análisis vertical para el año seleccionado
        df_b_view = df_balance.copy()
        tot_act_sel = df_b_view.set_index('Cuenta').loc['Total activos', selected_year]
        df_b_view[f'% Vert ({selected_year})'] = (df_b_view[selected_year] / tot_act_sel) * 100.0
        # Análisis horizontal 2021 vs 2025
        df_b_view['Var Abs (25 vs 21)'] = df_b_view[2025] - df_b_view[2021]
        df_b_view['Var % (25 vs 21)'] = ((df_b_view[2025] - df_b_view[2021]) / df_b_view[2021]) * 100.0
        
        # Formato visual
        format_dict = {y: "${:,.0f}" for y in years}
        format_dict[f'% Vert ({selected_year})'] = "{:.1f}%"
        format_dict['Var Abs (25 vs 21)'] = "${:,.0f}"
        format_dict['Var % (25 vs 21)'] = "{:+.1f}%"
        
        st.dataframe(df_b_view.style.format(format_dict), use_container_width=True, height=520)
        
    elif st_selector == "Estado de Resultados":
        st.subheader("Estado de Resultados (2021 - 2025)")
        df_er_view = df_er.copy()
        tot_vta_sel = df_er_view.set_index('Cuenta').loc['Ingresos operacionales (ventas)', selected_year]
        df_er_view[f'% Vert ({selected_year})'] = (df_er_view[selected_year] / tot_vta_sel) * 100.0
        df_er_view['Var Abs (25 vs 21)'] = df_er_view[2025] - df_er_view[2021]
        df_er_view['Var % (25 vs 21)'] = ((df_er_view[2025] - df_er_view[2021]) / df_er_view[2021]) * 100.0
        
        format_dict = {y: "${:,.0f}" for y in years}
        format_dict[f'% Vert ({selected_year})'] = "{:.1f}%"
        format_dict['Var Abs (25 vs 21)'] = "${:,.0f}"
        format_dict['Var % (25 vs 21)'] = "{:+.1f}%"
        
        st.dataframe(df_er_view.style.format(format_dict), use_container_width=True, height=450)
        
    elif st_selector == "Estado de Flujo de Efectivo":
        st.subheader("Estado de Flujos de Efectivo - Método Indirecto (2021 - 2025)")
        df_c_view = df_cff.copy()
        format_dict = {y: "${:,.0f}" for y in years}
        st.dataframe(df_c_view.style.format(format_dict), use_container_width=True, height=520)
        
    else:
        st.subheader("Tabla Maestra Multianual de Indicadores Financieros")
        df_kpi_transpose = df_kpis.set_index('Año').T
        st.dataframe(df_kpi_transpose.style.format("{:,.2f}"), use_container_width=True, height=550)

# =========================================================================
# TAB 8: DICTAMEN DEL ANALISTA
# =========================================================================
with tab_dictamen:
    st.markdown('<div class="section-header">Dictamen Financiero y Recomendaciones Estratégicas para la Junta Directiva</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### 🏛️ Informe del Analista Financiero Senior
    **Para:** Junta Directiva y Gerencia General | **Compañía:** Distribuciones Andina Comercial S.A.S.  
    **Período:** Cierre Quinquenal 2021 – 2025 | **Dictamen General:** Favorable con Evolución Destacada
    
    ---
    
    #### 1. Diagnóstico del Giro Estratégico (2021 vs 2025)
    * **Superación del Estrés de Caja:** En 2021, la empresa afrontó una crisis típica de empresas de rápido crecimiento en distribución: a pesar de vender $80,000M con $2,982M en utilidad neta, el flujo de caja libre fue negativo (-$288M) y el saldo de efectivo se desplomó a solo $740M, obligando a usar líneas de sobregiro y deuda de corto plazo.
    * **Saneamiento del Capital de Trabajo:** La gerencia implementó políticas estrictas de cobranza y optimización logística. La reducción del DSO de 50 a 43 días y del DIO de 65 a 58 días, combinada con la extensión de plazos con proveedores a 45 días, redujo el ciclo de conversión de efectivo de 75 a 56 días. Esta sola mejora liberó **$5,263M en caja operativa neta**.
    
    #### 2. Palanca Operativa y Transformación Digital
    * **Despliegue del Canal B2B Digital (2024-2025):** Permitió aumentar el volumen de ventas en 50% ($80,000M ➔ $120,000M) mientras los gastos de administración se redujeron del 7.50% al 6.50% y los de ventas del 8.80% al 8.00% sobre ingresos.
    * **Expansión del Margen EBITDA:** Pasó del 8.70% al 10.50% ($12,600M en 2025), consolidando un modelo escalable.
    
    #### 3. Estructura de Capital y Deuda
    * **Desapalancamiento y Cobertura:** La relación Deuda Neta / EBITDA cayó de 1.69x a **0.51x**. La cobertura de intereses aumentó a **8.69x**, permitiendo a la empresa acceder a calificaciones crediticias de menor riesgo y menores tasas en el sistema bancario colombiano.
    * **Acumulación de Tesorería:** El saldo final en caja de **$12,450M** en 2025 provee un colchón de seguridad extraordinario ante eventuales choques macroeconómicos o de tasa de cambio.
    
    ---
    
    ### 🚀 Recomendaciones Estratégicas Clave
    1. **Monetización del Excedente de Tesorería:** Con $12,450M en caja ociosa de bajo rendimiento, se recomienda estructurar un plan de colocación en fondos fiduciarios / TES de alta liquidez o anticipar pagos a proveedores importadores a cambio de descuentos por pronto pago (rendimiento financiero implícito > 18% E.A.).
    2. **Expansión de Marca Propia:** Dado que el margen bruto se mantuvo estable en 25.0%, se sugiere elevar la participación de las líneas de marca propia en seguridad electrónica e iluminación industrial para capturar 300-400 p.b. adicionales de margen bruto.
    3. **Política de Dividendos y Creación de Valor (EVA):** Mantener la tasa de distribución del 35% de utilidades netas para retribuir adecuadamente a los accionistas sin comprometer los programas de CAPEX tecnológico requeridos para 2026.
    """)
    
    st.success("✅ **Dictamen Final:** Distribuciones Andina Comercial S.A.S. ha completado una de las transiciones operativas más eficientes del sector mayorista, logrando crecer 50% con rentabilidad creciente, liquidez récord y riesgo financiero mínimo.")

# ---------------------------------------------------------
# PIE DE PÁGINA
# ---------------------------------------------------------
st.divider()
st.caption("Desarrollado para Análisis Financiero Avanzado | Distribuciones Andina Comercial S.A.S. | Python 3.14 & Streamlit")
