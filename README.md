# Vaccin spot

A Python application which will search into the Romanian COVID19 vaccine platform and look for an empty spot based on
the given configuration.

The application will look for an empty spot at a random interval between 20 and 60 seconds. If an empty spot is
available, it will automatically open a Chrome browser window where you can schedule the vaccination.

# Prerequisites

The application uses the `requests` library to make the API calls.

# Usage

```shell
# create a new Python virtual environment
python3 -m venv /path/to/new/virtual/environment
# activate the new venv
source /path/to/new/virtual/environment/bin/activate
# install the prerequisites
pip3 install -r requirements.txt
# run the application
python3 main.py
```

# Limitations

At this moment the application can only do searches for a single person at a time and in a single county.

Not all the Romanian counties are mapped by the current application. You can add the ones interesting for you by editing
the [judete.py](utils/judete.py) file.

Currently, the application only handles Chrome browser. If you use something else you need to edit the `open_browser`
function from the [main.py](main.py) file.

# Configuration

All the configuration needed for the application to work can be found in the [config.py](./config.py) file.

Mandatory variables:

- `cookie`: the cookie used by the sapplication to authenticate the requests;
- `persoane`: a dictionary containing all the persons you want to search a spot for. Acts more like a placeholder to
  have all the information prepared in the application;
- `looking_for_person`: the actual person the search will run for, must be either a reference from someone in
  the `persoane` dictionary or an instance of the [Person](utils/person.py) class;
- `looking_for_judet`: the county id for the earch, referenced from the [Judete](utils/judete.py) enum;
- `looking_for_vaccin`: the type of vaccine you're looking for, referenced from the [Vaccinuri](utils/vaccin.py) enum.

# Disclaimer

This is a project made in my spare time for fun. I'm not responsible for the platform changes that might break the usage
of this application nor if the platform administrators decide to ban your account from flooding them with requests.

The national identification number (CNP) and the registration ID are required by the vaccination platform for search and
not by my application.