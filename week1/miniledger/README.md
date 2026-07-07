# MiniLedger
A command-line banking app built in Python.

## Features
- Deposit and withdraw funds
- Check balance
- View full transaction history with timestamps
- Data persists across sessions using JSON storage

## Tech Stack
- Python 3.14
- JSON for data persistence

## How to Run
```bash
cd miniledger
python main.py
```

## Project Structure
- `main.py` — menu and user interaction
- `account.py` — BankAccount class and logic  
- `storage.py` — file save/load functions