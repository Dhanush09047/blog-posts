# 🚀 Deployment Guide - Render.com

## Prerequisites
- GitHub account with your blog repository pushed
- Render.com account (free tier available)
- Supabase project with tables created

## Step 1: Push to GitHub

```bash
# Initialize git (if not already done)
git init
git add .
git commit -m "Initial blog commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/blog-posts.git
git push -u origin main
```

## Step 2: Create Render.com Service

1. Go to [render.com](https://render.com)
2. Click **"New +"** → Select **"Web Service"**
3. Connect your GitHub repository
4. Fill in the form:
   - **Name:** `blog-website` (or your choice)
   - **Root Directory:** (leave empty if repo root)
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`

## Step 3: Add Environment Variables

In Render dashboard, go to your service → **Environment**

Add these variables:
```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-public-key
```

Get these from your Supabase Project Settings → API

## Step 4: Deploy

1. Click **"Create Web Service"**
2. Render will automatically deploy from GitHub
3. Wait for build to complete
4. Your app will be live at: `https://blog-website.onrender.com`

## Troubleshooting

### Error: "requirements.txt not found"
- Make sure `requirements.txt` is in the **root directory** of your GitHub repo
- Push the file: `git add requirements.txt && git push`

### Error: Module not found
- Clear build cache in Render dashboard
- Manual rebuild: Settings → "Clear all and redeploy"

### Supabase connection failed
- Double-check SUPABASE_URL and SUPABASE_KEY in environment variables
- Ensure your IP is allowed in Supabase (Network settings)

### Port issues
- Render uses PORT environment variable automatically
- App is configured to read: `os.environ.get("PORT", 5000)`

## Auto-Deploy

Once connected, Render will automatically deploy when you push to GitHub:

```bash
git add .
git commit -m "Update blog"
git push origin main
```

## Free Tier Limits
- 750 hours/month (always-on)
- Spins down after 15 minutes of inactivity
- Free SSL certificate included

## Next Steps

1. ✅ Push code to GitHub
2. ✅ Connect to Render
3. ✅ Add environment variables
4. ✅ Deploy!
5. 🎉 Your blog is live!

---

**Need help?** Check Render docs: https://render.com/docs
