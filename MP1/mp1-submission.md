<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Gagan Indukala Krishna Murthy (gi36)</td></tr>
<tr><td> <em>Generated: </em> 2/19/2023 5:10:40 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-1-tracker-app/grade/gi36" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219284872-f6ecfb7b-f47b-495d-bb63-1989bc7e440c.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>add_task code <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219285071-09ce6c37-11a0-4f67-87d4-d69679f279ee.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>tracker.json file after successfully adding a task<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219285308-59d5d055-1da4-4f52-8c84-4f4ce89a7897.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>terminal output and success message for adding a task<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219286799-529eda64-00f3-4702-8103-6c06b30a2ca3.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Task adding rejection due to invalid or missing task name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219286975-ef0b7313-0d9c-4999-9434-d0294aded813.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Task adding rejection due to invalid or missing task description<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219289759-f24e72c7-ad48-4b3f-add1-173a75b39194.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Task adding rejection due to invalid or missing task DUE DATE<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <p><b>Sub Task 1 and Sub Task 2:&nbsp;</b><div>1.&nbsp;&nbsp;<span style="font-size: 13px;">update lastActivity with the current<br>datetime value</span><div><b style="font-size: 13px;">Solution:</b><span style="font-size: 13px;">&nbsp;I imported the DateTime class from DateTime Module<br>and used datetime.now() to get the current date and time, then I used<br>strftime() to create a string representing date and time in another format.</span></div><div><span style="font-size:<br>13px;">2.&nbsp;</span><span style="font-size: 13px;">set the name, description, and due date (all must be provided)</span></div></div><div>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;<b>Solution</b>: to set the name, description and due date I used the<br>copy function from the copy module to the tasks dict and added the<br>values from the user input and appended it to the tasks list&nbsp;</span></div><div><span style="font-size:<br>13px;">3.</span><span style="font-size: 13px;">due date must match one of the formats mentioned in str_to_datetime()</span></div><div>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;<b>Solution:&nbsp; </b>used try catch and handled the due date format according to<br>the format in str_to_datetime()</span></div><div><span style="font-size: 13px;">4.&nbsp;</span><span style="font-size: 13px;">output a message confirming the new<br>task was added or if the addition was rejected due to missing data</span></div><div>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;<b>Solution: </b>Added a confirmation print message after the successfully adding a task<br>and handled all invalid data input or missing input and added a failure<br>print message for the same.</span></div><div><span style="font-size: 13px;">5.&nbsp;</span><span style="font-size: 13px;">make sure save() is still<br>called last in this function</span></div><div><span style="font-size: 13px;"><b>Solution:&nbsp;</b>&nbsp;after writing the successful print message and<br>appending the the task, save() function was called.</span></div><div><span style="font-size: 13px;">6.&nbsp;</span><span style="font-size: 13px;">include your<br>ucid and date as a comment of when you implemented this, briefly summarize<br>the solution</span></div><div><span style="font-size: 13px;"><b>Solution: </b>Added a comment in the add_task function at the<br>start of my name, ucid, date and brief solution.&nbsp;</span></div><div><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;"><b>Brief<br>summary:</b> I used the copy function of the copy module to the task<br>dict and initialized it with values from the user input and appended it<br>to the tasks list . I also performed input validation for input name,<br>description, due date from the user and also validated the proper datetime format<br>for due date by exception handling and I added a print statement in<br>the end for successfully adding a task.</span></div><div><span style="font-size: 13px;"><br></span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219332343-0c42c441-1106-407f-a983-1fe78303ee66.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>process_update code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219332410-af69cb41-7e9b-4526-9fb0-bdb6b46346cd.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>output - show the existing value of each property where the TODOs are<br>marked in the text of the inputs (replace the TODO related text) (line<br>97 to 99)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219332563-76c776d9-04db-4e80-8681-b4c1dab0b539.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>index out of bounds scenarios validated with error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <div><b>Sub-Task 1:</b></div>1.&nbsp;<span style="font-size: 13px;">get the task by index</span><div><span style="font-size: 13px;"><b>Solution: </b>Got the task<br>index by passing index to the tasks list - tasks[index]</span></div><div><span style="font-size: 13px;">2.&nbsp;&nbsp;</span><span style="font-size:<br>13px;">consider index out of bounds scenarios and include appropriate message(s) for invalid index</span></div><div><span<br>style="font-size: 13px;"><b>Solution:&nbsp;</b>To validate the index bound I added a if condition "len(tasks)-1 &lt;<br>index or index &lt; 0" if the condition passes then it print a<br>index out of bound error message</span></div><div><span style="font-size: 13px;">3.&nbsp;&nbsp;</span><span style="font-size: 13px;">show the existing value<br>of each property where the TODOs are marked in the text of the<br>inputs (replace the TODO related text)</span></div><div><span style="font-size: 13px;"><b>Solutions:&nbsp;</b>To start I passed index to<br>tasks list to get the index number, later to the same I passed<br>name, description&nbsp;</span><span style="font-size: 13px;">and due to get the current name, description and due<br>of the input index by the user and replaced it with TODO text<br>in the print function (line 97 to 99)</span></div><div><span style="font-size: 13px;">4. Include your ucid<br>and date as a comment of when you implemented this, briefly summarize the<br>solution</span></div><div><span style="font-size: 13px;"><b>Solution: </b>Added ucid, name, date and brief summary of the code<br>written (line 89-91)</span></div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219829990-69f660f8-c5c8-4ec1-b721-ea46f10fee99.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code of update_task<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219830037-ab09a5a2-52ed-4a48-9882-686cf9df7aa0.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>tracker.json file after the successfully updated<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219830083-b6f74eeb-86bd-43aa-bee8-12cd9daac872.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message/ task not updated message if the task was not updated due<br>to no changes made <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219830074-90ddff9c-1e71-4eae-9ef1-d66904da14ab.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>task successfully updated message and the output if the update_task<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <div><span style="font-size: 13px;"><b>Sub-Task 1 and Sub-Task 2 :</b></span></div><span style="font-size: 13px;">1. find the task<br>by index</span><div><span style="font-size: 13px;"><b>Solution:</b> I am finding the task by passing index to<br>it<b> -&nbsp;</b>tasks[index]&nbsp;</span></div><div><span style="font-size: 13px;">2.&nbsp;</span><span style="font-size: 13px;">consider index out of bounds scenarios and include<br>appropriate message(s) for invalid index</span></div><div><span style="font-size: 13px;"><b>Solution:&nbsp;</b></span><span style="font-size: 13px;">To validate the index bound<br>I added a if condition "len(tasks)-1 &lt; index or index &lt; 0" if<br>the condition passes then it print a index out of bound error message</span></div><div><span<br>style="font-size: 13px;">3.&nbsp;</span><span style="font-size: 13px;">update incoming task data if it's provided (if it's not<br>provided use the original task property value)</span></div><div><b style="font-size: 13px;">Solution:&nbsp;</b><span style="font-size: 13px;">I am call<br>3 if condition for name description and due to check if it not<br>equal to a empty string, if the condition passes then i will be<br>taking the input&nbsp;</span><span style="font-size: 13px;">passed from the process_update function and replacing with the<br>existing values( which is basically updating).</span><span style="font-size: 13px;">&nbsp;If the user is not giving<br>any input then I am keeping the existing value as it is.</span></div><div><span style="font-size:<br>13px;">4.&nbsp;</span><span style="font-size: 13px;">update lastActivity with the current datetime value</span></div><div><span style="font-size: 13px;"><b>Solution:&nbsp;&nbsp;</b></span><span style="font-size: 13px;">&nbsp;I<br>imported the DateTime class from DateTime Module and used datetime.now() to get the<br>current date and time, then I used strftime() to create a string representing<br>date and time in another format and passed it to the lastActivity key<br>of the given index</span></div><div><span style="font-size: 13px;">5.&nbsp;</span><span style="font-size: 13px;">output that the task was updated<br>if any items were changed, otherwise mention task was not updated</span></div><div><b style="font-size: 13px;">Solution:&nbsp;</b><span<br>style="font-size: 13px;">the final output for success message I am using a variable is_updated<br>which will be initially false, which I will be making true if a<br>if condition&nbsp;is executed.&nbsp;In the end if the is_updated is true then I am<br>printing the success message else I will print the task not updated message.</span></div><div><span<br>style="font-size: 13px;">6.&nbsp;</span><span style="font-size: 13px;">make sure save() is still called last in this function</span></div><div><b<br>style="font-size: 13px;">Solution:&nbsp;</b><span style="font-size: 13px;">&nbsp;Save function is being called in the last ( line<br>133)</span><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">I have added my name, ucid, date<br>of the code written and the summary of the function update_process.</span></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219938610-f8bf9d39-a2db-4af0-847d-920d3e563a0d.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Function for mark_done<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219938699-1ab18958-9d8a-4082-a42c-3a54a0d44888.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>index out of bound message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219938751-56b4af83-c3b8-4ad0-aa0a-ddaac3a7fcc5.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Mark done successful message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219938760-70fad505-bd70-42af-a12f-3dacaffa694d.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>task was already done message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <div><b>Sub- task 1 and sub - task 2 :&nbsp;</b></div>1.&nbsp;<span style="font-size: 13px;">find task from<br>list by index</span><div><span style="font-size: 13px;"><b>Solution:&nbsp;</b>tasks[index]</span></div><div><span style="font-size: 13px;">2.&nbsp;</span><span style="font-size: 13px;">consider index out of bounds<br>scenarios and include appropriate message(s) for invalid index</span></div><div><b style="font-size: 13px;">Solution:&nbsp;</b><span style="font-size: 13px;">I am<br>checking for the index out of bounds scenarios like the usual way like<br>how I have done in the previous functions</span><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">3.&nbsp;</span><span style="font-size:<br>13px;">if it's not done, record the current datetime as the value</span></div><div><b style="font-size: 13px;">Solution:&nbsp;</b><span<br>style="font-size: 13px;">&nbsp;I am using a if else condition in which I am checking<br>if done is equal to true for the given index, if this condition<br>passes&nbsp;then I am marking done as true and updating the lastActivity to current<br>datetime by using the datetime class from datetime module and formatting&nbsp;the datetime&nbsp;&nbsp;according&nbsp;to our<br>format required format and I am also printing the task was marked done<br>successfully message.</span></div><div><span style="font-size: 13px;">4.&nbsp;</span><span style="font-size: 13px;">if it is done, print a message saying<br>it's already completed</span></div><div><b style="font-size: 13px;">Solution:</b><span style="font-size: 13px;">&nbsp;</span><span style="font-size: 13px;">in the else I am<br>printing the message Task is already completed.<b>&nbsp;</b></span></div><div><span style="font-size: 13px;">5.&nbsp;</span><span style="font-size: 13px;">make sure save()<br>is still called last in this function</span></div><div><b style="font-size: 13px;">Solution: </b><span style="font-size: 13px;">the save<br>function is being called in the last.</span><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;"><br></span></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219939310-0df400e7-4b7c-4343-9548-2eb9c25b07bc.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>function of view_task<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219939341-21a60ed1-7185-4bc8-b958-046bc7abf5a9.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>index out of bound message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219939353-b90c5488-d1cb-4585-b9be-ff48b7b08e45.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>output for view_task function for the given index<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219939341-21a60ed1-7185-4bc8-b958-046bc7abf5a9.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>index out of bound message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219939464-e50c5847-1816-4928-81ea-137e10e487b1.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>list of all tasks<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219939629-9a2e1f4e-25f1-46bd-a682-2f039b6b9211.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>delete task fucntion<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219939655-62132bf6-734d-4d25-8be2-79d7e6872838.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>task was deleted successfully message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219939654-5779738c-be4f-43a8-a2fe-a2ed83498c1f.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>index out of bound message for invalid task number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <div><b>Sub-task 1 and sub-task 2:&nbsp;</b></div>1.&nbsp;<span style="font-size: 13px;">delete/remove task from list by index</span><div><b>Solution:&nbsp; T</b>o<br>remove a particular task I am using remove() method - The remove() method<br>takes a single element as an argument and removes it from the list.<br>I am passing the index to the remove() method&nbsp;<br><div><span style="font-size: 13px;">2.&nbsp;&nbsp;</span><span style="font-size: 13px;">message<br>should show if it was successful or not</span></div><div><b>Solution:&nbsp;</b>I am printing a success message<br>if the task is deleted successfully by the remove() method<span style="font-size: 13px;"><br></span></div><div><span style="font-size:<br>13px;">3.&nbsp;consider index out of bounds scenarios and include appropriate message(s) for invalid index</span></div><div><b>Solution:&nbsp;</b>I<br>am checking the index out of bound scenarios in the usual way(like previous<br>functions)<br></div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219940425-b3dad649-e2fb-4824-a198-ef8274f886dc.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>get_incomplete_task function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219940524-e8701dd2-6ae9-4e41-9f16-a2557db53c6e.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>no tasks found message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219940525-2fda72a1-711a-4005-88eb-967eac1535e0.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>viewing all the incomplete tasks<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <div><b>Sub-task 1 and sub-task 2:&nbsp;</b><br></div>1.&nbsp; &nbsp;<span style="font-size: 13px;">generate a list of tasks where<br>the task is not done and&nbsp;</span><span style="font-size: 13px;">pass that list into list_tasks()</span><div><b style="font-size:<br>13px;">Solution:&nbsp;</b><span style="font-size: 13px;">I am calling the load() function for loading the data in<br>to our task.&nbsp;&nbsp;later in the for loop we can checking a condition if<br>any task doesnot have task['done'] = true then we are appending those tasking<br>to the empty list&nbsp;&nbsp;which is __task = [] which was pre declared in<br>the template&nbsp;that list is being passed to the list_task functions where the print<br>statement is called for this.&nbsp;</span><span style="font-size: 13px;">I am passing print_flag = False to<br>load() function because I am using it as a condition to not print<br>the data which is being print in the load() function.</span><div><br></div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219940790-afffaec6-7265-477e-9bbe-459aaf7c75bd.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>get_overdue_tasks function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219940800-1bc76093-4a85-4032-bc01-baa5b5cbb390.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>no overdue tasks message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219940805-5f8f227f-5b87-49ec-bd27-8bfc88947768.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing the list of over due tasks.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <p><b>Solution:</b>&nbsp;&nbsp;I am using datetime class from datetime module for comparing with the due<br>time to checking if the task is overdue or not.&nbsp;I am calling the<br>load() function for loading the data in to our task. Later in the<br>for loop we can checking a condition if task[done] == false and the<br>due time is lesser the now, if this condition passes&nbsp;then I am appending<br>those tasks which satify the if condition to empty list of _tasksnow I<br>have the overdue data in my list _tasks, which I am passing to<br>list_tasks. list_tasks function has a print statement which is printing the result for<br>this function.&nbsp;I am passing print_flag = Flase to load() function because I am<br>using it as a condition to not print the data which is being<br>print in the load() function<div><br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219941069-5bcb7ad5-3d56-48fa-a33e-9ea47ce17a61.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>get_time_remaining() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219941111-45e90051-3b4f-47f1-b332-8afb6bb64f30.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>task already completed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219941130-cc8a160f-eabc-4b12-a06e-2377a4bbbf54.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing overdue time <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219941139-94982caf-581b-4096-a1ef-d72196d4218f.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>output of time remaining<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <p><b>Summary </b>: To start with I am checking the index out of bound<br>scenarios in the usual way(like previous functions). I am using datetime class from<br>datetime module to get the current time so that I can use it<br>my if else condition to get the remaining time for this functions I<br>have 3 major condition if, if else and else. In the if condition<br>I am checking two conditions. 1. done is equal to false for the<br>given index and 2. the due date of the task for the given<br>index is lesser than or equal to the current time. if this condition<br>passes then I am returning a print statement in which I am stating<br>the remaining time by subtracting the due date and time with the current<br>date and time and showing it to the user. In the if else<br>condition I am again checking 2 conditions 1. done is equal to false<br>for the given index and 2. the due date of the task for<br>the given index is greater than the current time. if this condition passes<br>the I am printing the overdue time by subtracting the current date and<br>time by the due date and time if both the if and if<br>else conditions fails then the else will get executed, which is the task<br>is already completed.<div><br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219941423-960c432c-918c-440e-8c72-a270472e7816.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>output of add function working<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219941424-629c9d5a-b8fa-48a4-bfcb-9b14b1cebda5.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>output of delete function working<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219941425-703ae5a5-3326-4eeb-8b41-678b34879215.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>output of done function working<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219941426-d850094f-5c00-4bfd-aebf-2efc1aaf5248.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>out of list function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219941427-647da120-165e-41a7-a0ed-ef135d733d20.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>output of overdue function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219941553-c726e485-1684-4054-b402-ebebe3c9dc5e.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Json file in the beginning <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219941555-71ee360a-90ca-4dd7-903c-0dd4194b0c2c.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>json file after add function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219941556-8f1f0f8c-b072-4ff7-896c-b4b8292af768.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>json file after delete function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/219941558-8244cb3d-d6b3-49d2-86b4-b1e24e38520e.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>json file after done function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <p>No issues. I knew everything. I was a little slow in the beginning<br>because I was still trying to understand the code, once I finished codding<br>3-4 function I was fully aware of what I was doing.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-1-tracker-app/grade/gi36" target="_blank">Grading</a></td></tr></table>