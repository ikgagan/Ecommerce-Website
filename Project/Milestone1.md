<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Gagan Indukala Krishna Murthy (gi36)</td></tr>
<tr><td> <em>Generated: </em> 4/14/2023 4:39:31 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone1-deliverable/grade/gi36" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231957324-4fa63564-905a-43a1-be63-35f7b3f97fe0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid email validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231957326-617543bb-1de3-43cd-ba5d-0de8ebb12d1e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>password does not match validaiton<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231957321-6a822675-b2c4-4426-9af1-2e8ed22ce018.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>username not available validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231957329-36f79006-d1a1-4465-ab73-56590670aba2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>password validaion<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231957331-d0763ba6-451a-455d-95e8-68f2e29148c5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passwords not much validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231958373-9d3c9578-aca4-4145-9dbd-4fb0834275a5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email not available validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231958558-658cdbc2-0264-4322-bab3-01d848585f58.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the form with valid data filled in after the form is submitted<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231958789-6e3cad4d-e1e5-425c-adbf-3482222775d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the form with valid data filled in before the form is submitted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231959809-5e52c70f-ca72-4762-a878-3f1878b28ee9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The valid user data from Task 1 -  Clearly highlighting which row<br>it is.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ikgagan/IS601/pull/39">https://github.com/ikgagan/IS601/pull/39</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>1. WTforms are utilized to gather input data through forms, and the form<br>is checked for validity upon submission.</div><div>2. Validators are pre-built into WTforms, which display<br>error messages on the front-end before sending a request to the back-end. The<br>back-end handles unique username and email validations by processing the error messages from<br>the database, which has constraints on username and email fields.</div><div>3. A password validator<br>is employed, and prior to being stored in the database, it is encrypted<br>using bcrypt. Bcrypt appends a salt value to the password and stores the<br>hash of this salt+password in the database.</div><div>4. The database is used to hold<br>the users' information, and constraints are added to the database tables. The database<br>helper is utilized to query the database, and the response is presented on<br>the front-end.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231960592-d0472e15-4b32-406d-9f3c-df6686546c9b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>password mismatch validation <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231960594-473ee9cc-c639-4bfd-b8dd-d056c608bbd7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> validation based on non-existing user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231960595-4a16bb0c-79ab-42ae-9ae7-182684e4b672.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>successful login flash message on landing page. <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ikgagan/IS601/pull/39">https://github.com/ikgagan/IS601/pull/39</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>1.WTforms are utilized to collect user input through forms and validate the form<br>upon submission.</div><div>2. Built-in validators in WTforms display error messages on the front-end before<br>sending a request to the backend. The backend processes the error message from<br>the database to ensure unique usernames and emails, which are constrained in the<br>database.</div><div>3. The password has a validator, and before it is stored in the<br>database, it undergoes encryption with bcrypt. Bcrypt adds a salt value to the<br>password, and the resulting hash of the salt+password is saved in the database.</div><div>4.<br>The database is employed to store user information, with constraints included in the<br>tables. The database helper is used to make queries to the database, and<br>the response is returned to the front-end.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231961425-fbda73e0-a01f-46ec-9286-b2b7b1df8c18.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>logout flash message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231961427-b860757e-d267-40d3-8ef4-4b80cec1fd97.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>message showing user cant enter a login protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ikgagan/IS601/pull/39">https://github.com/ikgagan/IS601/pull/39</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>Flask&#39;s built-in methods are used to maintain sessions, with flask_login used by Flask<br>to keep track of the current session. The current_user object stores information about<br>the currently logged-in user, which is used across different web pages to keep<br>the user logged in. User ID and user roles are retrieved and kept<br>consistent across pages to ensure proper session management.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231961427-b860757e-d267-40d3-8ef4-4b80cec1fd97.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>message showing user cant enter a login protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231962138-857baadc-040f-4541-bdd4-06f849595c5c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>message showing user cant enter a role protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231962415-5271c37f-ec7c-4e67-9297-d83ebecbbb2c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Roles table with valid data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231962421-beeae6cd-df3d-4406-83d1-6ecfe456f73c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>UserRoles table with valid data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ikgagan/IS601/pull/39">https://github.com/ikgagan/IS601/pull/39</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>To secure pages that require login, we utilize the built-in decorator known as<br>login_required. This verifies whether the user has been authenticated or not.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>To protect pages based on user roles, we retrieve the roles associated with<br>the user&#39;s session and verify if they match the required roles. Flask&#39;s built-in<br>permission requirement decorator is used to perform this check.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231960595-4a16bb0c-79ab-42ae-9ae7-182684e4b672.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>login pagestyled <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231966425-be2ab307-0fa0-4a57-8a9b-4e89eba01720.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>assign role page styled- proper table - proper checkbox<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ikgagan/IS601/pull/39">https://github.com/ikgagan/IS601/pull/39</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>changed nav bar styles - made it dark<br>changed the landing page for -<br>admin(gagan) - added a profile photo<br>changed the tables - added proper table borders<br>and stripes&nbsp;<br><br>everything looks pretty now<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231961425-fbda73e0-a01f-46ec-9286-b2b7b1df8c18.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>logged out message properly displayed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231960595-4a16bb0c-79ab-42ae-9ae7-182684e4b672.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>logged in message properly displayed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231960594-473ee9cc-c639-4bfd-b8dd-d056c608bbd7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid use error message displayed in a friendly manner <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231957331-d0763ba6-451a-455d-95e8-68f2e29148c5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>minimum password length required message properly shown<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ikgagan/IS601/pull/39">https://github.com/ikgagan/IS601/pull/39</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>for logout we are removing the user from the current session and<br>redirecting them to the login page with displaying a flash message with log<br>out success&nbsp;<div>2. for login once the user enters the username/email and password we<br>are validation it with the database if the match then we will redirect<br>them to the landing page and displaying them a flash message with login<br>sucess</div><div>3. for invalid username we are matching the username entered by the user<br>with the database if it doesnot match then we will throw a error<br>flash message displaying invalid username</div><div>4. for password minimum length we are using WTForms<br>validators length method - the minimum length is 8. if the input characters<br>is not 8 then the form displays a friendly message asking to input<br>minimum 8 characters.&nbsp;</div><div><br></div><br></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231968190-4c6cea84-7c01-44ec-a487-283cf495b766.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Users is be able to see their profile - email and username is<br>prefilled properly<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ikgagan/IS601/pull/39">https://github.com/ikgagan/IS601/pull/39</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>at the beginning of the session the formdata is fetched from the database<br>and it is displayed to the email and username forms for the particular<br>user.&nbsp;<br><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231970676-997fce83-6e15-4211-ab9c-81a2d589d8d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>username validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231970679-01a141b7-e891-4eee-9959-0574d7711263.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email already in use message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231970680-4161ec99-77d3-4c3f-a196-3803a4500a19.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231980893-4edebfa9-3444-4acc-90b4-c763c963d64c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid -  user validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/231986436-f87e2984-8df3-4b3c-9fbf-ab8c72f4c4d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid password validation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ikgagan/IS601/pull/39">https://github.com/ikgagan/IS601/pull/39</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p>for username validation we are checking with the database- if the same name<br>matches we are throwing an error and we are even doing WTForms validation<br>for checking the minimum length 2<div>for email validation we are doing the same<br>as the username and we are even doing WTForms validation to check for<br>the email format.</div><div>for current password we are doing the same like username and<br>email.<br>for new password and confirm we are using WTForms to check if they<br>are matching with each other and we are also making sure the length<br>is 8 for the new password.&nbsp;</div><div><br></div><div><br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p><span style="letter-spacing: 0.09996px;"><b>No issues<br><br>Learnings</b> - learnt about auth process - profile management -<br>user sessions - role managements(ie admin)<br><b>Resources </b>- Class modules and videos from the<br>professor.&nbsp;<br><br><br><b>Login Credentials</b>&nbsp;<br>Username: gagan<br>password: 123123123</span><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-gi36-prod.herokuapp.com/login">https://is601-gi36-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone1-deliverable/grade/gi36" target="_blank">Grading</a></td></tr></table>