# kirkwoodnight

[![A rectangular badge, half black half purple containing the text made at Code Astro](https://img.shields.io/badge/Made%20at-Code/Astro-blueviolet.svg)](https://semaphorep.github.io/codeastro/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/kirkwoodnight.svg)](https://badge.fury.io/py/kirkwoodnight)

Interactive command line tool to assist with planning and conducting observations at Indiana University's Kirkwood Observatory. Given a desired date, time, and duration of observation, this program allows the user to toggle various observational constraints to generate an observing schedule for up to 130 objects of interest, including solar system planets, bright stars, and Messier objects. The user may then select the specific objects they would like to observe during the night, upon text files will be generated for each object containing useful information (constellation, magnitude, type of object, etc.) as well as an observing schedule with observability and sky positions (Alt, Az) tabulated at various time intervals.

### Prerequisites
- [Python 3](https://www.python.org/downloads/) or greater
- [numpy](https://numpy.org)
- [pandas](https://pandas.pydata.org)
- [astropy](https://www.astropy.org)
- [astroplan](https://astroplan.readthedocs.io/en/latest/#)
- [skyfield](https://rhodesmill.org/skyfield/)
- [tabulate](https://pypi.org/project/tabulate/)
- [colorama](https://pypi.org/project/colorama/)

### Installing

kirkwoodnight may be installed simply with pip:

    $pip install kirkwoodnight

The package repository may also be accessed in full at https://github.com/ag161920/kirkwoodnight.

## Usage

It is highly recommended that this program is run from a new directory (e.g. "kirkwoodnights"). We also recommend that the terminal is maximized to fill the screen to best display the output tables.

Once the user is in the desired directory, the program may be initiated simply by typing its name in the command line:

    $kirkwoodnight

A series of prompts will then be displayed requesting the user to input the desired date (YYYY-MM-DD), time (HH:DD, military time in EST), and duration of their observing run. Then, the user will be asked about a series of observational constraints (hit ENTER to accept the defaults):
- Kirkwood's minimum altitude (deg), default is 20
- Kirkwood's maximum altitude (deg), default is 85
- Minimum separation from the moon (deg), default is 5
- Maximum allowable airmass, default is None
- Desired level of nighttime darkness (options are "civ", "naut", and "astro" respectively for "civil", "nautical", and "astronomical" conventions of nighttime), default is None
- Desired brightness level for the Moon (options are "grey" or "dark"), default is None
- How often the user wants to re-check observability (hours), default is 0.5 (every 30 minutes)

Finally, the user will be asked the number of objects they would like displayed in the output tables. Since these objects are sorted by observability, the tables returned will represent the objects that present the best combination of visibility and brightness. The output tables will contain relevant information about these objects, as well as observability over the course of the night.

The user will then be requested to input the ID numbers (second column, not the names!) of the objects they are most interested in. For each object, a text file will be generated containing characteristic information as well as an observing schedule (with Alt/Az sky positions) for the night. 

These text files, as well as a log file describing the parameters and constraints used for the run, will be collected and saved in a 
"output/[date_time]" directory automatically generated by the program. Each run of the program generates an additional subdirectory in "output", so it is recommended to either delete these output files or save elsewhere those associated with useful runs. 

## Collaboration and Individual Use
This code is a work in progress, so comments are welcome and encouraged! Any suggestions for improvement are appreciated, and this code is free to be altered and adapted locally to suit varied individual or institutional needs.


## Authors
  - Armaan Goyal (armgoyal@iu.edu)
  - Brandon Radzom (bradzom@iu.edu)
  - Jessica Ranshaw (jranshaw@iu.edu)
  - Xian-Yu Wang (xwa5@iu.edu)

## License

This project is distributed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for further
details.


