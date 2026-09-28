"""Report export to a fixed scratch file."""

import os
import tempfile
import time
from pathlib import Path

REPORT_PATH = Path(tempfile.gettempdir()) / "demo-service-report.txt"


def export_report(customer: str, rows: list[str]) -> Path:
    # Each export gets its own file so concurrent exports cannot clobber each other.
    fd, name = tempfile.mkstemp(prefix="demo-service-report-", suffix=".txt")
    path = Path(name)
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        fh.write(f"Report: {customer}\n" + "\n".join(rows))
    _notify_billing(customer)
    return path


def _notify_billing(customer: str) -> None:
    time.sleep(0.02)  # stands in for a network call to the billing service
