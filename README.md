# Fake Data Generator

This project is designed to generate random fake data, such as name, age, gender, phone number, passport details, and credit history. Data can be generated for different countries: Russia (ru), Poland (pl), USA (us).

## Requirements

To use the script, Python version 3.6 or higher and the `Faker` library are required.

### Installing Dependencies

1. **Install Python** (if not already installed):
   - For Ubuntu/Debian-based distributions, you can install Python with the following command:

     ```bash
     sudo apt update
     sudo apt install python3 python3-pip
     ```

2. **Install required dependencies** using `pip`:

    ```bash
    pip install faker
    ```
    **Or install for linux** using `pip3`:

   ```bash
    pip3 install faker --break-system-packages
    ```

## Usage

### Running from the Command Line

To run the script, use the command with arguments that define the country and the level of data generation:

```bash
python fakeus.py -c <country> -l <level>
```
