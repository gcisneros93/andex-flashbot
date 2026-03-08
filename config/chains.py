# Configuration for Chains

# Addresses for different chains
chains_config = {
    'Arbitrum': {
        'chain_address': '0x...ArbitrumAddress',
        'dex_router': '0x...ArbitrumDIEXRouter',
        'trading_pairs': [
            '0x...Token1:0x...Token2',
            '0x...Token3:0x...Token4'
        ]
    },
    'Base': {
        'chain_address': '0x...BaseAddress',
        'dex_router': '0x...BaseDEXRouter',
        'trading_pairs': [
            '0x...Token5:0x...Token6',
            '0x...Token7:0x...Token8'
        ]
    }
}