def query_get_all_products():
    return """
    SELECT * FROM produtos;
"""

def query_update_publish(id):
    return f"""
    UPDATE produtos SET publicado=True where id={id};
"""