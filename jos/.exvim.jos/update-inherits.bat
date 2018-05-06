@echo off
set DEST=.\.exvim.jos
set TOOLS=D:\Soft\exVim\vimfiles\tools\
set TMP=%DEST%\_inherits
set TARGET=%DEST%\inherits
call %TOOLS%\shell\batch\update-inherits.bat
