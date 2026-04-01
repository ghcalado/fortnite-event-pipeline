# 🎮 Fortnite Event Pipeline

Para uma experiência de Ingestão de Dados em Tempo Real.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Data Engineering](https://img.shields.io/badge/Data-Engineering-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

---

## 📌 Overview
The **Fortnite Event Pipeline** is a simulation tool designed to replicate how modern games handle massive streams of data. It generates randomized match events (kills, loot, movement, spawns) and structures them into a relational database.

This project demonstrates the core pillars of Data Engineering: **Ingestion**, **Transformation**, and **Persistence**, while maintaining a clean, modular architecture.

## ✨ Features
| Feature | Description |
| :--- | :--- |
| 🚀 **Real-Time Simulation** | Generates events with variable delays to mimic actual gameplay. |
| 🛠️ **Modular Architecture** | Separated logic for configuration, database management, and execution. |
| 📊 **Relational Mapping** | Transforms random unstructured events into structured SQL rows. |
| 🛡️ **Data Integrity** | Uses SQLite transactions to ensure every kill and loot is saved safely. |
| 🗃️ **Persistence** | Local storage in `.db` format for historical match analysis. |

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Database:** SQLite3 (SQL)
* **Design Pattern:** Producer-Storage Modular Architecture

## ⚡ Getting Started

### Prerequisites
* Python 3.x installed.
* No external libraries needed (Standard Library only).

### Installation & Running
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ghcalado/fortnite-event-pipeline.git](https://github.com/ghcalado/fortnite-event-pipeline.git)

    Navigate to the project folder:
    Bash

    cd fortnite-event-pipeline

    Run the pipeline:
    Bash

    python3 main.py

    Note: The database file fortnite.db will be created automatically inside the data/ folder.

🗂️ Project Structure
Plaintext

fortnite-event-pipeline/
├── main.py          # Application entry point and event loop
├── data/            # Local directory for the SQLite database
├── src/
│   ├── config.py    # Game constants (Skins, Weapons, Locations)
│   └── database.py  # SQL connection and insertion logic
├── .gitignore       # Prevents the database file from being committed
├── requirements.txt  # Project metadata
└── README.md        # Professional documentation

🖥️ How It Works

    Configuration: The src/config.py defines the "universe" of the match.

    Event Loop: main.py picks a random event and assembles the metadata.

    Ingestion: The src/database.py executes the INSERT INTO command.

    Storage: All match history is stored in tabela_eventos, ready for SQL analysis.

🔒 Security & Privacy

    The database file is strictly excluded from version control via .gitignore.

    This is a local-first project: no data is sent to external servers or APIs.

Author: Ghabriel Calado

Python & Web Developer | CS Student
