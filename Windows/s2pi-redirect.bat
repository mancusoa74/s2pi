@echo off
REM Author: Antonio Mancuso
REM Simple bat file to set windows portproxy to redirect traffic from Scratch2 Off-line editor to Raspberry-pi helper app
REM version 1.0: July 2017


set /p ip="Digita l'indirizzo IP del tuo raspberry-pi [A.B.C.D]: "
echo.
echo "Configurazione port forwadring da *:5000 -> %ip%:5000"
echo.

sc query "iphlpsvc" | find "RUNNING"
if %ERRORLEVEL% == 1 goto notrunning
if %ERRORLEVEL% == 0 goto running

:running
netsh interface portproxy reset
netsh interface portproxy add v4tov4 listenport=5000 connectport=5000 connectaddress=%ip% protocol=tcp 
netsh interface portproxy show all
echo.
echo "Configurazione completata con successo!!"
echo.
pause
goto end

:notrunning
echo "ERRORE"
echo "Il servizio IP Helper (iphlpsvc) non e' attivo. Si prega di attivare tale servizio"
echo.
pause 

:end
