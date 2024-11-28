@echo off

Net session >nul 2>&1 || (PowerShell start -verb runas '%~0' &exit /b)

REM ========================================================
REM Script para intercambiar los nombres de dos archivos
REM ========================================================

:: Configuración de variables
set "compartida=\\CANELO2\sysvol\crisol.ad.uc.cl\fondo"   REM Ruta de la carpeta compartida
set "usuario=braulio.ruiz@uc.cl"                REM Usuario para autenticar
set "password=Ewto1314$$$"                      REM Contraseña del usuario
set "archivoA=%compartida%\img0.jpg"       REM Ruta del archivo A
set "archivoB=%compartida%\img0_Encuesta1.jpg"       REM Ruta del archivo B
set "tempFile=%compartida%\temp_file.tmp"       REM Archivo temporal

:: Conectar a la carpeta compartida
echo Conectando a la carpeta compartida...
net use %compartida% /user:%usuario% %password% /persistent:no
if %errorlevel% neq 0 (
    echo Error: No se pudo conectar a la carpeta compartida.
    exit /b 1
)
echo Conexion exitosa.

:: Verificar la existencia de los archivos
if exist "%archivoA%" if exist "%archivoB%" (
    echo Intercambiando nombres de archivos...
    
    :: Intercambiar nombres usando un archivo temporal
    rename "%archivoA%" "temp_file.tmp" || (echo Error al renombrar %archivoA% a temporal && exit /b 1)
    rename "%archivoB%" "img0.jpg" || (echo Error al renombrar %archivoB% a img0.jpg && exit /b 1)
    rename "%tempFile%" "img0_Encuesta1.jpg" || (echo Error al renombrar archivo temporal a img0_Encuesta1.jpg && exit /b 1)
    echo Intercambio completado exitosamente.
) else (
    echo Error: Uno o ambos archivos no existen en la ruta especificada.
    echo Verifique las rutas: 
    echo - Archivo A: %archivoA%
    echo - Archivo B: %archivoB%
    exit /b 1
)

:: Desconectar la carpeta compartida
echo Desconectando de la carpeta compartida...
net use %compartida% /delete /yes
if %errorlevel% neq 0 (
    echo Advertencia: No se pudo desconectar de la carpeta compartida.
) else (
    echo Desconexion exitosa.
)

:: Finalizar
echo Proceso completado.
exit /b 0
