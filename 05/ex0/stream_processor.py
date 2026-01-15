class DataProcessor():
    def process(self, data) -> None:
        return data

    def validate(self, data: str) -> str:
        return True

    def format_output(self, data):
        print("")    

class NumericProcessor(DataProcessor):
    def process(self, data: list):
        total = 0
        count = 0
        for item in data:
            total += item
            count += 1
        avg = total / count
        return count, total, avg

    def validate(self, data):
        try:
            total = 0
            for item in data:
                total += item
            return True
        except TypeError:
            return False

    def format_output(self, result):
        count, total, avg = result
        return f"Processed {count} numeric values, sum={total}, avg={avg}"

class TextProcessor(DataProcessor):
    def process(self, data: str) -> None:
        # char_count = len("".join(data.split()))
        # char_count = len(data.replace(" ", ""))
        char_count = len(data)
        word_count = len(data.split())
        return data, char_count, word_count

    def validate(self, data: str):
        try:
            _ = data.split()
            return True
        except AttributeError:
            return False

    def format_output(self, result):
        text, char_count, word_count = result
        return f"Processed text: {char_count} characters, {word_count} words" 

class LogProcessor(DataProcessor):
    def process(self, data: str):
        try:
            level, message = data.split(":", 1)
            level = level.strip()
            message = message.strip()
            return level, message
        except ValueError:
            return "INFO", data.strip()

    def validate(self, data):
        try:
            _ = data.split()
            return True
        except AttributeError:
            return False


    def format_output(self, result):
        level, message = result
        if level.upper() == "ERROR":
            prefix = "[ALERT]"
        else:
            prefix = "[INFO]"
        return f"{prefix} {level.upper()} level detected: {message}"

print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

processor = NumericProcessor()
numeric_data = [1, 2, 3, 4, 5]

if processor.validate(numeric_data):
    result = processor.process(numeric_data)
    print("Initializing Numeric Processor...")
    print("Processing data:", numeric_data)
    print("Validation: Numeric data verified")
    print("Output:", processor.format_output(result))
else:
    print("Numeric data validation failed")

processor = TextProcessor()
text_data = "Hello Nexus World"

if processor.validate(text_data):
    result = processor.process(text_data)
    print("\nInitializing Text Processor...")
    print("Processing data:", f'"{text_data}"')
    print("Validation: Text data verified")
    print("Output:", processor.format_output(result))
else:
    print("Text data validation failed")

processor = LogProcessor()
log_data = "ERROR: Connection timeout"

if processor.validate(log_data):
    result = processor.process(log_data)
    print("\nInitializing Log Processor...")
    print("Processing data:", f'"{log_data}"')
    print("Validation: Log entry verified")
    print("Output: [ALERT] ERROR level detected: Connection timeout")
else:
    print("Log data validation failed")

print("\n=== Polymorphic Processing Demo ===")
print("Processing multiple data types through same interface...")

data_list = [
    [1, 2, 3],
    "Hello Nexus",
    "INFO: System ready"
]

processors = [
    NumericProcessor(),
    TextProcessor(),
    LogProcessor()
]

for i, (processor, data) in enumerate(zip(processors, data_list), start=1):
    if processor.validate(data):
        result = processor.process(data)
        output = processor.format_output(result)
        print(f"Result {i}:", output)
    else:
        print("Validation failed for:", data)

print("\nFoundation systems online. Nexus ready for advanced streams.")