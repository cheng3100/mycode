@echo off
set DEST=.\.exvim.jos
set TOOLS=D:\Soft\exVim\vimfiles\tools\
set TMP=%DEST%\_symbols
set TARGET=%DEST%\symbols
call %TOOLS%\shell\batch\update-symbols.bat
