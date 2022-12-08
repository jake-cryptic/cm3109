# cm3109-cw

Please run using Python 3.10 or higher if possible, that is the version of python I used when developing this.

Example of running code:
```bash
python3 src/run.py path/to/file.wmg
```

**Important**: Make sure to install numpy before running the application, as I use it to do matrix stuff

```bash
pip install -r requirements.txt
# OR
pip install numpy==1.23.5
```

Should do the trick

### Questions you may have
Why so many files?

	I like object oriented code


What do they do?

	Good question!

- graph_maker.py
  - Uses matplotlib to plot the graphs in the report
- param_hunter.py
  - Brute forces Simmulated Annealing parameters to find optimal ones
  - I planned to make this multi-threaded so it was faster... But I decided against that so I had time to write the report
- ranking.py
  - Stores a neighbourhood pretty much, has code to generate new ones
- run.py
  - Entrypoint for the coursework requirements
- sa.py
  - SimulatedAnnealing class that runs the pseudo-code from the lectures
- wmg.py
  - Parser for the wmg files, should be smart enough to work with more data sets than just this one! (Try it if you like)
