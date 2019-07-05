#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Author:  Nick Hughes
Title:   Udemy Tutorial
Website: django

Created: 2019

"""

"""

############
############ SECTION 1
############

This course will be used to setup a TDD (test driven development) Django rest API
that will create a recipe website.


--------------------------------------------
Methodologies
--------------------------------------------


    -- Python 3.7
            -- PEP 8
            -- Automatic Code Linting
    -- Django
            -- Python web framework
            -- Django ORM object Relational Mapper
                    -- Code to SQL database
            -- Django admin site for management
    -- Rest API
            -- Extension from Django
            -- Built Authentication
            -- Viewsets for the structure
            -- Serializes to validate and convert models
            -- Browser-able API
    -- Docker
            -- Visualization machine
            -- Light weight virtual machine
            -- Single environment
            -- Consistent dev environment
            -- Deploy to cloud platform


--------------------------------------------
Tavis-CI
--------------------------------------------

        -- Automate testing and linting system

           -- Can make a code for pushing code to github so that errors can be flagged


--------------------------------------------
Postgres SQL
--------------------------------------------


        -- Production grade database

        -- Easy to setup with Docker


--------------------------------------------
Unit tests
--------------------------------------------


    --> Isolate the code to test

    --> Check the code that works

    --> Brake the code down

            --> Setup     - create the database objects.

            --> Execution - Call the code with sample data that is correct.

            --> Assertion - Make sure that the fields that are correct are added.


    ??? Why write tests ???

        --> It is expected in most professional dev teams

        --> It makes it easier to change code

        --> saves on downtime.



    --> What is Test Driven Development TDD ?

        --> Write the unit tests and then write the code.



    --> Why use TDD

        --> Increased test coverage

        --> Ensure tests work

        --> Stay focused



--------------------------------------------
Installations
--------------------------------------------


"""
        conda create --name rest python=3.7

        # conda install django ### not needed yet

        conda install -c conda-forge docker-py

        conda install -c anaconda git

"""




--------------------------------------------
Dockerfile
--------------------------------------------




A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. Using docker build users can create an automated build that executes several command-line instructions in succession. This page describes the commands you can use in a Dockerfile




--------------------------------------------
Docker Compose File
--------------------------------------------



This allows us to run and control the different services that we run from the app.



--------------------------------------------
Creating a django project using our docker configuration
--------------------------------------------




Make the project using the config from this path

"""
    docker-compose run app sh -c "django-admin.py startproject app ."
"""





--------------------------------------------
Travis CI
--------------------------------------------



Travis CI is a hosted continuous integration service used to build and test software projects hosted at GitHub. Open source projects may be tested at no charge via travis-ci.org. Private projects may be tested at travis-ci.com on a fee basis





--------------------------------------------
Running tests
--------------------------------------------




"""
docker-compose run app sh -c "python manage.py test"

"""

Linting check

"""
docker-compose run app sh -c "python manage.py test && flake8"

"""






"""
