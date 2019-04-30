<h1>Text Alignment</h1>

In Python, a string of text can be aligned left, right and center.
<br>
<b>.ljust(width)</b>
<br>
This method returns a left aligned string of length width.
<br>
<hr>
>>>> width = 20
>>> print 'HackerRank'.ljust(width,'-')<br>
HackerRank---------- 
<hr>
<b>.center(width)</b>
<br>
This method returns a centered string of length width.
<hr>
>>> width = 20<br>
>>> print 'HackerRank'.center(width,'-')<br>
-----HackerRank-----<br>
<hr>
<b>.rjust(width)</b><br>
This method returns a right aligned string of length width.
<hr>
>>> width = 20<br>
>>> print 'HackerRank'.rjust(width,'-')</br>
----------HackerRank<br>
<b>Task</b>
You are given a partial code that is used for generating the HackerRank Logo of variable thickness. <br>
Your task is to replace the blank (______) with rjust, ljust or center.<br>
<b>Input Format</b>
A single line containing the thickness value for the logo.<br>
<b>Constraints</b><br>
The thickness must be an odd number. <br>
<b>0<thickness<50</b><br>
<b>Output Format</b><br>
Output the desired logo<br>
<h1>Sample Input</h1>
<hr>
<h1>5</h1><br>
<hr>
<h1>Sample Output</h1><br>
<a href="https://hr-testcases-us-east-1.s3.amazonaws.com/9953/output03.txt?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1556612515&Signature=kZtDim%2FKDBLH1ayZRh%2BNF%2Fejssk%3D&response-content-type=text%2Fplain"><h1> Click here! </h1>
