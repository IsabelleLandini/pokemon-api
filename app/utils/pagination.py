def build_pagination(*, total: int, limit: int, offset: int, base_url: str = '/pokemons'):
    next_offset = offset + limit
    prev_offset = offset - limit

    return {
        'total': total,
        'limit': limit,
        'offset': offset,
        'next': (
            f'{base_url}?limit={limit}&offset={next_offset}'
            if next_offset < total
            else None
        ),  
        'previous': (
            f'{base_url}?limit={limit}&offset={max(prev_offset, 0)}'   
            if offset > 0
            else None 
        )  
    }