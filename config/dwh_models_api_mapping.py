TABLE_CHEMBL_ID_LOOKUP_KEYS = [
    'chembl_id',
    'entity_type',
    'last_active',
    'resource_url',
    'score',
    'status'
]

TABLE_COMPOUND_STRUCTURES_KEYS = [
    'molecule_chembl_id',
    ['molecule_structures', [
        'canonical_smiles',
        'molfile',
        'standard_inchi',
        'standard_inchi_key'
    ]]
]

TABLE_MOLECULE_PROPERTIES_KEYS = [
    'molecule_chembl_id',
    ['molecule_properties', [
        'mw_freebase',
        'alogp',
        'hba',
        'hbd',
        'psa',
        'rtb',
        'ro3_pass',
        'num_ro5_violations',
        'cx_most_apka',
        'cx_most_bpka',
        'cx_logp',
        'cx_logd',
        'molecular_species',
        'full_mwt',
        'aromatic_rings'
    ]]
]

TABLE_MOLECULE_DICTIONARY_KEYS = [
    'molecule_chembl_id',
    'pref_name',
    'max_phase',
    'therapeutic_flag',
    'dosed_ingredient',
    'structure_type',
    'chebi_par_id',
    'molecule_type',
    'first_approval',
    'oral',
    'parenteral',
    'topical',
    'black_box_warning',
    'natural_product',
    'first_in_class',
    'chirality',
    'prodrug',
    'inorganic_flag',
    'usan_year',
    'availability_type',
    'usan_stem',
    'polymer_flag',
    'usan_substem',
    'usan_stem_definition',
    'indication_class',
    'withdrawn_flag',
    'chemical_probe',
    'orphan',
    'helm_notation',
    'score'
]
