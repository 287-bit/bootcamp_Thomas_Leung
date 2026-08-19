# Homework05
## Folder Structure
- **homework05/data/raw** → data table in csv format.
- **homework05/data/processed** → data table in parquet format.


## Formats used and why
- CVS - it is easy to read
- Parquet - it is compressed with a smaller file size and runs more efficient.
## How my code reads/writes using env variables
- Used DATA_DIR_RAW and DATA_DIR_PROCESSED variables from .env to write and read files.