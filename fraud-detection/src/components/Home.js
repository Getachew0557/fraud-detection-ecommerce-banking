import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Card, Row, Col, Table, ProgressBar } from 'react-bootstrap';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';

const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#8884D8', '#8DD1E1', '#83A6ED', '#A4DE6C', '#D0ED57', '#FF8042'];

const Home = () => {
  const [overviewData, setOverviewData] = useState({});
  const [distributionData, setDistributionData] = useState({});
  const [ipCountryData, setIpCountryData] = useState([]);

  useEffect(() => {
    // axios.get('http://localhost:8000/overview')
    axios.get(`${API_BASE_URL}/overview`)
      .then(response => setOverviewData(response.data))
      .catch(error => console.error('Error fetching overview data:', error));

    // axios.get('http://localhost:8000/distribution')
    axios.get(`${API_BASE_URL}/distribution`)
      .then(response => setDistributionData(response.data))
      .catch(error => console.error('Error fetching distribution data:', error));

    // axios.get('http://localhost:8000/ip-country-distribution')
    axios.get(`${API_BASE_URL}/ip-country-distribution`)
      .then(response => setIpCountryData(response.data))
      .catch(error => console.error('Error fetching IP-country data:', error));
  }, []);

  return (
    <div className="container mt-5">
      <h2 className="text-center">Fraud Detection Dashboard</h2>
      <p className="lead text-center">Explore fraud detection insights and IP distributions.</p>

      {/* First Row: Overview Cards */}
      <Row className="mb-4">
        <Col md={4}>
          <Card>
            <Card.Body>
              <Card.Title>Total Transactions</Card.Title>
              <h3>200,000</h3>
              <ProgressBar variant="primary" now={75} label="75%" />
            </Card.Body>
          </Card>
        </Col>
        <Col md={4}>
          <Card>
            <Card.Body>
              <Card.Title>Fraudulent Transactions</Card.Title>
              <h3>15,000</h3>
              <ProgressBar variant="danger" now={25} label="25%" />
            </Card.Body>
          </Card>
        </Col>
        <Col md={4}>
          <Card>
            <Card.Body>
              <Card.Title>Non-Fraudulent Transactions</Card.Title>
              <h3>185,000</h3>
              <ProgressBar variant="success" now={90} label="90%" />
            </Card.Body>
          </Card>
        </Col>
      </Row>

      {/* Second Row: Fraud Class Distribution and IP Distribution */}
      <Row className="mb-4">
        <Col md={6}>
          <Card>
            <Card.Body>
              <Card.Title>Fraud Class Distribution</Card.Title>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={Object.entries(distributionData).map(([key, value]) => ({ class: key, count: value }))}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="class" />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Bar dataKey="count" fill="#8884d8" />
                </BarChart>
              </ResponsiveContainer>
            </Card.Body>
          </Card>
        </Col>
        <Col md={6}>
          <Card>
            <Card.Body>
              <Card.Title>Top 20 Countries by IP Distribution</Card.Title>
              <ResponsiveContainer width="100%" height={300}>
                <PieChart>
                  <Pie
                    data={Object.entries(ipCountryData).map(([key, value]) => ({ name: key, value }))}
                    dataKey="value"
                    nameKey="name"
                    cx="50%"
                    cy="50%"
                    outerRadius={100}
                    fill="#8884d8"
                  >
                    {Object.entries(ipCountryData).map(([key], index) => (
                      <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                    ))}
                  </Pie>
                  <Tooltip />
                </PieChart>
              </ResponsiveContainer>
            </Card.Body>
          </Card>
        </Col>
      </Row>

      {/* Third Row: Scrollable Table */}
      <Row>
        <Col md={12}>
          <Card>
            <Card.Body>
              <Card.Title>IP Data Table</Card.Title>
              <div style={{ maxHeight: '300px', overflowY: 'scroll' }}>
                <Table striped bordered hover>
                  <thead>
                    <tr>
                      <th>Country</th>
                      <th>Lower Bound IP</th>
                      <th>Upper Bound IP</th>
                    </tr>
                  </thead>
                  <tbody>
                    {Object.entries(ipCountryData).map(([country, count], index) => (
                      <tr key={index}>
                        <td>{country}</td>
                        <td>{count}</td>
                        <td>{count}</td>
                      </tr>
                    ))}
                  </tbody>
                </Table>
              </div>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </div>
  );
};

export default Home;
