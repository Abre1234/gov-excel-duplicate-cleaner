"""
Government Excel Duplicate Row Cleaner
Official Data Quality Management System with Amharic and English support
"""

import streamlit as st
import pandas as pd
from io import BytesIO
import sys
from pathlib import Path
import plotly.express as px
import plotly.graph_objects as go
import time

# Add modules directory to path
sys.path.append(str(Path(__file__).parent))

from modules.excel_handler import ExcelHandler
from modules.duplicate_detector import DuplicateDetector
from modules.cleaner import DataCleaner
from modules.report_generator import ReportGenerator
from modules.utils import format_number, calculate_percentage
from translations import get_text

# Page configuration
st.set_page_config(
    page_title="Government Excel Duplicate Cleaner",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Government color scheme - Professional blues, greens, and golds (NO BLACK)
GOV_COLORS = {
    'primary': '#003DA5',      # Government blue
    'secondary': '#00843D',    # Government green
    'accent': '#FFB81C',       # Government gold
    'light_blue': '#E8F4F8',
    'light_green': '#E8F5E9',
    'light_gold': '#FFF8E1',
    'text_dark': '#1A2332',
    'text_medium': '#4A5568',
    'text_light': '#64748B',
    'success': '#00843D',
    'warning': '#FFB81C',
    'error': '#DC2626',
    'bg_light': '#F8FAFC'
}

# Custom CSS for government styling
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    * {{
        font-family: 'Inter', sans-serif;
    }}
    
    .main-header {{
        font-size: 2.8rem;
        font-weight: 700;
        background: linear-gradient(135deg, {GOV_COLORS['primary']} 0%, {GOV_COLORS['secondary']} 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        animation: fadeInDown 0.8s ease-out;
        text-align: center;
    }}
    
    .sub-header {{
        font-size: 1.3rem;
        color: {GOV_COLORS['text_medium']};
        margin-bottom: 2rem;
        animation: fadeInUp 0.8s ease-out;
        text-align: center;
    }}
    
    .gov-badge {{
        background: linear-gradient(135deg, {GOV_COLORS['primary']} 0%, {GOV_COLORS['secondary']} 100%);
        color: white;
        padding: 0.3rem 1rem;
        border-radius: 0.3rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 0.5rem;
        font-size: 0.85rem;
        letter-spacing: 1px;
    }}
    
    @keyframes fadeInDown {{
        from {{
            opacity: 0;
            transform: translateY(-20px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    @keyframes fadeInUp {{
        from {{
            opacity: 0;
            transform: translateY(20px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    @keyframes fadeIn {{
        from {{
            opacity: 0;
        }}
        to {{
            opacity: 1;
        }}
    }}
    
    .privacy-notice {{
        background: {GOV_COLORS['light_blue']};
        padding: 1.5rem;
        border-radius: 0.8rem;
        border: 2px solid {GOV_COLORS['primary']};
        font-size: 0.95rem;
        margin-top: 2rem;
        animation: fadeIn 1s ease-out;
        box-shadow: 0 4px 15px rgba(0, 61, 165, 0.15);
    }}
    
    .warning-box {{
        background: {GOV_COLORS['light_gold']};
        padding: 1.5rem;
        border-radius: 0.8rem;
        border: 2px solid {GOV_COLORS['warning']};
        margin: 1rem 0;
        animation: fadeIn 0.6s ease-out;
        box-shadow: 0 4px 15px rgba(255, 184, 28, 0.15);
    }}
    
    .success-box {{
        background: {GOV_COLORS['light_green']};
        padding: 1.5rem;
        border-radius: 0.8rem;
        border: 2px solid {GOV_COLORS['success']};
        margin: 1rem 0;
        animation: fadeIn 0.6s ease-out;
        box-shadow: 0 4px 15px rgba(0, 132, 61, 0.15);
    }}
    
    .info-box {{
        background: {GOV_COLORS['light_blue']};
        padding: 1.5rem;
        border-radius: 0.8rem;
        border: 2px solid {GOV_COLORS['primary']};
        margin: 1rem 0;
        animation: fadeIn 0.6s ease-out;
        box-shadow: 0 4px 15px rgba(0, 61, 165, 0.15);
    }}
    
    .step-badge {{
        background: linear-gradient(135deg, {GOV_COLORS['primary']} 0%, {GOV_COLORS['secondary']} 100%);
        color: white;
        padding: 0.5rem 1.5rem;
        border-radius: 2rem;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 1rem;
        font-size: 0.9rem;
        letter-spacing: 1.5px;
    }}
    
    .stat-card {{
        background: white;
        padding: 1.5rem;
        border-radius: 0.8rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
        border: 2px solid {GOV_COLORS['bg_light']};
    }}
    
    .stat-card:hover {{
        transform: translateY(-3px);
        border-color: {GOV_COLORS['primary']};
        box-shadow: 0 8px 25px rgba(0, 61, 165, 0.15);
    }}
    
    /* Streamlit button styling */
    .stButton>button {{
        background: linear-gradient(135deg, {GOV_COLORS['primary']} 0%, {GOV_COLORS['secondary']} 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 0.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 61, 165, 0.25);
    }}
    
    .stButton>button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 61, 165, 0.35);
    }}
    
    /* Progress bar styling */
    .stProgress > div > div > div > div {{
        background: linear-gradient(90deg, {GOV_COLORS['primary']} 0%, {GOV_COLORS['secondary']} 100%);
    }}
    
    /* Metric styling */
    [data-testid="stMetricValue"] {{
        font-size: 2rem;
        font-weight: 700;
        color: {GOV_COLORS['text_dark']};
    }}
    
    /* Language toggle */
    .lang-toggle {{
        background: {GOV_COLORS['bg_light']};
        padding: 0.5rem;
        border-radius: 0.5rem;
        border: 2px solid {GOV_COLORS['primary']};
    }}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None
if 'df' not in st.session_state:
    st.session_state.df = None
if 'selected_sheet' not in st.session_state:
    st.session_state.selected_sheet = None
if 'analysis_done' not in st.session_state:
    st.session_state.analysis_done = False
if 'duplicate_info' not in st.session_state:
    st.session_state.duplicate_info = None
if 'cleaned_df' not in st.session_state:
    st.session_state.cleaned_df = None
if 'language' not in st.session_state:
    st.session_state.language = 'en'

def reset_session():
    """Reset session state"""
    lang = st.session_state.language  # Preserve language
    st.session_state.clear()
    st.session_state.language = lang
    st.session_state.uploaded_file = None
    st.session_state.df = None
    st.session_state.selected_sheet = None
    st.session_state.analysis_done = False
    st.session_state.duplicate_info = None
    st.session_state.cleaned_df = None

def t(key):
    """Shorthand for translation"""
    return get_text(st.session_state.language, key)

def main():
    # Government header with bilingual support
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col1:
        st.markdown(f"""
        <div class="gov-badge">
            🏛️ OFFICIAL SYSTEM
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        # Language toggle
        lang_options = {'English': 'en', 'አማርኛ': 'am'}
        selected_lang = st.selectbox(
            t('language'),
            options=list(lang_options.keys()),
            index=0 if st.session_state.language == 'en' else 1,
            key='lang_selector'
        )
        if lang_options[selected_lang] != st.session_state.language:
            st.session_state.language = lang_options[selected_lang]
            st.rerun()
    
    st.markdown(f'<div class="main-header">🏛️ {t("app_title")}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="sub-header">📊 {t("app_subtitle")}</div>', unsafe_allow_html=True)
    
    # Enhanced Sidebar
    with st.sidebar:
        st.markdown(f"### 📋 **{t('about_title')}**")
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {GOV_COLORS['primary']} 0%, {GOV_COLORS['secondary']} 100%); 
                    padding: 1rem; border-radius: 0.8rem; color: white; margin-bottom: 1rem;'>
            <h4 style='margin: 0; color: white;'>🎯 {t('key_features')}</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        - 📤 {t('feature_upload')}
        - 🔍 {t('feature_detection')}
        - 📊 {t('feature_analytics')}
        - 🔎 {t('feature_search')}
        - 🧹 {t('feature_cleaning')}
        - 📥 {t('feature_download')}
        """)
        
        st.markdown("---")
        
        st.markdown(f"### ⚙️ **{t('display_settings')}**")
        rows_per_page = st.selectbox(
            f"📄 {t('rows_per_page')}",
            options=[25, 50, 100, 250],
            index=1
        )
        
        st.markdown("---")
        
        # Statistics if analysis done
        if st.session_state.analysis_done and st.session_state.duplicate_info:
            st.markdown(f"### 📈 **{t('quick_stats')}**")
            info = st.session_state.duplicate_info
            st.metric(t('total_rows'), format_number(info['total_rows']))
            st.metric(t('duplicates'), format_number(info['duplicate_count']))
            st.metric(t('duplicate_rate'), f"{info['duplicate_percentage']:.1f}%")
        
        st.markdown("---")
        
        with st.expander(f"❓ {t('need_help')}"):
            st.markdown(t('help_text'))
    
    # Privacy Notice
    st.markdown(f"""
    <div class="privacy-notice">
        🔒 <strong>{t('privacy_title')}:</strong> {t('privacy_text')}
        <span style='color: {GOV_COLORS['primary']}; font-weight: 600;'>{t('privacy_badge')}</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Step 1: Upload
    st.markdown(f'<div class="step-badge">📤 {t("step1_title").upper()}</div>', unsafe_allow_html=True)
    st.markdown(f"## {t('step1_title')}")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        uploaded_file = st.file_uploader(
            t('upload_prompt'),
            type=['xlsx', 'xls'],
            help=t('upload_help')
        )
    
    with col2:
        st.markdown(f"""
        <div style='background: {GOV_COLORS['bg_light']}; padding: 1rem; border-radius: 0.8rem; margin-top: 0.5rem;
                    border: 2px solid {GOV_COLORS['primary']};'>
            <h4 style='margin: 0 0 0.5rem 0; color: {GOV_COLORS['text_dark']};'>📋 {t('supported_formats')}</h4>
            <ul style='margin: 0; padding-left: 1.2rem; color: {GOV_COLORS['text_medium']};'>
                <li>{t('format_xlsx')}</li>
                <li>{t('format_xls')}</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    if uploaded_file is not None:
        st.session_state.uploaded_file = uploaded_file
        st.success(f"✅ {t('file_uploaded')}")
        
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
        progress_bar.empty()
        
        try:
            with st.spinner(f"🔄 {t('reading_file')}"):
                excel_handler = ExcelHandler(uploaded_file)
                sheet_names = excel_handler.get_sheet_names()
            
            if not sheet_names:
                st.error(f"❌ {t('no_data')}")
                return
            
            st.markdown("---")
            if len(sheet_names) > 1:
                st.markdown(f"""
                <div class="info-box">
                    📑 <strong>{t('multiple_sheets')}</strong><br>
                    {len(sheet_names)} {t('sheets_available')}
                </div>
                """, unsafe_allow_html=True)
                
                col1, col2 = st.columns([2, 1])
                with col1:
                    selected_sheet = st.selectbox(
                        f"📊 {t('select_sheet')}",
                        sheet_names
                    )
                with col2:
                    st.info(f"**{len(sheet_names)}** {t('sheets_available')}")
            else:
                selected_sheet = sheet_names[0]
                st.markdown(f"""
                <div class="success-box">
                    ✅ <strong>{t('using_sheet')}:</strong> {selected_sheet}
                </div>
                """, unsafe_allow_html=True)
            
            st.session_state.selected_sheet = selected_sheet
            
            with st.spinner(f"📖 {t('loading_data')}"):
                df = excel_handler.read_sheet(selected_sheet)
            
            if df is None or df.empty:
                st.error(f"❌ {t('no_sheet_data')}")
                return
            
            st.session_state.df = df
            
            # File info with government colors
            st.markdown(f"### 📊 {t('file_info')}")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.markdown(f"""
                <div class="stat-card">
                    <h4 style='color: {GOV_COLORS['primary']}; margin: 0;'>📝 {t('total_rows')}</h4>
                    <h2 style='margin: 0.5rem 0 0 0; color: {GOV_COLORS['text_dark']};'>{format_number(len(df))}</h2>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="stat-card">
                    <h4 style='color: {GOV_COLORS['secondary']}; margin: 0;'>📋 {t('total_columns')}</h4>
                    <h2 style='margin: 0.5rem 0 0 0; color: {GOV_COLORS['text_dark']};'>{format_number(len(df.columns))}</h2>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"""
                <div class="stat-card">
                    <h4 style='color: {GOV_COLORS['accent']}; margin: 0;'>💾 {t('file_size')}</h4>
                    <h2 style='margin: 0.5rem 0 0 0; color: {GOV_COLORS['text_dark']};'>{uploaded_file.size / 1024:.2f} KB</h2>
                </div>
                """, unsafe_allow_html=True)
            
            with col4:
                sheet_display = selected_sheet[:12] + "..." if len(selected_sheet) > 12 else selected_sheet
                st.markdown(f"""
                <div class="stat-card">
                    <h4 style='color: {GOV_COLORS['primary']}; margin: 0;'>📄 {t('sheet')}</h4>
                    <h2 style='margin: 0.5rem 0 0 0; color: {GOV_COLORS['text_dark']}; font-size: 1.2rem;'>{sheet_display}</h2>
                </div>
                """, unsafe_allow_html=True)
            
            # Data Preview
            st.markdown("---")
            st.markdown(f"### 👀 {t('data_preview')}")
            
            tab1, tab2 = st.tabs([f"📊 {t('table_view')}", f"📈 {t('column_info')}"])
            
            with tab1:
                st.dataframe(df.head(rows_per_page), use_container_width=True, height=400)
                st.caption(t('showing_rows').format(min(rows_per_page, len(df)), format_number(len(df))))
            
            with tab2:
                col_info = pd.DataFrame({
                    t('column_name'): df.columns,
                    t('data_type'): df.dtypes.values,
                    t('non_null_count'): df.count().values,
                    t('null_count'): df.isnull().sum().values
                })
                st.dataframe(col_info, use_container_width=True, height=400)
            
            st.markdown("---")
            
            # Step 2: Analyze
            st.markdown(f'<div class="step-badge">🔍 {t("step2_title").upper()}</div>', unsafe_allow_html=True)
            st.markdown(f"## {t('step2_title')}")
            
            st.markdown(f"""
            <div class="info-box">
                <h4 style='margin: 0 0 0.5rem 0;'>🎯 <strong>{t('how_detection_works')}</strong></h4>
                <ul style='margin: 0; padding-left: 1.5rem;'>
                    <li>{t('detection_rule1')}</li>
                    <li>{t('detection_rule2')}</li>
                    <li>{t('detection_rule3')}</li>
                    <li>{t('detection_rule4')}</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button(f"🔎 **{t('analyze_button')}**", type="primary", use_container_width=True):
                    with st.spinner(f"🔄 {t('analyzing')}"):
                        progress_text = st.empty()
                        progress_bar = st.progress(0)
                        
                        for percent_complete in range(100):
                            time.sleep(0.02)
                            progress_bar.progress(percent_complete + 1)
                            if percent_complete < 30:
                                progress_text.text(f"📖 {t('reading_data')}")
                            elif percent_complete < 60:
                                progress_text.text(f"🔍 {t('detecting_duplicates')}")
                            elif percent_complete < 90:
                                progress_text.text(f"📊 {t('analyzing_groups')}")
                            else:
                                progress_text.text(f"✅ {t('finalizing')}")
                        
                        detector = DuplicateDetector(df)
                        duplicate_info = detector.detect_duplicates()
                        st.session_state.duplicate_info = duplicate_info
                        st.session_state.analysis_done = True
                        
                        progress_bar.empty()
                        progress_text.empty()
                    
                    st.success(f"✅ {t('analysis_complete')}")
                    st.balloons()
                    time.sleep(1)
                    st.rerun()
            
        except Exception as e:
            st.error(f"❌ {t('error_reading')}")
            with st.expander(f"🔍 {t('view_error')}"):
                st.code(str(e))
            return
    
    # Display results (continues in next part due to length)
    if st.session_state.analysis_done and st.session_state.duplicate_info is not None:
        display_results(rows_per_page)

def display_results(rows_per_page):
    """Display analysis results"""
    duplicate_info = st.session_state.duplicate_info
    
    st.markdown("---")
    st.markdown(f'<div class="step-badge">📊 {t("step3_title").upper()}</div>', unsafe_allow_html=True)
    st.markdown(f"## {t('step3_title')}")
    
    if duplicate_info['duplicate_count'] == 0:
        st.markdown(f"""
        <div class="success-box">
            <h3 style='margin: 0;'>🎉 <strong>{t('congratulations')}</strong></h3>
            <p style='margin: 0.5rem 0 0 0; font-size: 1.1rem;'>{t('no_duplicates')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        fig = go.Figure(data=[go.Pie(
            labels=[t('unique_rows')],
            values=[duplicate_info['total_rows']],
            marker=dict(colors=[GOV_COLORS['success']]),
            hole=0.4
        )])
        fig.update_layout(title=t('all_unique'), height=400)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.markdown(f"### 📈 {t('key_metrics')}")
        
        col1, col2, col3, col4 = st.columns(4)
        
        metrics = [
            (f"📝 {t('total_rows')}", duplicate_info['total_rows'], GOV_COLORS['primary']),
            (f"✨ {t('unique_rows')}", duplicate_info['unique_rows'], GOV_COLORS['success']),
            (f"⚠️ {t('duplicate_rows')}", duplicate_info['duplicate_count'], GOV_COLORS['warning']),
            (f"📊 {t('duplicate_rate')}", f"{duplicate_info['duplicate_percentage']:.1f}%", GOV_COLORS['error'])
        ]
        
        for col, (label, value, color) in zip([col1, col2, col3, col4], metrics):
            with col:
                formatted_value = format_number(value) if isinstance(value, int) else value
                st.markdown(f"""
                <div style='background: {color}; padding: 1.5rem; border-radius: 0.8rem; 
                            text-align: center; color: white; box-shadow: 0 4px 15px rgba(0,0,0,0.1);'>
                    <h4 style='margin: 0; font-size: 0.9rem; opacity: 0.9;'>{label}</h4>
                    <h2 style='margin: 0.5rem 0 0 0; font-size: 2rem;'>{formatted_value}</h2>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric(f"🔢 {t('columns_analyzed')}", format_number(duplicate_info['total_columns']))
        with col2:
            st.metric(f"🔗 {t('duplicate_groups')}", format_number(duplicate_info['duplicate_groups']))
        
        # Visualizations
        st.markdown("---")
        st.markdown(f"### 📊 {t('visual_analytics')}")
        
        viz_tab1, viz_tab2, viz_tab3 = st.tabs([
            f"📈 {t('overview')}", 
            f"🥧 {t('distribution')}", 
            f"📊 {t('group_analysis')}"
        ])
        
        with viz_tab1:
            fig = go.Figure(data=[
                go.Bar(name=t('unique_rows'), x=[t('unique_rows')], y=[duplicate_info['unique_rows']],
                       marker_color=GOV_COLORS['success'], text=[format_number(duplicate_info['unique_rows'])],
                       textposition='auto'),
                go.Bar(name=t('duplicate_rows'), x=[t('duplicate_rows')], y=[duplicate_info['duplicate_count']],
                       marker_color=GOV_COLORS['warning'], text=[format_number(duplicate_info['duplicate_count'])],
                       textposition='auto')
            ])
            fig.update_layout(title=t('unique_vs_duplicate'), height=400, barmode='group')
            st.plotly_chart(fig, use_container_width=True)
        
        with viz_tab2:
            fig = go.Figure(data=[go.Pie(
                labels=[t('unique_rows'), t('duplicate_rows')],
                values=[duplicate_info['unique_rows'], duplicate_info['duplicate_count']],
                marker=dict(colors=[GOV_COLORS['success'], GOV_COLORS['warning']]),
                hole=0.4
            )])
            fig.update_layout(title=t('data_composition'), height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with viz_tab3:
            duplicate_df = duplicate_info['duplicate_df']
            if not duplicate_df.empty:
                group_sizes = duplicate_df.groupby('Duplicate_Group_ID')['Total_Occurrences'].first().value_counts().sort_index()
                fig = go.Figure(data=[go.Bar(
                    x=[f"{x} duplicates" for x in group_sizes.index],
                    y=group_sizes.values,
                    marker_color=GOV_COLORS['primary'],
                    text=group_sizes.values,
                    textposition='auto'
                )])
                fig.update_layout(
                    title=t('group_distribution'),
                    xaxis_title=t('num_duplicates'),
                    yaxis_title=t('num_groups'),
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)
        
        # Continue with Step 4, 5, 6...
        display_duplicate_rows(duplicate_info, rows_per_page)

def display_duplicate_rows(duplicate_info, rows_per_page):
    """Display duplicate rows section"""
    st.markdown("---")
    st.markdown(f'<div class="step-badge">🔍 {t("step4_title").upper()}</div>', unsafe_allow_html=True)
    st.markdown(f"## {t('step4_title')}")
    
    st.markdown(f"""
    <div class="warning-box">
        <h4 style='margin: 0;'>⚠️ <strong>{t('duplicates_detected')}</strong></h4>
        <p style='margin: 0.5rem 0 0 0;'>{t('found_duplicates').format(duplicate_info['duplicate_count'], duplicate_info['duplicate_groups'])}</p>
    </div>
    """, unsafe_allow_html=True)
    
    duplicate_df = duplicate_info['duplicate_df']
    
    st.markdown(f"### 🔎 {t('search_filter')}")
    
    col1, col2, col3 = st.columns([2, 2, 1])
    
    with col1:
        search_term = st.text_input(f"🔍 {t('search_placeholder')}", placeholder=t('search_placeholder'), help=t('search_help'))
    
    with col2:
        duplicate_groups = sorted(duplicate_df['Duplicate_Group_ID'].unique())
        selected_group = st.selectbox(f"🏷️ {t('filter_group')}", options=[t('all_groups')] + list(duplicate_groups), help=t('filter_help'))
    
    with col3:
        sort_by = st.selectbox(f"📊 {t('sort_by')}:", options=['Duplicate_Group_ID', 'Total_Occurrences', 'Duplicate_Row'], help=t('sort_help'))
    
    filtered_df = duplicate_df.copy()
    
    if search_term:
        mask = filtered_df.astype(str).apply(lambda row: row.str.contains(search_term, case=False, na=False).any(), axis=1)
        filtered_df = filtered_df[mask]
    
    if selected_group != t('all_groups'):
        filtered_df = filtered_df[filtered_df['Duplicate_Group_ID'] == selected_group]
    
    filtered_df = filtered_df.sort_values(sort_by)
    
    st.markdown(f"""
    <div class="info-box">
        📊 {t('showing_results').format(len(filtered_df), len(duplicate_df))}
    </div>
    """, unsafe_allow_html=True)
    
    total_dup_rows = len(filtered_df)
    
    if total_dup_rows > 0:
        total_pages = (total_dup_rows - 1) // rows_per_page + 1
        
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            page_num = st.number_input(
                t('page_indicator').format(total_pages),
                min_value=1,
                max_value=total_pages,
                value=1,
                key="duplicate_page",
                help=t('page_help').format(total_pages)
            )
        
        start_idx = (page_num - 1) * rows_per_page
        end_idx = min(start_idx + rows_per_page, total_dup_rows)
        
        st.markdown(f"### 📋 {t('duplicate_table')}")
        st.dataframe(filtered_df.iloc[start_idx:end_idx], use_container_width=True, height=450)
        st.caption(t('showing_page').format(start_idx + 1, end_idx, format_number(total_dup_rows)))
        
        if selected_group != t('all_groups'):
            group_count = filtered_df['Total_Occurrences'].iloc[0] if len(filtered_df) > 0 else 0
            st.info(t('group_occurrences').format(selected_group, group_count))
    else:
        st.warning(f"🔍 {t('no_matches')}")
    
    # Step 5 and 6
    display_cleaning_section(duplicate_info, rows_per_page)

def display_cleaning_section(duplicate_info, rows_per_page):
    """Display cleaning and download sections"""
    st.markdown("---")
    st.markdown(f'<div class="step-badge">🧹 {t("step5_title").upper()}</div>', unsafe_allow_html=True)
    st.markdown(f"## {t('step5_title')}")
    
    st.markdown(f"""
    <div class="warning-box">
        <h4 style='margin: 0;'>⚠️ <strong>{t('review_before')}</strong></h4>
        <ul style='margin: 0.5rem 0 0 1.5rem;'>
            <li>{t('will_retain')}</li>
            <li>{t('will_remove').format(duplicate_info['duplicate_count'])}</li>
            <li>{t('will_preserve')}</li>
            <li>{t('will_maintain')}</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        confirm = st.checkbox(
            t('confirm_remove').format(duplicate_info['duplicate_count']),
            help=t('confirm_help')
        )
    
    with col2:
        if confirm:
            st.success(f"✅ {t('ready_proceed')}")
        else:
            st.info(f"ℹ️ {t('confirmation_required')}")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button(f"🧹 **{t('remove_button')}**", type="primary", disabled=not confirm, use_container_width=True):
            with st.spinner(f"🔄 {t('removing')}"):
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.01)
                    progress_bar.progress(i + 1)
                
                cleaner = DataCleaner(st.session_state.df)
                cleaned_df = cleaner.remove_duplicates()
                st.session_state.cleaned_df = cleaned_df
                progress_bar.empty()
            
            st.markdown(f"""
            <div class="success-box">
                <h3 style='margin: 0;'>✅ <strong>{t('success_title')}</strong></h3>
                <p style='margin: 0.5rem 0 0 0; font-size: 1.1rem;'>
                    {t('success_message').format(duplicate_info['duplicate_count'], len(cleaned_df))}
                </p>
            </div>
            """, unsafe_allow_html=True)
            st.balloons()
            time.sleep(1)
            st.rerun()
    
    st.markdown("---")
    
    # Step 6: Downloads
    st.markdown(f'<div class="step-badge">⬇️ {t("step6_title").upper()}</div>', unsafe_allow_html=True)
    st.markdown(f"## {t('step6_title')}")
    
    st.markdown(f"""
    <div class="info-box">
        <h4 style='margin: 0;'>📦 <strong>{t('available_downloads')}</strong></h4>
        <p style='margin: 0.5rem 0 0 0;'>{t('download_info')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div style='background: {GOV_COLORS['success']}; padding: 1.5rem; border-radius: 0.8rem; 
                    color: white; text-align: center; box-shadow: 0 4px 15px rgba(0, 132, 61, 0.25); margin-bottom: 1rem;'>
            <h3 style='margin: 0; font-size: 2rem;'>✨</h3>
            <h4 style='margin: 0.5rem 0;'>{t('cleaned_excel')}</h4>
            <p style='margin: 0; font-size: 0.9rem; opacity: 0.9;'>{t('cleaned_desc')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.cleaned_df is not None:
            report_gen = ReportGenerator()
            cleaned_excel = report_gen.generate_cleaned_excel(st.session_state.cleaned_df)
            st.download_button(
                label=f"📥 {t('download_cleaned')}",
                data=cleaned_excel,
                file_name="cleaned_excel.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )
        else:
            st.info(t('remove_first'))
    
    with col2:
        st.markdown(f"""
        <div style='background: {GOV_COLORS['warning']}; padding: 1.5rem; border-radius: 0.8rem; 
                    color: white; text-align: center; box-shadow: 0 4px 15px rgba(255, 184, 28, 0.25); margin-bottom: 1rem;'>
            <h3 style='margin: 0; font-size: 2rem;'>⚠️</h3>
            <h4 style='margin: 0.5rem 0;'>{t('duplicate_rows_title')}</h4>
            <p style='margin: 0; font-size: 0.9rem; opacity: 0.9;'>{t('duplicates_desc')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        report_gen = ReportGenerator()
        duplicate_excel = report_gen.generate_duplicate_excel(duplicate_info['duplicate_df'])
        st.download_button(
            label=f"📥 {t('download_duplicates')}",
            data=duplicate_excel,
            file_name="duplicate_rows.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )
    
    with col3:
        st.markdown(f"""
        <div style='background: {GOV_COLORS['primary']}; padding: 1.5rem; border-radius: 0.8rem; 
                    color: white; text-align: center; box-shadow: 0 4px 15px rgba(0, 61, 165, 0.25); margin-bottom: 1rem;'>
            <h3 style='margin: 0; font-size: 2rem;'>📊</h3>
            <h4 style='margin: 0.5rem 0;'>{t('analysis_report')}</h4>
            <p style='margin: 0; font-size: 0.9rem; opacity: 0.9;'>{t('report_desc')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        report_excel = report_gen.generate_duplicate_report(duplicate_info)
        st.download_button(
            label=f"📥 {t('download_report')}",
            data=report_excel,
            file_name="duplicate_report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )
    
    # Preview cleaned data
    if st.session_state.cleaned_df is not None:
        st.markdown("---")
        st.markdown(f"### ✨ {t('cleaned_preview')}")
        
        tab1, tab2 = st.tabs([f"📊 {t('preview')}", f"📈 {t('statistics')}"])
        
        with tab1:
            st.dataframe(st.session_state.cleaned_df.head(rows_per_page), use_container_width=True, height=400)
            st.caption(t('showing_rows').format(min(rows_per_page, len(st.session_state.cleaned_df)), format_number(len(st.session_state.cleaned_df))))
        
        with tab2:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(t('original_rows'), format_number(duplicate_info['total_rows']), help=t('original_help'))
            with col2:
                st.metric(t('cleaned_rows'), format_number(len(st.session_state.cleaned_df)), help=t('cleaned_help'))
            with col3:
                st.metric(
                    t('rows_removed'),
                    format_number(duplicate_info['duplicate_count']),
                    delta=f"-{duplicate_info['duplicate_percentage']:.1f}%",
                    delta_color="normal",
                    help=t('removed_help')
                )
    
if __name__ == "__main__":
    main()
