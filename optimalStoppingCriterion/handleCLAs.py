


class HandleCommandLineArguments():
  def __init__(self, args):
    self.args = args
    self.case = ''
    self.window = list()
    self.convergence_threshold = 0.01
    self._process_cla()
    self._print_help()

  def _process_cla(self):
    has_case = False

    if '-c' in self.args:
      has_case = True
      self.case = self.args[self.args.index('-c') + 1]
    elif '--case' in self.args:
      has_case = True
      self.case = self.args[self.args.index('--case') + 1]

    if not has_case:
      raise Exception('No case specified. Use --help to see usage.')
    
    if '-w' in self.args:
      min_win = int(self.args.index('-w') + 1)
      max_win = int(self.args.index('-w') + 2)
      increments = int(self.args.index('-w') + 3)
      self.window = self.args[min_win, max_win, increments]

    elif '--window' in self.args:
      min_win = int(self.args.index('--window') + 1)
      max_win = int(self.args.index('--window') + 2)
      increments = int(self.args.index('--window') + 3)
      self.window = self.args[min_win, max_win, increments]

    else:
      self.window = [10, 100, 5]
      print('No window size specified. Using default window size of min_window = 10, max_window = 100, increments = 5')
      print('If you want to change these defaults, see the help message with -h or --help\n')


    if '-ct' in self.args:
      self.convergence_threshold = float(self.args[self.args.index('-ct') + 1])
    elif'--convergence-threshold' in self.args:
      self.convergence_threshold = float(self.args[self.args.index('--convergence-threshold') + 1])
    else:
      print('No convergence threshold specified. Using default convergence threshold of 0.01 (i.e. 1%)\n')


  def _print_help(self):
    if '-h' in self.args or '--help' in self.args:
      print('Usage: python3 pyOSC.py -c <case>\n')
      print('  -c, --case <case>  Case to run')
      print('  -h, --help         Show this help message and exit')
      print('  -w, --window       Window size to use for convergence analysis')
      print('                     Specified as a list of integers separated by spaces')
      print('                     Use the format <smallest window> <largest window> <increments>')
      print('                     Example: -w 10 100 10. Smallest window = 10')
      print('                     largest window = 100, and window increments = 10')
      print('                     If no window size is specified, the default 10 100 5 is used')
      print('  -ct, --convergence-threshold')
      print('                     Convergence threshold to use for convergence analysis.')
      print('                     This value will be used to check if coefficients have converged')
      print('                     to the asymptotic value at the end of the simulation.')

      exit()


  