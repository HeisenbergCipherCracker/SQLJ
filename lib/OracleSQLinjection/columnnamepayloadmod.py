def columnnamepayloadmodification(table,iD,columnname):
    payload = f"""
SELECT {columnname} FROM {iD} WHERE table_name = '{table}';
SELECT {columnname} FROM {iD} WHERE table_name = '{table}' and owner = 'foo';
"""
    retval = payload
    return retval
    