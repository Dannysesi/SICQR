# SICQR - Student identity Card with QR code 
---
This Django-based web application manages student identity cards with QR code scanning. It automates the generation of unique QR codes for each student, linking to their information.

## Features

- **Automatic QR Code Generation:** QR codes are dynamically generated and linked to each student's information.
- **Efficient Student ID Management:** Streamlined processes for creating, updating, and displaying student identity cards.
- **Enhanced Security:** Improved security features with QR code authentication and quick verification.

## Getting Started

To run this project locally, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/Dannysesi/SICQR
   # Install Dependencies:
   pip install -r requirements.txt
   # Apply migrations:
   python manage.py migrate
   # Create superuser:
   python manage.py createsuperuser
   # Runserver (default: http://localhost:8000)
   python manage.py runserver

2. Contributing:

If you'd like to contribute to this project, please follow these steps:

```bash
# Fork the repository
git clone https://github.com/Dannysesi/SICQR
cd BookHaven

# Create a new branch for your feature
git checkout -b feature-name

# Make your changes and commit them
git add .
git commit -m 'Add some feature'

# Push to the branch
git push origin feature-name


## License

[MIT](https://choosealicense.com/licenses/mit/)

