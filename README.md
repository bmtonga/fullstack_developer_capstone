
#fullstack_developer_capstone
# The Auto Hub

A comprehensive **Car Dealership Management System** designed to streamline operations for both dealerships and customers. This platform serves as a bridge between buyers and sellers, offering advanced features for vehicle discovery, inventory management, and customer engagement.

## 🚀 Key Features

### For Customers
- **Browse & Discover**: Explore a diverse inventory of new and used vehicles with detailed specifications and high-quality images.
- **Advanced Search & Filtering**: Find the perfect car instantly using powerful filters (make, model, year, price, mileage, etc.).
- **Detailed Vehicle Pages**: View complete vehicle information including specs, pricing, features, and status (available/sold).
- **User Authentication**: Secure login and profile management for a personalized experience.
- **Wishlist & Favorites**: Save vehicles of interest for future reference.

### For Dealerships (Admin)
- **Inventory Management**: Seamlessly add, update, and remove vehicle listings.
- **Vehicle Details Control**: Manage specific attributes like price, status, images, description, and mileage.
- **User Management**: Track and manage all registered users and customers.
- **Reporting**: Generate insights and reports on dealership performance (future integration).

## 🛠️ Tech Stack

This project is built with a modern, robust **MERN** (MongoDB, Express.js, React, Node.js) stack.

### Frontend
- **Framework**: [React.js](https://reactjs.org/)
- **Language**: JavaScript (ES6+)
- **Styling**:
  - [Tailwind CSS](https://tailwindcss.com/) for utility-first styling.
  - [CSS Modules](https://github.com/css-modules/css-modules) for component-scoped styles.
- **Routing**: [React Router](https://reactrouter.com/)
- **Build Tool**: Vite

### Backend
- **Runtime**: [Node.js](https://nodejs.org/)
- **Framework**: [Express.js](https://expressjs.com/)
- **Database**: [MongoDB](https://www.mongodb.com/)
- **ORM/ODM**: [Mongoose](https://mongoosejs.com/)
- **Authentication**: JWT (JSON Web Tokens)
- **API Type**: RESTful API

## 📂 Project Structure

```
The Auto Hub/
├── frontend/         # React.js Client Application
│   ├── src/
│   │   ├── components/ # Reusable UI Components
│   │   ├── pages/      # Page Components (Home, Login, Dashboard, etc.)
│   │   ├── services/   # API Service Layer
│   │   └── App.jsx     # Root Component
│   ├── package.json
│   └── vite.config.js
├── backend/          # Node.js / Express Server
│   ├── config/       # Database Configuration
│   ├── controllers/  # Request Handlers
│   ├── models/       # Mongoose Schemas
│   ├── routes/       # API Route Definitions
│   ├── server.js     # Application Entry Point
│   └── package.json
├── .gitignore
├── README.md         # Project Documentation
└── package.json      # Root Level (if any)
```

## 🚀 Getting Started

### Prerequisites
- [Node.js](https://nodejs.org/) (v14 or higher)
- [npm](https://www.npmjs.com/) (usually comes with Node.js)
- [MongoDB](https://www.mongodb.com/try/download/community) (local or cloud service like Atlas)

### Installation

1. **Clone the repository** (if using Git)
   ```bash
   git clone <repository-url>
   cd TheAutoHub
   ```

2. **Install Backend Dependencies**
   ```bash
   cd backend
   npm install
   ```

3. **Install Frontend Dependencies**
   ```bash
   cd ../frontend
   npm install
   ```

### Configuration

Ensure your backend is connected to your MongoDB database. You can configure the connection string in `backend/config/db.js` or via environment variables.

Example `backend/.env`:
```env
PORT=5000
MONGODB_URI=mongodb://localhost:27017/autohub
JWT_SECRET=your_secure_secret_here
```

### Running the Application

You can start both the backend and frontend simultaneously using a concurrent script (if configured) or by running them in separate terminal windows.

**Terminal 1: Backend**
```bash
cd backend
npm run dev
```
*(This will typically start the server on `http://localhost:5000`)*

**Terminal 2: Frontend**
```bash
cd frontend
npm run dev
```
*(This will start the development server, usually on `http://localhost:5173`)*

## 🗺️ API Routes Overview

### Authentication
- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login user (returns JWT token)
- `GET /api/auth/me` - Get current logged-in user profile

### Vehicles
- `GET /api/vehicles` - Get all vehicles (supports query params for filtering)
- `GET /api/vehicles/:id` - Get a single vehicle by ID
- `POST /api/vehicles` - Create a new vehicle (Admin)
- `PUT /api/vehicles/:id` - Update a vehicle (Admin)
- `DELETE /api/vehicles/:id` - Delete a vehicle (Admin)

### Users (Admin)
- `GET /api/users` - Get all users
- `GET /api/users/:id` - Get user details
- `DELETE /api/users/:id` - Delete user (Admin)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1. Open an issue to discuss changes.
2. Create a feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
