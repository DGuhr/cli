import math
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import ConsoleMetricExporter, PeriodicExportingMetricReader

class Telemetry:
    def __init__(self):
        self.exporter = ConsoleMetricExporter()
        # using math.inf so it doesnt collect preiodically. we do this in collect ourselves, one-time.
        self.reader = PeriodicExportingMetricReader(self.exporter, export_interval_millis=math.inf) 
        provider = MeterProvider(metric_readers=[self.reader])
        metrics.set_meter_provider(provider)

    def collect(self):
        self.reader.collect()
