import os
import sys

# Ensure root directory is in sys.path so app and database can be imported
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app
