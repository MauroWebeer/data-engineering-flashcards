@echo off
title Data Engineering Flashcards
color 0b

echo [1/3] Iniciando o servidor FastAPI...
cd /d %~dp0
call .venv\Scripts\activate
start cmd /k "uvicorn backend.main:app --reload"

echo [2/3] Aguardando o servidor subir...
timeout /t 2 /nobreak > nul

echo [3/3] Abrindo o navegador na Home...
start "" "%~dp0frontend\index.html"

echo.
echo ========================================================
echo   Aplicacao iniciada com sucesso! 
echo   Para fechar o servidor, basta fechar a janela preta.
echo ========================================================
pause