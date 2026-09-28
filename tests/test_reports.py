from demo_service.reports import export_report


def test_export_report_starts_with_the_customer():
    path = export_report("acme", ["line 1", "line 2"])
    assert path.read_text(encoding="utf-8").startswith("Report: acme\n")
