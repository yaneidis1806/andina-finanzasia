# 📊 Dashboard Financiero Ejecutivo: Distribuciones Andina Comercial S.A.S. (2021–2025)

Aplicación web interactiva de visualización y diagnóstico financiero para **Distribuciones Andina Comercial S.A.S.**, desarrollada con **Python**, **Streamlit** y **Plotly**.

---

## 🎯 Objetivo del Dashboard
Evaluar la transformación estratégica y financiera de la compañía durante el quinquenio 2021–2025, analizando el paso de una etapa de tensión de liquidez por capital de trabajo (*"crecimiento sin caja"* en 2021) hacia un modelo escalable, altamente rentable y con desapalancamiento neto récord en 2025.

---

## 🚀 Cómo Ejecutar la Aplicación

### Opción 1: Ejecución Rápida en Windows
Haga doble clic en el archivo:
```text
ejecutar_dashboard.bat
```

### Opción 2: Ejecución desde la Terminal / PowerShell
```powershell
C:\Python314\python.exe -m streamlit run app.py --server.port 8501
```

Luego abra su navegador web en: **[http://localhost:8501](http://localhost:8501)**

---

## 🧩 Arquitectura del Dashboard

El tablero cuenta con **8 módulos interactivos** diseñados bajo estándares internacionales de análisis de estados financieros y el modelo de Inductores de Valor de Óscar León García:

1. **🎯 Resumen Ejecutivo (Scorecard Gerencial):**
   - Tarjetas KPI con deltas automáticos frente al año previo: Ventas, Margen EBITDA, ROE, CCE, FCF y Deuda Neta/EBITDA.
   - Gráfico dual de evolución de ventas vs. margen EBITDA.
   - Semáforo integral de salud financiera (Liquidez, KTNO, Solvencia, Rentabilidad y Apalancamiento).

2. **📈 Rentabilidad & Descomposición DuPont:**
   - Cascada P&L (*Waterfall Chart*) desde Ventas hasta Utilidad Neta.
   - Dinámica histórica de márgenes (Bruto, EBITDA, Operacional, Neto).
   - Árbol DuPont de 3 factores: Margen Neto × Rotación de Activos × Multiplicador de Capital = ROE.
   - Comparativo de retornos: ROE vs. ROA vs. ROIC.
   - Análisis de dilución de gastos operacionales (SG&A de 16.3% a 14.5% sobre ventas gracias a digitalización B2B).

3. **🔄 Gestión del Capital de Trabajo (KTNO) y Ciclo de Efectivo (CCE):**
   - Desglose del Ciclo de Conversión de Efectivo: Días de Inventario (DIO), Días de Cartera (DSO) y Días de Proveedores (DPO).
   - Productividad del Capital de Trabajo (PKT: 18.8% ➔ 14.5%).
   - Palanca de Crecimiento (PDC = Margen EBITDA / PKT): de 0.46 (destrucción de caja en 2021) a 0.73 en 2025.
   - **Cálculo de Caja Liberada:** Demostración de **$5,263M COP** liberados directamente en caja por eficiencia en KTNO.

4. **🛡️ Solvencia, Deuda y Estructura de Capital:**
   - Ratios de Liquidez: Razón Corriente (1.92x ➔ 2.14x), Prueba Ácida (1.05x ➔ 1.41x) y Razón de Efectivo.
   - Desapalancamiento neto: Deuda Neta / EBITDA cae de **1.69x a 0.51x**.
   - Cobertura de Intereses (EBITDA / Gastos Financieros) asciende a **8.69x**.
   - Composición de la deuda bancaria (Corto Plazo vs. Largo Plazo).

5. **💵 Flujo de Caja y Liquidez (CFO, CFI, CFF & FCF):**
   - Dinámica de los 3 flujos: Operación (CFO), Inversión/CAPEX (CFI) y Financiación (CFF).
   - Evolución del Flujo de Caja Libre (FCF): de -$288M en 2021 a récord de **+$4,288M** en 2025.
   - Saldo final de efectivo: escala de $740M a **$12,450M**.
   - Ratio de Calidad de la Utilidad (CFO / Utilidad Neta): de 0.74x a 1.17x.

6. **🎛️ Simulador What-If (Escenarios Interactivos):**
   - Controles deslizantes para ajustar Ventas, Margen Bruto, DSO, DIO, DPO y ahorros en SG&A.
   - Recalcula en tiempo real el nuevo KTNO proyectado, el impacto en caja liberada/absorbida, el CCE y el nuevo EBITDA.

7. **📑 Estados Financieros Completos:**
   - Balance General clasificado con Análisis Vertical (%) y Horizontal (%).
   - Estado de Resultados clasificado con Análisis Vertical (%) y Horizontal (%).
   - Estado de Flujos de Efectivo clasificado.
   - Tabla maestra de ratios financieros.
   - **Botón de exportación a Excel multi-hoja**.

8. **🧠 Dictamen del Analista Financiero Senior:**
   - Conclusiones ejecutivas y recomendaciones para la Junta Directiva en torno a tesorería, marca propia, crédito y política de dividendos.

---

## 📂 Estructura de Archivos del Proyecto

```text
├── app.py                                   # Aplicación principal Streamlit con UI y dashboards Plotly
├── data_engine.py                           # Motor de cálculo financiero, ratios, balances y métricas
├── ejecutar_dashboard.bat                   # Script ejecutable de 1 clic para Windows
├── README.md                                # Documentación técnica y financiera
├── balance_general.xlsx                     # Datos fuente del Balance General (2021-2025)
├── estado_de_resultados.xlsx                # Datos fuente del Estado de Resultados (2021-2025)
├── estado_flujo_efectivo.xlsx               # Datos fuente del Flujo de Efectivo (2021-2025)
└── Caso Distribuciones Andina Comercial SAS.docx # Documento de contexto estratégico del caso
```
