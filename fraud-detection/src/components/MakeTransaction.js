import React, { useState } from 'react';

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
    ip_address: ''
  });

  const [prediction, setPrediction] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await fetch('http://localhost:8000/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData)
    });
    
    const data = await response.json();
    setPrediction(data.prediction === 1 ? 'Fraudulent' : 'Not Fraudulent');
  };

  return (
    <div className="container mt-5">
      <h2 className="text-center">Make a Transaction</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>User ID</label>
          <input type="text" name="user_id" value={formData.user_id} onChange={handleChange} className="form-control" required />
        </div>
        <div className="form-group">
          <label>Signup Time</label>
          <input type="datetime-local" name="signup_time" value={formData.signup_time} onChange={handleChange} className="form-control" required />
        </div>
        <div className="form-group">
          <label>Purchase Time</label>
          <input type="datetime-local" name="purchase_time" value={formData.purchase_time} onChange={handleChange} className="form-control" required />
        </div>
        <div className="form-group">
          <label>Purchase Value</label>
          <input type="number" name="purchase_value" value={formData.purchase_value} onChange={handleChange} className="form-control" required />
        </div>
        <div className="form-group">
          <label>Device ID</label>
          <input type="text" name="device_id" value={formData.device_id} onChange={handleChange} className="form-control" required />
        </div>
        <div className="form-group">
          <label>Source</label>
          <input type="text" name="source" value={formData.source} onChange={handleChange} className="form-control" required />
        </div>
        <div className="form-group">
          <label>Browser</label>
          <input type="text" name="browser" value={formData.browser} onChange={handleChange} className="form-control" required />
        </div>
        <div className="form-group">
          <label>Sex</label>
          <input type="text" name="sex" value={formData.sex} onChange={handleChange} className="form-control" required />
        </div>
        <div className="form-group">
          <label>Age</label>
          <input type="number" name="age" value={formData.age} onChange={handleChange} className="form-control" required />
        </div>
        <div className="form-group">
          <label>IP Address</label>
          <input type="text" name="ip_address" value={formData.ip_address} onChange={handleChange} className="form-control" required />
        </div>
        <button type="submit" className="btn btn-primary mt-3">Predict</button>
      </form>

      {prediction && (
        <div className="alert mt-3 alert-info" role="alert">
          Transaction Prediction: {prediction}
        </div>
      )}
    </div>
  );
};

export default MakeTransaction;
