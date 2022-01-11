import hashlib

import verthash

verthash_data = None
if verthash_data is None:
    with open('verthash.dat', 'rb') as f:
        verthash_data = f.read()

    verthash_sum = hashlib.sha256(verthash_data).hexdigest()
    assert verthash_sum == 'a55531e843cd56b010114aaf6325b0d529ecf88f8ad47639b6ededafd721aa48'

def verthash_hash(dat):
    return verthash.getPoWHash(dat, verthash_data)
