
# ChemBL

This project loads ChemBL data about molecules into PostgreSQL database. essentially creating for tables for molecule id lookup, compound properties, compound structure and molecule dictionary for other properties.

## Table of Contents
1. [Dependencies](#dependencies)
2. [Setup](#setup)
3. [Configuration](#configuration)
4. [Usage](#usage)

## Dependencies
Make sure you have the following dependencies installed:

- `postgres`
- `libpq-dev`
- `python3-dev`

You can install python dependencies using the following command:
```sh
pip install -r requirements.txt
```

## Setup
1. Clone the repository:
```sh
git clone https://github.com/I-Bumblebee/chembl.git
```

2. Change the directory:
```sh
cd chembl
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

## Configuration

 Copy the `.env.example` file to `.env`:
```sh
cp .env.example .env
```
##### Fill out the following environment variables in the `.env` file:
##### PostgreSQL database :
---

- `DATABASE_USERNAME=`
- `DATABASE_PASSWORD=`
- `DATABASE_HOST=`
- `DATABASE_PORT=`
- `DATABASE_NAME=`

## Usage

Run the following commands to load ChemBL data into database:
```sh
python ./scripts/create_db.py
```
```sh
python ./scripts/fetch_chembl_data.py
```
