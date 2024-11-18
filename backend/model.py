# Function to mock LSTM predictions
def lstm_predict(data):
    # Mock prediction logic (replace with actual LSTM model)
    predictions = data['temperature'] * 0.8 + data['humidity'] * 0.2  # Just a placeholder formula
    return predictions
