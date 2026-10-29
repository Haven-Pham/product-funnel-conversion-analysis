"""Executes the analysis notebook in place and refreshes its outputs, figures and tables.

    python scripts/run_notebook.py
"""
from pathlib import Path

import nbformat
from nbclient import NotebookClient

NOTEBOOK = Path(__file__).resolve().parent.parent / "notebooks" / "product_funnel_conversion.ipynb"

nb = nbformat.read(NOTEBOOK, as_version=4)
NotebookClient(nb, timeout=1800, kernel_name="python3",
               resources={"metadata": {"path": str(NOTEBOOK.parent)}}).execute()
for cell in nb.cells:
    cell.metadata.pop("execution", None)
nbformat.write(nb, NOTEBOOK)
print(f"Executed {NOTEBOOK.name}")
