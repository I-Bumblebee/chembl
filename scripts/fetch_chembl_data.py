from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.dwh_models_api_mapping import (
    TABLE_CHEMBL_ID_LOOKUP_KEYS,
    TABLE_COMPOUND_STRUCTURES_KEYS,
    TABLE_MOLECULE_DICTIONARY_KEYS,
    TABLE_MOLECULE_PROPERTIES_KEYS,
)
from config.settings import DATABASE_URL
from models.dwh_models import (
    ChemblIdLookup,
    CompoundProperties,
    CompoundStructure,
    MoleculeDictionary,
)
from scripts.batch_fetch_and_store import concurrent_fetch_and_store_data

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


def main():
    model_api_mappings = {
        'chembl_id_lookup': {
            'endpoint': 'chembl_id_lookup.json',
            'path_items_key': 'chembl_id_lookups',
            'model': ChemblIdLookup,
            'keys': TABLE_CHEMBL_ID_LOOKUP_KEYS
        },
        'compound_structures': {
            'endpoint': 'molecule.json',
            'path_items_key': 'molecules',
            'model': CompoundStructure,
            'keys': TABLE_COMPOUND_STRUCTURES_KEYS
        },
        'compound_properties': {
            'endpoint': 'molecule.json',
            'path_items_key': 'molecules',
            'model': CompoundProperties,
            'keys': TABLE_MOLECULE_PROPERTIES_KEYS
        },
        'molecule_dictionary': {
            'endpoint': 'molecule.json',
            'path_items_key': 'molecules',
            'model': MoleculeDictionary,
            'keys': TABLE_MOLECULE_DICTIONARY_KEYS
        }
    }

    for model_name, model_data in model_api_mappings.items():
        concurrent_fetch_and_store_data(
            session_maker=sessionmaker,
            model_name=model_name,
            model_data=model_data,
            batch_size=100,
            number_of_threads=5,
            total=1000
        )


if __name__ == '__main__':
    main()
