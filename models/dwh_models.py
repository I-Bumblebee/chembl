from sqlalchemy import DECIMAL, Boolean, Column, Float, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ChemblIdLookup(Base):
    __tablename__ = 'chembl_id_lookup'
    chembl_id = Column(String, primary_key=True, nullable=False)
    entity_type = Column(String, nullable=False)
    last_active = Column(Integer, nullable=True)
    resource_url = Column(String, nullable=False)
    score = Column(Float, nullable=True)
    status = Column(
        String,
        nullable=False,
        default='ACTIVE'
    )


class CompoundStructure(Base):
    __tablename__ = 'compound_structures'
    molecule_chembl_id = Column(
        String,
        primary_key=True,
        unique=True,
        nullable=False)
    canonical_smiles = Column(
        String,
        unique=True,
        nullable=True)
    molfile = Column(Text, unique=True, nullable=True)
    standard_inchi = Column(
        String,
        unique=True,
        nullable=True)
    standard_inchi_key = Column(
        String,
        unique=True,
        nullable=True)


class CompoundProperties(Base):
    __tablename__ = 'compound_properties'
    molecule_chembl_id = Column(String, primary_key=True, nullable=False)
    mw_freebase = Column(Float, nullable=True)
    alogp = Column(Float, nullable=True)
    hba = Column(Float, nullable=True)
    hbd = Column(Float, nullable=True)
    psa = Column(Float, nullable=True)
    rtb = Column(Float, nullable=True)
    ro3_pass = Column(String, nullable=True)
    num_ro5_violations = Column(Float, nullable=True)
    cx_most_apka = Column(Float, nullable=True)
    cx_most_bpka = Column(Float, nullable=True)
    cx_logp = Column(Float, nullable=True)
    cx_logd = Column(Float, nullable=True)
    molecular_species = Column(String, nullable=True)
    full_mwt = Column(Float, nullable=True)
    aromatic_rings = Column(Float, nullable=True)
    heavy_atoms = Column(Float, nullable=True)
    qed_weighted = Column(Float, nullable=True)
    mw_monoisotopic = Column(Float, nullable=True)
    full_molformula = Column(String, nullable=True)
    hba_lipinski = Column(Float, nullable=True)
    hbd_lipinski = Column(Float, nullable=True)
    num_lipinski_ro5_violations = Column(Float, nullable=True)
    np_likeness_score = Column(Float, nullable=True)


class MoleculeDictionary(Base):
    __tablename__ = 'molecule_dictionary'
    molecule_chembl_id = Column(String, primary_key=True, nullable=False)
    pref_name = Column(String, nullable=True)
    max_phase = Column(DECIMAL, nullable=True)
    therapeutic_flag = Column(Boolean, nullable=True)
    dosed_ingredient = Column(Boolean, nullable=True)
    structure_type = Column(String, nullable=True)
    chebi_par_id = Column(Integer, nullable=True)
    molecule_type = Column(String, nullable=True)
    first_approval = Column(Integer, nullable=True)
    oral = Column(Boolean, nullable=True)
    parenteral = Column(Boolean, nullable=True)
    topical = Column(Boolean, nullable=True)
    black_box_warning = Column(Integer, nullable=True)
    natural_product = Column(Integer, nullable=True)
    first_in_class = Column(Integer, nullable=True)
    chirality = Column(Integer, nullable=True)
    prodrug = Column(Integer, nullable=True)
    inorganic_flag = Column(Integer, nullable=True)
    usan_year = Column(Integer, nullable=True)
    availability_type = Column(Integer, nullable=True)
    usan_stem = Column(String, nullable=True)
    polymer_flag = Column(Integer, nullable=True)
    usan_substem = Column(String, nullable=True)
    usan_stem_definition = Column(String, nullable=True)
    indication_class = Column(String, nullable=True)
    withdrawn_flag = Column(Boolean, nullable=True)
    chemical_probe = Column(Integer, nullable=True)
    orphan = Column(Integer, nullable=True)
    helm_notation = Column(String, nullable=True)
    score = Column(Float, nullable=True)
