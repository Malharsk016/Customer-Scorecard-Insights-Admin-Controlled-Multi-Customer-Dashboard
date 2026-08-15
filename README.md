# 📊 Customer Scorecard & Insights

> A Bosch-branded, single-page web dashboard for managing IATF & Non-IATF customer scorecards, project updates, and audit reports with admin-controlled data editing and PDF report management.

---

## 📌 Overview

**Customer Scorecard & Insights** is a fully self-contained, browser-based quality tracking tool built for Bosch. It provides a centralized interface to monitor and manage customer performance data across scorecards, project updates, and audit reports with no backend infrastructure required.

---

## ✨ Features

- 🏢 **Multi-Customer Dashboard** : Supports IATF and Non-IATF customer categories
- 📋 **Scorecard View** : Filter by vendor code, view ratings (A–D), and upload PDF scorecards
- 📁 **Project Updates** : Track project name, status, timeline, and attach report files
- ✅ **Audit Status** : Log audit dates, types, OPL completion counts, and upload audit PDFs
- 🔐 **Admin Login** : Role-based authentication reveals hidden edit controls
- 📤 **PDF Upload & Preview** : Upload PDFs with progress bar simulation and inline iframe preview
- 💾 **Data Persistence** : Customer data stored and reloaded via `localStorage`
- 📱 **Responsive Layout** : CSS Grid & Flexbox with media query breakpoints

---

## 🗂️ Project Structure

```
project/
│
├── index.html              # Main single-page application
├── bosch.jpg               # Bosch navbar logo
│
├── IATF Customer Logos
│   ├── gm.jpeg             # General Motors
│   ├── vw.jpeg             # Volkswagen
│   ├── stellantis.jpeg     # Stellantis
│   └── renault.jpeg        # Renault
│
├── Non-IATF Customer Logos
│   ├── msil.jpeg           # Maruti Suzuki (MSIL)
│   ├── honda.jpeg          # Honda
│   ├── tvs.png             # TVS
│   ├── mazda.png           # Mazda
│   └── vinfast.jpeg        # Vinfast
│
└── Dashboard Previews
    ├── scorebpard.png      # Scorecard preview image
    ├── report.png          # Project updates preview image
    └── audit.png           # Audit status preview image
```

---

## 🚀 Getting Started

### Prerequisites
* Any modern web browser (Chrome, Edge, Firefox, Safari)
* No installations, servers, or dependencies required

### Running the App
1. Clone or download the project folder
2. Ensure all image assets are in the same directory as `index.html`
3. Open `index.html` in your browser

```bash
# Simply open in browser
open index.html
# or
double-click index.html
```

---

## 🔐 Admin Access

Click the **Login** button in the navbar to access the admin panel.

| Role  | Access Level                          |
|-------|---------------------------------------|
| Guest | View-only access to all dashboards    |
| Admin | Full edit access to all customer data |

> Admin credentials are verified via the `verifyCredentials()` function in the script. Update this function to integrate with your authentication system.

---

## 📄 Pages & Navigation

| Page               | Description                                         |
|--------------------|-----------------------------------------------------|
| Home               | Customer selection grid (IATF & Non-IATF)           |
| Customer Overview  | Highlights and navigation to sub-sections           |
| Scorecard          | View/upload vendor scorecards with ratings          |
| Project Updates    | Track ongoing and completed projects                |
| Audit Status       | View audit history, OPL stats, and upload reports   |

---

## 🛠️ Tech Stack

| Technology       | Usage                                         |
|------------------|-----------------------------------------------|
| HTML5            | Page structure and semantic layout            |
| CSS3             | Styling, Flexbox/Grid layout, responsiveness  |
| Vanilla JavaScript | Page routing, DOM manipulation, logic       |
| FileReader API   | PDF file reading and array buffer handling    |
| localStorage API | Client-side data persistence per customer     |
| iFrame           | Inline PDF preview after upload               |

---

## 📦 Key Functionalities

### PDF Upload Flow
1. Admin selects a PDF file (max **10MB**)
2. File size validation triggers an alert if exceeded
3. Simulated upload progress bar animates to 100%
4. PDF is previewed inline via `URL.createObjectURL()`
5. File metadata (name, date, size) is saved to `localStorage`

### Data Management
* `saveCustomerData(customerName, section, data)` : Persists data to localStorage
* `getCustomerData(customerName, section)` : Retrieves stored data
* `loadCustomerData(customerName)` : Loads all sections on customer navigation
* `initializeCustomerData()` : Seeds default structure on first load

---

## 🖥️ Supported Customers

| Category     | Customers                                      |
|--------------|------------------------------------------------|
| IATF         | General Motors, VW, Stellantis, Renault        |
| Non-IATF     | MSIL, Honda, TVS, Mazda, Vinfast               |

---

## ⚠️ Known Limitations

* PDF file contents are **not** permanently stored in localStorage (only metadata is saved); actual files are session-based via `URL.createObjectURL()`
* Admin credentials should be secured server-side for production use
* No backend or database — all data resets on browser cache clear

---

## 🔮 Future Improvements

* [ ] Backend integration (Node.js / Firebase) for persistent file storage
* [ ] Export scorecard data as Excel or PDF report
* [ ] Email notifications for audit deadlines
* [ ] Search and filter across all customers
* [ ] Dark mode support

---

## 👤 Author

Developed for **Bosch** internal quality and customer management operations.

---

## 📃 License

This project is intended for internal Bosch use only. Unauthorized distribution is prohibited.
