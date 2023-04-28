<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 Shop Project</td></tr>
<tr><td> <em>Student: </em> Gagan Indukala Krishna Murthy (gi36)</td></tr>
<tr><td> <em>Generated: </em> 4/28/2023 2:40:15 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-3-shop-project/grade/gi36" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Orders will be able to be recorded </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Orders table with valid data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/235056102-de71be3e-d3d1-4791-8c85-b19f98a3bfa6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>a screenshot of the Orders table with valid data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of OrderItems table with validate data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/235056258-039be8ed-affe-4218-b580-ebe68347be62.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>a screenshot of OrderItems table with validate data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the purchase form UI from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/235061257-87f2b615-eeaf-4e9a-9a69-05291ce0d0f3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>a screenshot of the purchase form UI from Heroku<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot showing the items pending purchase from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/235061255-f4f60f76-fe6f-497c-acd1-7ecc57f8820c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>a screenshot showing the items pending purchase from Heroku<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/235061591-1c93100c-9723-4079-aa90-4266854b4580.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart.unit_cost differs from Products.unit_cost<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a screenshot showing the Order Process validations from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/235061943-c5688bcf-f305-4ebc-bb0f-4856c981d1da.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>payment method<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/235062154-51a05f46-e95d-451a-9f62-1ace2b73b68f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Verify stock/price of items - 	Verify address pieces -  code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/235062156-15c2babb-1246-474b-b3cd-e932430eb8db.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Verify stock/price of items - Verify address pieces -  code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a screenshot showing the Order Process validations from the UI (Heroku)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/235061591-1c93100c-9723-4079-aa90-4266854b4580.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Price difference message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/235062455-8e0cceb5-7eec-4415-9d31-44de694af04a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>unavailable stock message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/235062563-e77970c3-9177-45e8-afec-0c003d6954d0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> invalid &quot;Money Received&quot; message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly describe the code flow/process of the purchase process</td></tr>
<tr><td> <em>Response:</em> <div>When the user clicks on the "Place Order" button on the cart page,<br>they will be directed to the "Place Order" page.</div><div>On this page, the details<br>of the user's cart are first verified. If the details are correct and<br>the items are in stock, a form is presented to the user to<br>enter their shipping address and payment details.</div><div>Once the user enters their information, they<br>will be redirected to a payment page to complete the transaction.</div><div>If the payment<br>is successful, the order will be confirmed. In the backend, the stock and<br>price are verified again. If the verification is successful, an entry is made<br>into the orders table. For each item in the order, an entry is<br>made into the orderitems table.</div><div>If there are no issues, those items are removed<br>from the cart table. In addition, the stock of those respective products is<br>updated.</div><div>Finally, the user is presented with a confirmation page displaying the order ID.</div><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ikgagan/IS601/pull/48">https://github.com/ikgagan/IS601/pull/48</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-gi36-prod.herokuapp.com/confirm_order">https://is601-gi36-prod.herokuapp.com/confirm_order</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Order Confirmation Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot showing the order details from the purchase form and the related items that were purchased with a thank you message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/235061257-87f2b615-eeaf-4e9a-9a69-05291ce0d0f3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the order details from the purchase form and the related items that were<br>purchased with a thank you message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how this information is retrieved and displayed from a code logic perspective</td></tr>
<tr><td> <em>Response:</em> <p><font color="#d1d5db" face="Söhne, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans,<br>sans-serif, Helvetica Neue, Arial, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol,<br>Noto Color Emoji"><span style="font-size: 16px; white-space: pre-wrap;">When an order is placed, the user&#39;s<br>address and payment information are stored in the orders table. <br>When the order<br>is confirmed, the system retrieves this information and displays it in a table<br>format.</span></font><br><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ikgagan/IS601/pull/48">https://github.com/ikgagan/IS601/pull/48</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-gi36-prod.herokuapp.com/place_order">https://is601-gi36-prod.herokuapp.com/place_order</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> User will be able to see their Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history for a user</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/235066120-49778758-f520-4743-9389-eeb79e55dde4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>a screenshot showing purchase history for a user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/235071406-64dd984f-3389-4f0c-a896-70535709f698.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>a screenshot showing full details of a purchase (Order Details Page)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details</td></tr>
<tr><td> <em>Response:</em> <div>To view all orders of a user, the system first fetches all orders<br>from the orders table based on the user id.</div><div>Each order in the list<br>contains a "view" button.</div><div>When a user clicks on the "view" button, data is<br>fetched by joining the orders table and the orderitems table based on the<br>orderid and userid (to ensure that users can only see their own data).</div><div>The<br>items ordered in that particular order are retrieved and displayed in a table.</div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ikgagan/IS601/pull/46">https://github.com/ikgagan/IS601/pull/46</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-gi36-prod.herokuapp.com/orders">https://is601-gi36-prod.herokuapp.com/orders</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Store Owner Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history from multiple users</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/235066323-808e840e-db0e-44f0-9870-0d9eb350f5a4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>a screenshot showing purchase history from multiple users<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/235071659-172e67e2-ef19-4176-816b-ed71b2c01b8b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>a screenshot showing full details of a purchase (Order Details Page)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details (mostly how it differs from the user's purchase history feature)</td></tr>
<tr><td> <em>Response:</em> <p><font color="#d1d5db" face="Söhne, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans,<br>sans-serif, Helvetica Neue, Arial, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol,<br>Noto Color Emoji"><span style="font-size: 16px; white-space: pre-wrap;">Similar to the previous implementation, the same<br>logic is applied here.</span></font><div><font color="#d1d5db" face="Söhne, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Ubuntu,<br>Cantarell, Noto Sans, sans-serif, Helvetica Neue, Arial, Apple Color Emoji, Segoe UI Emoji,<br>Segoe UI Symbol, Noto Color Emoji"><span style="font-size: 16px; white-space: pre-wrap;"> However, there is<br>a difference in the initial query used to retrieve order details. </span></font></div><div>&lt;font color=&quot;#d1d5db&quot;<br>face=&quot;Söhne, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, sans-serif, Helvetica<br>Neue, Arial, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color<br>Emoji&quot;&gt;<span style="font-size: 16px; white-space: pre-wrap;">In this case, the orders table is joined with<br>the users table to retrieve the username associated with the order. </span></font></div><div>&lt;font color=&quot;#d1d5db&quot;<br>face=&quot;Söhne, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, sans-serif, Helvetica<br>Neue, Arial, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color<br>Emoji&quot;&gt;<span style="font-size: 16px; white-space: pre-wrap;">When the view button is clicked, the orders table<br>is joined with the orderitems table on itemid to fetch the relevant data.<br></span></font></div><div><font color="#d1d5db" face="Söhne, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans,<br>sans-serif, Helvetica Neue, Arial, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol,<br>Noto Color Emoji"><span style="font-size: 16px; white-space: pre-wrap;">Since the user viewing the order is<br>an admin, the user_id is not used.</span></font><br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ikgagan/IS601/pull/46">https://github.com/ikgagan/IS601/pull/46</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-gi36-prod.herokuapp.com/admin/orders">https://is601-gi36-prod.herokuapp.com/admin/orders</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart page showing the button to place an order</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/235071867-8e6b1a60-26ee-45de-aca5-00039f8fe038.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Cart page showing the button to place an order<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Had issues with import custom CSS and JS file.&nbsp;<br>Later clarified by the professor.<br><div><br></div><div><b>Learnings:</b></div><div><div>Learnt<br>about GET POST request&nbsp;<br>How requests and forms work in Flask<br>Learnt how to pass<br>global variables in Flask<br><br></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-3-shop-project/grade/gi36" target="_blank">Grading</a></td></tr></table>