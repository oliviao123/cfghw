Section 1: Theory Questions [31 marks]
1.1 What does SDLC stand for? (1 mark)

Answer: SDLC stands for Software Development Life Cycle.

1.2 What exception is thrown when you divide a number by 0? (1 mark)

Answer:  The ArithmeticException is thrown when you divide a number by 0.

1.3 What is the git command that moves code from the local repository to the remote repository? (1 mark)

Answer: The git command that moves code from the local repository to the remote repository is "git push".

1.4 What does NULL represent in a database? (1 mark)

Answer:  NULL represents the absence of a value in a database.

1.5 Name 2 responsibilities of the Scrum Master (2 marks)

Two responsibilities of the Scrum Master are:

Answer: 
1.Facilitating the Scrum events, such as the Sprint Planning, Daily Scrum, Sprint Review, and Sprint Retrospective.
2.Removing any impediments or obstacles that are blocking the team's progress towards their Sprint Goal.

1.6 Name 2 debugging methods, and when you would use them. (4 marks)

Answer: Two debugging methods are:

1. You can print out values of variables at different points in the code, either by adding print statements to the code or using a special tool called a debugger. This can help you figure out where the code is not working correctly.

2.You can use a technique called "error-handling" to catch and handle any errors that might happen while the code is running. This can help you identify and fix specific errors that are causing the code to fail.

1.7 Looking at the following code, describe a case where this function would throw an error when called. Describe this case and talk about what exception handling you’ll need. (5 marks)

def can_pay(price, cash_given):
   if cash_given >= price:
       return True
   else:
       return False

Answer: This is a function that checks if a person can pay for something based on the price and the amount of cash given.

If the cash given is less than the price, the function will return False, which means the person cannot pay for the item. However, if the cash given is greater than or equal to the price, the function will return True, which means the person can pay for the item.

There is a case where this function could throw an error, and that is when the price or cash_given is not a number. For example, if someone calls the function with a price or cash_given that is a string or another data type that is not a number, the function will throw a TypeError.

To handle this exception, we can use a try-except block to catch the TypeError and return an error message to the user, asking them to input the correct data type.

1.8 What is git branching? Explain how it is used in Git. (6 marks)

Answer:  Git branching is a way to work on different versions of code at the same time. When you create a branch, it's like creating a separate copy of your code that you can work on without affecting the original code.

This is useful when you want to add new features or fix bugs without disrupting the main codebase. You can create a branch, make changes to the code in that branch, and then merge the changes back into the main codebase when you're ready.

For example, imagine you're working on a website and want to add a new feature, like a search bar. You can create a branch for the search feature and work on it without affecting the rest of the website. Once the feature is complete, you can merge the changes back into the main codebase.

Git branching also allows multiple people to work on the same project simultaneously without interfering with each other's work. Each person can create their own branch, make changes, and then merge them back into the main codebase when they're ready.

In summary, Git branching is a way to create separate copies of code so that changes can be made without affecting the original codebase. It's a useful tool for developing new features or fixing bugs, and it allows multiple people to work on the same project simultaneously.	

   1.9  Design a restaurant ordering system. 
           You do not need to write code, but describe a high-level approach: 
a.	Draw a list of key requirements
b.	What are your main considerations and problems?
c.	What components or tools would you potentially use? 	  10 marks
a. List of key requirements for a restaurant ordering system:

Answer: 

Menu management: A way to manage the restaurant menu, including items, descriptions, prices, and images.
Order management: A way to manage orders placed by customers, including order details, payment processing, and order status.
User management: A way to manage user accounts, including customer profiles, order history, and loyalty programs.
Kitchen management: A way to manage orders from the kitchen, including order preparation, order status, and delivery.
Reporting and analytics: A way to track sales, inventory, and customer behaviour to help make data-driven decisions.

b. Main considerations and problems:

User experience: The ordering system should be easy to use and navigate for customers, employees, and management.
Security: The system should be secure and protect customer information and payment details.
Integration: The system should integrate with existing restaurant technology, inventory management, and online delivery platforms.

Scalability: The system should be scalable and able to handle increased demand during busy periods.
Cost: The system should be cost-effective and provide a good return on investment.

c. Potential components or tools:

Cloud-based platform: A cloud-based platform can provide scalability, security, and accessibility.
Point-of-sale system: A point-of-sale system can help manage orders and payments.
Mobile app: A mobile app can provide a convenient and user-friendly way for customers to place orders and manage their accounts.
Payment gateway: A payment gateway can securely process customer payments.
Analytics tool: An analytics tool can provide valuable insights into sales, customer behaviour, and inventory management.
Kitchen display system: A kitchen display system can help streamline order preparation and improve efficiency.	
