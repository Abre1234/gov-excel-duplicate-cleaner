"""
Translation module for Amharic and English languages
"""

TRANSLATIONS = {
    'en': {
        # Header
        'app_title': 'Government Excel Duplicate Row Cleaner',
        'app_subtitle': 'Official Data Quality Management System',
        'language': 'Language',
        
        # Sidebar
        'about_title': 'About This System',
        'key_features': 'Key Features',
        'feature_upload': 'Drag & Drop upload',
        'feature_detection': 'Smart Detection (ALL columns)',
        'feature_analytics': 'Visual Analytics dashboard',
        'feature_search': 'Search & Filter duplicates',
        'feature_cleaning': 'Safe Cleaning with confirmation',
        'feature_download': 'Multiple Downloads options',
        
        'display_settings': 'Display Settings',
        'rows_per_page': 'Rows per page',
        'appearance': 'Appearance',
        'quick_stats': 'Quick Stats',
        'total_rows': 'Total Rows',
        'duplicates': 'Duplicates',
        'duplicate_rate': 'Duplicate Rate',
        'need_help': 'Need Help?',
        
        # Help text
        'help_text': '''**How it works:**
1. Upload your Excel file
2. Select worksheet (if multiple)
3. Click Analyze Duplicates
4. Review results
5. Remove duplicates
6. Download cleaned data

**Support:** Contact your IT department''',
        
        # Privacy notice
        'privacy_title': 'Privacy & Security',
        'privacy_text': 'Your data is processed locally and securely. No files are stored permanently or shared with external services.',
        'privacy_badge': '100% Private Processing ✓',
        
        # Step 1
        'step1_title': 'Upload Your Excel File',
        'upload_prompt': 'Choose an Excel file (.xlsx or .xls)',
        'upload_help': 'Drag and drop or click to browse your files',
        'supported_formats': 'Supported Formats',
        'format_xlsx': 'Excel 2007+ (.xlsx)',
        'format_xls': 'Excel 97-2003 (.xls)',
        'file_uploaded': 'File uploaded successfully!',
        'reading_file': 'Reading your Excel file...',
        'no_data': 'The uploaded Excel file does not contain usable data.',
        'multiple_sheets': 'Multiple Sheets Detected!',
        'select_sheet': 'Select worksheet to analyze:',
        'sheets_available': 'sheets available',
        'using_sheet': 'Using worksheet:',
        'loading_data': 'Loading worksheet data...',
        'no_sheet_data': 'The selected worksheet does not contain usable data.',
        
        # File info
        'file_info': 'File Information',
        'total_columns': 'Columns',
        'file_size': 'File Size',
        'sheet': 'Sheet',
        
        # Data preview
        'data_preview': 'Data Preview',
        'table_view': 'Table View',
        'column_info': 'Column Info',
        'showing_rows': 'Showing first {0} rows of {1} total rows',
        'column_name': 'Column Name',
        'data_type': 'Data Type',
        'non_null_count': 'Non-Null Count',
        'null_count': 'Null Count',
        
        # Step 2
        'step2_title': 'Analyze For Duplicate Rows',
        'how_detection_works': 'How Duplicate Detection Works',
        'detection_rule1': 'Complete Row Comparison: All column values must match',
        'detection_rule2': 'First Occurrence Preserved: The original row is kept',
        'detection_rule3': 'Smart Detection: Handles empty cells, whitespace, and data types',
        'detection_rule4': 'Group Organization: Duplicates are grouped for easy review',
        'analyze_button': 'ANALYZE DUPLICATES',
        'analyzing': 'Analyzing your data...',
        'reading_data': 'Reading data...',
        'detecting_duplicates': 'Detecting duplicates...',
        'analyzing_groups': 'Analyzing groups...',
        'finalizing': 'Finalizing results...',
        'analysis_complete': 'Analysis complete! Scroll down to see results.',
        
        # Step 3
        'step3_title': 'Analysis Results & Statistics',
        'congratulations': 'Congratulations!',
        'no_duplicates': 'No duplicate rows were found. Your dataset contains only unique rows based on all columns.',
        'data_quality': 'Data Quality Overview',
        'all_unique': 'All Rows Are Unique ✓',
        'key_metrics': 'Key Metrics',
        'unique_rows': 'Unique Rows',
        'duplicate_rows': 'Duplicate Rows',
        'columns_analyzed': 'Total Columns Analyzed',
        'duplicate_groups': 'Duplicate Groups Found',
        
        # Visualizations
        'visual_analytics': 'Visual Analytics',
        'overview': 'Overview',
        'distribution': 'Distribution',
        'group_analysis': 'Group Analysis',
        'unique_vs_duplicate': 'Unique vs Duplicate Rows Comparison',
        'data_composition': 'Data Composition',
        'group_distribution': 'Duplicate Group Size Distribution',
        'num_duplicates': 'Number of Duplicate Occurrences',
        'num_groups': 'Number of Groups',
        
        # Step 4
        'step4_title': 'Review Duplicate Rows',
        'duplicates_detected': 'Duplicates Detected',
        'found_duplicates': 'Found {0} duplicate rows organized into {1} groups.',
        'search_filter': 'Search & Filter',
        'search_placeholder': 'Type anything to search...',
        'search_help': 'Search across all columns in duplicate rows',
        'filter_group': 'Filter by Duplicate Group:',
        'filter_help': 'View specific duplicate groups',
        'sort_by': 'Sort by:',
        'sort_help': 'Sort the results',
        'all_groups': 'All Groups',
        'showing_results': 'Showing {0} of {1} duplicate rows',
        'duplicate_table': 'Duplicate Data Table',
        'page_indicator': 'Page (1-{0})',
        'page_help': 'Navigate through {0} pages',
        'showing_page': 'Showing rows {0} to {1} of {2}',
        'group_occurrences': 'Group {0} has {1} total occurrences (including original)',
        'no_matches': 'No duplicate rows match your search criteria.',
        
        # Step 5
        'step5_title': 'Remove Duplicate Rows',
        'review_before': 'Review Before Proceeding',
        'will_retain': 'First occurrence of each duplicate group will be retained',
        'will_remove': '{0} duplicate rows will be removed',
        'will_preserve': 'Original column names and data values will be preserved',
        'will_maintain': 'Row order will remain unchanged',
        'confirm_remove': 'I confirm that I want to remove {0} duplicate rows',
        'confirm_help': 'Check this box to enable the Remove Duplicates button',
        'ready_proceed': 'Ready to proceed!',
        'confirmation_required': 'Confirmation required',
        'remove_button': 'REMOVE DUPLICATES NOW',
        'removing': 'Removing duplicate rows...',
        'success_title': 'Success!',
        'success_message': 'Successfully removed {0} duplicate rows! Your cleaned dataset now contains {1} unique rows.',
        
        # Step 6
        'step6_title': 'Download Your Results',
        'available_downloads': 'Available Downloads',
        'download_info': 'Choose what you want to download. All files are generated in Excel format.',
        'cleaned_excel': 'Cleaned Excel',
        'cleaned_desc': 'Data without duplicates',
        'download_cleaned': 'Download Cleaned File',
        'duplicate_rows_title': 'Duplicate Rows',
        'duplicates_desc': 'Only duplicate entries',
        'download_duplicates': 'Download Duplicates',
        'analysis_report': 'Analysis Report',
        'report_desc': 'Complete analysis',
        'download_report': 'Download Report',
        'remove_first': 'Remove duplicates first',
        
        # Error messages
        'error_reading': 'Unable to read this Excel file. Please verify that the file is valid and try again.',
        'view_error': 'View Error Details',
    },
    
    'am': {
        # Header (Amharic)
        'app_title': 'የመንግስት ኤክሴል ድግግሞሽ ረድፍ ማጽዳት',
        'app_subtitle': 'ኦፊሴላዊ የመረጃ ጥራት አስተዳደር ስርዓት',
        'language': 'ቋንቋ',
        
        # Sidebar
        'about_title': 'ስለዚህ ስርዓት',
        'key_features': 'ቁልፍ ባህሪያት',
        'feature_upload': 'መጎተት እና መጣል ስራ',
        'feature_detection': 'ብልህ ግኝት (ሁሉም አምዶች)',
        'feature_analytics': 'የእይታ ትንተና ዳሽቦርድ',
        'feature_search': 'ፍለጋ እና ማጣሪያ ድግግሞሽ',
        'feature_cleaning': 'ደህንነቱ የተጠበቀ ማፅዳት ምን ማረጋገጫ',
        'feature_download': 'ብዙ ማውረጃዎች አማራጮች',
        
        'display_settings': 'የማሳያ ቅንጅቶች',
        'rows_per_page': 'ረድፎች በገጽ',
        'appearance': 'መልክ',
        'quick_stats': 'ፈጣን ስታቲስቲክስ',
        'total_rows': 'ጠቅላላ ረድፎች',
        'duplicates': 'ድግግሞሾች',
        'duplicate_rate': 'የድግግሞሽ መጠን',
        'need_help': 'እርዳታ ያስፈልግዎታል?',
        
        # Help text
        'help_text': '''**እንዴት እንደሚሰራ:**
1. የእርስዎን ኤክሴል ፋይል ይስቀሉ
2. የስራ ሉህ ይምረጡ (ብዙ ከሆነ)
3. ድግግሞሾችን ተንትን ይጫኑ
4. ውጤቶችን ይገምግሙ
5. ድግግሞሾችን ያስወግዱ
6. የተጸዳ መረጃ ያውርዱ

**ድጋፍ:** የእርስዎን የአይቲ ክፍል ያግኙ''',
        
        # Privacy notice
        'privacy_title': 'ግላዊነት እና ደህንነት',
        'privacy_text': 'የእርስዎ መረጃ በአካባቢው እና በደህንነት ይሰራል። ምንም ፋይሎች በቋሚነት አይከማቹም ወይም ከውጭ አገልግሎቶች ጋር አይጋራም።',
        'privacy_badge': '100% የግል ሂደት ✓',
        
        # Step 1
        'step1_title': 'የእርስዎን ኤክሴል ፋይል ይስቀሉ',
        'upload_prompt': 'የኤክሴል ፋይል ይምረጡ (.xlsx ወይም .xls)',
        'upload_help': 'መጎተት እና መጣል ወይም ፋይሎችዎን ለማሰስ ጠቅ ያድርጉ',
        'supported_formats': 'የተደገፉ ቅርጸቶች',
        'format_xlsx': 'ኤክሴል 2007+ (.xlsx)',
        'format_xls': 'ኤክሴል 97-2003 (.xls)',
        'file_uploaded': 'ፋይል በተሳካ ሁኔታ ተስቀሏል!',
        'reading_file': 'የእርስዎን ኤክሴል ፋይል በማንበብ ላይ...',
        'no_data': 'የተሰቀለው ኤክሴል ፋይል ጥቅም ላይ የሚውል መረጃ የለውም።',
        'multiple_sheets': 'ብዙ ሉሆች ተገኝተዋል!',
        'select_sheet': 'ለመተንተን የስራ ሉህ ይምረጡ:',
        'sheets_available': 'ሉሆች ይገኛሉ',
        'using_sheet': 'የስራ ሉህ በመጠቀም:',
        'loading_data': 'የስራ ሉህ መረጃ በመጫን ላይ...',
        'no_sheet_data': 'የተመረጠው የስራ ሉህ ጥቅም ላይ የሚውል መረጃ የለውም።',
        
        # File info
        'file_info': 'የፋይል መረጃ',
        'total_columns': 'አምዶች',
        'file_size': 'የፋይል መጠን',
        'sheet': 'ሉህ',
        
        # Data preview
        'data_preview': 'የመረጃ ቅድመ እይታ',
        'table_view': 'የሰንጠረዥ እይታ',
        'column_info': 'የአምድ መረጃ',
        'showing_rows': 'የመጀመሪያዎቹን {0} ረድፎች ከ{1} ጠቅላላ ረድፎች በማሳየት ላይ',
        'column_name': 'የአምድ ስም',
        'data_type': 'የመረጃ ዓይነት',
        'non_null_count': 'ባዶ ያልሆነ ቆጠራ',
        'null_count': 'ባዶ ቆጠራ',
        
        # Step 2
        'step2_title': 'ለድግግሞሽ ረድፎች ይተንትኑ',
        'how_detection_works': 'የድግግሞሽ ግኝት እንዴት እንደሚሰራ',
        'detection_rule1': 'ሙሉ ረድፍ ማወዳደር: ሁሉም የአምድ እሴቶች መገጣጠም አለባቸው',
        'detection_rule2': 'የመጀመሪያ ክስተት ተጠብቋል: የመጀመሪያው ረድፍ ይቀመጣል',
        'detection_rule3': 'ብልህ ግኝት: ባዶ ሴሎችን፣ ክፍት ቦታን እና የመረጃ አይነቶችን ያስተናግዳል',
        'detection_rule4': 'የቡድን ድርጅት: ድግግሞሾች ለቀላል ግምገማ ተቆርቋሪ ናቸው',
        'analyze_button': 'ድግግሞሾችን ተንትን',
        'analyzing': 'መረጃዎን በመተንተን ላይ...',
        'reading_data': 'መረጃ በማንበብ ላይ...',
        'detecting_duplicates': 'ድግግሞሾችን በማግኘት ላይ...',
        'analyzing_groups': 'ቡድኖችን በመተንተን ላይ...',
        'finalizing': 'ውጤቶችን በማጠናቀቅ ላይ...',
        'analysis_complete': 'ትንተና ተጠናቅቋል! ውጤቶችን ለማየት ወደ ታች ይሸብልሉ።',
        
        # Step 3
        'step3_title': 'የትንተና ውጤቶች እና ስታቲስቲክስ',
        'congratulations': 'እንኳን ደስ አለዎት!',
        'no_duplicates': 'ምንም የተደጋገሙ ረድፎች አልተገኙም። የእርስዎ የመረጃ ስብስብ በሁሉም አምዶች ላይ በመመስረት ልዩ ረድፎችን ብቻ ይዟል።',
        'data_quality': 'የመረጃ ጥራት አጠቃላይ እይታ',
        'all_unique': 'ሁሉም ረድፎች ልዩ ናቸው ✓',
        'key_metrics': 'ቁልፍ መለኪያዎች',
        'unique_rows': 'ልዩ ረድፎች',
        'duplicate_rows': 'የተደጋገሙ ረድፎች',
        'columns_analyzed': 'ጠቅላላ የተተነተኑ አምዶች',
        'duplicate_groups': 'የተገኙ የድግግሞሽ ቡድኖች',
        
        # Visualizations
        'visual_analytics': 'የእይታ ትንተና',
        'overview': 'አጠቃላይ እይታ',
        'distribution': 'ስርጭት',
        'group_analysis': 'የቡድን ትንተና',
        'unique_vs_duplicate': 'ልዩ እና የተደጋገሙ ረድፎች ማወዳደር',
        'data_composition': 'የመረጃ ቅንብር',
        'group_distribution': 'የድግግሞሽ ቡድን መጠን ስርጭት',
        'num_duplicates': 'የድግግሞሽ ክስተቶች ብዛት',
        'num_groups': 'የቡድኖች ብዛት',
        
        # Step 4
        'step4_title': 'የተደጋገሙ ረድፎችን ይገምግሙ',
        'duplicates_detected': 'ድግግሞሾች ተገኝተዋል',
        'found_duplicates': '{0} የተደጋገሙ ረድፎች በ{1} ቡድኖች ተደራጅተዋል።',
        'search_filter': 'ፍለጋ እና ማጣሪያ',
        'search_placeholder': 'ለመፈለግ ማንኛውንም ነገር ይተይቡ...',
        'search_help': 'በሁሉም አምዶች ውስጥ ድግግሞሾችን ይፈልጉ',
        'filter_group': 'በድግግሞሽ ቡድን አጣራ:',
        'filter_help': 'የተወሰኑ የድግግሞሽ ቡድኖችን ይመልከቱ',
        'sort_by': 'ደርድር በ:',
        'sort_help': 'ውጤቶችን ደርድር',
        'all_groups': 'ሁሉም ቡድኖች',
        'showing_results': '{0} ከ{1} የተደጋገሙ ረድፎችን በማሳየት ላይ',
        'duplicate_table': 'የድግግሞሽ መረጃ ሰንጠረዥ',
        'page_indicator': 'ገጽ (1-{0})',
        'page_help': 'በ{0} ገፆች ውስጥ ያስሱ',
        'showing_page': 'ረድፎች {0} እስከ {1} ከ{2} በማሳየት ላይ',
        'group_occurrences': 'ቡድን {0} {1} ጠቅላላ ክስተቶች አሉት (መጀመሪያውን ጨምሮ)',
        'no_matches': 'ምንም የተደጋገሙ ረድፎች ከፍለጋዎ መስፈርት ጋር አይዛመዱም።',
        
        # Step 5
        'step5_title': 'የተደጋገሙ ረድፎችን ያስወግዱ',
        'review_before': 'ከመቀጠልዎ በፊት ይገምግሙ',
        'will_retain': 'የእያንዳንዱ የድግግሞሽ ቡድን የመጀመሪያ ክስተት ይቀመጣል',
        'will_remove': '{0} የተደጋገሙ ረድፎች ይወገዳሉ',
        'will_preserve': 'የመጀመሪያ የአምድ ስሞች እና የመረጃ እሴቶች ይጠበቃሉ',
        'will_maintain': 'የረድፍ ቅደም ተከተል ሳይለወጥ ይቀራል',
        'confirm_remove': '{0} የተደጋገሙ ረድፎችን ማስወገድ እንደምፈልግ አረጋግጣለሁ',
        'confirm_help': 'የድግግሞሾችን አስወግድ ቁልፍን ለማንቃት ይህን ሳጥን ይፈትሹ',
        'ready_proceed': 'ለመቀጠል ዝግጁ!',
        'confirmation_required': 'ማረጋገጫ ያስፈልጋል',
        'remove_button': 'አሁን ድግግሞሾችን አስወግድ',
        'removing': 'የተደጋገሙ ረድፎችን በማስወገድ ላይ...',
        'success_title': 'ስኬታማ!',
        'success_message': '{0} የተደጋገሙ ረድፎችን በተሳካ ሁኔታ ተወግደዋል! የተጸዳው የመረጃ ስብስብዎ አሁን {1} ልዩ ረድፎችን ይዟል።',
        
        # Step 6
        'step6_title': 'ውጤቶችዎን ያውርዱ',
        'available_downloads': 'የሚገኙ ማውረጃዎች',
        'download_info': 'ማውረድ የሚፈልጉትን ይምረጡ። ሁሉም ፋይሎች በኤክሴል ቅርጸት ይመነጫሉ።',
        'cleaned_excel': 'የተጸዳ ኤክሴል',
        'cleaned_desc': 'ድግግሞሾች ሳይኖራቸው መረጃ',
        'download_cleaned': 'የተጸዳ ፋይል አውርድ',
        'duplicate_rows_title': 'የተደጋገሙ ረድፎች',
        'duplicates_desc': 'የተደጋገሙ ግቤቶች ብቻ',
        'download_duplicates': 'ድግግሞሾችን አውርድ',
        'analysis_report': 'የትንተና ሪፖርት',
        'report_desc': 'ሙሉ ትንተና',
        'download_report': 'ሪፖርት አውርድ',
        'remove_first': 'መጀመሪያ ድግግሞሾችን ያስወግዱ',
        
        # Error messages
        'error_reading': 'ይህን ኤክሴል ፋይል ማንበብ አልተቻለም። እባክዎ ፋይሉ ትክክለኛ መሆኑን ያረጋግጡ እና እንደገና ይሞክሩ።',
        'view_error': 'የስህተት ዝርዝሮችን ይመልከቱ',
    }
}

def get_text(lang, key):
    """Get translated text for a given language and key"""
    return TRANSLATIONS.get(lang, TRANSLATIONS['en']).get(key, key)
