# SHARN Welcome
A Simple CTF Challenge that expects user to see Client Side Files (HTML, CSS and JavaScript), edit request methods and headers.
## Requirements
Language Used = Python3<br />
Modules/Packages used:
* flask
<!-- -->
Install the dependencies:
```bash
pip install -r requirements.txt
```
## Solution
* 1st Part of the Flag is Hidden in HTML
* 2nd Part of the Flag is Hidden in CSS
* 3rd Part of the Flag is Hidden in JavaScript
* For obtaining 4th Part of the Flag, we've to send *POST* request to **/secret_route** with *User-Agents* Request Header set to *sharn*