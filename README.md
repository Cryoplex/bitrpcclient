# bitrpcclient
BitRPCClient is a JSON-RPC client for bitcoind.

## Sample code
```
>>> import bitrpcclient
>>> cl = bitrpcclient.BitRPCClient('<username>', '<password>', port=18332)
>>> cl.getinfo()
{u'connections': 8, u'errors': u'Warning: unknown new rules activated (versionbit 28)', u'blocks': 874973, u'paytxfee': 0.0, u'keypoololdest': 1466689788, u'walletversion': 60000, u'difficulty': 1, u'testnet': True, u'version': 120100, u'proxy': u'', u'protocolversion': 70012, u'timeoffset': -1, u'balance': 0.0, u'relayfee': 1e-05, u'keypoolsize': 101}
>>> cl.getblockhash(0)
u'000000000933ea01ad0ee984209779baaec3ced90fa3f408719526f8d77f4943'
```

## Run bitcoind
To run the above sample, run the bitcoind daemon:
```
bitcoind -server -rpcuser=<username> -rpcpassword=<password> -testnet
```
## Errors
A `BitRPCException` is raised if something wrong. On properly handled errors from the JSON-RPC server a `BitRPCErrorResponse` with the code and the message of the error. Otherwise a BitRPCException will be raised with a message.

## License
bitrpcclient is distributed under Apache License 2.0. See LICENSE file.

