# Customer Manager

Customer Manager is a client management application developed in Python using Tkinter. It allows users to manage their client database through CRUD (Create, Read, Update, Delete) operations.

## Features

- **Client Management**: Easily add, modify, and delete clients.
- **Graphical Interface**: Access the application through an intuitive user interface or via the terminal.
- **Unit Testing**: Includes unit tests to ensure the application functions correctly.

## Installation

To run Customer Manager, ensure you have Python 3 installed on your system. Then, clone this repository and navigate to the project directory.

```bash
git clone https://github.com/your_username/CustomerManager.git
cd CustomerManager
```

## Install the Necessary Dependencies

Install the dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Usage

Once the installation is complete, you can start using Customer Manager. Choose between terminal mode or graphical user interface mode:

1. **Terminal Mode**: Use this mode for a text-based interaction.

   ```bash
   python3 run.py -t
   ```

2. **User Interface (UI)**: Launch the application with a graphical interface.
   ```bash
   python3 run.py
   ```

## Running Tests

To ensure everything is working correctly, you can run the unit tests using `pytest`. Execute the following command in the project directory:

```bash
pytest tests/
```

## Project Structure

```plaintext
└── 📁CustomerManager
    ├── 📁tests
    │   ├── __init__.py
    │   ├── clients_test.csv
    │   └── test_database.py
    ├── clients.csv
    ├── config.py
    ├── database.py
    ├── helpers.py
    ├── menu.py
    ├── README.md
    ├── requirements.txt
    ├── run.py
    └── ui.py

```
