# socket-lab2
Socket programming with botnet and C&amp;C server


### Overview

The bots will listen commands from C&C Server and execute the commands.

```
             +-----+
             | BOT |
             +-----+
                |
+-----+   +------------+   +------------+
| BOT |---| C&C Server |---| BOT Master |
+-----+   +------------+   +------------+
                |
             +-----+
             | BOT |
             +-----+
```

### The lab purpose

All students need to program a BOT client for lab2.

### TODO

- [x] Improve C&C Server: Change return content when BOT master PUT the commands to it.
- [x] A BOT Master program (Using Requests HTTP library PUT the commands to C&C server).
- [ ] A BOT Master program: A bot master program use `raw socket` to change C&C server content.
