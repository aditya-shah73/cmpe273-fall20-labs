# Lab 2

## Requirements

Implement a master-work pattern to calculate the square root of the numbers using ZeroMQ.

```

                       PUSH      PULL      PUSH 
|--------------------| ------> | Worker | -------> |-----------|
| Generator (Master) | ------> | Worker | -------> | Dashboard |
|--------------------| ------> | Worker | -------> |-----------|

```

* Generator

The generator component generates a list of numbers from 0 to 10,000 and sends (PUSH) those numbers to Worker.


* Worker

The worker component listens (PULL) the numbers from the generator in a round robin fashion and calculate a square root of the numbers. Finally, sends the result to the dashboard.


* Dashboard

The dashboard component receives the result from the workers and displays the result to the console.

## Steps to execute

```
pipenv shell
pipenv install
python dashboard.py #Terminal 1
python worker.py #Terminal 2
python worker.py #Terminal 3
python worker.py #Terminal 4
python generator.py #Terminal 5
```

### Output

The output from all the terminal sessions is stored in output.txt
