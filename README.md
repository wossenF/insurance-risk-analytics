# insurance-risk-analytics

A small project for exploratory data analysis and risk analytics on an insurance dataset. It contains data loading utilities, EDA helpers, visualizations, and tests to help analyze policy-level premiums and claims.

## Contents
- `data/` — raw and processed data. The raw dataset used here is `data/raw/MachineLearningRating_v3.txt`.
- `notebooks/01_eda.ipynb` — example exploratory analysis and visualizations.
- `src/` — project source code:
	- `src/data_loader.py` — helper to load the raw dataset.
	- `src/eda_utils.py` — EDA utility functions (missing-value summaries, derived metrics).
	- `src/visualization.py` — plotting helpers.
- `tests/` — unit tests (run with `pytest`).

## Quickstart
1. Create a virtual environment and install dependencies:

```
python -m venv .venv
.\.venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

2. Run the EDA notebook (recommended using Jupyter or VS Code):

- Open `notebooks/01_eda.ipynb` and run the cells. The notebook inserts the repository root into `sys.path` so the `src` package imports resolve when running from the `notebooks/` folder.

3. Run tests:

```
pytest -q
```

## Data
- Place raw data files under `data/raw/`. The example dataset used in this project is `data/raw/MachineLearningRating_v3.txt`.

Notes on data loading
- The `load_data` function in `src/data_loader.py` reads the pipe-separated file. Pandas may emit a `DtypeWarning` for mixed-type columns (e.g., columns 32 and 37); you can set `low_memory=False` or provide explicit `dtype` mappings to avoid the warning.

## Development notes
- Notebook imports: notebooks add the repo root to `sys.path` with `sys.path.insert(0, str(Path.cwd().parent))` to allow `from src...` imports.
- Converting numeric columns: some numeric-looking columns may be strings; the notebook coerces these with `pd.to_numeric(..., errors='coerce')` before plotting.

## Contributing
- Open an issue or create a pull request. Follow the existing project style and add tests for new helpers.

## License
This repository does not include a license file. Add one if you wish to publish or share the code publicly.
