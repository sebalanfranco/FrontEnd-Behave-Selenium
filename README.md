# Demoblaze automation testing

## What is the purpose of this repo?

The main goal is to complete the coding exercise sent by BoostUp, implementing an automation testing framework to test the [Demoblaze](https://www.demoblaze.com/) site.
The project is based on [Python](https://www.python.org/), [Behave](https://behave.readthedocs.io/en/latest/) and [Selenium](https://selenium-python.readthedocs.io/).

## Some practices used.

**Page object patter**: in order to interact with the different pages of the site, this pattern is implemented. It is useful in reducing code duplication and improves test case maintenance.

**Utils custom modules**: aiming at keeping the steps definition as simple as possible, all external libraries are used in modules within the `steps/utils/` folder.

**Scenarios tagging**: all scenarios are organized in suites based on priority and featured affected using [tags](https://behave.readthedocs.io/en/latest/tag_expressions.html).

## Table of contents
- [Pre-requisites and setup](docs/Setup.md)
- [Tests execution](docs/TestsExecution.md)
