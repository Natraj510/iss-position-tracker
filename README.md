# Real-Time International Space Station (ISS) Data Pipeline

An automated, lightweight ETL (Extract, Transform, Load) pipeline that fetches the live coordinates of the International Space Station (ISS), processes the telemetry data, and maintains a local time-series dataset.

## 🛠️ Tech Stack & Concepts
- **Language:** Python 3.11
- **Libraries:** Pandas, Requests, Time/Datetime
- **Orchestration:** Cron (Scheduled to run every 2 minutes)
- **Data Engineering Concepts:** API Ingestion, JSON Flattening, Schema Standardization, Append-Mode File I/O.

## 🏗️ Architecture Flow
1. **Extract:** Queries the public Open-Notify API to fetch raw JSON telemetry.
2. **Transform:** Normalizes the nested JSON string, extracts latitude/longitude, and parses Unix timestamps into readable standard timestamps.
3. **Load:** Appends rows to a centralized data store while managing write safety (`index=False`) to avoid schema corruption.
