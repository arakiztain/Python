from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Tuple


class DataStream(ABC):
    """Abstract base class for all data streams."""

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter data based on criteria (default: no filtering)."""
        return data_batch

    @abstractmethod
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        pass


class SensorStream(DataStream):
    """Stream for environmental sensor data."""

    def process_batch(self, data_batch: List[Tuple[str, float]]) -> str:
        try:
            self.processed_count += len(data_batch)
            temps = [v for k, v in data_batch if k == "temp"]
            avg_temp = sum(temps) / len(temps) if temps else 0.0
            return (f"[SENSOR] {len(data_batch)} readings"
                    f" processed, avg temp: {avg_temp}°C")
        except Exception as e:
            return f"[SENSOR] Processing error: {e}"

    def filter_data(
        self,
        data_batch: List[Tuple[str, float]],
        criteria: Optional[str] = None
    ) -> List[Tuple[str, float]]:
        if criteria == "critical":
            return (
                [item for item in data_batch if item[0] in (
                    "temp", "humidity"
                    )]
                )
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": "Environmental Data",
            "processed_readings": self.processed_count,
        }


class TransactionStream(DataStream):
    """Stream for financial transaction data."""

    def process_batch(self, data_batch: List[Tuple[str, int]]) -> str:
        try:
            self.processed_count += len(data_batch)
            net_flow = sum(
                amount if action == "buy" else -amount for action,
                amount in data_batch
                )
            sign = "+" if net_flow >= 0 else ""
            return (
                f"[TRANSACTION] {len(data_batch)} operations, net"
                f" flow: {sign}{net_flow} units"
                )
        except Exception as e:
            return f"[TRANSACTION] Processing error: {e}"

    def filter_data(
        self, data_batch: List[Tuple[str, int]], criteria: Optional[str] = None
    ) -> List[Tuple[str, int]]:
        if criteria == "large":
            return [item for item in data_batch if item[1] >= 150]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": "Financial Data",
            "processed_operations": self.processed_count,
        }


class EventStream(DataStream):
    """Stream for system event data."""

    def process_batch(self, data_batch: List[str]) -> str:
        try:
            self.processed_count += len(data_batch)
            error_count = len(
                [event for event in data_batch if event == "error"]
                )
            return (
                f"[EVENT] {len(data_batch)} events,"
                f" {error_count} error detected"
                )
        except Exception as e:
            return f"[EVENT] Processing error: {e}"

    def filter_data(
        self, data_batch: List[str], criteria: Optional[str] = None
    ) -> List[str]:
        if criteria == "error":
            return [event for event in data_batch if event == "error"]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": "System Events",
            "processed_events": self.processed_count,
        }


print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
print()

streams: List[DataStream] = [
    SensorStream("SENSOR_001"),
    TransactionStream("TRANS_001"),
    EventStream("EVENT_001"),
]

data_batches: List[List[Any]] = [
    [("temp", 22.5), ("humidity", 65), ("pressure", 1013)],
    [("buy", 100), ("sell", 150), ("buy", 75)],
    ["login", "error", "logout"],
]

for stream, data in zip(streams, data_batches):
    stats = stream.get_stats()
    print(
        f"Initializing "
        f"{stream.__class__.__name__.replace('Stream', ' Stream')}..."
        )
    print(f"Stream ID: {stats['stream_id']}, Type: {stats['type']}")
    filtered_data = stream.filter_data(data)
    if isinstance(stream, (SensorStream, TransactionStream)):
        display_data = (
            "[" + ", ".join(f"{k}:{v}" for k, v in filtered_data) + "]"
            )
    else:
        display_data = "[" + ", ".join(filtered_data) + "]"
    print(
        f"Processing "
        f"{stream.__class__.__name__.replace('Stream', '').lower()} batch:"
        f" {display_data}"
        )
    print(stream.process_batch(filtered_data))
    print()

print("=== Polymorphic Stream Processing ===")
print("Processing mixed stream types through unified interface...")
print()

mixed_batches: List[List[Any]] = [
    [("temp", 21.0), ("temp", 23.0)],
    [("buy", 50), ("sell", 200), ("buy", 25), ("sell", 100)],
    ["login", "error", "logout"],
]

print("Batch 1 Results:")
for stream, batch in zip(streams, mixed_batches):
    filtered_bch = stream.filter_data(batch)
    stream.process_batch(filtered_bch)
    data_type = stream.get_stats()['type'].split()[0]
    print(
        f"- {data_type} data: {len(filtered_bch)} {data_type.lower()} "
        "processed"
        )

critical_sensors = streams[0].filter_data(data_batches[0], "critical")
large_transactions = streams[1].filter_data(data_batches[1], "large")
print()
print("Stream filtering active: High-priority data only")
print(
    f"Filtered results: {len(critical_sensors)} critical sensor alerts,"
    f" {len(large_transactions)} large transaction"
    )

print()
print("All streams processed successfully. Nexus throughput optimal.")
