## Commands
```shell
$ getoc dl 4.1 # Gets latest 4.1
$ getoc dl 4.6.4
$ getoc dl stable-4.6
$ getoc dl latest-4.5

$ getoc # Default behavior is to show prompt on downloading binaries
$ getoc switch # Switch your oc link to point to something else 

$ getoc stable-4.6 --include-kubectl
$ getoc usage # Displays disk usage summary of binaries
$ getoc clean # Removes all downloaded binaries from ~/.local/getoc/bin
```

## Directories
- The `oc` binaries downloaded are stored in `~/.local/getoc/bin`
- `~/.local/getoc/bin` is automatically added to user's `$PATH`.

## Development

```shell
$ git clone https://github.com/bostrt/getoc.git
$ cd getoc
$ virtualenv v
$ source v/bin/activate
$ pip install -e .
$ getoc -h
```
