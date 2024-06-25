# MOTD Rotator

This is a simple tool to help make ssh a little less boring. I wrote this with the intention of creating an automated way of making the MOTD be fun messages.

&copy; 2024 [Pete Smith](https://www.psmit.dev/). This tool is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

## Usage

This tool effectively has two parts that need to happen. Firstly, the possible messages need to be set. Secondly, it (optionally) (but it will be so much better if you do) be automated.

### Changing the MOTDs

Changing the possible MOTDs is relatively straightforward and is done via a JSON file, "motds.json", in the same directory as the script. The JSON's default structure is as follows:

```JSON
{
	"messages": [list of strings],
	"prideMonth": "custom MOTD for pride month",
	"birthday": "birthday message"
}
```

The contents of the "prideMonth" field will always be used during the month of June. Outside of the month of June, a random selection from "messages" will be chosen. The only exception to this is the "birthday" field. If desired, users should manually enter their birthday into the script to make the contents of the "birthday" field appear on their birthday. Regardless, the MOTD will always be appended by a newline character for aesthetic purposes.

Other special cases may be added à la "prideMonth", however the script will have to be updated to reflect those additions. Their implementations should be similar to the script's current implementation for handling the "prideMonth" field.

### Automating the script

Because it edits `/etc/motd`, the script requires root access. To use this as part of a crontab, be sure to use `sudo crontab -e` instead of just `crontab -e`. Similarly, if running the script manually instead of via automation, be sure to use `sudo python3 rotator.py` (or whatever other python interpreter is installed instead of python3).

Because it requires root access and uses system calls to effectively use the command line, be sure to use extra caution and implement various protections. If allowing for arbitrary user inputs, be sure to implement some form of checks to prevent users from inserting malicious code. By default, this script does not any implement any such protections because I only wrote it for myself with my specific use case in mind.

