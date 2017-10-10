# General Commands

Useful commands for Rika's bioinfromatics class.

## ssh into liverpool / baross

Liverpool

```bash
ssh michelsd@liverpool.its.carleton.edu
```

Baross

```bash
ssh michelsd@baross.its.carleton.edu
```

## Screen / Tmux

See: [Cheat Sheet](http://www.dayid.org/comp/tm.html)

| Action                     | tmux         | screen   |
|----------------------------|--------------|----------|
| start new session          | `tmux`       | `screen` |
| detach from currently attached session | `^b d`OR `^b :detach`|`^a ^d` OR `^a :detach`|
| re-attach detached session | `tmux attach`| `screen-r` |

## File Transfer

### Filezilla

- Open Filezilla
- Host: sftp://liverpool.its.carleton.edu
- Username: Carleton username
- Password: Carleton password
- Port: 22
- Click QuickConnect

### Secure Copy

From liverpool to local:

```bash
scp [username]@liverpool.its.carleton.edu:/Accounts/[username]/[path of your destination directory]/[some_file.txt] ~/Desktop
```

From local to liverpool:

```bash
scp ~/Desktop/[some_file.txt] [username]@liverpool.its.carleton.edu:/Accounts/[username]/[path of your destination directory]
```