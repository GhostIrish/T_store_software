# T-Store Project

## Introduction

This is the T-Store project, an application for product management using a graphical interface built with CustomTkinter and a MySQL database in Docker containers.

## Prerequisites

Before starting, ensure that your machine has the following software installed:

- **Python**
- **Git**: [Install Git](https://git-scm.com/)
- **Docker**: [Install Docker](https://www.docker.com/products/docker-desktop)

If you don't have these installed, you can find all the necessary installers in the Downloads folder.

## Setup and Execution Steps

Follow these steps to set up and run the application:

1. **Install Dependencies**:
   - Install Docker, Git, and Python if they are not already installed on your machine.

2. **Run the `setup.bat`**:

   - Execute the script by clicking on `setup.bat`:
     ```cmd
     setup.bat
     ```

## What the Script Does

When `setup.bat` is executed, it performs the following steps:

1. **Builds and Starts the MySQL Database Container**:
   - The script prepares, configures, and starts the MySQL database container on your Docker Desktop.

2. **Installs Project Dependencies**:
   - The script runs the command to install the required packages listed in `requirements.txt`.

3. **Sets Up the Database**:
   - The script executes the setup file that configures the MySQL database according to the project requirements.

## Verification

After running the script, check the following:

1. **Running Containers**:
   - Open Docker Desktop and verify that the MySQL and application containers are running.

2. **Database Access**:
   - Ensure that the MySQL database has started correctly and that the application is connected to it.

3. **Application Execution**:
   - Start the API located in the *dist* folder by clicking on the executable.

4. **Run the Software**:
   - After completing these steps, you can finally run the software executable and test the application!

## Support

If you encounter issues or have questions, feel free to open an issue on the GitHub repository or contact support.