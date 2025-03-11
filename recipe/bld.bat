mkdir %LIBRARY_INC%
if errorlevel 1 exit 1
copy %SRC_DIR%\include\cudnn*.h %LIBRARY_INC%\
if errorlevel 1 exit 1

mkdir %LIBRARY_LIB%
if errorlevel 1 exit 1
copy %SRC_DIR%\lib\x64\cudnn*.lib %LIBRARY_LIB%\
if errorlevel 1 exit 1

mkdir %LIBRARY_BIN%
if errorlevel 1 exit 1
copy %SRC_DIR%\bin\cudnn*.dll %LIBRARY_BIN%\
if errorlevel 1 exit 1
