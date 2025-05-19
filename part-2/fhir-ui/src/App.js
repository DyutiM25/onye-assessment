import React, { useState } from "react";
import axios from "axios";

// Chart.js setup
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
} from "chart.js";
import { Bar } from "react-chartjs-2";

ChartJS.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend);

function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  const handleSubmit = () => {
    axios
      .post("http://localhost:5000/parse", { query })
      .then((res) => {
        setResults(res.data.patients);
      })
      .catch((err) => {
        console.error("API error:", err);
        alert("Something went wrong! Is your backend running?");
      });
  };

  // Chart data based on results
  const chartData = {
    labels: results.map((p) => p.name),
    datasets: [
      {
        label: "Patient Age",
        data: results.map((p) => p.age),
        backgroundColor: "rgba(75, 192, 192, 0.6)",
        borderRadius: 5,
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    plugins: {
      legend: { position: "top" },
    },
  };

  return (
    <div style={{ padding: 20, fontFamily: "Arial, sans-serif" }}>
      <h2>FHIR Query Tool</h2>

      <div style={{ marginBottom: 20 }}>
        <input
          type="text"
          placeholder="Enter a health query"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          style={{ width: 300, padding: 8 }}
        />
        <button onClick={handleSubmit} style={{ marginLeft: 10, padding: "8px 16px" }}>
          Submit
        </button>
      </div>

      {results.length > 0 && (
        <>
          <h3>Age Distribution</h3>
          <div style={{ maxWidth: 600, margin: "0 auto 30px auto" }}>
            <Bar data={chartData} options={chartOptions} />
          </div>

          <h3>Results</h3>
          <div style={{ overflowX: "auto" }}>
            <table
              border="1"
              cellPadding="10"
              style={{
                borderCollapse: "collapse",
                width: "100%",
                maxWidth: 600,
                margin: "0 auto",
              }}
            >
              <thead style={{ backgroundColor: "#f0f0f0" }}>
                <tr>
                  <th>Name</th>
                  <th>Age</th>
                  <th>Condition</th>
                </tr>
              </thead>
              <tbody>
                {results.map((p, idx) => (
                  <tr key={idx}>
                    <td>{p.name}</td>
                    <td>{p.age}</td>
                    <td>{p.condition}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </>
      )}
    </div>
  );
}

export default App;
