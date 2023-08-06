BIP39-compliant 24 word seed phrase generator for crypto wallets.

Based on the Python package [`mnemonic`](https://github.com/trezor/python-mnemonic)

You can run it locally on your machine with [run.sh](run_locally.sh)
or on an internet isolated docker container with [run_in_docker.sh](run_in_docker.sh)

The script will create a `words.txt` file with the seed phrase in the `output` folder.
It will then ask you for a password to create an encrypted `words.zip` file, which you may want to back up somewhere.
