# socket-lab2
Socket programming with botnet and C&amp;C server


### Overview

The bots will listen commands from C&C Server and execute the commands.

```
+-----+   +------------+   +------------+
| BOT |---| C&C Server |---| BOT Master |
+-----+   +------------+   +------------+
```

### The lab purpose

All students need to program a BOT client for lab2.

### TODO

- [x] Improve C&C Server: Change return content when BOT master PUT the commands to it. 
- [x] A BOT Master program (Using requests lib PUT the command)
- [ ] A BOT Master program: a bot master program use raw socket to change C&C server content.
