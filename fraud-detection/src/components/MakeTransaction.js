import React, { useState } from 'react';
import { Form, Button, Alert, Row, Col, Container } from 'react-bootstrap';

const MakeTransaction = () => {
  const [formData, setFormData] = useState({
    user_id: '',
    signup_time: '',
    purchase_time: '',
    purchase_value: '',
    device_id: '',
    source: '',
    browser: '',
    sex: '',
    age: '',
    ip_address: '',
  });

  const [prediction, setPrediction] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await fetch('http://localhost:8000/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    });

    const data = await response.json();
    setPrediction(data.prediction === 1 ? 'Fraudulent' : 'Not Fraudulent');
  };

  return (
    <Container className="mt-5">
      <h2 className="text-center mb-4">Make a Transaction</h2>
      <p className="text-muted text-center mb-4">
        Enter the transaction details below to predict whether the transaction is fraudulent or not.
      </p>

      <Form onSubmit={handleSubmit} className="p-4 shadow rounded" style={{ backgroundColor: '#f8f9fa' }}>
        <Row>
          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>User ID</Form.Label>
              <Form.Control
                type="text"
                name="user_id"
                value={formData.user_id}
                onChange={handleChange}
                placeholder="Enter user ID"
                required
              />
            </Form.Group>
          </Col>
          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>Signup Time</Form.Label>
              <Form.Control
                type="datetime-local"
                name="signup_time"
                value={formData.signup_time}
                onChange={handleChange}
                required
              />
            </Form.Group>
          </Col>
        </Row>

        <Row>
          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>Purchase Time</Form.Label>
              <Form.Control
                type="datetime-local"
                name="purchase_time"
                value={formData.purchase_time}
                onChange={handleChange}
                required
              />
            </Form.Group>
          </Col>
          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>Purchase Value</Form.Label>
              <Form.Control
                type="number"
                name="purchase_value"
                value={formData.purchase_value}
                onChange={handleChange}
                placeholder="Enter purchase value"
                required
              />
            </Form.Group>
          </Col>
        </Row>

        <Row>
          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>Device ID</Form.Label>
              <Form.Control
                type="text"
                name="device_id"
                value={formData.device_id}
                onChange={handleChange}
                placeholder="Enter device ID"
                required
              />
            </Form.Group>
          </Col>
          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>Source</Form.Label>
              <Form.Control
                type="text"
                name="source"
                value={formData.source}
                onChange={handleChange}
                placeholder="Enter source (e.g., website, app)"
                required
              />
            </Form.Group>
          </Col>
        </Row>

        <Row>
          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>Browser</Form.Label>
              <Form.Control
                type="text"
                name="browser"
                value={formData.browser}
                onChange={handleChange}
                placeholder="Enter browser (e.g., Chrome)"
                required
              />
            </Form.Group>
          </Col>
          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>Sex</Form.Label>
              <Form.Control
                type="text"
                name="sex"
                value={formData.sex}
                onChange={handleChange}
                placeholder="Enter sex (Male/Female)"
                required
              />
            </Form.Group>
          </Col>
        </Row>

        <Row>
          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>Age</Form.Label>
              <Form.Control
                type="number"
                name="age"
                value={formData.age}
                onChange={handleChange}
                placeholder="Enter age"
                required
              />
            </Form.Group>
          </Col>
          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>IP Address</Form.Label>
              <Form.Control
                type="text"
                name="ip_address"
                value={formData.ip_address}
                onChange={handleChange}
                placeholder="Enter IP address"
                required
              />
            </Form.Group>
          </Col>
        </Row>

        <Button type="submit" variant="primary" className="w-100 mt-3">
          Predict Transaction
        </Button>
      </Form>

      {prediction && (
        <Alert className="mt-4 text-center" variant={prediction === 'Fraudulent' ? 'danger' : 'success'}>
          <strong>Transaction Prediction:</strong> {prediction}
        </Alert>
      )}
    </Container>
  );
};

export default MakeTransaction;
