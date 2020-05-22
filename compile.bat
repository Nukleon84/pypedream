REM SET PATH=%PATH%;C:\Program Files (x86)\Microsoft Visual C++ Build Tools
REM set CLPATH="C:\Program Files (x86)\Microsoft Visual Studio 15.0\VC\bin\amd64\cl.exe"

set "var=%cd%"
call "C:\Program Files (x86)\Microsoft Visual C++ Build Tools\vcbuildtools.bat"

cd %var%
g:
python setup.py build_ext --inplace
