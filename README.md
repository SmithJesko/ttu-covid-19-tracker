![Imgur](https://i.imgur.com/NIWbW3O.png)

# Introduction
TTU COVID-19 Case Tracker is a tool that tracks the reported cases of COVID-19 at Texas Tech University. Reported cases are posted regularly. Case counts are based on self-reports to TTUHSC and include information allowed according to student and employee confidentiality laws.

Data pulled from: [TTUHSC](https://www.depts.ttu.edu/communications/emergency/coronavirus/)

Made by [Smith Jesko](https://smithjesko.com/)
<font color="#999">*Not an official service from Texas Tech University</font>

## Installation
- Clone the Repo: ```git clone https://github.com/SmithJesko/ttu-covid-19-tracker.git```
- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ``` requirements.txt ```
- Run the following commands:
```bash
cd $PATH/ttu-covid-19-tracker/src
pip3 install -r requirments.txt
```

## Usage
- Run the Django 2.2 server with the command: ``` python3 manage.py runserver ```
- Access the website on ``` https://127.0.0.1:8000/ ```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT License](https://choosealicense.com/licenses/mit/)

Copyright (c) 2020 Smith Jesko

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