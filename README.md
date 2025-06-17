# InstaVibe

A modern, AI-powered bio generator built using **Streamlit**, **LangChain**, and **Google Gemini API**. InstaVibe helps users instantly create impressive bios tailored for social media, portfolios, or professional platforms.

---

## 🚀 Features

- **Smart Bio Generation**: Generate professional and catchy bios with one click  
- **LangChain Integration**: Prompt-template driven AI responses  
- **Google Gemini AI**: Powered by Google's cutting-edge language model  
- **Streamlit UI**: Clean, interactive, and minimalistic interface  
- **Real-time Feedback**: Dynamic prompt updates and instant results  
- **One-Tap Copy**: Easily copy bios with a single click  
- **Secure Environment**: `.env`-based API key management

---

## 🧱 Tech Stack

### Frontend:

- Streamlit (Python)
- Custom CSS for styling
- Clipboard API for copy feature

### Backend:

- LangChain PromptTemplate and LLMChain
- Google Gemini API via `langchain_google_genai`
- Python `os` for environment variable handling

---

## 🧰 Getting Started

### 📦 Prerequisites

- Python 3.9 or above
- Google Gemini API key

### 🔧 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Aditya-padale/InstaVibe.git
   cd InstaVibe

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your `.env` file:**
   Create a `.env` file in the root directory:

   ```env
   GOOGLE_API_KEY=your-gemini-api-key
   ```

4. **Run the app:**

   ```bash
   streamlit run app.py
   ```

---

## 🌐 Application URL

Live Demo: [https://instavibe.streamlit.app](https://instavibe.streamlit.app)

---

## 📋 API Usage (via LangChain & Gemini)

* Uses `PromptTemplate` to format user inputs.
* Sends requests to Gemini Pro via LangChain's `ChatGoogleGenerativeAI`.
* Returns bio suggestions in natural language format.

---

## 📁 Project Structure

```
instavibe/
├── app.py                  # Main Streamlit application
├── .env                   # Environment variables (API key)
├── requirements.txt       # Python dependencies
├── .gitignore             # Ignored files
└── README.md              # Project documentation
```

---

## 🧪 Testing

* ✅ Test the Streamlit UI on `http://localhost:8501`
* ✅ Enter a few name/role combinations and check for real-time bio generation
* ✅ Click the copy button and validate clipboard interaction
* ✅ Check for API errors or missing keys

---

## 🧼 Available Scripts

```bash
streamlit run app.py             # Run the app locally
pip install -r requirements.txt  # Install all dependencies
```

---

## 🎨 Features Showcase

* ✨ **Responsive UI** with real-time interaction
* 🧠 **Context-aware Prompts** for tailored bios
* 🔒 **Secure API Integration** using `.env` file
* 🖱️ **One-click Copy** for user convenience
* 🎯 **Fast, Lightweight** deployment with Streamlit Cloud

---

## 📬 Connect with Me

**Aditya Padale**
📧 [adityapadale2003@gmail.com](mailto:adityapadale2003@gmail.com)
🔗 [GitHub](https://github.com/Aditya-padale)

---

## ⭐ Support

If you like this project, don’t forget to ⭐ the repository and share it with others!

---

## 📄 License

This project is licensed under the [MIT License](LICENSE)

```

---

Let me know if you'd like a `LICENSE` file or a `.env.example` file created too!
```

