<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Gagan Indukala Krishna Murthy (gi36)</td></tr>
<tr><td> <em>Generated: </em> 2/27/2023 9:58:42 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/m4-simple-calc/grade/gi36" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sum-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221131485-707f371f-2b10-48d2-acbe-d1c29cce912c.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Float Validation - for string of number<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221131488-ff0ea849-1218-4297-bfe7-c366a6a702b5.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p> Int Validation - for string of number<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221131487-f1596c49-0465-4ef1-87b5-c314c2050d2d.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p> Float and int conversion from string<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221132382-78daf8fb-32a3-4fbb-8426-745d108aaa31.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221742023-d5e2878c-d6af-4a6d-a39a-4364962c225b.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>while loop - In which it is checking the operations and splitting the<br>string and sending the to the main functions<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221132395-e9aa0474-9a5b-4c95-93b9-3561a7de3abc.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>sub function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221742023-d5e2878c-d6af-4a6d-a39a-4364962c225b.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>while loop - In which it is checking the operations and splitting the<br>string and sending the to the main functions<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221132389-d042e991-3e96-4d24-9884-1e945a02101e.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>mult function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221742023-d5e2878c-d6af-4a6d-a39a-4364962c225b.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>while loop - In which it is checking the operations and splitting the<br>string and sending the to the main functions<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221132386-edeab567-27df-4ca9-b145-4d1c35ee9a00.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>div function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221742023-d5e2878c-d6af-4a6d-a39a-4364962c225b.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>while loop - In which it is checking the operations and splitting the<br>string and sending the to the main functions<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221741043-4b018003-227a-488e-a162-efcb010dac63.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>number add number test case <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221741357-fde1012c-63f4-4784-8c5b-afdf2dcad720.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221741357-fde1012c-63f4-4784-8c5b-afdf2dcad720.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases passed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221741036-705df8f9-de90-4425-93a7-636c8d80ed7d.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans add number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221741357-fde1012c-63f4-4784-8c5b-afdf2dcad720.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases passed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221741046-866fc26d-c38d-4dfb-9a70-3f49a204a42f.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>number-sub-number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221741357-fde1012c-63f4-4784-8c5b-afdf2dcad720.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases passed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221741042-fc0223c8-dd44-4d09-b68d-b0034091c3bc.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p> ans-sub-number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221741045-5d574f44-13a3-461c-b87f-18ae8f91f126.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p> number-mult-number<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221741357-fde1012c-63f4-4784-8c5b-afdf2dcad720.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221741040-fec64f20-1643-4884-8284-9aba1dd7c926.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p> ans-multi-numbe<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221741357-fde1012c-63f4-4784-8c5b-afdf2dcad720.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221741357-fde1012c-63f4-4784-8c5b-afdf2dcad720.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases passed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221741044-7d38e528-226b-4fbf-b2a1-fec550927b6b.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>number-div-number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221741357-fde1012c-63f4-4784-8c5b-afdf2dcad720.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases passed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/221741039-40b73afd-7e71-4349-abce-ba921f275985.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans-div-number<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <div>I knew most of the things from this assignment apart from few things<br>in Pytest and fixtures.<br><br></div><div>Pytest is a Python testing framework that provides a powerful<br>and flexible platform for writing and executing tests. It supports a wide range<br>of testing scenarios, from simple unit tests to complex integration and end-to-end tests.<br>Fixtures are a key feature of Pytest, allowing developers to define and manage<br>the set-up and<span style="letter-spacing: 0.09996px;">&nbsp;Discuss how test cases work and anything new you<br>learned about them while doing this assignment</span>&nbsp;tear-down of test environments. Fixtures provide a<br>way to define reusable code that can be shared across tests, reducing duplication<br>and improving maintainability.</div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <div><font color="#d1d5db" face="Söhne, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans,<br>sans-serif, Helvetica Neue, Arial, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol,<br>Noto Color Emoji"><span style="font-size: 16px; white-space: pre-wrap;">Test cases provide a way to verify<br>that the software is working as intended and meets the specified requirements. In<br>the context of Pytest, test cases are defined as functions that use assertions<br>to verify the behavior of the code being tested.</span></font></div><div><font color="#d1d5db" face="Söhne, ui-sans-serif, system-ui,<br>-apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, sans-serif, Helvetica Neue, Arial, Apple<br>Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji"><span style="font-size: 16px;<br>white-space: pre-wrap;"><br></span></font></div><div><font color="#d1d5db" face="Söhne, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto<br>Sans, sans-serif, Helvetica Neue, Arial, Apple Color Emoji, Segoe UI Emoji, Segoe UI<br>Symbol, Noto Color Emoji"><span style="font-size: 16px; white-space: pre-wrap;">Pytest makes it easy to define<br>and organize test cases, with a simple syntax and flexible framework that allows<br>tests to be written in a clear and concise way. Pytest also supports<br>a wide range of testing scenarios, from simple unit tests to more complex<br>integration and end-to-end tests. </span></font><font color="#d1d5db" face="Söhne, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto,<br>Ubuntu, Cantarell, Noto Sans, sans-serif, Helvetica Neue, Arial, Apple Color Emoji, Segoe UI<br>Emoji, Segoe UI Symbol, Noto Color Emoji"><span style="font-size: 16px; white-space: pre-wrap;">During this assignment,<br>I learnt some new techniques for organizing and structuring test cases in Pytest.<br>For example, I learned about the use of fixtures to manage the setup<br>and tear-down of test environments, which can help to reduce duplication and improve<br>the maintainability of test cases. </span></font><span style="background-color: ; color: rgb(209, 213, 219); font-family:<br>Söhne, ui-sans-serif, system-ui, -apple-system, &quot;Segoe UI&quot;, Roboto, Ubuntu, Cantarell, &quot;Noto Sans&quot;, sans-serif, &quot;Helvetica<br>Neue&quot;, Arial, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;, &quot;Noto Color<br>Emoji&quot;; font-size: 16px; white-space: pre-wrap;">I also learned about the use of parametrized tests,<br>which allow multiple inputs to be tested using a single test case. This<br>can be a useful technique for testing functions or methods that have multiple<br>possible inputs, and can help to reduce the amount of code needed to<br>write and maintain tests.</span></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/m4-simple-calc/grade/gi36" target="_blank">Grading</a></td></tr></table>