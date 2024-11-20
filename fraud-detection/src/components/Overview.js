import React from 'react';
import { Card, Row, Col, ProgressBar, Alert } from 'react-bootstrap';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const fraudData = [
  { name: 'Fraudulent', count: 15000 },
  { name: 'Non-Fraudulent', count: 185000 },
];

const countryData = [
  { country: 'USA', count: 6000 },
  { country: 'UK', count: 4000 },
  { country: 'India', count: 3000 },
  { country: 'Germany', count: 2000 },
  { country: 'Canada', count: 1500 },
];

const Overview = () => {
  return (
    <div className="container mt-5">
      <h1 className="text-center mb-4">Overview of Fraud Detection</h1>

      <p className="lead text-center">
        Gain insights into fraud detection metrics and trends. This dashboard provides an overview of transaction data, fraud distribution, and key analytics.
      </p>

      <Alert variant="info" className="text-center">
        Fraud Detection Overview: Analyze transactional data to predict and prevent fraudulent activities effectively. 
        <br />
        * Global financial fraud cost businesses approximately $4.2 trillion in 2023.
        <br />
        * Credit card fraud alone accounted for $28 billion in global losses in 2023.
      </Alert>

      <p className="text-center text-muted">
        Fraud detection is critical in mitigating risks and preventing losses. Businesses use advanced machine learning models and statistical methods to safeguard transactions. Below are metrics and trends from real-world fraud detection systems.
      </p>

      {/* Key Metrics */}
      <Row className="mt-5">
        <Col md={4}>
          <Card className="text-center">
            <Card.Body>
              <Card.Title>Total Transactions</Card.Title>
              <h3>200,000</h3>
              <ProgressBar variant="primary" now={75} label="75%" />
            </Card.Body>
          </Card>
        </Col>
        <Col md={4}>
          <Card className="text-center">
            <Card.Body>
              <Card.Title>Fraudulent Transactions</Card.Title>
              <h3>15,000</h3>
              <ProgressBar variant="danger" now={25} label="25%" />
            </Card.Body>
          </Card>
        </Col>
        <Col md={4}>
          <Card className="text-center">
            <Card.Body>
              <Card.Title>Non-Fraudulent Transactions</Card.Title>
              <h3>185,000</h3>
              <ProgressBar variant="success" now={90} label="90%" />
            </Card.Body>
          </Card>
        </Col>
      </Row>

      {/* Global Visualization Section */}
      <h3 className="mt-5 text-center">Global Trends in Fraud Detection</h3>
      <p className="text-center text-muted">
        Fraud detection varies across regions, influenced by factors such as digital infrastructure, payment systems, and consumer behavior. Below is a snapshot of fraud trends by country.
      </p>
      <Row>
        <Col md={6}>
          <Card>
            <Card.Body>
              <Card.Title className="text-center">Fraud Class Distribution</Card.Title>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={fraudData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="name" />
                  <YAxis />
                  <Tooltip />
                  <Bar dataKey="count" fill="#8884d8" />
                </BarChart>
              </ResponsiveContainer>
            </Card.Body>
          </Card>
        </Col>
        <Col md={6}>
          <Card>
            <Card.Body>
              <Card.Title className="text-center">Fraud by Country</Card.Title>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={countryData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="country" />
                  <YAxis />
                  <Tooltip />
                  <Bar dataKey="count" fill="#82ca9d" />
                </BarChart>
              </ResponsiveContainer>
            </Card.Body>
          </Card>
        </Col>
      </Row>

      {/* Insights Section */}
      <div className="mt-5 text-center">
        <h4>Insights from Global Fraud Analytics</h4>
        <p className="text-muted">
          * The USA has the highest number of fraud incidents due to the large volume of online transactions.
          <br />
          * Emerging economies like India and Brazil show increasing fraud cases with the rise in digital payment systems.
          <br />
          * Advanced fraud detection systems in Europe have reduced fraudulent transactions by 15% in the past year.
        </p>
      </div>

      {/* Footer Section */}
      <div className="mt-5 text-center">
        <p className="text-muted">
          Explore in-depth fraud analysis to mitigate risks and enhance security. Stay ahead with accurate predictions and actionable insights.
        </p>
      </div>
    </div>
  );
};

export default Overview;
