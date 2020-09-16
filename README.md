# K-Drive-Leveler
A simple macro program to automatically level your K-Drive, with support for certain K Drive mods to increase the efficiency of the macro.

## Installation
Download and run the latest release executable from the [releases page](https://github.com/ProneToAdjust/K-Drive-Leveler/releases).

## Usage
### Set up
![](../assets/preferred_starting_position.jpg)  
- Postion your frame and K-Drive on a flat area, with alot of forward space, preferably the coolant lake outside of Fortuna's entrance in the Orb Vallis
### Macro usage
![](../assets/gui_screenshot.png)  
- Press left or right control on your keyboard to toggle the macro.
- Tick the checkboxes if you have the mods installed on your K-Drive.

## Developing
- Python version: [3.8.1](https://www.python.org/downloads/release/python-381/)
#### Installing dependencies
```
pip install -r requirements.txt
```
#### Testing and debugging
```
python k_drive_leveler.py
```
#### Executable packaging
```
pyinstaller k_drive_leveler.spec
```