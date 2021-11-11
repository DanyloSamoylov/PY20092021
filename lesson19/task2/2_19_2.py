import sys
import os
"""
правельное написание пути для PYTHONPATH. 
"""
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

for i in sys.path:
    print(i)
