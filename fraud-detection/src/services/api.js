const API_URL = 'http://localhost:8000'; // Ensure this matches your Flask app URL

// Function to handle making a transaction prediction
export const makePrediction = async (transactionData) => {
  try {
    const response = await fetch(`${API_URL}/predict`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(transactionData),
    });
    
    const result = await response.json();
    
    if (response.ok) {
      return result;  // Prediction result
    } else {
      throw new Error(result.error || 'Error during prediction');
    }
  } catch (error) {
    console.error('Error making prediction:', error);
    throw error;  // Rethrow error for handling in React component
  }
};
