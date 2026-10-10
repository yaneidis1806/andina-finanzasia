@echo off
title Dashboard Financiero - Distribuciones Andina Comercial S.A.S.
echo ======================================================================
echo    INICIANDO DASHBOARD FINANCIERO - ANDINA COMERCIAL S.A.S.
echo ======================================================================
echo.
echo Verificando entorno de ejecucion...
C:\Python314\python.exe -m streamlit run app.py --server.port 8501
pause
