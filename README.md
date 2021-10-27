# nrip-jamaica


> WORK IN PROGRESS 

Tools developed for National Risk Information Platform (NRIP) project in Jamaica in 2021

## Setup and installation

Clone or download this repository from
[GitHub](https://github.com/nismod/jamaica-infrastructure):

    git clone git@github.com:nismod/jamaica-infrastructure.git

Install required python packages:

    pip install -r requirements.txt

Toolsets include: 
- Geometric analysis toolset
  - Hostpot (density) analysis tool 
  - Proximity analysis tool
  - Intersection analysis tool
- Hydrological analysis toolset
  - Fill calculator
  - Flow direction calculator
  - Flow accumulation calculator
  - Flow network calculator
  - Integrated hydrological routine
- Coastal inundation toolset
  - Sea level rise mapping
  - Storm surge calculator
- Geomorphological flood risk toolset
  - Buffer flow network
  - Slope masking

Toolsets are currently implemented using arcpy, which requires an ArcGIS Desktop / ArcGIS Pro basic license. Some tools require the Data Management and Spatial Analyst extensions.
