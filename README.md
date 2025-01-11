cd..# Project Title: Preskool - Dashboard

## Description
Preskool is a web application designed for managing student information and school administration. It provides a user-friendly interface for administrators to manage student records, view dashboards, and handle authentication.

## Technology Stack
- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite
- **Version Control**: Git

## Functionality
- **Student Management**: Add, edit, and view student details.
- **Authentication**: User login and registration functionality.
- **Dashboard**: Overview of student statistics and notifications.
- **Error Handling**: Custom error pages, including a 404 page for not found errors.

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd home
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage
- Access the application at `http://127.0.0.1:8000/`.
- Use the login page to access the dashboard.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
