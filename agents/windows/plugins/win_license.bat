<<<<<<< HEAD
@echo off
REM
REM plugin to gather and output Windows activation status
REM
=======
set VERSION="2.0.0i2"
@echo off
REM ***
REM * plugin to gather and output Windows activation status
REM ***
>>>>>>> upstream/master

echo ^<^<^<win_license^>^>^>
cscript //NoLogo %windir%/System32/slmgr.vbs /dli
