# Quality Asurance approach

Listed below some of the QA practices implemented on this project.

The idea is to provide an overview of QA aspect used to build the tests and explain why each desition is taken.

## BDD: Gherkin as communication language

All the scenarios are written in [Gherkin syntax](https://cucumber.io/docs/gherkin/). 

Using the Given - When - Then structure, each test is written in a friendly syntax allowing to share and interact over them with different team members' roles. Using this as a common language to describe how a system should behave, allows QAs, devs, POs and other roles to interact more efficiently at early stages of the development proces. 

## Scenario tagging

This is a powerfull tool available in most of the automation frameworks that allows to orgnize the tests cases based on a totally customizable criteria.

In this project, the tests are organized and tagged based on the fuctionality and, crossing this criteria, prioritized into smoke, sanity and regression suites. This approach adds flexibility on executions, allowing to execute all the scenarios to test an specific feature or use them as a part of continues integration pipelines by playing with the smoke, sanity and regression tags. 

## Page object model

Page object model, also known as POM, is a design pattern in that creates an object repository for storing all web elements. It is useful in reducing code duplication and improves test case maintenance.

This particular implementating is structured on creating a base page class, providing the logic to interact with the web site using [Selenium](https://selenium-python.readthedocs.io/). All site pages are mapped into base page's child classes.
