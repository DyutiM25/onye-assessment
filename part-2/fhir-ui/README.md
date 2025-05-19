
# 🩺 FHIR Query Tool – Natural Language Interface for Simulated Healthcare Data

This project is a full-stack application built as part of the **Full-Stack Engineer – AI on FHIR** assessment. It lets users type natural language queries like:

> _"Show me all diabetic patients over 50"_

and receive simulated patient data, both in table and chart form.

---

## 🧠 Features

- ✅ Accepts natural language health queries
- ✅ Extracts intent using **spaCy** NLP (e.g., age, condition)
- ✅ Simulates FHIR-like patient data
- ✅ Renders results in a table
- ✅ Displays age distribution using `react-chartjs-2` (bar chart)
- ✅ Built with Flask (Python) and React (JavaScript)

---

## 🧪 Example Queries

You can try:

- `Show me diabetic patients over 50`
- `List asthma patients under 18`
- `Find cancer patients older than 60`
- `Get flu patients below 40`
- `Show covid patients`
- `Find hypertension patients aged 45`

---

## 📦 Project Structure

```

root/
├── part-1/               # Backend (Flask + spaCy)
│   ├── app.py
│   ├── fhir\_query\_parser.py
├── part-2/fhir-ui/       # Frontend (React)
│   ├── src/App.js
│   ├── public/
│   └── package.json

````

---

## 🚀 Getting Started

### Backend (Python Flask + spaCy)

1. Navigate to the backend folder:

   cd part-1

2. Create a virtual environment and install dependencies:

   python -m venv venv
   venv\Scripts\activate          # On Windows
   pip install flask flask-cors spacy
   python -m spacy download en_core_web_sm
  
3. Run the Flask server:

   python app.py


> ✅ The server will start on `http://localhost:5000`

---

### Frontend (React)

1. Navigate to the frontend folder:

   cd part-2/fhir-ui

2. Install the required packages:

 
   npm install

3. Start the frontend server:

   npm start

> ✅ Opens at `http://localhost:3000`
> Make sure your Flask server is running on port `5000`

---

## 📊 Technologies Used

* React (Create React App)
* Axios
* Flask (Python)
* spaCy (`en_core_web_sm`)
* Chart.js via `react-chartjs-2`

---

## 🌍 Deployment

Frontend deployed manually using **Netlify**.
👉 https://onye-assessment-dyuti-mengji.netlify.app/

---

## 🗃 Original Create React App Info

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app). See full CRA documentation [here](https://facebook.github.io/create-react-app/docs/getting-started).

---

## ✅ Deliverables Summary

| Item                     | Status |
| ------------------------ | ------ |
| Flask backend with NLP   | ✅ Done |
| React frontend with UI   | ✅ Done |
| Chart + table rendering  | ✅ Done |
| Sample inputs/outputs    | ✅ Done |
| README file              | ✅ Done |
| GitHub Repo              | ✅ Done |
| Optional: Netlify deploy | ✅ Done |

---

## 🧑‍⚕️ Author

**Dyuti M.**
Built as part of the take-home challenge for **AI on FHIR**


