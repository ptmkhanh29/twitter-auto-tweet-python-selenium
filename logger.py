class Logger():
    def __init__(self, name_stage):
        self.name_stage = name_stage
        self.green = '\033[92m'
        self.orange = '\033[93m'
        self.light_cyan = '\033[96m'
        self.red = '\033[91m'
        self.reset = '\033[0m'
        self.light_blue = '\033[94m'
        self.blue = '\033[34m'

    def error(self, log_message):
        print(f"{self.blue}{self.name_stage}{self.reset} |ERROR| {self.red}{log_message}{self.reset}")

    def success(self, log_message):
        print(f"{self.blue}{self.name_stage}{self.reset} |SUCCESS| {self.green}{log_message}{self.reset}")

    def info(self, log_message):
        print(f"{self.blue}{self.name_stage}{self.reset} |SUCCESS| {self.light_cyan}{log_message}{self.reset}")

    def warning(self, log_message):
        print(f"{self.blue}{self.name_stage}{self.reset} |SUCCESS| {self.orange}{log_message}{self.reset}")