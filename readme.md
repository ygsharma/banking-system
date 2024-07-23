# Banking System using Django Framework

## Overview

This project is a comprehensive banking system built using the Django framework. It encompasses various banking functionalities, including account management, loan processing, and transaction handling. The project is designed to be scalable and maintainable, making use of Django's robust features and extensibility.

## Features

- **Account Management**: Create, update, and manage user accounts with ease.
- **Loan Processing**: Apply for loans, process loan applications, and manage loan repayments.
- **Transaction Handling**: Record and track all transactions within the system.
- **Data Management**: Use JSON files for data dumps and university lists.
- **Docker Support**: Easily deploy the application using Docker and Docker Compose.

## Project Structure

banking-system/
├── accounts/                 # Updated views for account management
├── banking_system/           # Main project settings and URLs
├── core/                     # Core functionalities and utilities
├── loans/                    # Loan-related views and functionalities
├── screenshots/              # Screenshots of the website.
├── scripts/                  # Additional scripts for various tasks
├── static/                   # Static files (CSS, JS, images)
├── templates/                # HTML templates for the frontend
├── transactions/             # Transaction-related views and functionalities
├── .gitignore                # Git ignore file
├── Dockerfile                # Dockerfile for containerization
├── config.yml                # Configuration file for Docker Compose
├── docker-compose.yml        # Docker Compose configuration
├── manage.py                 # Django management script
├── readme.md                 # Project README file
├── relational_model.png      # Relational model diagram
├── requirements.jpg          # Image of requirements
├── requirements.txt          # Python dependencies


## Setup Instructions

### Prerequisites

- Python 3.x
- Docker (optional, for containerization)
- Git (for version control)

### Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/ygsharma/banking-system.git
    cd banking-system
    ```

2. **Create and Activate a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the Requirements**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**
    ```bash
    python manage.py migrate
    ```

5. **Run the Application**
    ```bash
    python manage.py runserver
    ```

### Using Docker (Optional)

1. **Build the Docker Image**
    ```bash
    docker build -t banking-system .
    ```

2. **Run the Docker Container**
    ```bash
    docker-compose up
    ```

## Usage

- Access the application at `http://127.0.0.1:8000` after running the server.
- Use the admin panel at `http://127.0.0.1:8000/admin` for administrative tasks (create a superuser using `python manage.py createsuperuser`).

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact [Your Name](mailto:your.email@example.com).
