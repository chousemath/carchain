### General Notes on Blockchains

* Blockchains can provide a single source of truth that cannot be tampered with
* A blockchain is a constantly growing ledger that keeps a permanent record of all the transactions that have taken place, in a secure, chronological, and immutable way
* A blockchain is immutable and as a result once something has been added into it, it cannot be changed
* Cryptographic hashes are a one-way function, you can go from input data to hash (a unique fingerprint of the input data), but there is no good way to go back from just the hash to input data
* By convention, a block with a hash with 4 leading zeroes represents a valid block
* Nonce: `number`-`used`-`once`, used to figure out how to make a block give you a valid hash, you can mine for a nonce that, when combined with the block number and the data, gives you a valid hash
* Every block in the blockchain is cryptographically tied to the previous block in the chain
* If you were to tamper with the data in `block-n`, the hash for that block would be alterered, invalidating all the blocks in front of that block in the chain, if you breakdown a block, it tears down the entire structure in front of that block, even if you mine for a nonce that generates a valid hash for `block-n`, you would have to repeat the process for every block in the chain in front of `block-n`
* The difficult level of solving for a cryptographic hash increases as the number of nodes in the system increases
* The difficulty level is adjusted every 2 weeks so that it takes approximately 10 minutes for any given block to be mined
* For someone to effectively tamper with the blockchain, they would need to have control of at least 51% of the computing power in the system, and would have to validate their own changes within 10 minutes (before someone else effectively mines the block)
* Blocks in a Blockchain are linked to each other through the process of cryptographic hashing. Each block is cryptographically hashed and includes the hash from the previous block as part of the hash, this makes it very easy to see if anyone has tampered with any block as changing the value of a hash for a block will automatically "break the chain" and make all the blocks after that block invalid
* Disintermediation: Disintermediation is the process of reducing or eliminating intermediaries (i.e.. "middle-men") between parties in a transaction. The fact that Bitcoin enables the exchange of value between two parties directly over the Internet without requiring the services of a bank or some other institution is an example of disintermediation
* Distributed-Trustless-Consensus: all the nodes agree that a transaction took place
* You don't actually store the coins in a Block but rather the transactions between users
* Each block has data, the previous block's hash, and its own hash
* Every hash algorithm has 5 requirements, `1. one-way`, `2. must be deterministic`, `3. fast computation`, `4. avalanche effect`, `5. must withstand collisions`

### General Notes on Bitcoin

* The role of a bitcoin miner is to build the blockchain of records (blocks, record of transactions) that form the bitcoin ledger
* A new block is added about once every 10 minutes
* The first block on the blockchain is referred to as `the genesis block`
* The genesis block does not have the previous block's hash, because it is by definition the first block in the chain
* SHA-256 is a type of cryptographic hash function which is used in Bitcoin
* You are not really anonymous when making transactions on the Bitcoin network, this is because all of your transactions are linked to your public address, and are published for all to see

### General Notes on Bitcoin Cash

* This is a new cryptocurrency created by a hard-fork from the original Bitcoin protocol, and enforces an 8MB block size limit (as opposed to Bitcoin's 1MB block size limit)

### General Notes on Ethereum

* A smart contract is a piece of code that lives on the Ethereum blockchain
* A node is a machine running an Ethereum client
* Ethereum technologies for developers include `Web3.js`, and technologies for consumers include `Metamask` and `Mist`
* An account on the Ethereum network has three components, `1. Account Address`, `2. Public Key`, and `3. Private Key`
* Your Ethereum account is completely decoupled from the numerous Ethereum networks out there, therefore you can have the exact same Ethereum account on multiple networks

```bash
# Parts of an Ethereum transaction
nonce: how many times a person has sent a transaction
to: address of account to which the ether is being sent
value: amount of ether being sent
gasPrice: amount of ether the sender is willing to pay per unit gas to get this transaction processed
startGas/gasLimit: units of gas that this transaction can consume
(v/r/s): cryptographic pieces of data used to generate the sender's account address, generated from the sender's private key
```

### Resources

* https://blockexplorer.com/
* https://www.blockchain.com/
