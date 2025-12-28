# Ksero Insurance Extract API

This is a FastAPI-based microservice that extracts structured data from OCR text of medical, dental, and vision insurance cards. It uses payer-specific rules to identify member ID, group number, plan name, policyholder, and more — with confidence scoring and validation.

---

## 🚀 Features

- ✅ Supports major payers: UHC, Aetna, Cigna, BCBS, Delta Dental, VSP, EyeMed, TRICARE, CHAMPVA, Medicare, Medicaid
- 🧠 Payer-specific logic for accurate extraction
- 🧾 Returns structured JSON with confidence score
- 🔐 Ready for API monetization via RapidAPI

---

## 📦 Installation

```bash
pip install -r requirements.txt
uvicorn main:app --reload