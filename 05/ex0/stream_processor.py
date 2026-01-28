from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    """Abstract base class for all data processors."""

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    """Processor for numeric list data."""

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False
        try:
            return all(isinstance(x, (int, float)) for x in data)
        except TypeError:
            return False

    def process(self, data: List[Any]) -> str:
        total = sum(data)
        count = len(data)
        avg = total / count if count else 0.0
        return f"Processed {count} numeric values, sum={total}, avg={avg}"

    def format_output(self, result: str) -> str:
        return result


class TextProcessor(DataProcessor):
    """Processor for text data."""

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: str) -> str:
        chars = len(data)
        words = len(data.split())
        return f"Processed text: {chars} characters, {words} words"

    def format_output(self, result: str) -> str:
        return result


class LogProcessor(DataProcessor):
    """Processor for log entries."""

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: str) -> str:
        try:
            level, message = data.split(":", 1)
            level = level.strip().upper()
            message = message.strip()
        except ValueError:
            level = "INFO"
            message = data.strip()

        prefix = "[ALERT]" if level == "ERROR" else "[INFO]"
        return f"{prefix} {level} level detected: {message}"

    def format_output(self, result: str) -> str:
        return result


print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

numeric_processor: DataProcessor = NumericProcessor()
numeric_data = [1, 2, 3, 4, 5]

print("Initializing Numeric Processor...")
print("Processing data:", numeric_data)

if numeric_processor.validate(numeric_data):
    print("Validation: Numeric data verified")
    print("Output:", numeric_processor.format_output(
        numeric_processor.process(numeric_data)
    ))
print()

text_processor: DataProcessor = TextProcessor()
text_data = "Hello Nexus World"

print("Initializing Text Processor...")
print('Processing data: "Hello Nexus World"')

if text_processor.validate(text_data):
    print("Validation: Text data verified")
    print("Output:", text_processor.format_output(
        text_processor.process(text_data)
    ))
print()

log_processor: DataProcessor = LogProcessor()
log_data = "ERROR: Connection timeout"

print("Initializing Log Processor...")
print('Processing data: "ERROR: Connection timeout"')

if log_processor.validate(log_data):
    print("Validation: Log entry verified")
    print("Output:", log_processor.format_output(
        log_processor.process(log_data)
    ))
print()

print("=== Polymorphic Processing Demo ===")
print("Processing multiple data types through same interface...")

processors: List[DataProcessor] = [
    NumericProcessor(),
    TextProcessor(),
    LogProcessor()
]

data_samples: List[Any] = [
    [1, 2, 3],
    "Hello Nexus",
    "INFO: System ready"
]

for i, (processor, data) in enumerate(zip(processors, data_samples), start=1):
    if processor.validate(data):
        print(f"Result {i}:", processor.format_output(processor.process(data)))

print()
print("Foundation systems online. Nexus ready for advanced streams.")
