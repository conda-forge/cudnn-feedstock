rem The redist archives nest the binaries under an architecture directory.
set "ARCH_DIR=x64"
if /I "%target_platform%" == "win-arm64" set "ARCH_DIR=arm64"

if not exist %LIBRARY_INC% (
    mkdir %LIBRARY_INC%
    if errorlevel 1 exit 1
)

copy %SRC_DIR%\include\cudnn*.h %LIBRARY_INC%\
if errorlevel 1 exit 1

if not exist %LIBRARY_LIB% (
    mkdir %LIBRARY_LIB%
    if errorlevel 1 exit 1
)

copy %SRC_DIR%\lib\%ARCH_DIR%\cudnn*.lib %LIBRARY_LIB%\
if errorlevel 1 exit 1

if not exist %LIBRARY_BIN% (
    mkdir %LIBRARY_BIN%
    if errorlevel 1 exit 1
)

copy %SRC_DIR%\bin\%ARCH_DIR%\cudnn*.dll %LIBRARY_BIN%\
if errorlevel 1 exit 1
