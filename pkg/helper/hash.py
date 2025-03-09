import hashlib


def sha256(input_string: str) -> str:
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()


def check_sha256(input_string: str, stored_hash: str) -> bool:
    return sha256(input_string) == stored_hash


def md5(input_string: str) -> str:
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()


def check_md5(input_string: str, stored_hash: str) -> bool:
    return md5(input_string) == stored_hash
