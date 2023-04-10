<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Gagan Indukala Krishna Murthy (gi36)</td></tr>
<tr><td> <em>Generated: </em> 4/10/2023 5:17:56 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-3-business-management/grade/gi36" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230871290-7c772080-8a45-4e22-880f-5dcc387e02d3.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Index Page - Home Page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230871288-73e23fdd-0e59-479b-8f72-4789f26b26c8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>employee add<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230871286-88c8890f-3710-4308-8c2d-9d9ec9b36ef3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>employee search/list<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230871279-083a7e4a-f713-43de-a0f5-f752d157adc7.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>company search/list<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230871278-383fa682-54ab-407e-90f9-35df4fe19577.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>company add <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230871277-c8b895ca-c705-4ea4-97dc-883cfa7b5d48.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>admin - import<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230871285-21d49767-d045-4a56-b835-bf997efc2caa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>database employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230871283-c0d0defd-dc57-49e2-931a-481e2b9ce5d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>database company<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230873943-cf54bb86-5e55-415a-bc86-5fdd803fd3af.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code to check if the file is a .csv file otherwise reject with<br>a flash<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230873944-704a4c83-6a08-4f6b-81cc-df176bb1072a.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code to return proper flash message for success and failure of uploading data<br>- It also displays how many records were added - it also gives<br>a flash message if the list was empty or if no added was<br>inserted. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230874996-edccf5c3-2877-4357-aa7a-a7bd12dc9fd1.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>CSV file is being read from the provided stream as a dict and<br>appending them<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230873938-e55db7ad-8582-42a2-ab36-db02cbd423fd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>no file selected<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230873942-eaae5f10-6513-4d9b-9ba1-c935ec257c5f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>file format not csv error message <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230873945-e2479896-5a65-4a04-8ddc-068fa1fe16d8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success message  and number of data uploaded<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230871283-c0d0defd-dc57-49e2-931a-481e2b9ce5d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after company data was uploaded<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230871285-21d49767-d045-4a56-b835-bf997efc2caa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after employee data uploaded <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230875997-6f8269ba-3abd-4862-a9ce-3f52a5f30872.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for retrieving first_name, last_name, company , email - flash messages added for<br>missing first_name last_name email  - added INSERT query - Except block have<br>a user-friendly<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230875995-c1964d92-a754-4158-8edb-a5c614c853b1.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>type = email - this is the validation for email.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230876985-47faf070-75f6-4ed3-86c4-ab908733bdb7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230876990-7bae28d0-1ca6-4dd1-8e98-807b5ae8934a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230876988-c6be77cc-55c7-4cae-9e7e-b9e7aaf9f578.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing first_name error message - the flash messages are not being shown because<br>it has 2 layer validation - 1st layer is html tag validation -<br>the submission is not getting a POST request that is the reason the<br>flash message are not displayed - please dont reduce marks for this :)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230876989-da5ecbb2-9de3-4b70-a6ae-2d7806be6420.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing last_name error message - the flash messages are not being shown because<br>it has 2 layer validation - 1st layer is html tag validation -<br>the submission is not getting a POST request that is the reason the<br>flash message are not displayed - please dont reduce marks for this :)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230876987-96fa081e-059e-45d5-bd6a-ec3dafbfdf82.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing email error message - the flash messages are not being shown because<br>it has 2 layer validation - 1st layer is html tag validation -<br>the submission is not getting a POST request that is the reason the<br>flash message are not displayed - please dont reduce marks for this :)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230877684-4f0cfb0c-da0d-4668-9b02-9126b0a34543.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>error message for proper email validation <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230878022-1d887975-0078-4504-aa1a-543c570573d9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>valid employee data shown previously - search for WHERE  first_name = &quot;Testing11&quot;<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230879771-633fb8fd-83e3-4f6f-85f1-0e0976164b28.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>SELECT query to pull employ id, first_name, last_name, email, company_id, company_name via a<br>LEFT JOIN<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230880405-25b690b1-de6b-4c3d-be32-b24452d5774d.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>request args for fn, ln, email, company, column, order, limit - appending like<br>filter for first_name if provided -  appending like filter for last_name if<br>provided -  appending like filter for email if provided - appending equality<br>filter for company_id if provided - appending sorting if column and order are<br>provided and within the allowed columns and order options (asc, desc) allowed_columns =<br>[&quot;first_name&quot;, &quot;last_name&quot;, &quot;email&quot;, &quot;company_name&quot;] - appending limit (default 10) or limit greater than<br>or equal to 1 and less than or equal to 100- 	provided a<br>proper error message if limit isn&#39;t a number or if it&#39;s out of<br>bounds - Except block has a user friendly message flashed and a print()<br>of the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230880790-51559b40-30e4-4d7e-aa53-4edd2f18cd7d.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>Showing  results with first_name filter applied&lt;br&gt;
</code></pre>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230880791-449db415-6664-4527-b629-e054c77a4b0c.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>Showing  results with last_name filter applied&lt;br&gt;
</code></pre>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230880792-ec0ed6cf-35f8-4db0-a558-d2cbf3dc87cb.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>Showing  results with email filter applied&lt;br&gt;
</code></pre>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230880793-3f9f461e-8a90-4c4d-8d29-b78320266269.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>Showing  results with company filter applied&lt;br&gt;
</code></pre>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230880793-3f9f461e-8a90-4c4d-8d29-b78320266269.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>Showing one asc filter applied - first name is being used for filter&lt;br&gt;&lt;br&gt;
</code></pre>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230880796-c24f3d4a-a61e-4a13-aa44-15e736c8b04a.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>Showing one desc filter applied - first name is being used for filter&lt;br&gt;&lt;br&gt;
</code></pre>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230883896-6aed527f-b3b4-4df4-819d-fb22417928e1.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>code for - first_name is required (flash proper error message) -  	last_name&lt;br&gt;is required (flash proper error message) - 	company doesn&#39;t require a flash and&lt;br&gt;may be empty/None - 	email is required (flash proper error message) &lt;br&gt;
</code></pre>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230884323-5cc8e98c-fe73-4ad3-a294-c3a986e91a5f.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code should retrieve id (from request args) first_name, last_name, company (id), email from<br>form<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230883897-ca8cae7f-ae5f-407a-849f-1a1f303ac98f.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Missing id should be handled with a flash message and redirected back to<br>employee search.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230883903-0fd7c318-da9f-49a3-81a6-4f71a9930728.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>UPDATE query <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230883894-3468d0b9-86b7-4626-8e23-e545dbebf55d.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>Except blocks (two) should has a user friendly message flashed and a print()&lt;br&gt;of the exception&lt;br&gt;
</code></pre>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230883900-40c7cab7-1e66-48eb-8889-04f6e143bbe2.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>SELECT query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230883899-6bdd4555-e31f-483d-b554-1a74406dfa34.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>render template<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230884912-e794c0b3-f606-4ac4-a78b-1f7e9245099d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230884916-29162412-0753-4644-a665-284a1af7a22c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after edit - proper flash message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230885344-0c21432f-47a3-4b9d-ad41-cb274a43aa6c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>database screenshot before editing for james <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230885345-c6e07fb7-3e9b-4b79-9925-4640f1f9f7ee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>database screenshot after editing - last_name change to ButtEdited from Butt for James<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230888978-506b79d1-98b1-46dd-ba94-8f0b46f75d9a.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>name, address,  city ,state, country , website  and zipcode  is<br>required (flash proper error message if missing)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230888980-255240c9-1187-4363-b114-941a0243d889.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>code is retrieving form data for name, address, city, state, country, zip, website&lt;br&gt;
</code></pre>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230888981-0a571e24-e177-428e-913f-3d830c816579.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p> INSERT query and Except block should has a user-friendly message flashed and<br>a print() of the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230889679-b9df2ee8-90f3-4d4b-8318-6585bd4bb0b4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230889681-f0cdf4ee-9cc8-4c03-a860-e5fdbef57b30.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230889684-e1a0983f-a85f-4d20-a50e-57318deb92e0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230889685-02114d9d-5a0d-410f-b04a-805a8efd1ff1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>address error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230889687-6a7e4f52-57ef-40e1-9d23-e20121c47a7b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>city error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230889689-b6b161ad-7616-4bb0-93b8-d1e1a4a9e964.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>zip error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230889899-97fa6c28-1fca-43de-aafc-e8311e69680f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>country  error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230889900-67c0a916-d6a8-4717-a4ee-f536819195d2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>State error message <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230890394-53ee6e2c-2d56-4e0f-87d6-8ca295b06a62.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>added valid company data shown previously into the database<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230890998-853c71b1-ec1f-4ed9-9a93-86020c115cb9.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>append sorting if column and order are provided and within the allows columsn<br>and allowed order asc,desc allowed_columns = [&quot;name&quot;, &quot;city&quot;, &quot;country&quot;, &quot;state&quot;]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230891075-a97c4488-44c2-4143-93bd-f4f6793b2d5a.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing allowed_sorting to sort_filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230891000-02f4408c-7a1f-4287-bf41-6caeca630ed4.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>request args for name, country, state, column, order, limit - 	append a LIKE<br>filter for name if provided; should have proper wildcards - 	append an equality<br>filter for country if provided - 	append an equality filter for state if<br>provided - append limit (default 10) or limit greater than or equal to<br>1 and less than or equal to 100 - provide a proper error<br>message if limit isn&#39;t a number or if it&#39;s out of bounds<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230890999-6d2a80ad-97c0-4a3c-a32c-49ae083090f2.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>Except block should have a user friendly message flashed and a print() of&lt;br&gt;the exception&lt;br&gt;
</code></pre>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230891615-9e074b02-00d0-441f-a9ae-22f6c9e9e34b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> results with name filter applied; don&#39;t combine filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230891618-1e8a2e3a-9e80-491b-9f10-2550763eec75.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> results with country filter applied; don&#39;t combine filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230891621-5c7c9534-ff33-4724-8a6f-35156c097dfe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with state filter applied; don&#39;t combine filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230891623-51e4b6e0-986e-4787-9819-35bfeea5e432.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>name asc<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230891624-adca42a1-c567-4b46-9dfe-e1610c760202.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>name desc<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230995758-7632d45a-a822-4baf-b873-350316641f17.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code is retrieving id (from request args) name, address, city, state, country, zip,<br>website from form.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230995760-40918a79-ec15-41f1-b5e6-e03841ab36c2.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>name, address, city, state, country  is required validation done<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230995764-f9c269a3-570a-49e7-b525-dc52f36ef023.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>update query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230995753-dd20d821-713c-4287-bed2-688ca127396b.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Except blocks (two) has a user friendly message flashed and a print() of<br>the exception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230995763-2f96acc1-3fd1-451e-97a4-6d9c6407b13c.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>select query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230995762-c37389b4-fcce-4b77-a67e-32a6bb053e70.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>data being passed to render template<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230999048-b48218e4-f9a5-44f9-8143-ff16db0cffed.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>company data before editing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230999050-d8a95068-52a8-414e-9c60-d7ac61eca45b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>company data after editing - success message - company name is edited<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230999620-7bcc8399-1a88-4054-98a3-5a3b9dec846e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>id =13 - database before the id = 13 - company name is<br>changed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230999621-21d696b6-c3d0-402a-8931-fcd90e827f05.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>id =13 - database after the id = 13 - company name is<br>changed - company name changed to &quot;database name change&quot;<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230885811-2a557f45-059e-4a7c-abb4-5cfb39de7a76.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>delete company code - all the above condition are taken care.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230886168-5f5b19d1-0f4e-4e7f-8a88-9ad23445d7ac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before deleting james<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230886171-58e6aa73-e6df-4a1f-9d41-34ff69c8601c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after deleting james<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230885811-2a557f45-059e-4a7c-abb4-5cfb39de7a76.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>delete employee code - all the above condition are taken care.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230886286-de850de6-ba54-445a-b354-b11a8070d624.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before deleting asd company <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230886288-4e24f24b-ab25-4cce-b9ba-f02bec6f3b38.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after deleting asd company <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230886977-0a8cc8c8-8a8f-422a-93ec-594018bec1e7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>running pytest -rA -  test_add_company - test_add_employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230886979-60760486-d730-4bb7-97c6-6a4353f4766d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_edit_company  - test_edit_employee - filter_name - filter_ country - filter_state - sort_<br>asc_name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230886980-672c12f6-01a1-47e0-a3f2-ea32201551f1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>sort desc name - sort asc city - sort desc city - sort<br>asc country - sort desc country<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230886981-0b981b9e-b703-4222-98c9-543e0976bd8d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>sort asc state- sort desc state - test employee count - test filter<br>fn<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230886984-0342dc88-7377-4b23-a81f-85168bf82040.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> test filter ln - test filter email - test filter company <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230886985-ceb691b8-1d03-43c0-ad0d-719ee715cd43.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>sort asc fn - sort desc fn - sort asc ln - sort<br>desc ln - <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230886988-01601db2-4ebf-4ffc-90a2-a00d9a040249.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>sort asc email - sort desc email - sort asc company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230886990-8011840d-2e42-45d2-80b2-fa39bdf9f422.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>sort desc company - test upload csv - showing passed of all test<br>cases<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/230886992-e52537ea-64e7-4738-8f0b-943ec7e3e441.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>all 29 test cases passed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <div><span style="letter-spacing: 0.09996px;"><b>Learnings</b>:</span></div><div><span style="letter-spacing: 0.09996px;">1. learnt more regarding lists (appending), request renders.</span></div><div><span style="letter-spacing:<br>0.09996px;">2. learnt sending multiple inputs for the same function while storing it in<br>a array.</span></div><div><span style="letter-spacing: 0.09996px;">3. few HTML validation through HTML input tags.</span><br></div><div><span style="letter-spacing: 0.09996px;"><br></span></div><div><b>Issues:</b>&nbsp;no<br>issues, everything was easy, but taking the screenshots and uploading to learn platform<br>was difficult and tiring.&nbsp;<br><br><br><span style="letter-spacing: 0.09996px;">Website&nbsp;url:</span></div><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-3-business-management/grade/gi36" target="_blank">Grading</a></td></tr></table>