import logging
from decimal import Decimal

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        if isinstance(self.a, int) and isinstance(self.b, int):
            return self.a + self.b
        else:
            return float(Decimal(str(self.a)) + Decimal(str(self.b)))

    def sub(self):
        if isinstance(self.a, int) and isinstance(self.b, int):
            return self.a - self.b
        else:
            return float(Decimal(str(self.a)) - Decimal(str(self.b)))

    def mul(self):
        if isinstance(self.a, int) and isinstance(self.b, int):
            return self.a * self.b
        else:
            return float(Decimal(str(self.a)) * Decimal(str(self.b)))

    def div(self):
        if self.b == 0 and isinstance(self.b, int):
            logging.info("除法运算中：分母不能为0")
            return 0
        elif self.b == 0.0 and isinstance(self.b, float):
            logging.info("除法运算中：分母不能为0")
            return 0
        elif self.a % self.b == 0:
            return self.a / self.b
        else:
            return float(Decimal(str(self.a)) / Decimal(str(self.b)))
