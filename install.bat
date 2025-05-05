@echo off
title Installing Bot Dependencies

echo -----------------------------------------
echo Installing required packages...

pip install discord.py
pip install aiohttp
pip install requests

echo -----------------------------------------
echo Installation complete!
pause
