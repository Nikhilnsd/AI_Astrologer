# 🔮 AI Astrologer App

A simple AI Astrologer application that takes user birth details and provides personalized astrology-based responses with AI-powered Q&A functionality.

## 🌟 Features

- **Birth Chart Analysis**: Enter your birth details to get your zodiac sign and traits
- **Daily Horoscope**: Get today's horoscope with mood, lucky numbers, and colors
- **AI-Powered Q&A**: Ask any astrology-related questions and get intelligent responses
- **Clean UI**: User-friendly Streamlit interface
- **No API Key Required**: Uses free AI services for question answering

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ai-astrologer.git
cd ai-astrologer
```

2. **Install dependencies**
```bash
pip install streamlit requests datetime
```

3. **Run the application**
```bash
streamlit run app.py
```

4. **Open your browser**
The app will automatically open at `http://localhost:8501`

## 📱 Usage

1. **Enter Your Details**
   - Name
   - Date of Birth
   - Time of Birth
   - Place of Birth

2. **Get Your Horoscope**
   - Click "Get Today's Horoscope" to see your daily reading
   - View your zodiac traits, mood, lucky number, and color

3. **Ask Questions**
   - Type any astrology-related question in the text area
   - Click "Ask the AI Astrologer" for personalized responses

### Example Output
**Capricorn ♑**
- **Trait:** Ambitious, disciplined, long-term thinker
- **❤️ Mood:** Determined 
- **🍀 Lucky Number:** 10 
- **🎨 Lucky Color:** Brown

## 🛠 Technologies Used

- **Python 3.x** - Core programming language
- **Streamlit** - Web app framework
- **Requests** - HTTP library for API calls
- **API Ninjas** - Horoscope data provider
- **Free GPT API** - AI-powered question answering

## 📁 Project Structure

```
ai-astrologer/
├── app.py              # Main Streamlit application
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies (optional)
└── demo_video/         # Demo video files
```

## 🔧 Configuration

The app uses:
- **API Ninjas** for horoscope data (API key included in code)
- **Free GPT API** for AI responses (no key required)

## 📋 Requirements.txt

```txt
streamlit>=1.28.0
requests>=2.31.0
```

## 🎯 Features Implemented

- ✅ Clean UI for user input collection
- ✅ Zodiac sign calculation from birth date
- ✅ Daily horoscope integration
- ✅ AI-powered free-text question answering
- ✅ Astrology-based response generation
- ✅ No API key requirement for Q&A

## 🔮 How It Works

1. **User Input**: Collects birth details through a clean form
2. **Zodiac Calculation**: Determines zodiac sign from birth date
3. **Horoscope Fetch**: Retrieves daily horoscope from API Ninjas
4. **AI Integration**: Uses free GPT API to answer user questions with context
5. **Response Generation**: Combines astrology data with AI for personalized answers

## 🚀 Demo

### Sample Questions You Can Ask:
- "What does my birth chart say about my career?"
- "How will my zodiac sign affect my relationships?"
- "What should I focus on today based on my horoscope?"
- "Tell me about my personality traits as a [Your Sign]"

## 👨‍💻 Author

**Nikhil**
- Email: nikhilnsd01@gmail.com
- GitHub: [Nikhilnsd](https://github.com/Nikhilnsd)

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

If you encounter any issues or have questions:
- Create an issue on GitHub
- Email: nikhilnsd01@gmail.com

---

⭐ **Star this repo if you found it helpful!**
