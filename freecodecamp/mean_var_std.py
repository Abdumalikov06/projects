import numpy as np
user_input = input("Enter 9 numbers separated by spaces: ")
def calculate(data):
    """
    Calculate the mean, variance, and standard deviation of the input data.
    """
    if len(data)< 9:
        raise ValueError("List must contain nine numbers.")
    arr= np.array(list(map(float, data.split()))).reshape(3, 3)
    mean = [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arr).item()]
    # variance
    variance = [np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), np.var(arr).item()]
    # standard deviation
    std_dev = [np.std(arr, axis=0).tolist(), np.std(arr, axis=1).tolist(), np.std(arr).item()]
    # max
    max_vals = [np.max(arr, axis=0).tolist(), np.max(arr, axis=1).tolist(), np.max(arr).item()]
    # min
    min_vals = [np.min(arr, axis=0).tolist(), np.min(arr, axis=1).tolist(), np.min(arr).item()]
    # sum
    sum_vals = [np.sum(arr, axis=0).tolist(), np.sum(arr, axis=1).tolist(), np.sum(arr).item()]
    return {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_vals,
        'min': min_vals,
        'sum': sum_vals
    }
    
result = calculate(user_input)
print(result)

    
    


    
