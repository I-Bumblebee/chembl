from concurrent.futures import ThreadPoolExecutor

import requests
from sqlalchemy import Engine, create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from config.settings import CHEMBL_API_URL, DATABASE_URL


def fetch_and_store_data(
        session_maker: sessionmaker,
        engine: Engine,
        model_name: str,
        model_data: dict,
        batch_size: int,
        offset: int = 0,
        total: int = None
):
    session = session_maker(bind=engine)
    while True and (total is None or offset < total):
        api_url = f"{CHEMBL_API_URL}/data/{model_data['endpoint']}?limit={batch_size}&offset={offset}"
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        items = data.get(model_data['path_items_key'], [])
        if not items:
            break

        records = []
        for item in items:
            record = {}
            for key in model_data['keys']:
                if isinstance(key, list):
                    nested_key, sub_keys = key[0], key[1]
                    nested_data = item.get(nested_key, {})
                    for sub_key in sub_keys:
                        record[sub_key] = nested_data.get(sub_key, None)
                else:
                    record[key] = item.get(key, None)
            records.append(model_data['model'](**record))

        try:
            session.bulk_save_objects(records)
            session.commit()
        except IntegrityError:
            session.rollback()
            for record in records:
                try:
                    session.add(record)
                    session.commit()
                except IntegrityError:
                    session.rollback()

        offset += batch_size

    session.close()
    print(f"Finished fetching and storing {model_name}")


def concurrent_fetch_and_store_data(
        session_maker: sessionmaker,
        model_name: str,
        model_data: dict,
        batch_size: int,
        number_of_threads: int,
        offset: int = 0,
        total: int = None
):
    engine = create_engine(DATABASE_URL)

    with ThreadPoolExecutor(max_workers=number_of_threads) as executor:
        for i in range(number_of_threads):
            executor.submit(
                fetch_and_store_data,
                session_maker=session_maker,
                engine=engine,
                model_name=model_name,
                model_data=model_data,
                batch_size=batch_size,
                offset=offset + i * batch_size,
                total=total // number_of_threads
            )
    print(f"Finished fetching and storing {model_name}")
