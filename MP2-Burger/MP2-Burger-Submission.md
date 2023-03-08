<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Burgers</td></tr>
<tr><td> <em>Student: </em> Gagan Indukala Krishna Murthy (gi36)</td></tr>
<tr><td> <em>Generated: </em> 3/7/2023 9:27:23 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-2-burgers/grade/gi36" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb">https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder BurgerMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/223074572-a5f33bd8-13d6-4231-acc8-f1c68592842b.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Calculate_cost function()<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/223074957-abf0a561-74b2-4dcd-963e-96edc9452349.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Calculate_cost function() call <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p>Summary :&nbsp;<div>- Keeping cost initially as zero&nbsp;<div>- adding the input item cost from<br>the user in a loop for every input of items(adding this to the<br>initially maintained cost)</div></div><div>- in the end returning the final cost and round it<br>to 2 decimal numbers so that it can be used as currency.&nbsp;</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/223077012-c67e2a32-3422-406a-b208-afc5c46bfd4b.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>NeedsCleaningException <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/223077008-04074eba-8462-42ad-a968-ea6e787ed77e.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>clean machine function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/223077014-f822faa8-b96f-481d-9e97-30410aea18c7.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>condition for NeedsCleaningException <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/223077568-6b796249-c9ac-4a6d-b035-ea87facc3401.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>OutOfStockException <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/223077570-e7eb1ce6-10ec-4bef-adcb-05307939168b.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>condition for out of stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/223078199-c58899da-f8f9-449f-8bc1-16f6c55e552a.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>condition for invalid choice<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/223078198-63e81660-99f5-4cf1-bc44-943c8c09a917.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>InvalidChoiceException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/223078680-85e22dcd-0179-497b-aceb-103b80ba140d.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>condition for ExceededRemainingChoicesExceptions <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/223078682-4d613967-e7c7-47e9-8429-4c0f1f19e188.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>ExceededRemainingChoicesException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/223079264-cf95994e-39e8-4c21-8b1a-5e6872d42234.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>condition for invalid payment<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/223079266-9d957855-5126-4a47-aa50-011f024cefa5.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>InvalidPaymentException handling<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 13px;"><b>Summary:</b></span><div><span style="font-size: 13px;"><b>OutOfStockException: </b>In our use function we are checking for<br>a condition if our quantity is less than zero, if this condition is<br>true then we will raise the&nbsp;</span><b style="font-size: 13px;">OutOfStockException </b><span style="font-size: 13px;">exception and we<br>are calling&nbsp;</span><b style="font-size: 13px;">OutOfStockException </b><span style="font-size: 13px;">in our main function and printing &quot;The<br>selected option is out of stock. Please select another option&quot;</span></div><div><span style="font-size: 13px;"><br></span></div><div><b style="font-size:<br>13px;">NeedsCleaningException:&nbsp;</b><span style="font-size: 13px;">In our pick_patty&nbsp;function we are checking for a condition if our<br>remaining_uses is less than equal to zero, if this condition is true then<br>we will raise the&nbsp;</span><b style="font-size: 13px;">NeedsCleaningException&nbsp;</b><span style="font-size: 13px;">exception and we are calling&nbsp;</span><b style="font-size:<br>13px;">NeedsCleaningException</b><span style="font-size: 13px;">in our main function and printing &quot;Sorry, The machine needs cleaning!<br>Please type &#39;clean&#39; to clean the machine&quot; and we will ask the user<br>to type clean if the user enters clean then we will reset the&nbsp;remaining_uses<br>to default&nbsp;and continue with our regular burger making.</span></div><div><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;"><b>&nbsp;InvalidChoiceException: </b>In<br>our&nbsp;pick_bun,&nbsp;pick_pattym,&nbsp;pick_toppings functions we can checking for a condition where the existing bun name,<br>patty name and toppings name should match the input from the user, if<br>the condition fails then we will raise the&nbsp;</span><b style="font-size: 13px;">InvalidChoiceException </b><span style="font-size: 13px;">excepition<br>and will call the&nbsp;</span><b style="font-size: 13px;">InvalidChoiceException </b><span style="font-size: 13px;">in our main function and<br>print &quot;You&#39;ve entered an invalid choice. Please choose from the given options&quot; and<br>rerun the same stage again.</span></div><div><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;"><b>ExceededRemainingChoicesException:&nbsp; </b>In the initial state<br>we have set the&nbsp;remaining_patties and&nbsp;remaining_toppings as 3. So whenever the user selects a<br>patty and topping for the same burger then&nbsp;</span><span style="font-size: 13px;">remaining_patties</span><span style="font-size: 13px;">&nbsp; and&nbsp;</span>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;remaining_toppings</span><span style="font-size: 13px;">&nbsp; will decrease by 1. When&nbsp;</span><span style="font-size: 13px;">remaining_patties</span><span style="font-size: 13px;">&nbsp;<br>and&nbsp;</span><span style="font-size: 13px;">remaining_toppings</span><span style="font-size: 13px;">&nbsp; becomes less than or equal to 0 then<br>we are raising the&nbsp;</span><b style="font-size: 13px;">ExceededRemainingChoicesException </b><span style="font-size: 13px;">exception and&nbsp;</span><b style="font-size: 13px;">ExceededRemainingChoicesException</b><span style="font-size:<br>13px;">&nbsp;is called in our main function twice. once while the user is selecting<br>the patty and the second time while user is selecting the toppings and<br>it prints &quot;Sorry! You&#39;ve exceeded the maximum number of pattys that you can<br>select, please choose a topping&quot; and &quot;&nbsp;Sorry! You&#39;ve exceeded the maximum number of<br>toppings; proceeding to the payment portal&quot; respectively and moves to the next stage.</span></div><div>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;&nbsp;</span></div><div><span style="font-size: 13px;"><b>InvalidPaymentException: </b>In our function&nbsp;handle_pay we are checking the the total<br>price of the burger is equal to the price entered by&nbsp; the user.<br>If this condition is false then we are raising the exception&nbsp;</span><b style="font-size: 13px;">InvalidPaymentException<br></b><span style="font-size: 13px;">and it is called in our main function and prints the<br>message &quot;You&#39;ve entered a wrong amount. Please try again :&quot; and asks the<br>user to reenter the amount.&nbsp;<br></span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/223591439-35647638-3cb3-478f-80ef-05473b9e0813.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>all 8 test casses passed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/223591490-54c1319f-2ee2-47ad-8e3c-46e295312d2f.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 1 - bun must be the first selection<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/223591580-862260b5-46e2-45b7-91c2-935f178fbd55.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 2 - can only add patties if they&#39;re in stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/223591582-82a2a57b-50b8-4a7c-a1cc-fd990028bc61.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>Test 3 - can only add toppings if they&#39;re in stock&lt;br&gt;
</code></pre>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/223591677-beaed053-a2dd-4366-b57f-54896661403f.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 4 - Can add up to 3 patties of any combination<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/223591678-3325b0c8-174c-4f66-970c-8ec39ec56059.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p> Can add up to 3 toppings of any combination<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/223591790-5d48285f-3595-45cd-856d-20ac4c7cf60c.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 6 - cost must be calculated properly based on the choices<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/223591792-dae8f626-090a-4eb4-8870-1408c2bd3bc5.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 7 - Total Sales<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/223591791-e6f8b6cd-7082-4e30-a918-315e9a5a4e73.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 8 - Total burgers should properly increment for each purchase<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 13px;"><b>Test 1 - bun must be the first selection -&nbsp;</b>The order<br>of the selection has to be correct&nbsp;</span><span style="font-size: 13px;">and the exception is raised<br>if the order is not correct. For the order to be correct the<br>bun has to be correct. In the above screen short we are testing<br>by giving a invalid order.&nbsp;</span><div><span style="font-size: 13px;"><b><br></b></span></div><div><span style="font-weight: bold; font-size: 13px;">Test 2 -<br>can only add patties if they&#39;re in stock&nbsp;</span><span style="font-size: 13px;"><b>- </b>This test case<br>checks if the patties are in stock<b>&nbsp;</b>and also checks if the exception is<br>raised when the out of stock patty is chosen&nbsp;by the user.</span><b><span style="font-size: 13px;"><br></span></b></div><div>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;<b><br></b></span></div><div><b><span style="font-size: 13px;">Test 3 - can only add toppings if they&#39;re in<br>stock&nbsp;</span><span style="font-size: 13px;">-&nbsp;</span></b><span style="font-size: 13px;">This test case checks if the toppings are in<br>stock</span><b style="font-size: 13px;">&nbsp;</b><span style="font-size: 13px;">and also checks if the exception is raised when<br>the out of stock&nbsp;</span><span style="font-size: 13px;">toppings</span><span style="font-size: 13px;">&nbsp;is&nbsp;</span><span style="font-size: 13px;">chosen</span><span style="font-size: 13px;">&nbsp;by the<br>user.</span><b><span style="font-size: 13px;"><br></span></b></div><div><span style="font-size: 13px;"><b><br></b></span></div><div><span style="font-weight: bold; font-size: 13px;">Test 4 - Can add<br>up to 3 patties of any combination&nbsp;</span><span style="font-weight: bold; font-size: 13px;">-&nbsp;&nbsp;</span><span style="font-size: 13px;">&nbsp;</span>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;This test case checks if the user has not added more than<br>3 patties</span><span style="font-size: 13px;">&nbsp;</span><span style="font-size: 13px;">and</span><span style="font-size: 13px;">&nbsp;checks if the exception is raised<br>when the user chooses more the 3 patties.</span><span style="font-weight: bold; font-size: 13px;"><br></span></div><div><span style="font-size:<br>13px;"><b><br></b></span></div><div><b><span style="font-size: 13px;">Test 5 - Can add up to 3 toppings of any<br>combination&nbsp;</span><span style="font-size: 13px;">-&nbsp;</span></b><span style="font-size: 13px;">This test case checks if the user has not<br>added more than 3 toppings and&nbsp;</span><span style="font-size: 13px;">checks if the exception is raised<br>when the user chooses more the 3 toppings.</span></div><div><span style="font-size: 13px;"><b><br></b></span></div><div><b style="font-size: 13px;">Test 6<br>- cost must be calculated properly based on the choices -&nbsp;</b><span style="font-size: 13px;">&nbsp;This<br>functions checks if the total cost returned&nbsp;by the calculate_cost is correct. It is<br>checking for all scenarios like bun, patties and flavor&nbsp;using random module.&nbsp;</span></div><div><span style="font-size: 13px;"><b><br></b></span></div><div><b>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;Test 7 - Total Sales (sum of costs) must be calculated properly&nbsp;</span>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;- T</span></b><span style="font-size: 13px;">his functions test for total_sales. It checks </span><span style="font-size:<br>13px;">if the total_sales is calculated properly,&nbsp;</span><span style="font-size: 13px;">we are doing this test case<br>using fixtures.</span></div><div><span style="font-size: 13px;"><b>&nbsp;</b></span></div><div><span style="font-weight: bold; font-size: 13px;">Test 8 - Total burgers should<br>properly increment for each purchase&nbsp;</span><span style="font-size: 13px;"><b>-</b>&nbsp;T</span><span style="font-size: 13px;">his function is for total_burgers&nbsp;</span>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;to check if the total_burgers&nbsp; is increased properly&nbsp;</span><span style="font-size: 13px;">we are testing<br>this function using fixtures.</span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td>Not provided</td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>No issues and difficulties.<br>I knew everything before I started the assignment.&nbsp;<br><div>I got to<br>strengthen my usage of fixtures for testing.&nbsp;</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/223081708-46580901-1822-4b1e-84ea-579bbbd2aae5.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>output 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/223081709-ebc190d3-ca7e-4bcf-9035-6bf85d18b8ed.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>output 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/223081711-33d1a8bc-a86c-44c3-ace8-a98208b6c05d.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>output 3<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-2-burgers/grade/gi36" target="_blank">Grading</a></td></tr></table>