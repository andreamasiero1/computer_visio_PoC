# test_setup.py — verifica che le librerie siano installate correttamente

print("Controllo librerie...")

import cv2
print(f"✅ OpenCV: {cv2.__version__}")

import numpy as np
print(f"✅ NumPy: {np.__version__}")

from ultralytics import YOLO
print(f"✅ Ultralytics (YOLOv8) installato")

import torch
print(f"✅ PyTorch: {torch.__version__}")

# Controlla se il Mac ha Apple Silicon (M1/M2/M3)
if torch.backends.mps.is_available():
    print("🚀 Trovato Apple Silicon! Useremo MPS per accelerare")
else:
    print("💻 Useremo CPU (va bene per il testing)")

print("\nTutto ok! Sei pronto per il prossimo step.")