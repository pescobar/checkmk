# Info

## Here we can place only:
1. *.sln
2. readme.txt
3. build scripts
4. CMakeLists.txt 
5. .gitignore
<<<<<<< HEAD

## Test Scripts
call_unit_tests.cmd
or
To check only few tests
call_unit_tests.cmd EventLog*
or
To check only few tests also in 64-bit version
call_unit_tests.cmd EventLog* both

## Assorted
To build and measure time:
x time_build_release.ps1

To unit-test and measure time:
x time_unit_tests.ps1
=======
6. Makefile

## Installation

**You need have choco already installed** to build release

Run *windows_setup.cmd*. This is **Simplest** method to install some required Windows software

Alternatively you can **choco install make** and use Makefile

## Build Scripts
1. build_release.cmd - to build MSI in artefacts
2. build_watest.cmd- to build 32-bit watest to be used later


## Test Scripts
1. Unit Testss Full: call_unit_tests.cmd
2. Unit Tests Part: call_unit_tests.cmd EventLog*
3. Integration Tests: call_integration_tests.cmd

## Assorted
To build and measure time use ptime
To run arbitrary powershell script use x

## Build of frozen binaries
*make frozen_binaries* to build exe and put it into  the artefacts directory
or
*make clean* to clean directories from the trash
>>>>>>> upstream/master
