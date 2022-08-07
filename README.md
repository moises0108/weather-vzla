# weather-avg next 15 days
## Description

take the next 15 days pronostic weather from https://www.visualcrossing.com/weather-api and graph with the warming and coldest day from any location
## Install and Run
- First of all you need to install de package in [requeriments.txt](requeriments.txt)
- Create a account in https://www.visualcrossing.com/weather-api and copy the apikey
- Paste the apikey in a new file called config.py like this: api_key="YOUR KEY" 
- if you want to change the coords just modift the variables 'lat'(latitude) and 'lon'(longitude) from th file [request.py](request.py)
- if you want to change de title just change variable 'title' in [graphic.py](graphic.py)
## How to use
- Just run the file main.py and you will se the graph like this
![image](https://user-images.githubusercontent.com/49890569/183305098-a9d50ad6-6155-48f0-a4a1-6491d9d7de65.png)
## License
MIT License

Copyright (c) [2022] [Moises Alejandro Patino Hernandez]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
