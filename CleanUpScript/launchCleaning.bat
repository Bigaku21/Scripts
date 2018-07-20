python-base-3.6.5 %~dp0deleteOldReports.py
echo %date:~-4,4%-%date:~-10,2%-%date:~-7,2% %time:~0,2%:%time:~3,2%:%time:~6,2% >> %cd%\cleaning_logs.txt