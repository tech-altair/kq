import React, { useState } from 'react';
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';
import { FaPlane, FaUsers, FaBell, FaChartLine, FaShoppingCart } from 'react-icons/fa';
import './App.css';

function App() {
  const [sentimentData] = useState([
    { timestamp: 'Jan', sentiment_score: 10 },
    { timestamp: 'Feb', sentiment_score: 20 },
    { timestamp: 'Mar', sentiment_score: 30 },
    { timestamp: 'Apr', sentiment_score: 40 },
    { timestamp: 'May', sentiment_score: 20 },
    { timestamp: 'Jun', sentiment_score: 50 },
    { timestamp: 'Jul', sentiment_score: 70 },
    { timestamp: 'Aug', sentiment_score: 90 },
  ]);

  return (
    <div className="App">
      <div className="sidebar">
        <h2>Kenya Airways</h2>
        <ul>
          <li className="active"><FaChartLine /> Dashboard</li>
          <li><FaPlane /> Flights <span className="badge">25</span></li>
          <li><FaUsers /> Customers <span className="badge">197</span></li>
          <li><FaShoppingCart /> Bookings</li>
        </ul>
      </div>
      <div className="main-content">
        <div className="top-bar">
          <div className="welcome">
            <span>Welcome, Sydney Nzunguli</span>
            <FaBell className="notification-icon" />
            <span className="badge">4</span>
          </div>
          <input type="text" placeholder="Search..." className="search-bar" />
        </div>
        <div className="dashboard">
          <div className="stats">
            <div className="stat-card">Revenue <br></br><br></br><b className='stat-bold'>Ksh.200,000</b></div>
            <div className="stat-card">New Customers <br></br><br></br><b className='stat-bold'>1040</b></div>
            <div className="stat-card">Booked Flights <br></br><br></br><b className='stat-bold'>3543</b></div>
          </div>
          <div className="chart-container">
            <h3><b>Customer Sentiment Analysis</b></h3>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart data={sentimentData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="timestamp" />
                <YAxis />
                <Tooltip />
                <Line type="monotone" dataKey="sentiment_score" stroke="#e63946" />
              </LineChart>
            </ResponsiveContainer>
          </div>
          <div className="table-container">
            <h3><b>Recent Flights</b></h3>
            <table>
              <thead>
                <tr>
                  <th>Label</th>
                  <th>Label</th>
                  <th>Label</th>
                  <th>Label</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Item default</td>
                  <td>Item default</td>
                  <td>Item default</td>
                  <td><span className="label">Item</span></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
