


class StoppingCriterion():
  def __init__(self, convergence_data):
    self.convergence_data = convergence_data
    self.best_convergence_parameters = dict()

    self._find_best_window_size()

  def _find_best_window_size(self):

    for boundary, coefficients in self.convergence_data.items():
      self.best_convergence_parameters[boundary] = dict()
      for coefficient, entries in coefficients.items():
        best_window_size = -1
        number_of_iterations = -1
        for i in range(0, len(entries[0])):
          if entries[0][i] is True:
            if best_window_size == -1:
              number_of_iterations = entries[1][i]
              best_window_size = entries[2][i]
            else:
              if entries[1][i] < number_of_iterations:
                number_of_iterations = entries[1][i]
                best_window_size = entries[2][i]
        self.best_convergence_parameters[boundary][coefficient] = {
          'window_size': best_window_size,
          'iterations': number_of_iterations
        }

  def get_window_size(self):
    return self.best_convergence_parameters

  def get_best_window_size(self):
    best_window_size = -1
    worst_iterations = -1
    for boundary, coefficients in self.best_convergence_parameters.items():
      for coefficient, entries in coefficients.items():
        if best_window_size == -1:
          best_window_size = entries['window_size']
          worst_iterations = entries['iterations']
        else:
          if entries['iterations'] > worst_iterations:
            best_window_size = entries['window_size']
            worst_iterations = entries['iterations']
    
    return best_window_size
        