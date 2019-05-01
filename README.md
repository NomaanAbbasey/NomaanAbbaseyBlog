# NomaanAbbaseyBlog

All Requirements have been fulfilled. 
The application: Lists a view posts, shows detail view of any post,
can create a post with a simple html form (in this case a django form),
can edit a selected post, and posts persist with the use of a database

The major roadblock in the making of this application would be the html form. The issue was a drop down 
as you couldn't get the value from the POST and thus I had to switch over to using a django form and pas
sing it into the view in order to render data inputs I can read. 

Another issue arose when updating the the blog post. The object instance of that blog post was not sub
scriptable (this issue came up in creation too ). Therefore I had to figure what would give me the object
in a way that I can change it. The change from programming languages that solve things before runtime
to django and python that figure it out what to in runtime attributed to this difficulty. 

Due to time constraints I wasn't able to handle every issue such as using modals to inform the user if 
the blog form was valid and what not. I also was not able to implement a date picker and proper date input field 
for the creation form. As of now I lack knowledge as to how to properly style the the form which utilizes 
th and tr elements without a table to encapsulate them and the fact they render from a form object. 

Overall, I am happy to add more experience to my limited python and django experience and build up on it.
This was a great opportunity.   



