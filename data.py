import random
import pandas as pd

class DataGenerator:
    def __init__(self, num_registers=32, max_value=100):
        self.num_registers = num_registers
        self.max_value = max_value
        self.instructions = ["ADD", "SUB", "MUL", "DIV", "LOAD", "STORE", "AND", "OR", "XOR", "SHIFT"]
        
    def generate_war_hazard(self):
        register1 = random.randint(0, self.num_registers - 1)
        register2 = random.randint(0, self.num_registers - 1)
        value1 = random.randint(0, self.max_value)
        value2 = random.randint(0, self.max_value)

        instruction1 = f"{random.choice(self.instructions)} R{register1}, R1, R2"
        instruction2 = f"{random.choice(self.instructions)} R{register2}, R{register1}, R3"

        return instruction1, instruction2, "WAR"

    def generate_raw_hazard(self):
        register1 = random.randint(0, self.num_registers - 1)
        register2 = random.randint(0, self.num_registers - 1)
        value1 = random.randint(0, self.max_value)
        value2 = random.randint(0, self.max_value)

        instruction1 = f"{random.choice(self.instructions)} R{register1}, R0, {value1}"
        instruction2 = f"{random.choice(self.instructions)} R{register2}, R{register1}, R2"

        return instruction1, instruction2, "RAW"

    def generate_waw_hazard(self):
        register1 = random.randint(0, self.num_registers - 1)
        register2 = random.randint(0, self.num_registers - 1)
        value1 = random.randint(0, self.max_value)
        value2 = random.randint(0, self.max_value)

        instruction1 = f"{random.choice(self.instructions)} R{register1}, R0, {value1}"
        instruction2 = f"{random.choice(self.instructions)} R{register1}, R0, {value2}"

        return instruction1, instruction2, "WAW"

    def generate_no_conflict(self):
        register1 = random.randint(0, self.num_registers - 1)
        register2 = random.randint(0, self.num_registers - 1)

        instruction1 = f"{random.choice(self.instructions)} R{register1}, R1, R2"
        instruction2 = f"{random.choice(self.instructions)} R{register2}, R3, 10"

        return instruction1, instruction2, "No_CONFLICT"

    def generate_dataset(self, num_samples_per_hazard):
        dataset = []

        for _ in range(num_samples_per_hazard):
            hazard_tye = random.randint(0, 3)

            if hazard_tye == 0:
                instructions = self.generate_war_hazard()
            elif hazard_tye == 1:
                instructions = self.generate_raw_hazard()
            elif hazard_tye == 2:
                instructions = self.generate_waw_hazard()
            else:
                instructions = self.generate_no_conflict()

            dataset.append(instructions)

        return dataset

num_samples_per_hazard = 5000

data_generator = DataGenerator(num_registers=16, max_value=50)

dataset = data_generator.generate_dataset(num_samples_per_hazard)

df = pd.DataFrame(dataset, columns=["Instruction 1", "Instruction 2", "Conflict Type"])

df.to_csv("pipeline_conflict.csv", index=False)