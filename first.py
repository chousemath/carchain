blockchain = [[0, 0]]


def get_last_block_value(chain):
    return chain[-1][1]


def add_value(chain, value):
    chain.append([get_last_block_value(blockchain), value])
    return chain


add_value(blockchain, 123.123)
add_value(blockchain, 333.333)
add_value(blockchain, 222.222)
print(blockchain)
print(get_last_block_value(blockchain))
