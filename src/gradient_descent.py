from src.training_set import TrainingSet

training_set = TrainingSet()

alpha = 0.00109
previous_parameters = []
parameters = [0 for i in range(0, training_set.n)]


def summation_mean_error_function(parameter_index):
    summation = 0
    for m_index in range(0, training_set.m):
        hypothesis_function = 0
        for n_index in range(0, training_set.n):
            hypothesis_function += previous_parameters[n_index] * training_set.data_set[m_index][n_index]
        summation += (hypothesis_function - training_set.labels[m_index]) * training_set.data_set[m_index][
            parameter_index]
    return summation


def derivative_of_cost_function(parameter_index):
    return (1 / training_set.m) * summation_mean_error_function(parameter_index)


def cost_function():
    summation = 0
    for m_index in range(0, training_set.m):
        hypothesis_function = 0
        for n_index in range(0, training_set.n):
            hypothesis_function += parameters[n_index] * training_set.data_set[m_index][n_index]
        summation += (hypothesis_function - training_set.labels[m_index]) ** 2
    return (1 / (2 * training_set.m)) * summation


loop_breaker = 3200000
loop_count = 0
while loop_count <= loop_breaker:
    loop_count += 1
    previous_parameters = list(parameters)
    for i in range(0, training_set.n):
        parameters[i] = previous_parameters[i] - alpha * derivative_of_cost_function(i)
    if parameters == previous_parameters:
        print('Converged')
        break

for i in range(0, training_set.n):
    print(parameters[i])

print("Cost : " + str(cost_function()))
