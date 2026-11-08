Windows : <br/>
python screenshotBolter.py 1 2 <br/>
Linux / Mac : <br/>
python3 screenshotBolter.py 1 2  <br/>
<br/>
Saves to the directory specified in the file with a UNIX timestamp

<br/>
<br/>

Create an environment for it, if you don't it doesn't matter too much. <br/>   
Under Windows this is : <br/>

python -m venv .venv <br/>
.\\.venv\Scripts\Activate.ps1 <br/>
<br/>
For Linux use python3 <br/>

(.venv) will now show before the prompt.   <br/>
Install the necessary python libraries : <br/>
<br/>
pip3 install mss <br/>
pip3 install pillow <br/>

Then to use : <br/>

python .\screenshotBolter.py 1 2  <br/>
Successfully saved ./monitor_1_1794103911269.428.png <br/>
Successfully saved ./monitor_2_1794103911315.223.png <br/>

Successfully saved combined image as ./combined_monitors_1794103911336.7268.png
