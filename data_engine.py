"""
Motor de Datos y Métricas Financieras para Distribuciones Andina Comercial S.A.S.
Calcula todos los indicadores financieros, balances, estados de resultados y flujos de caja.
"""

import pandas as pd
import numpy as np

def load_financial_data():
    years = [2021, 2022, 2023, 2024, 2025]
    
    # 1. Balance General (en Millones de COP)
    balance_dict = {
        'Cuenta': [
            # Activos Corrientes
            'Efectivo y equivalentes',
            'Deudores (cuentas por cobrar)',
            'Inventarios',
            'Otros activos corrientes',
            'Total activo corriente',
            # Activos No Corrientes
            'Propiedad, planta y equipo (neto)',
            'Intangibles (neto)',
            'Total activos',
            # Pasivos Corrientes
            'Obligaciones financieras CP',
            'Proveedores',
            'Cuentas por pagar y otros pasivos',
            'Impuestos por pagar',
            'Total pasivo corriente',
            # Pasivo No Corriente
            'Obligaciones financieras LP',
            'Total pasivos',
            # Patrimonio
            'Capital social',
            'Reservas',
            'Resultados acumulados',
            'Total patrimonio',
            'Total pasivo + patrimonio'
        ],
        2021: [740, 10959, 10685, 1200, 23584, 13300, 1500, 38384, 4385, 6575, 1043, 256, 12259, 8143, 20402, 10000, 2000, 5982, 17982, 38384],
        2022: [3233, 11573, 11392, 1200, 27398, 14800, 1500, 43698, 4905, 7595, 1119, 306, 13925, 9109, 23034, 10000, 2000, 8664, 20664, 43698],
        2023: [5866, 12225, 12358, 1200, 31649, 16400, 1500, 49549, 5483, 8571, 1203, 376, 15633, 10183, 25816, 10000, 2000, 11733, 23733, 49549],
        2024: [8882, 13315, 13315, 1200, 36712, 18100, 1500, 56312, 6048, 9986, 1296, 468, 17798, 11232, 29030, 10000, 2000, 15282, 27282, 56312],
        2025: [12450, 14137, 14301, 1200, 42088, 20000, 1500, 63588, 6615, 11096, 1392, 573, 19676, 12285, 31961, 10000, 2000, 19627, 31627, 63588]
    }
    df_balance = pd.DataFrame(balance_dict)
    
    # 2. Estado de Resultados
    er_dict = {
        'Cuenta': [
            'Ingresos operacionales (ventas)',
            'Costo de ventas',
            'Utilidad bruta',
            'Gastos de administración',
            'Gastos de ventas',
            'Depreciaciones y amortizaciones',
            'Utilidad operacional (EBIT)',
            'Gastos financieros (intereses)',
            'Utilidad antes de impuestos (EBT)',
            'Impuesto de renta',
            'Utilidad neta'
        ],
        2021: [80000, 60000, 20000, 6000, 7040, 1200, 5760, 1500, 4260, 1278, 2982],
        2022: [88000, 66000, 22000, 6424, 7568, 1300, 6708, 1600, 5108, 1532, 3576],
        2023: [97000, 72750, 24250, 6887, 8148, 1400, 7815, 1550, 6265, 1880, 4385],
        2024: [108000, 81000, 27000, 7344, 8856, 1500, 9300, 1500, 7800, 2340, 5460],
        2025: [120000, 90000, 30000, 7800, 9600, 1600, 11000, 1450, 9550, 2865, 6685]
    }
    df_er = pd.DataFrame(er_dict)

    # 3. Flujo de Efectivo
    cff_dict = {
        'Concepto': [
            'Utilidad neta',
            '(+) Depreciación y amortización',
            'Variación cuentas por cobrar',
            'Variación inventarios',
            'Variación otros activos corrientes',
            'Variación proveedores',
            'Variación otros pasivos corrientes',
            'Variación impuestos por pagar',
            'Flujo neto operación (CFO)',
            'Compras de PPE (CAPEX)',
            'Flujo neto inversión (CFI)',
            'Variación obligaciones financieras',
            'Dividendos pagados',
            'Flujo neto financiación (CFF)',
            'Variación neta de efectivo',
            'Efectivo inicial',
            'Efectivo final'
        ],
        2021: [2982, 1200, -1959, -685, -100, 575, 143, 56, 2212, -2500, -2500, -1472, 0, -1472, -1760, 2500, 740],
        2022: [3576, 1300, -614, -707, 0, 1020, 76, 50, 4701, -2800, -2800, 1486, -894, 592, 2493, 740, 3233],
        2023: [4385, 1400, -652, -966, 0, 976, 84, 70, 5297, -3000, -3000, 1652, -1316, 336, 2633, 3233, 5866],
        2024: [5460, 1500, -1090, -957, 0, 1415, 93, 92, 6513, -3200, -3200, 1614, -1911, -297, 3016, 5866, 8882],
        2025: [6685, 1600, -822, -986, 0, 1110, 96, 105, 7788, -3500, -3500, 1620, -2340, -720, 3568, 8882, 12450]
    }
    df_cff = pd.DataFrame(cff_dict)
    
    return years, df_balance, df_er, df_cff

def calculate_kpis():
    years, df_balance, df_er, df_cff = load_financial_data()
    
    # Extraer series indexadas por año
    b_indexed = df_balance.set_index('Cuenta')
    e_indexed = df_er.set_index('Cuenta')
    c_indexed = df_cff.set_index('Concepto')
    
    records = []
    for y in years:
        ventas = e_indexed.loc['Ingresos operacionales (ventas)', y]
        costo_v = e_indexed.loc['Costo de ventas', y]
        util_bruta = e_indexed.loc['Utilidad bruta', y]
        gastos_adm = e_indexed.loc['Gastos de administración', y]
        gastos_vta = e_indexed.loc['Gastos de ventas', y]
        deprec = e_indexed.loc['Depreciaciones y amortizaciones', y]
        ebit = e_indexed.loc['Utilidad operacional (EBIT)', y]
        ebitda = ebit + deprec
        intereses = e_indexed.loc['Gastos financieros (intereses)', y]
        ebt = e_indexed.loc['Utilidad antes de impuestos (EBT)', y]
        impuestos = e_indexed.loc['Impuesto de renta', y]
        util_neta = e_indexed.loc['Utilidad neta', y]
        
        efectivo = b_indexed.loc['Efectivo y equivalentes', y]
        cartera = b_indexed.loc['Deudores (cuentas por cobrar)', y]
        inventario = b_indexed.loc['Inventarios', y]
        activo_cte = b_indexed.loc['Total activo corriente', y]
        ppe_neto = b_indexed.loc['Propiedad, planta y equipo (neto)', y]
        intangibles = b_indexed.loc['Intangibles (neto)', y]
        activo_total = b_indexed.loc['Total activos', y]
        
        deuda_cp = b_indexed.loc['Obligaciones financieras CP', y]
        proveedores = b_indexed.loc['Proveedores', y]
        otros_pas_cte = b_indexed.loc['Cuentas por pagar y otros pasivos', y]
        impuestos_pagar = b_indexed.loc['Impuestos por pagar', y]
        pasivo_cte = b_indexed.loc['Total pasivo corriente', y]
        deuda_lp = b_indexed.loc['Obligaciones financieras LP', y]
        deuda_fin_total = deuda_cp + deuda_lp
        pasivo_total = b_indexed.loc['Total pasivos', y]
        patrimonio = b_indexed.loc['Total patrimonio', y]
        
        cfo = c_indexed.loc['Flujo neto operación (CFO)', y]
        capex = abs(c_indexed.loc['Compras de PPE (CAPEX)', y])
        fcf = cfo - capex  # Flujo de caja libre directo
        cff = c_indexed.loc['Flujo neto financiación (CFF)', y]
        divid = abs(c_indexed.loc['Dividendos pagados', y])
        
        # 1. Ratios de Liquidez
        razon_corriente = activo_cte / pasivo_cte
        prueba_acida = (activo_cte - inventario) / pasivo_cte
        razon_efectivo = efectivo / pasivo_cte
        ktn_contable = activo_cte - pasivo_cte
        
        # 2. Ratios de Actividad y Capital de Trabajo
        dso = (cartera / ventas) * 365.0
        rot_cartera = ventas / cartera
        dio = (inventario / costo_v) * 365.0
        rot_inventario = costo_v / inventario
        dpo = (proveedores / costo_v) * 365.0
        rot_proveedores = costo_v / proveedores
        ciclo_operativo = dio + dso
        cce = ciclo_operativo - dpo
        ktno = (cartera + inventario) - proveedores
        pkt = (ktno / ventas) * 100.0  # en %
        
        # Palanca de crecimiento (García Serna): Margen EBITDA (%) / PKT (%)
        margen_ebitda = (ebitda / ventas) * 100.0
        pdc = margen_ebitda / pkt if pkt > 0 else 0
        
        # 3. Ratios de Rentabilidad
        margen_bruto = (util_bruta / ventas) * 100.0
        margen_operacional = (ebit / ventas) * 100.0
        margen_neto = (util_neta / ventas) * 100.0
        roa = (util_neta / activo_total) * 100.0
        roe = (util_neta / patrimonio) * 100.0
        
        # DuPont (3 pasos)
        rot_activos = ventas / activo_total
        apalancamiento_dupont = activo_total / patrimonio
        roe_calc = (margen_neto / 100.0) * rot_activos * apalancamiento_dupont * 100.0
        
        # DuPont (5 pasos)
        tax_burden = util_neta / ebt
        interest_burden = ebt / ebit
        ebit_margin = ebit / ventas
        
        # ROIC
        tasa_imp = 0.30
        nopat = ebit * (1.0 - tasa_imp)
        capital_invertido = ktno + ppe_neto + intangibles
        roic = (nopat / capital_invertido) * 100.0
        
        # 4. Endeudamiento y Solvencia
        endeudamiento_total = (pasivo_total / activo_total) * 100.0
        endeudamiento_financiero = (deuda_fin_total / activo_total) * 100.0
        cobertura_intereses = ebitda / intereses
        cobertura_ebit = ebit / intereses
        deuda_neta = deuda_fin_total - efectivo
        deuda_neta_ebitda = deuda_neta / ebitda
        deuda_ebitda = deuda_fin_total / ebitda
        leverage_pasivo_patr = pasivo_total / patrimonio
        
        # 5. Gastos operativos sobre ventas
        gastos_adm_pct = (gastos_adm / ventas) * 100.0
        gastos_vta_pct = (gastos_vta / ventas) * 100.0
        sg_and_a_pct = ((gastos_adm + gastos_vta) / ventas) * 100.0
        
        # 6. Calidad de utilidades
        cfo_sobre_util_neta = cfo / util_neta
        
        records.append({
            'Año': y,
            'Ventas': ventas,
            'Costo de Ventas': costo_v,
            'Utilidad Bruta': util_bruta,
            'EBITDA': ebitda,
            'EBIT': ebit,
            'EBT': ebt,
            'Utilidad Neta': util_neta,
            'Margen Bruto (%)': margen_bruto,
            'Margen EBITDA (%)': margen_ebitda,
            'Margen Operacional (%)': margen_operacional,
            'Margen Neto (%)': margen_neto,
            'ROA (%)': roa,
            'ROE (%)': roe,
            'ROIC (%)': roic,
            'Rotación Activos': rot_activos,
            'Multiplicador Capital': apalancamiento_dupont,
            'Tax Burden': tax_burden,
            'Interest Burden': interest_burden,
            'Efectivo': efectivo,
            'Cartera': cartera,
            'Inventario': inventario,
            'Proveedores': proveedores,
            'KTNO': ktno,
            'PKT (%)': pkt,
            'PDC (Palanca Crecimiento)': pdc,
            'DSO (Días Cartera)': dso,
            'DIO (Días Inventario)': dio,
            'DPO (Días Proveedores)': dpo,
            'Ciclo Operativo (Días)': ciclo_operativo,
            'CCE (Días)': cce,
            'Razón Corriente': razon_corriente,
            'Prueba Ácida': prueba_acida,
            'Razón Efectivo': razon_efectivo,
            'KTN Contable': ktn_contable,
            'Activo Total': activo_total,
            'Pasivo Total': pasivo_total,
            'Patrimonio': patrimonio,
            'Deuda Financiera Total': deuda_fin_total,
            'Deuda Neta': deuda_neta,
            'Endeudamiento Total (%)': endeudamiento_total,
            'Endeudamiento Financiero (%)': endeudamiento_financiero,
            'Deuda Neta / EBITDA': deuda_neta_ebitda,
            'Deuda / EBITDA': deuda_ebitda,
            'Cobertura Intereses': cobertura_intereses,
            'Cobertura EBIT': cobertura_ebit,
            'Intereses': intereses,
            'CFO': cfo,
            'CAPEX': capex,
            'FCF': fcf,
            'CFF': cff,
            'Dividendos': divid,
            'CFO / Utilidad Neta': cfo_sobre_util_neta,
            'Gastos Adm (%)': gastos_adm_pct,
            'Gastos Vta (%)': gastos_vta_pct,
            'SG&A (%)': sg_and_a_pct
        })
        
    df_kpis = pd.DataFrame(records)
    return df_kpis, df_balance, df_er, df_cff

if __name__ == '__main__':
    kpis, b, er, c = calculate_kpis()
    print("KPIs DataFrame successfully computed!")
    print(kpis[['Año', 'Ventas', 'Margen EBITDA (%)', 'ROE (%)', 'CCE (Días)', 'PKT (%)', 'Deuda Neta / EBITDA', 'FCF']].to_string())
