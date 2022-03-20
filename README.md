# GenesisH0
A python script for creating the parameters required for a unique genesis block. SHA256/scrypt/X11/X13/X15/scrypt-n/lyra2re/lyra2rev2/lyra2rev3/verthash.

### Dependencies
    pip install scrypt construct==2.5.2 vertcoinhash

### Examples

Create the original genesis hash found in Vertcoin

    python3 genesis.py -a scrypt-n -p "???"

Create the original genesis hash found in Bitcoin

    python3 genesis.py -z "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks" -n 2083236893 -t 1231006505
Output:

    algorithm: sha256
    merkle hash: 4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b
    pszTimestamp: The Times 03/Jan/2009 Chancellor on brink of second bailout for banks
    pubkey: 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
    time: 1231006505
    bits: 0x1d00ffff
    Searching for genesis hash..
    genesis hash found!
    nonce: 2083236893
    genesis hash: 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
Create the regtest genesis hash found in Bitcoin

    python3 genesis.py -z "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks" -n 2 -t 1296688602 -b 0x207fffff

Create the original genesis hash found in Litecoin

    python3 genesis.py -a scrypt -z "NY Times 05/Oct/2011 Steve Jobs, Apple’s Visionary, Dies at 56" -p "040184710fa689ad5023690c80f3a49c8f13f8d45b8c857fbcbc8bc4a8e4d3eb4b10f4d4604fa08dce601aaf0f470216fe1b51850b4acf21b179c45070ac7b03a9" -t 1317972665 -n 2084524493
    
Create a unique genesis hash with custom pszTimestamp

    python genesis.py -a scrypt -z "Time flies like an arrow. Fruit flies like a banana."
     
### Options
    Usage: genesis.py [options]
    
    Options:
      -h, --help show this help message and exit
      -t TIME, --time=TIME  the (unix) time when the genesisblock is created
      -z TIMESTAMP, --timestamp=TIMESTAMP
         the pszTimestamp found in the coinbase of the genesisblock
      -n NONCE, --nonce=NONCE
         the first value of the nonce that will be incremented
         when searching the genesis hash
      -a ALGORITHM, --algorithm=ALGORITHM
         the PoW algorithm: [SHA256|scrypt|X11|X13|X15|scrypt-n|lyra2re|lyra2rev2|lyra2rev3|verthash]
      -p PUBKEY, --pubkey=PUBKEY
         the pubkey found in the output script
      -v VALUE, --value=VALUE
         the value in coins for the output, full value (exp. in bitcoin 5000000000 - To get other coins value: Block Value * 100000000)
      -b BITS, --bits=BITS
         the target in compact representation, associated to a difficulty of 1

