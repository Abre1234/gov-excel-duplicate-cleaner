# 🏛️ Excel Duplicate Row Cleaner

**Official Data Quality Management System**

A professional, bilingual (English/አማርኛ) web-based tool for detecting and removing duplicate rows in Excel files, designed specifically for institutional use.

![Government Badge](https://img.shields.io/badge/Government-Official%20System-003DA5)
![Language](https://img.shields.io/badge/Language-English%20%7C%20አማርኛ-00843D)
![Status](https://img.shields.io/badge/Status-Production%20Ready-FFB81C)

## 🌟 Key Features

### Core Functionality
- **🔍 Smart Duplicate Detection**: Analyzes ALL columns to identify exact duplicates
- **🌐 Bilingual Interface**: Full support for English and አማርኛ (Amharic)
- **📊 Visual Analytics**: Interactive charts and comprehensive statistics
- **🔎 Advanced Search**: Search and filter duplicate rows
- **🧹 Safe Cleaning**: Review duplicates before removal with confirmation
- **📥 Multiple Export Options**: 
  - Cleaned Excel (data without duplicates)
  - Duplicate rows (only duplicate entries)
  - Comprehensive analysis report

### Design & Security
- **🏛️ Appropriate Design**: Official colors (Blue, Green, Gold) 
- **🔒 100% Private Processing**: All data processed locally, no external sharing
- **📱 Responsive**: Works on desktop, tablet, and mobile devices
- **🔐 Secure**: No permanent file storage, HTTPS ready

## 📋 How It Works

### Duplicate Detection Logic

A row is considered a duplicate **ONLY** when ALL column values match:

✅ **These are duplicates:**
```
Row 1: 101 | Abebe | 25 | IT | Active
Row 2: 101 | Abebe | 25 | IT | Active
```

❌ **These are NOT duplicates:**
```
Row 1: 101 | Abebe | 25 | IT | Active
Row 2: 101 | Abebe | 26 | IT | Active  (Age differs)
```

### Null Cell Coloring

- **Color**: Light Red (RGB: #FFCCCC)
- **Applied to**: All null, empty, or whitespace-only cells
- **Visible in**: Cleaned Excel, Duplicate Excel, and Analysis Report
- **Report includes**: Color name and RGB code in summary

### Null Cell Coloring

- **Color**: Light Red (RGB: #FFCCCC)
- **Applied to**: All null, empty, or whitespace-only cells
- **Visible in**: Cleaned Excel, Duplicate Excel, and Analysis Report
- **Report includes**: Color name and RGB code in summary

## 💻 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/YOUR_USERNAME/gov-excel-cleaner.git
cd gov-excel-cleaner
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the application:**
```bash
streamlit run app.py
```

4. **Open your browser:**
```
http://localhost:8501
```

## 🎯 Usage Guide

### Step-by-Step

1. **Select Language**
   - Choose English or አማርኛ from the dropdown

2. **Upload Excel File**
   - Drag and drop or click to browse
   - Supported formats: .xlsx, .xls
   - Multi-sheet files supported

3. **Analyze Duplicates**
   - Click "ANALYZE DUPLICATES"
   - View statistics and visualizations
   - Review duplicate groups

4. **Download Results**
   - **Cleaned Excel**: Data without duplicates
   - **Duplicate Rows**: Only the duplicates
   - **Analysis Report**: Complete Excel report with:
     - Summary statistics
     - Duplicate details
     - Group summary

## 🗂️ Project Structure

```
gov-excel-cleaner/
├── app.py                    # Main application
├── translations.py           # English + Amharic translations
├── requirements.txt          # Python dependencies
├── modules/
│   ├── excel_handler.py     # Excel file operations
│   ├── duplicate_detector.py# Duplicate detection logic
│   ├── cleaner.py           # Data cleaning operations
│   ├── report_generator.py # Excel exports with RGB coloring
│   └── utils.py             # Utility functions
├── .streamlit/
│   └── config.toml          # Theme configuration
└── README.md                # This file
```

## 🎨 Color Scheme

### Government Official Colors
- **Primary Blue**: #003DA5
- **Secondary Green**: #00843D
- **Accent Gold**: #FFB81C

**Note**: No black colors used - professional gray tones throughout

## 🌐 Language Support

### Currently Available
- **English** (en) - Complete interface
- **አማርኛ (Amharic)** (am) - Complete interface

### Adding New Languages
Edit `translations.py` to add new language codes and translations.

## 🔒 Security & Privacy

### Data Protection
- ✅ Local processing only
- ✅ No external API calls
- ✅ No permanent file storage
- ✅ No sensitive data logging
- ✅ HTTPS ready for deployment

### Suitable For
- Government data processing
- Institutional use
- Sensitive information handling
- Compliance with data protection regulations

## 📊 Technical Details

### Technologies
- **Streamlit**: Web framework
- **Pandas**: Data manipulation
- **Plotly**: Interactive visualizations
- **OpenPyXL**: Excel handling
- **xlrd**: Legacy Excel format support

### Performance
- Handles files up to 100MB
- Processes 50,000+ rows efficiently
- Optimized duplicate detection algorithm
- Responsive UI during processing

## 🧪 Testing

Tested with:
- ✅ Files with no duplicates
- ✅ Files with multiple duplicate groups
- ✅ Rows appearing 3+ times
- ✅ Files with null/empty cells
- ✅ Files with dates and special characters
- ✅ Multi-sheet workbooks
- ✅ Large files (10,000+ rows)

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is provided for institutional government use.

## 🆘 Support

### Issues & Questions
- **GitHub Issues**: Report bugs or request features
- **Documentation**: See this README for usage

### Troubleshooting

**File Upload Error**
- Ensure valid Excel format (.xlsx or .xls)
- Check file size (recommended < 100MB)

**Language Not Switching**
- Refresh the page after selecting language
- Clear browser cache if issue persists

## 📧 Contact

For support or inquiries:
- **GitHub**: [Create an issue](https://github.com/Abre1234/gov-excel-cleaner/issues)
- **Email**: abrarawayal@gmail.com

## 🙏 Acknowledgments

- Designed for Ethiopian institutions
- Built with Streamlit framework
- Amharic language support

---

**🏛️ Built for Government Excellence | Made with ❤️ for Data Quality**

## 📸 Features Showcase

### Bilingual Support
- Switch seamlessly between English and አማርኛ
- All UI elements fully translated

### Interactive Analytics
- Visual charts and graphs
- Duplicate group distribution
- Real-time statistics

### Safe Data Processing
- Review before deletion
- Confirmation required
- First occurrence preserved

---

**Quick Start:**
```bash
pip install -r requirements.txt
streamlit run app.py
```

**Your app will open at:** http://localhost:8501

---

**Repository Status:** ✅ Ready for GitHub Push
