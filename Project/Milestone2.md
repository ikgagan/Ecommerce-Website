<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Gagan Indukala Krishna Murthy (gi36)</td></tr>
<tr><td> <em>Generated: </em> 4/23/2023 8:25:39 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-2-shop-project/grade/gi36" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233553433-d3360124-72bf-4e6b-9750-0f55a6dd7909.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>empty create item page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233553436-d3844e44-5dd5-45d6-b394-dbd9f4cea6af.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data filled in create item page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233553439-80b22fb1-88b6-4db2-986d-b37335a77b92.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>saved create item page - flash message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233553795-f7b29dd8-1796-43b2-ac6c-5aefcc7a8482.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>database where the item is added ( id = 10)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <p>The form data is received and verified in the backend, and then a<br>simple insert statement is used to enter the data into the database.<br>Moreover, if<br>the stock is greater than 0, the visibility is set as true.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ikgagan/IS601/pull/44">https://github.com/ikgagan/IS601/pull/44</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-gi36-prod.herokuapp.com/admin/item">https://is601-gi36-prod.herokuapp.com/admin/item</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233563997-e7895c6f-a630-4ed4-b9bc-bb13ed914275.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>5 items displayed without sort or filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233564000-dc28830b-4303-4052-bc1f-b6d2b01c473c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>2nd set of 5 items displayed without sort or filter<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233564381-97b68887-bb65-4439-b869-99e2e70b474d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Name search - dior<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233564384-7a622ef9-fa3e-4ae6-94a6-8c37fb43fb0f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>name desc order sort<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233564389-720d57fa-493a-42aa-b318-117b4a2d25b3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>unit price asc order sort<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233565365-e382e9c2-d958-4792-b588-4a80855fe570.PNG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code logic for sort and filter<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <p>On the listing page, only products with visibility equal to True are retrieved.<br><br>The data is then filtered and sorted using different parameters. <br>For instance, the<br>name and description filters use the &quot;like&quot; command to match the user&#39;s input<br>with the available items. <br>The sorting is done using the Order by command,<br>which can sort the items in ascending or descending order, as per the<br>user&#39;s preference.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ikgagan/IS601/pull/44">https://github.com/ikgagan/IS601/pull/44</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-gi36-prod.herokuapp.com/shop">https://is601-gi36-prod.herokuapp.com/shop</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233565854-63db5ac9-0c6a-4318-a2c0-a2879b8de500.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>admin/list page showing the list of all the products (even non visible products)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <div>In this page, all items are fetched from the products table regardless of<br>the visibility. ie.&nbsp; A simple select * command with a limit value and<br>no other filters</div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ikgagan/IS601/pull/44">https://github.com/ikgagan/IS601/pull/44</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-gi36-prod.herokuapp.com/admin/items">https://is601-gi36-prod.herokuapp.com/admin/items</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233563997-e7895c6f-a630-4ed4-b9bc-bb13ed914275.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit button on shop page <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233573999-92670b52-097a-4dfc-b82d-f36c048a3a27.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit button product detail page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233565854-63db5ac9-0c6a-4318-a2c0-a2879b8de500.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit button on admin/list page which is product list page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233574564-ce065482-3c65-4276-a17d-d9df11598b39.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before editing a item for stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233813291-15aa6581-c638-49d1-86d9-5eb09d6883d8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after editing a item - changed stock from 5 to 11<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233871476-f407d83c-bc1b-4055-b2b7-5578bf2e4db1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before editing a item for cost<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233871478-cf6b1e6d-6f24-4b4a-a586-3eb1398604ac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after editing a item - changed cost from 151 to 200<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>The default action is assigned to all edit buttons.<br>To prefill the form, a<br>query is executed to retrieve data from the database.&nbsp;<div>Once the form is filled,<br>any changes made to the form are updated in the backend. <br>Additionally, every<br>update call checks whether the quantity is zero. If the quantity is zero,<br>the visibility is also set to false.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ikgagan/IS601/pull/44">https://github.com/ikgagan/IS601/pull/44</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-gi36-prod.herokuapp.com/admin/items">https://is601-gi36-prod.herokuapp.com/admin/items</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233871593-9c13840f-ae60-4de2-99f1-7e8a1e721455.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>clickable view button on each items which get directed to the product detail<br>page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233871598-309a83a4-acce-4102-b5ae-f11e1248ccdc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after click the view button - it goes to the product details page<br>- displaying all the details+<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <div>When a user clicks the view button, a call is made to shop_item<br>endpoint. In the backend, data of that particular items is fetched from db<br>and displayed in the frontend.</div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ikgagan/IS601/pull/44">https://github.com/ikgagan/IS601/pull/44</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-gi36-prod.herokuapp.com/shop/item">https://is601-gi36-prod.herokuapp.com/shop/item</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233871774-4ca896fb-34b1-4bc3-9d4e-5cec13d266ee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the success message of adding to cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233871890-7045dd9f-8faa-4594-8ba7-d6b1585fca71.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>error message when you go to cart page without logging in <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233872063-86261582-e78c-4137-9baf-569556528c3f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> a screenshot of the Cart table with data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <p>A single cart is assigned to each user at a time, and when<br>an order is placed, the cart is emptied.&nbsp;<div>Additionally, users have the ability to<br>modify the quantity of items in their cart at any point.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <p>When a user clicks on the &quot;add to cart&quot; button, the item they<br>selected is added to their cart. In the backend, a new entry is<br>added to the cart table specifically for that item. <br>Each user can have<br>multiple entries in the cart table, with each row in the table corresponding<br>to a specific item in their cart.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ikgagan/IS601/pull/44">https://github.com/ikgagan/IS601/pull/44</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233871807-3a76965c-eb1e-457d-95ca-9f0ad192e319.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>a screenshot of the Cart page with data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <p>The items in the cart are retrieved from the database, and then the<br>unit price for each item is multiplied by its corresponding quantity to calculate<br>the subtotal.&nbsp;<div>The subtotal is displayed on the frontend. The subtotals are then added<br>together to get the total, which is also displayed on the frontend.&nbsp;</div><div>Namespaces are<br>utilized on the frontend to ensure that the total object remains in scope<br>until the end.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ikgagan/IS601/pull/44">https://github.com/ikgagan/IS601/pull/44</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-gi36-prod.herokuapp.com/cart">https://is601-gi36-prod.herokuapp.com/cart</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233873858-efccdd38-e258-406c-b65d-75622abcdb6f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before updating the cart quantity  - dior x jordan is 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233873859-7f1b54ce-46c4-49ec-ab6a-ced50cf1d470.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after updating the cart quantity  - dior x jordan is 3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233874010-2c4b355a-9aa7-42e2-8c7c-f5fa142d50e2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before the making the cart quantity of dior x jordan to 0<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233874012-e5d154dc-51ea-4897-8b2b-b9b23ad0ff97.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after the making the cart quantity of dior x jordan to 0 -<br>success message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233874253-9eef7f18-b42e-47cc-ae26-ea6de037f0cc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before updating the quantity to -5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233874258-43cffe40-8740-42f9-ab1b-0bce17fd5bfe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after updating - if the quantity is less than zero it will get<br>deleted same as the quantity 0<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <div><font color="#e6edf3" face="-apple-system, BlinkMacSystemFont, Segoe UI, Noto Sans, Helvetica, Arial, sans-serif, Apple Color<br>Emoji, Segoe UI Emoji"><span style="font-size: 16px;">When an user sets the quantity as 0<br>or a negative values, it&nbsp;</span></font><span style="font-size: 16px; color: rgb(230, 237, 243); font-family: -apple-system,<br>BlinkMacSystemFont, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI<br>Emoji&quot;;">is considered as item deletion in the backend.<br>&nbsp;i.e that particular item is&nbsp;</span><span style="font-size:<br>16px; color: rgb(230, 237, 243); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica,<br>Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;">deleted from the cart of that<br>particular user</span></div><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ikgagan/IS601/pull/44">https://github.com/ikgagan/IS601/pull/44</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233874371-cde4ca62-0609-45b5-8456-4d9ea6c51954.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before deleting a single item from the cart using the &#39;x&#39; delete button<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233874373-78d7b3fc-00e0-4083-bcd8-67f94763ff51.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after deleting a single item from the cart using the &#39;x&#39; delete button<br>- success flash message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233874467-4527c9b4-39ad-45a6-81e6-f69835851d12.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before clearing the cart to 0 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420429/233874468-69e07ecf-d1b9-4560-b616-7115e4eca117.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after clearing the cart to 0 <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <div>To delete an item from the cart, a delete request is sent to<br>the server with the item's ID and the current user's ID.&nbsp;</div><div>This results in<br>the corresponding entry being removed from the cart table.</div><div>When the user chooses to<br>clear their entire cart, all items associated with the user are removed from<br>the cart table in a single delete operation.<br></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ikgagan/IS601/pull/44">https://github.com/ikgagan/IS601/pull/44</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>No issues&nbsp;<br><br>Learnt some CSS and GET POST method in python flask&nbsp;<br><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-gi36-prod.herokuapp.com/login">https://is601-gi36-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-2-shop-project/grade/gi36" target="_blank">Grading</a></td></tr></table>