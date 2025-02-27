Get-ExecutionPolicy

Set-ExecutionPolicy Unrestricted -Scope CurrentUser

py -m venv venv

.\venv\Scripts\Activate

pip install -r requirements.txt

streamlit run app.py
