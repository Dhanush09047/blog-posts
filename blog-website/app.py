from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from config import supabase
import uuid

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Home
@app.route("/")
def index():
    posts = supabase.table("posts").select("*").eq("status", "published").execute()
    return render_template("index.html", posts=posts.data)

# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        name = request.form["name"]

        try:
            # Create Supabase Auth user
            result = supabase.auth.sign_up({
                "email": email,
                "password": password
            })

            # IMPORTANT: Use Auth UUID for users table
            user_id = result.user.id

            # Insert into custom users table with same UUID
            supabase.table("users").insert({
                "id": user_id,
                "name": name,
                "email": email,
                "role": "author"
            }).execute()

            return redirect("/login")
        except Exception as e:
            return render_template("register.html", error=str(e))
    
    return render_template("register.html")

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        try:
            user = supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })

            user_id = user.user.id

            # Check if user exists in users table
            existing_user = supabase.table("users").select("*").eq("id", user_id).execute()
            
            # If user doesn't exist in users table, create them
            if not existing_user.data:
                supabase.table("users").insert({
                    "id": user_id,
                    "name": email.split("@")[0],  # Use email prefix as name
                    "email": email,
                    "role": "author"
                }).execute()

            # Store Auth UUID in session
            session["user_id"] = user_id
            session["email"] = email
            
            return redirect("/dashboard")
        except Exception as e:
            return render_template("login.html", error=str(e))

    return render_template("login.html")

# Dashboard
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")

    posts = supabase.table("posts").select("*").execute()
    return render_template("dashboard.html", posts=posts.data)

# Create Post
@app.route("/create", methods=["GET", "POST"])
def create_post():
    if "user_id" not in session:
        return redirect("/login")
    
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        try:
            supabase.table("posts").insert({
                "id": str(uuid.uuid4()),
                "title": title,
                "slug": title.replace(" ", "-").lower(),
                "content": content,
                "author_id": session["user_id"],  # FK SAFE - matches users.id
                "status": "published"
            }).execute()

            return redirect("/dashboard")
        except Exception as e:
            return render_template("create_post.html", error=str(e))

    return render_template("create_post.html")

# View Post
@app.route("/post/<slug>")
def post(slug):
    try:
        post = supabase.table("posts").select("*").eq("slug", slug).single().execute()
        return render_template("post.html", post=post.data)
    except Exception as e:
        return render_template("404.html", error="Post not found"), 404

# Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run()

