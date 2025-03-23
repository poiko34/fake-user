# Fake Data Generator

This project is a tool to generate random fake data, such as name, age, gender, phone number, passport details, and credit history. The data can be generated for different countries: Russia (ru), Poland (pl), and the USA (us).

## Requirements

To use the script, you need to have Python version 3.6 or higher installed along with the `Faker` library.

### Installing Dependencies

1. **Install Python** (if not already installed):
   - For **Ubuntu/Debian-based distributions**, you can install Python using the following commands:

     ```bash
     sudo apt update
     sudo apt install python3 python3-pip
     ```

2. **Install required dependencies** using `pip`:

    ```bash
    pip install faker
    ```

   Or, for Linux users, install with `pip3`:

   ```bash
    pip3 install faker
    ```

3. **Alternatively, for Linux, you can use the provided setup script** to install dependencies:
   - Navigate to the `fakeus` directory:
   
     ```bash
     cd fakeus
     ```
   
   - Make the setup script executable:
   
     ```bash
     chmod +x setup.sh
     ```

   - Run the setup script:
   
     ```bash
     ./setup.sh
     ```

## Usage

### Running from the Command Line

To run the script, use the command with arguments that specify the country and the level of data generation:

#### For Windows:
```bash
python fakeus.py -c <country> -l <level>
