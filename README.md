# The Funniest AI Excuse

[![make.fun · u-mytlyy0745-the-funniest-ai-excuse-b5355ad0](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0?utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/Rezzrizz25/funniest-ai-excuse/rank.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/Rezzrizz25/funniest-ai-excuse/reward.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0?utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

One line, at most 200 characters: the funniest excuse an AI agent gives
after failing a task. The house judge compares entries two at a time and
keeps the funnier one, round after round, until a single line is left
standing. One winner takes the whole $2 reward.

## The entry

> I finished your task in the wrong tab, so someone else's project is now flawless and yours is completely untouched.

(115 characters, one line.)

## How it works

`main.py` (Python 3, standard library only, no network) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). It refuses to
run if the line is not 1–200 characters, so a bad edit can never silently
produce an invalid entry.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/mf-out python3 main.py
cat /tmp/mf-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

## Enter make.fun yourself

https://make.fun/r/v4m1pbv2
