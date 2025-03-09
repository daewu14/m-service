class Paginate:
    def __init__(self, limit: int = 30, offset: int = 0):
        self.limit = limit
        self.offset = offset

    def get_meta(self, data: list | None) -> dict:
        next_page = self.offset + self.limit
        pref_page = self.offset - self.limit
        if len(data) < self.limit:
            next_page = None

        if pref_page <= 0 and self.offset == 0:
            pref_page = None

        return {
            "next_page": next_page,
            "pref_page": pref_page,
            "total_data": len(data)
        }


def new_paginate(limit: int = 30, offset: int = 0) -> Paginate:
    return Paginate(limit=limit, offset=offset)
