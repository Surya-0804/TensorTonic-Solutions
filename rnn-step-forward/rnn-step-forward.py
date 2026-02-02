import numpy as np

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    """
    Returns: h_t of shape (H,)
    """
    # Write code here
    current_para=np.dot(x_t,Wx)
    previous_para=np.dot(h_prev,Wh)
    return np.tanh(current_para+previous_para+b)
