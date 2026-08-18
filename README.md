# fullstack_developer_capstone
# The Auto Hub

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Stack](https://img.shields.io/badge/Stack-MERN-blue.svg)](https://react.dev)
[![Build](https://img.shields.io/badge/Build-Vite-646CFF.svg)](https://vitejs.dev)

A comprehensive **Car Dealership Management System** designed to streamline operations for both dealerships and customers. The platform serves as a bridge between automotive buyers and sellers, offering advanced features for vehicle discovery, inventory management, customer engagement, and review analytics.

---

## 🚀 Key Features

### For Customers
* **Browse & Discover:** Explore a diverse inventory of new and pre-owned vehicles complete with detailed technical specifications and high-quality image galleries.
* **Advanced Search & Filtering:** Filter vehicles dynamically by make, model, year, price range, state, and mileage.
* **Detailed Vehicle Pages:** Access full vehicle specifications, real-time availability status, pricing, and seller details.
* **Sentiment-Analyzed Reviews:** Read authentic customer feedback backed by automated sentiment analysis (Positive, Neutral, Negative).
* **Wishlist & Favorites:** Save vehicles of interest to personal profiles for quick reference.

### For Dealerships & Admins
* **Inventory Management:** Effortlessly create, update, and remove vehicle listings across multiple branches.
* **Vehicle Attribute Control:** Manage price updates, availability status, media assets, descriptions, and mileage records.
* **User & Review Management:** Review registered user accounts and moderate incoming customer feedback.
* **Performance Reporting:** Track platform interaction metrics and inventory turnover trends.

---

## 🛠️ Tech Stack

Built on a modern **MERN** microservices and monolithic hybrid architecture:

### Frontend
* **Framework:** [React.js](https://react.dev/) (v18+)
* **Build Tool:** [Vite](https://vitejs.dev/)
* **Routing:** [React Router](https://reactrouter.com/) (v6+)
* **Styling:** Bootstrap 5 & CSS3
* **Language:** JavaScript (ES6+)

### Backend & Database
* **Runtime:** [Node.js](https://nodejs.org/)
* **Framework:** [Express.js](https://expressjs.com/) & Django
* **Database:** [MongoDB](https://www.mongodb.com/) (Atlas / Local)
* **ORM/ODM:** [Mongoose](https://mongoosejs.com/)
* **Authentication:** JSON Web Tokens (JWT) & Session Storage
* **API Architecture:** RESTful APIs

---

## 📂 Project Structure

```text
TheAutoHub/
├── frontend/                  # React + Vite Client Application
│   ├── src/
│   │   ├── assets/           # Static media, icons, and stylesheets
│   │   ├── components/       # Reusable UI components (Header, Cards, Modals)
│   │   ├── pages/            # View components (Home, Dealers, PostReview, Login)
│   │   ├── services/         # API integration services
│   │   ├── App.jsx           # Application route definitions
│   │   └── main.jsx          # React DOM entry point
│   ├── package.json
│   └── vite.config.js
├── backend/                   # Express.js Server & Microservices
│   ├── config/               # Database and environment configurations
│   ├── controllers/          # API business logic and route handlers
│   ├── models/               # Mongoose database schemas
│   ├── routes/               # Express endpoint definitions
│   ├── server.js             # Express application entry point
│   └── package.json
├── .gitignore
├── LICENSE                   # Project software license
└── README.md                 # Project documentation