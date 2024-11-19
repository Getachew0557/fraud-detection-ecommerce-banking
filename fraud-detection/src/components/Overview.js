import React from 'react';

const Overview = () => {
  return (
    <div className="container mt-5">
      <h2 className="text-center">Overview of Fraud Detection</h2>
      <p className="lead">
        Fraud detection models analyze the historical transactional data and provide accurate predictions regarding fraudulent activities.
      </p>
      <div className="alert alert-info" role="alert">
        Fraud Detection Overview: An in-depth analysis based on various features such as transaction value, user behavior, and other transaction metadata.
      </div>
    </div>
  );
};

export default Overview;
