# 📸 JPEG 1st Year Slot Availability Checker

[Open the App](https://jpegslotavailability-hdmosr5ttnvjuappqrbpbr.streamlit.app/) 🚀

## Description  
This web-app is built for the JPEG Photography Club 1st Year students to quickly check who is free at a given day & time.  
Students can input a day and a time-range (24-hour format) and see:
- Who is free for the **entire slot**
- Hour-by-hour availability within that slot

The interface supports dark mode and it’s mobile-friendly.

## 🧭 How to Use  
1. Open the App link above.  
2. Select a day (Monday through Saturday).  
3. Enter a time slot in the format `9-12` (meaning 9:00–12:00).  
4. The app will display:
   - Members free for the *whole* entered slot.  
   - Hourly breakdown showing who is free each hour.  
5. Use the **Copy** button to copy results and share in your group.  
6. Use the **Download** button to save the results as a `.txt` (printable or PDF friendly).

## ✅ Features  
- Dark theme with high contrast for mobile readability.  
- Works seamlessly on phones, tablets and desktops.  
- Quick access via a share-link (no install required).  
- Copy and download options for sharing and printing.  
- Hour-by-hour breakdown + full-slot availability.

## 🛠 Installation (for local development)  
```bash
git clone <your-repo-url>
cd <repo-folder>
pip install streamlit
streamlit run app.py
