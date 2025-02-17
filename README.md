# Habit Tracker CLI

A simple command-line application to track daily habits using Python and Click.

## Features
- Add new habits
- Mark habits as completed
- List all tracked habits
- Show habit completion history
- Remove habits

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Ilia01/HabitTracker.git
   cd HabitTracker
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the CLI with:
```sh
python(python3) habit_tracker.py 
```

### Commands
- **Add a habit:**
  ```sh
  python habit_tracker.py add --name "Exercise"
  ```
- **Mark a habit as completed:**
  ```sh
  python habit_tracker.py complete --name "Exercise"
  ```
- **List all habits:**
  ```sh
  python habit_tracker.py list
  ```
- **Show habit history:**
  ```sh
  python habit_tracker.py history --name "Exercise"
  ```
- **Remove a habit:**
  ```sh
  python habit_tracker.py remove --name "Exercise"
  ```

## Data Storage
The application stores habit data in a simple JSON file (`habits.json`).

## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

## License
This project is licensed under the MIT License.
