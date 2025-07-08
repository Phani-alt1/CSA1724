import numpy as np

# Sigmoid and its derivative
def sigmoid(x): return 1 / (1 + np.exp(-x))
def sigmoid_deriv(x): return x * (1 - x)

# Input data (4 samples, 2 features)
X = np.array([[0,0],[0,1],[1,0],[1,1]])

# Output data (for XOR logic)
y = np.array([[0],[1],[1],[0]])

# Random weights for input->hidden (2 inputs, 3 hidden)
w1 = np.random.rand(2, 3)
# Random weights for hidden->output (3 hidden, 1 output)
w2 = np.random.rand(3, 1)

# Training loop
for epoch in range(10000):
    # Feedforward
    l1 = sigmoid(np.dot(X, w1))
    out = sigmoid(np.dot(l1, w2))

    # Backpropagation
    error = y - out
    d_out = error * sigmoid_deriv(out)
    
    d_l1 = d_out.dot(w2.T) * sigmoid_deriv(l1)

    # Update weights
    w2 += l1.T.dot(d_out) * 0.1
    w1 += X.T.dot(d_l1) * 0.1

# Prediction
print("Predictions:")
print(out.round(2))
