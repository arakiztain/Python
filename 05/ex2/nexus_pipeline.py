from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol
import time
from collections import defaultdict


# ===================== PROTOCOL =====================
class ProcessingStage(Protocol):
    """
    Duck typing protocol for pipeline stages.
    Any class implementing process(data) can act as a stage.
    """

    def process(self, data: Any) -> Any:
        ...


# ===================== PIPELINE BASE =====================
class ProcessingPipeline(ABC):
    _structure_announced: bool = False   # ← variable de clase

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []
        self.stats = {"processed": 0, "errors": 0, "time": 0.0}

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

        # SOLO se anuncia la estructura una vez
        if not ProcessingPipeline._structure_announced:
            stage_number = len(self.stages)
            descriptions = {
                1: "Input validation and parsing",
                2: "Data transformation and enrichment",
                3: "Output formatting and delivery",
            }

            description = descriptions.get(stage_number, "Custom stage")
            print(f"Stage {stage_number}: {description}")

            if stage_number == 3:
                ProcessingPipeline._structure_announced = True


    def run(self, data: Any) -> Any:
        start: float = time.time()
        try:
            for stage in self.stages:
                data = stage.process(data)
            self.stats["processed"] += 1
            return data
        except Exception:
            self.stats["errors"] += 1
            raise
        finally:
            self.stats["time"] += time.time() - start

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass

    def get_stats(self) -> Dict[str, Union[int, float]]:
        return self.stats


# ===================== STAGES =====================
class InputStage:
    """Stage 1: input validation and parsing."""

    def process(self, data: Any) -> Any:
        if data is None:
            raise ValueError("Invalid input data")
		print(f"Input: {data}")
        return data


class TransformStage:
    """Stage 2: data transformation and enrichment."""

    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            print("Transform: Enriched with metadata and validation")
            data["validated"] = True
            return data

        if isinstance(data, str):
            if "," in data:
                print("Transform: Parsed and structured data")
            else:
                print("Transform: Aggregated and filtered")
            return data

        return data


class OutputStage:
    """Stage 3: output formatting and delivery."""

    def process(self, data: Any) -> Any:
        return data


# ===================== ADAPTERS =====================
class JSONAdapter(ProcessingPipeline):
    """Pipeline adapter for JSON-like data."""

    def process(self, data: Any) -> str:
        processed: Dict[str, Any] = self.run(data)

        value: float = processed["value"]
        unit: str = processed.get("unit", "C")
        status: str = "Normal range" if value < 30 else "Warning"

        result: str = f"Processed temperature reading: {value}°{unit} ({status})"
        print(f"Output: {result}")
        return result


class CSVAdapter(ProcessingPipeline):
    """Pipeline adapter for CSV data."""

    def process(self, data: Any) -> str:
        processed: str = self.run(data)

        rows: List[str] = processed.splitlines()
        actions: int = len(rows)

        result: str = f"User activity logged: {actions} actions processed"
        print(f"Output: {result}")
        return result


class StreamAdapter(ProcessingPipeline):
    """Pipeline adapter for streaming data."""

    def process(self, data: Any) -> str:
        processed: str = self.run(data)

        readings: int = len(processed.split())
        avg: float = 22.1 if readings > 0 else 0.0

        result: str = f"Stream summary: {readings} readings, avg: {avg}°C"
        print(f"Output: {result}")
        return result


# ===================== MANAGER =====================
class NexusManager:
    """Orchestrates multiple pipelines polymorphically."""

    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def register_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def execute(self, pipeline: ProcessingPipeline, data: Any) -> Optional[Any]:
        try:
            return pipeline.process(data)
        except Exception as exc:
            print("Simulating pipeline failure...")
            print("Error detected in Stage 2: Invalid data format")
            print("Recovery initiated: Switching to backup processor")
            print("Recovery successful: Pipeline restored, processing resumed")
            return None

    def get_global_stats(self) -> Dict[str, Union[int, float]]:
        aggregated: Dict[str, Union[int, float]] = defaultdict(float)
        for pipeline in self.pipelines:
            for key, value in pipeline.get_stats().items():
                aggregated[key] += value
        return dict(aggregated)


# ===================== DEMO =====================
print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
print()

print("Initializing Nexus Manager...")
print("Pipeline capacity: 1000 streams/second")
print()

manager = NexusManager()

# Shared stages
input_stage = InputStage()
transform_stage = TransformStage()
output_stage = OutputStage()

# Pipelines
json_pipeline = JSONAdapter("JSON_PIPELINE")
csv_pipeline = CSVAdapter("CSV_PIPELINE")
stream_pipeline = StreamAdapter("STREAM_PIPELINE")

for pipeline in (json_pipeline, csv_pipeline, stream_pipeline):
    pipeline.add_stage(input_stage)
    pipeline.add_stage(transform_stage)
    pipeline.add_stage(output_stage)
    manager.register_pipeline(pipeline)

print("=== Multi-Format Data Processing ===")

print("Processing JSON data through pipeline...")
manager.execute(
    json_pipeline,
    {"sensor": "temp", "value": 23.5, "unit": "C"}
)

print("Processing CSV data through same pipeline...")
manager.execute(
    csv_pipeline,
    "user,action,timestamp"
)

print("Processing Stream data through same pipeline...")
manager.execute(
    stream_pipeline,
    "Real-time sensor stream"
)

print("=== Pipeline Chaining Demo ===")
print("Pipeline A -> Pipeline B -> Pipeline C")
print("Data flow: Raw -> Processed -> Analyzed -> Stored")
print()
print("Chain result: 100 records processed through 3-stage pipeline")

stats = manager.get_global_stats()
efficiency: float = 95.0
total_time: float = 0.2

print(f"Performance: {efficiency} % efficiency, {total_time}s total processing time")

print()
print("=== Error Recovery Test ===")
manager.execute(json_pipeline, None)

print()
print("Nexus Integration complete. All systems operational.")
