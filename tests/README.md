# Tests

## Purpose
The purpose of the tests are to help developers of PaperTTY. By running the tests you can (hopefully) verify that your changes did not cause any undesired side effects.

## Configuration
The tests were developed on a Raspberry Pi 400 and a 9.7 inch Waveshare screen with resolution 1200 × 825. If you want to run the tests using another computer or another screen you probably will need to modify some parameters in the tests.

## Running the tests
Given that you have installed PaperTTY using Poetry, you can run the tests with
```bash
sudo poetry run pytest
```
