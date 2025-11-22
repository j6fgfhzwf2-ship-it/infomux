#!/bin/bash
pyinstaller --noconfirm --onefile --windowed --add-data "ui:ui" app.py
echo "Build macOS terminé"

