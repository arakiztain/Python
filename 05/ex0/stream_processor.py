from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    """Abstract base class for all data processors."""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process input data and return a result string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate input data."""
        pass

    def format_output(self, result: str) -> str:
        """Format the output string."""
        return result


class NumericProcessor(DataProcessor):
    """Processor for numeric list data."""

    def process(self, data: List[Any]) -> str:
        total: float = sum(data)
        count: int = len(data)
        avg: float = total / count if count > 0 else 0.0
        return f"Processed {count} numeric values, sum={total}, avg={avg}"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False
        try:
            for item in data:
                _ = item + 0
            return True
        except TypeError:
            return False


class TextProcessor(DataProcessor):
    """Processor for text data."""

    def process(self, data: str) -> str:
        char_count: int = len(data)
        word_count: int = len(data.split())
        return f"Processed text: {char_count} characters, {word_count} words"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)


class LogProcessor(DataProcessor):
    """Processor for log entries."""

    def process(self, data: str) -> str:
        try:
            level, message = data.split(":", 1)
            level = level.strip().upper()
            message = message.strip()
        except ValueError:
            level = "INFO"
            message = data.strip()

        prefix: str = "[ALERT]" if level == "ERROR" else "[INFO]"
        return f"{prefix} {level} level detected: {message}"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)


print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
print()

numeric_processor: DataProcessor = NumericProcessor()
numeric_data: List[int] = [1, 2, 3, 4, 5]

print("Initializing Numeric Processor...")
print("Processing data:", numeric_data)

if numeric_processor.validate(numeric_data):
    print("Validation: Numeric data verified")
    result: str = numeric_processor.process(numeric_data)
    print("Output:", numeric_processor.format_output(result))
print()

text_processor: DataProcessor = TextProcessor()
text_data: str = "Hello Nexus World"

print("Initializing Text Processor...")
print('Processing data: "Hello Nexus World"')

if text_processor.validate(text_data):
    print("Validation: Text data verified")
    result = text_processor.process(text_data)
    print("Output:", text_processor.format_output(result))
print()

log_processor: DataProcessor = LogProcessor()
log_data: str = "ERROR: Connection timeout"

print("Initializing Log Processor...")
print('Processing data: "ERROR: Connection timeout"')

if log_processor.validate(log_data):
    print("Validation: Log entry verified")
    result = log_processor.process(log_data)
    print("Output:", log_processor.format_output(result))
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
        result = processor.process(data)
        print(f"Result {i}:", processor.format_output(result))

print()
print("Foundation systems online. Nexus ready for advanced streams.")
