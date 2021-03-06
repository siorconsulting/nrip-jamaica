![alt text](nrip-logo.png)

# Toolset for National Risk Information Platform (NRIP) in Jamaica

Tools developed for National Risk Information Platform (NRIP) project in Jamaica in 2021.

## Project Context

The National Risk Information Platform (NRIP) is a multi-hazard risk information platform that will allow users to visualize risk data and perform analysis on various elements of risk data in Jamaica (http://nripja.com/). Its purpose is to promote a culture of safety and risk reduction by providing access to knowledge and information on hazard, vulnerability, exposure and loss and making it available for decision-making in development and land use planning, investments in social, economic and environmental sectors and risk transfer strategies. 

The NRIP is conceptualized as a platform that provides users with the ability to visualize and interact with hazard, vulnerability, and risk data through a series of map layers that can be activated and deactivated based on scenarios or analysis that the user wishes to perform. Each map layer will have supporting attribute data, as well as links to detailed information on hazards, vulnerability and losses contained in tables, photographs and reports that provide added information for location-specific analyses. In addition to the map feature, an NRIP module will include a community of practice that operates as a discussion forum for specialists and practitioners to share views, discuss ideas and concepts and suggest recommendations for best practices that benefit the sector (https://nripja.discoursehosting.net/). 

Sior Consulting Ltd. (https://siorconsulting.com/) supported the development of the platform by undertaking data manipulation, particularly LiDAR-driven data derivation for coastal, hydrological and geomorphological hazards in three study locations in Jamaica, and developing risk modelling toolsets (as provided here) and case studies to showcase the capabilities and outputs of the analysis tools.

## Versions

The NRIP Risk Analysis toolset is available in two analogous versions:

* Open-source version: https://github.com/siorconsulting/nrip-jamaica-open-source

* Licensed (ArcGIS) version: https://github.com/siorconsulting/nrip-jamaica-arcgis

<!--
Toolsets are currently implemented using arcpy, which requires an ArcGIS Desktop / ArcGIS Pro basic license. Some tools require the Data Management and Spatial Analyst extensions.
<!-- 

-->
## Setup and Installation

Clone or download this repository from
[GitHub](https://github.com/siorconsulting/nrip-jamaica):

    git clone git@github.com:siorconsulting/nrip-jamaica.git

Install required python packages:

    pip install -r requirements.txt

-->
## Toolsets  

(to be updated)

Toolsets include: 
- Geometric analysis toolset
  - Hotspot (density) analysis
  - Proximity analysis
  - Zonal (summarise-within) analysis
- Hydrological analysis toolset
  - Fill calculator
  - Flow direction calculator
  - Flow accumulation calculator
  - Flow network calculator
  - Basin delineator
  - Integrated hydrological routine
- Coastal inundation toolset
  - Sea level rise mapping 
  - Storm surge calculator 
- Geomorphological flood risk toolset
  - Buffer flow network
  - Slope masking

-->

## NRIP Analyst Training Program - Example notebooks on Gradient.run

- Link to Session 2: https://console.paperspace.com/te1mxcp78/notebook/r3hcpm3u8smht7a?file=nrip-training-session-2.ipynb
- Link to Session 3: https://console.paperspace.com/te1mxcp78/notebook/r3hcpm3u8smht7a?file=nrip-training-session-3.ipynb
- Link to Session 4: https://console.paperspace.com/te1mxcp78/notebook/r3hcpm3u8smht7a?file=nrip-training-session-4.ipynb
- Link to Session 5: https://console.paperspace.com/te1mxcp78/notebook/r3hcpm3u8smht7a?file=nrip-training-session-5.ipynb

<!--
### Example notebook on Google Colab
Link to Colab notebook: https://colab.research.google.com/drive/1GjPS-aYbshqJlh5eYuFvNsh488_z2FFQ?usp=sharing
<!-- 
