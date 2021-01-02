# Indeed Job Scrapping
Scrap jobs on [Indeed](https://www.indeed.com/) with this Python script.

Features
--------
- Search for jobs by their title and location.
- Print results in a table (using pandas).
- Save a csv file with user's authorization.

You can currently use the program to search jobs in these countries : France, United Kingdom, USA, Spain and Germany. I will more likely include other countries aswell.

Requirements
------------
You will need these following packages :
- [pandas](https://github.com/pandas-dev/pandas) ``pip install pandas`` v.1.1.4 or higher
- [requests](https://github.com/psf/requests) ``pip install requests``
- Beautiful Soup ``pip install beautifulsoup4``/``pip install bs4`` (you will also need a parser, in this case [html5lib](https://github.com/html5lib/html5lib-python) ``pip install html5lib``
- [tabulate](https://github.com/astanin/python-tabulate) ``pip install tabulate``

Alternatively, you can install all these packages by running ``pip install -r requirements.txt``.

Usage
------
1. Download the code, then open your terminal and set the directory to the ``indeed-scrapper.py`` directory folder, in this case /src/ (or simply MAJ + right click then "Open PowerShell window here").
2. Run the file with the following commande ``python indeed-scrapper.py``.
3. Enjoy !
