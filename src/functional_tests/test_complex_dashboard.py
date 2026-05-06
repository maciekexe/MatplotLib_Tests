# TODO: implement complex dashboard test
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import os
def test_complex_dashboard(tmp_path):
    output_file = tmp_path / "dashboard.png"