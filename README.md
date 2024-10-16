# MapMitra - Connecting Donors with NGOs

MapMitra is an AI-powered platform designed to help donors easily connect with nearby NGOs or receivers in need of donations. The application utilizes geolocation to display real-time NGO locations and offers a seamless way to schedule pick-ups or directly donate items in person.

## Parent Repository: [Sankalp](https://github.com/LAKSHYA1509/HackIndia-Spark-3-Hackn-Roll)

## Table of Contents

- [Technology Used](#technology-used)
- [Core Features](#core-features)
- [How Users Can Use It](#how-users-can-use-it)
- [Installation Instructions](#installation-instructions)
- [Usage Instructions](#usage-instructions)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## Technology Used

### Frontend:
- **HTML, CSS, JavaScript**: Provides a smooth, responsive, and user-friendly interface with animations and smooth scrolling for better user experience.

### Backend:
- **Python**: Manages server-side operations and processes user interactions.

### Database:
- **MongoDB/MySQL**: Used to store donor, receiver, and NGO data.

### API:
- **Google Maps API**: Provides geolocation services and maps, enabling users to find nearby NGOs and get real-time directions.

---

## Deployment
## You can see the site: [MapMitra](https://komal-bhardwaj.github.io/Mapmitra/)

## Core Features

- **Geolocation Services**: Displays nearby NGOs based on the donor’s location using Google Maps API.
  
- **Donation Management**: Facilitates donations of goods such as food, clothes, and essential items.
  
- **Real-Time Directions**: Offers route directions to help donors drop off their donations at an NGO.

- **Pick-up Scheduling**: Allows donors to schedule pickups for their donations.

- **Inventory Management**: Donors can select items from their profile's inventory to donate.

---

## How Users Can Use It

### 1. Sign Up / Login
- Users can create a new account or log in using their credentials to access the platform's features.

### 2. Search for Nearby NGOs
- Once logged in, users can search for nearby NGOs or receivers based on their current location. The platform will display a map with real-time data of NGO locations and specific donation needs.

### 3. Select Items for Donation
- Users can choose from their inventory of items (such as clothes, food, etc.) and opt to donate them to a selected NGO.

### 4. Deliver or Schedule Pickup
- Users can either follow the real-time directions provided to deliver items directly or schedule a pickup through the platform, making it convenient to donate without hassle.

---

## Installation Instructions

### 1. Clone the Repository
```bash
git clone https://komal-bhardwaj.github.io/Mapmitra/
```

### 2. Navigate to the Project Directory
```bash
cd project-folder
```

### 3. Install Dependencies
Ensure you have **Node.js** and **npm** installed. Then, run the following command:
```bash
npm install
```

### 4. Set up Environment Variables
Create a `.env` file in the root directory and add the following:
```
GOOGLE_MAPS_API_KEY=your_google_maps_api_key
DB_CREDENTIALS=your_database_credentials
```

### 5. Run the Project
Start the server with:
```bash
npm start
```

### 6. Access the Application
Open your browser and go to:
```
http://localhost:3000
```

---

## Usage Instructions

1. **Sign Up/Login**: Create an account or log in to gain access to the donation features.
  
2. **Search for Nearby NGOs**: Use the search feature to find NGOs near your current location. The map will display the locations and details of NGOs in need.

3. **Select Items for Donation**: From your inventory, choose the items you want to donate.

4. **Deliver or Schedule Pickup**: Follow the directions on the map to deliver the items directly to the NGO, or use the pick-up scheduling feature to arrange for the NGO to collect your donations.

---

## Future Enhancements

- **AI-Powered Donation Matching**: Using AI to recommend NGOs or receivers based on the donor's history and preferences.
  
- **Real-Time NGO Needs**: Adding a live feed to show NGOs' urgent needs.
  
- **Automated Pickup Scheduling**: Integrating logistics services for automated pickup scheduling.

---

## Contributing

We welcome contributions from developers! If you’d like to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Create a new Pull Request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


