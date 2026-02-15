# Blog Website - Feature-Rich Blog Platform

A modern, scalable blog website built with **Flask**, **HTML/CSS/JavaScript**, and **Supabase**.

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Database Schema](#database-schema)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [API Routes](#api-routes)
- [Future Enhancements](#future-enhancements)

## 🎯 Project Overview

This is a full-stack blog application that allows users to:
- Register and authenticate securely
- Create, read, and manage blog posts
- Browse published posts on the homepage
- Manage their content through a personalized dashboard

## ✨ Features

✅ User authentication & registration  
✅ Blog CRUD operations (Create, Read, Update, Delete)  
✅ Secure password hashing  
✅ Post publishing workflow  
✅ Responsive design  
✅ Session management  
✅ Error handling  
✅ Clean, modular code structure  

## 🛠️ Tech Stack

**Frontend:**
- HTML5
- CSS3 (Custom with responsive design)
- Vanilla JavaScript (ES6+)

**Backend:**
- Python 3.8+
- Flask (Web framework)
- Flask Sessions (User management)

**Database & Authentication:**
- Supabase (PostgreSQL)
- Supabase Auth
- Supabase Storage (for future image uploads)

**Other:**
- python-dotenv (Environment variables)
- werkzeug (Security utilities)

## 📁 Project Structure

```
blog-website/
│
├── app.py                              # Flask application & routes
├── config.py                           # Supabase configuration
├── requirements.txt                    # Python dependencies
├── .env.example                        # Environment variables template
│
├── templates/                          # HTML templates
│   ├── base.html                       # Base template with navigation
│   ├── index.html                      # Homepage with post listing
│   ├── login.html                      # Login page
│   ├── register.html                   # Registration page
│   ├── dashboard.html                  # User dashboard
│   ├── create_post.html                # Create/Edit post form
│   ├── post.html                       # Individual post view
│   └── 404.html                        # Error page
│
└── static/                             # Static files
    ├── css/
    │   └── style.css                   # Global styles
    └── js/
        └── main.js                     # Client-side scripts
```

## 🚀 Setup Instructions

### 1. Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- A Supabase account (free tier at supabase.com)

### 2. Install Dependencies

```bash
cd blog-website
pip install -r requirements.txt
```

### 3. Create Database Tables in Supabase

Go to your Supabase dashboard and create these tables:

**Table: `users`**
```sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  role TEXT DEFAULT 'author',
  created_at TIMESTAMP DEFAULT NOW()
);
```

**Table: `posts`**
```sql
CREATE TABLE posts (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  title TEXT NOT NULL,
  slug TEXT UNIQUE NOT NULL,
  content TEXT NOT NULL,
  author_id UUID REFERENCES users(id),
  status TEXT DEFAULT 'published',
  created_at TIMESTAMP DEFAULT NOW()
);
```

### 4. Environment Variables

Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

Edit `.env` and add your Supabase credentials:
```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-public-key
```

Get these from your Supabase project settings.

### 5. Run the Application

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

## 📊 Database Schema

### Users Table
| Column | Type | Description |
|--------|------|-------------|
| id | UUID | Primary key |
| name | TEXT | User's full name |
| email | TEXT | Unique email address |
| role | TEXT | User role (admin, author) |
| created_at | TIMESTAMP | Account creation date |

### Posts Table
| Column | Type | Description |
|--------|------|-------------|
| id | UUID | Primary key |
| title | TEXT | Post title |
| slug | TEXT | URL-friendly identifier |
| content | TEXT | Post body content |
| author_id | UUID | Foreign key to users |
| status | TEXT | published/draft/archived |
| created_at | TIMESTAMP | Post creation date |

## 🔐 Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| SUPABASE_URL | Supabase project URL | https://xyz.supabase.co |
| SUPABASE_KEY | Supabase anonymous key | eyJhbGciOiJIUzI1NiIs... |

## ▶️ Running the Application

```bash
# 1. Navigate to project directory
cd blog-website

# 2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file with Supabase credentials
cp .env.example .env
# Edit .env with your credentials

# 5. Run Flask application
python app.py

# 6. Open browser
# Visit http://localhost:5000
```

## 🛣️ API Routes

| Route | Method | Description | Auth Required |
|-------|--------|-------------|----------------|
| `/` | GET | Homepage with published posts | No |
| `/register` | GET, POST | User registration | No |
| `/login` | GET, POST | User login | No |
| `/logout` | GET | User logout | Yes |
| `/dashboard` | GET | User dashboard | Yes |
| `/create` | GET, POST | Create new post | Yes |
| `/post/<slug>` | GET | View single post | No |
| `/edit/<id>` | GET, POST | Edit post (coming soon) | Yes |
| `/delete/<id>` | POST | Delete post (coming soon) | Yes |

## 🔄 Future Enhancements

Planned features to add:
- 📝 **Markdown Editor** - Rich text editing with preview
- 🏷️ **Tags & Categories** - Organize posts better
- 💬 **Comments System** - Reader engagement
- ❤️ **Likes & Bookmarks** - Social features
- 🖼️ **Image Upload** - Supabase Storage integration
- 📊 **Admin Dashboard** - Analytics and statistics
- 🔍 **Search Functionality** - Full-text search
- 📧 **Email Notifications** - Post updates via email
- 🎨 **Theme Customization** - Dark mode and themes
- 📱 **Mobile App** - React Native/Flutter version

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements.

## 📄 License

This project is open source and available under the MIT License.

## 📞 Support

For issues or questions:
1. Check the existing documentation
2. Review Flask and Supabase documentation
3. Open an issue in the repository

---

**Built with ❤️ for developers**
