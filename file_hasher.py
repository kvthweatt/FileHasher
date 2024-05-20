import hashlib

def compute_hashes(file_path) -> dict | None:
    sha512_hash = hashlib.sha512()
    sha256_hash = hashlib.sha256()
    md5_hash = hashlib.md5()

    if file_path == "":
        print(f"No file entered. Please specify a file name.\n")
        return None

    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha512_hash.update(byte_block)
                sha256_hash.update(byte_block)
                md5_hash.update(byte_block)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None
    
    return {
        'SHA-512': sha512_hash.hexdigest(),
        'SHA-256': sha256_hash.hexdigest(),
        'MD5': md5_hash.hexdigest()
    }

while (True):
    file_path = input("Enter a file to hash: ")
    hash_results = compute_hashes(file_path)

    if hash_results is None:
        continue
    
    print(f"Hashes for '{file_path}':\n")
    print(f"SHA-512: {hash_results['SHA-512']}\n")
    print(f"SHA-256: {hash_results['SHA-256']}\n")
    print(f"MD5: {hash_results['MD5']}\n")
