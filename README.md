# 🚀 GitHub Webhook Dashboard

A full-stack application that listens to GitHub Webhooks for **Push**, **Pull Request**, and **Merge** actions, and stores them in **MongoDB**. A sleek frontend dashboard automatically fetches and displays the latest events every 15 seconds with pagination and smooth user interactions.


---

## 📦 Features

- ✅ GitHub Webhook integration for:
  - **Push**
  - **Pull Request**
  - **Merge**
- ✅ Stores events in **MongoDB Atlas**
- ✅ Frontend dashboard (HTML/CSS/JS)
  - Refreshes every **15 seconds**
  - Supports **"See More"** / **"See Less"** interaction
  - Responsive and modern UI
- ✅ Timestamps are stored in **IST**
- ✅ MongoDB stores structured schema with:
  - `request_id`
  - `author`
  - `action_type`
  - `from_branch`
  - `to_branch`
  - `timestamp`

---

## 🧠 Example Messages

- `"SwarnavaPanda pushed to main on 05 July 2025 - 03:00 PM IST"`
- `"SwarnavaPanda submitted a pull request from dev to main on 05 July 2025 - 03:05 PM IST"`
- `"SwarnavaPanda merged branch dev to main on 05 July 2025 - 03:10 PM IST"`

---

## 🛠️ Tech Stack

| Component   | Tech Used              |
|-------------|------------------------|
| Backend     | Flask + Flask-CORS     |
| Database    | MongoDB Atlas          |
| Frontend    | HTML + CSS + JS        |
| Webhooks    | GitHub Webhooks        |
| Hosting     | ngrok (for local dev)  |
| Timezones   | `pytz` for IST support |

---

## 🗂️ Project Structure
webhook-repo/
│
├── app.py # Flask backend
├── .env # MongoDB URI (keep secret!)
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # Frontend UI
