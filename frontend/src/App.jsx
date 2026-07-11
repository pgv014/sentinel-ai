import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [devices, setDevices] = useState([]);
  const [lastUpdated, setLastUpdated] = useState("");

  const fetchData = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:8000/analysis");
      setDevices(res.data);
      setLastUpdated(new Date().toLocaleTimeString());
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchData();
    const interval = setInterval(fetchData, 3000);
    return () => clearInterval(interval);
  }, []);

  const healthy = devices.filter(
    (d) => d.severity === "Healthy"
  ).length;

  const warning = devices.filter(
    (d) => d.severity === "Medium"
  ).length;

  const critical = devices.filter(
    (d) => d.severity === "High" || d.severity === "Critical"
  ).length;

  return (
    <div className="container">
      <h1>🛰 Sentinel AI Dashboard</h1>

      <p className="subtitle">
        Live monitoring of industrial equipment with predictive risk analysis.
      </p>

      <p className="last-updated">
        Last Updated: {lastUpdated}
      </p>

      <div className="cards">
        <div className="card green">
          <h2>{healthy}</h2>
          <p>Healthy</p>
        </div>

        <div className="card yellow">
          <h2>{warning}</h2>
          <p>Warning</p>
        </div>

        <div className="card red">
          <h2>{critical}</h2>
          <p>Critical</p>
        </div>
      </div>

      <table>
        <thead>
          <tr>
            <th>Device</th>
            <th>Risk</th>
            <th>Status</th>
            <th>Temperature</th>
            <th>Vibration</th>
            <th>Pressure</th>
            <th>Power</th>
            <th>Recommendation</th>
          </tr>
        </thead>

        <tbody>
          {devices.map((d) => (
            <tr
              key={d.device}
              style={{
                background:
                  d.risk >= 80
                    ? "#ffe5e5"
                    : d.risk >= 60
                    ? "#fff3cd"
                    : "white",
              }}
            >
              <td>{d.device}</td>

              <td>
                <strong>{d.risk}%</strong>
              </td>

              <td>
                <span
                  style={{
                    padding: "6px 12px",
                    borderRadius: "20px",
                    color: "white",
                    background:
                      d.severity === "Critical"
                        ? "#dc2626"
                        : d.severity === "High"
                        ? "#ea580c"
                        : d.severity === "Medium"
                        ? "#ca8a04"
                        : "#16a34a",
                  }}
                >
                  {d.severity}
                </span>
              </td>

              <td>{d.temperature.toFixed(1)}</td>
              <td>{d.vibration.toFixed(2)}</td>
              <td>{d.pressure.toFixed(1)}</td>
              <td>{d.power.toFixed(1)}</td>
              <td>{d.recommendation}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;