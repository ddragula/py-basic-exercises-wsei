# py-basic-exercises-wsei

## Description

A collection of Python programming exercises completed as part of final assignments for classes at WSEI.

## Structure

```
.
├── .venv/                # Python virtual environment
├── ex1.py                # Task 2.1 - Parameter logging decorator
├── ex2.py                # Task 2.2 - Number generator
├── ex3.py                # Task 2.3 - Retrieving data from API (universities)
├── ex4.py                # Task 2.4 - Function value calculation with multiprocessing
├── ex5.py                # Task 2.5 - BankAccount class with unit tests
├── ex6.py                # Task 2.6 - Processing data from IMGW
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies list
```

## Tasks

### 2.1 Parameter Logging Decorator
Implementation of a decorator that logs information about the name and type of input parameters of a function.

### 2.2 Number Generator
A class implementing a generator of the next `n` powers of the number `a` using the `__iter__()` and `__next__()` methods.

### 2.3 Retrieving Data from API (Universities)
A program retrieving data about universities from an API, using multithreading (`threading` module).

### 2.4 Function Value Calculation
A program calculating the values of the function:  
![Bez tytułu](https://github.com/user-attachments/assets/b2d24fb4-58c2-4657-abcd-9a7ee2b1987d)

using parallel processing (`multiprocessing` module).

### 2.5 BankAccount Class
Implementation of the `BankAccount` class with basic banking operations and unit tests using `unittest`.

### 2.6 Processing Data from IMGW
A program reading data from IMGW in XML format, processing information about wind speed, and presenting it in a bar chart.

## Requirements

- Python 3.8+
- Dependencies listed in the `requirements.txt` file

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_address>
   cd py-basic-exercises-wsei
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Each `exX.py` file can be run separately:
```bash
python ex1.py
```

## Author

Project completed by Dawid Draguła as part of final assignments for classes at WSEI.

