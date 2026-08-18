# xrwvm-fullstack_developer_capstone

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0-092E20.svg)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED.svg)](https://www.docker.com/)

A comprehensive **Car Dealership Management & Review Platform** built using Python, Django, Express/MongoDB microservices, and React. The system features automated sentiment analysis for dealer reviews, state-based dealership filtering, and containerized deployment workflows using Docker.

---

## 🚀 Key Features

### For Customers
* **Browse & Discover:** Search vehicle inventories and locate dealerships across various US states.
* **Sentiment-Analyzed Reviews:** View customer feedback categorized into Positive, Neutral, or Negative sentiment.
* **Submit Reviews:** Registered users can post detailed reviews for specific car makes, models, and purchase years.
* **User Authentication:** Secure signup, login, and session persistence.

### For Dealerships & Admins
* **Dealership Directory Management:** Manage dealership records, addresses, and state listings.
* **Vehicle Inventory Control:** Add, update, and track car makes, models, and technical specifications.
* **Review Moderation:** Monitor incoming customer reviews and feedback trends.

---

## 🛠️ Tech Stack

* **Core Backend:** Python 3.12, Django Framework, Gunicorn WSGI
* **Microservices:** Express.js, Node.js, MongoDB (Dealership & Review Microservices)
* **Frontend:** React.js, Bootstrap 5, JavaScript (ES6+)
* **Containerization:** Docker, Dockerfiles
* **CI/CD Pipeline:** GitHub Actions (`flake8` for Python, `jshint` for JavaScript)

---

## 📂 Repository Structure

```text
xrwvm-fullstack_developer_capstone/
├── .github/
│   └── workflows/
│       └── main.yaml            # GitHub Actions CI/CD pipeline
├── server/
│   ├── Dockerfile               # Production Docker image build file
│   ├── requirements.txt         # Python backend dependencies
│   ├── entrypoint.sh            # Container startup execution script
│   ├── djangoproj/              # Django project core settings
│   ├── djangoapp/               # Main Django application app
│   └── database/                # Express.js & MongoDB microservices
├── frontend/                    # React frontend application
├── .gitignore
└── README.md                    # Project documentation