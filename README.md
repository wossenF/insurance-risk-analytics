# insurance-risk-analytics

A small project for exploratory data analysis and risk analytics on an insurance dataset. It contains data loading utilities, EDA helpers, visualizations, and tests to help analyze policy-level premiums and claims.

## Contents
- `data/` — raw and processed data. The raw dataset used here is `data/raw/MachineLearningRating_v3.txt`.
- `notebooks/01_eda.ipynb` — example exploratory analysis and visualizations.
- `notebooks/02_hypothesis_testing.ipynb` — hypothesis testing workflow for province, zipcode, and gender comparisons.
- `notebooks/03_modeling.ipynb` — modeling workflow for claim risk/severity experiments and premium estimation features.
- `src/` — project source code:
	- `src/data_loader.py` — helper to load the raw dataset.
	- `src/eda_utils.py` — EDA utility functions (missing-value summaries, derived metrics).
	- `src/hypothesis_tests.py` — statistical test helpers for t-tests, chi-square tests, and z-tests.
	- `src/modeling.py` — factory helpers that return regression and classification model dictionaries.
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

3. Run the hypothesis testing notebook:

- Open `notebooks/02_hypothesis_testing.ipynb` to reproduce the statistical tests used in the project. It loads the raw dataset through `src.data_loader.load_data`, computes derived columns such as `HasClaim` and `Margin`, and summarizes the results of chi-square and t-tests in a final table.

4. Run the modeling notebook:

- Open `notebooks/03_modeling.ipynb` to run baseline regression and classification experiments. The notebook uses numeric features, imputes missing values before model fitting, and reports RMSE/R2 for regression plus Accuracy/Precision/Recall/F1 for classification.

5. Run tests:

```
pytest -q
```

## Data
- Place raw data files under `data/raw/`. The example dataset used in this project is `data/raw/MachineLearningRating_v3.txt`.

Notes on data loading
- The `load_data` function in `src/data_loader.py` reads the pipe-separated file. Pandas may emit a `DtypeWarning` for mixed-type columns (e.g., columns 32 and 37); you can set `low_memory=False` or provide explicit `dtype` mappings to avoid the warning.

Data versioning with DVC
- This repository uses DVC for versioning and pushing large data files to a remote storage. If you cloned the repo and need the data, install DVC and pull the data with:

```
pip install dvc
dvc pull
```

- To push data (if you have write access to the configured DVC remote):

```
dvc push
```

Ensure your DVC remote is configured (see `.dvc/config` or run `dvc remote list`). The project may require authentication to access the remote storage.

## Development notes
- Notebook imports: notebooks add the repo root to `sys.path` with `sys.path.insert(0, str(Path.cwd().parent))` to allow `from src...` imports.
- Converting numeric columns: some numeric-looking columns may be strings; the notebook coerces these with `pd.to_numeric(..., errors='coerce')` before plotting.
- Hypothesis testing helpers: `src/hypothesis_tests.py` wraps `scipy.stats` functions so the notebook can reuse `t_test`, `chi_square_test`, and `z_test` consistently.
- Modeling helpers: `src/modeling.py` provides `get_regression_models()` and `get_classification_models()` used by `notebooks/03_modeling.ipynb`.

## Git workflow
- Work in feature branches. Example to create and push a branch for a change:

```
git checkout -b task-1
git add -A
git commit -m "chore(task-1): add README and fix notebook import and histogram"
git push --set-upstream origin task-1
```

This project pushed recent changes in branch `task-1` including the README updates and notebook fixes.

## Contributing
- Open an issue or create a pull request. Follow the existing project style and add tests for new helpers.

## License
This repository does not include a license file. Add one if you wish to publish or share the code publicly.
