from flask import Blueprint, jsonify, render_template, redirect, url_for, flash, request, session
from app.utils.utility import login_required
from app import db
from app.blog.model import Blog 
from app.user.model import User 


blog = Blueprint('blog', __name__)
    


@blog.route('/add', methods=['POST'])
@login_required
def post_blog():
    usr=User.query.get(session["user_id"])
    if request.method == 'POST':
        author = session["user_id"]
        title = request.form['title']
        posting = request.form['post']
     
        new_post = Blog(author=author, title=title, post=posting )

        try:
            # Add  commit the transaction
            db.session.add(new_post)
            db.session.commit()
            
        except Exception as e:
            # Handle registration failure
            db.session.rollback()
            return 'Posting failed: ' + str(e)

    return 'Posting successful!'

@blog.route('/update/<int:post_id>', methods=['PUT'])
@login_required
def update(post_id):
    blg=Blog.query.get(post_id)
    
    if blg.author==session["user_id"]:
        if "title" is not None:
            blg.title=request.form["title"]
        if "post" is not None:
            blg.post=request.form["post"]
    

        try:
            # Add  commit the transaction
            db.session.add(blg)
            db.session.commit()
            
            return 'Update Success' 
            
        except Exception as e:
            # Handle failure
            db.session.rollback()
            return 'Posting failed: ' + str(e)
        
    
    return 'Update unauthorized', 401        


   

@blog.route('/posts', methods=['GET'])
@login_required
def get_all():
    blogs = Blog.query.all()
    blogs_data = [blog.as_dict() for blog in blogs]
    if blogs_data is not None:
        return jsonify(blogs_data)
    return "Not Found"



@blog.route('/post/<int:post_id>', methods=['GET'])
@login_required
def get_single(post_id):
    blogs = Blog.query.get(post_id)
    if blogs is not None:
        return blogs.as_dict()
    return "Not Found"


@blog.route('/delete/<int:post_id>', methods=['DELETE'])
@login_required
def delete_post(post_id):
    blog_to_delete = Blog.query.get(post_id)
    if blog_to_delete:
        # Perform the delete operation
        db.session.delete(blog_to_delete)
        db.session.commit()
        return "Blog deleted successfully."
    else:
        return "Blog not found", 404